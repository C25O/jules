import pytest
from httpx import AsyncClient
import yaml

pytestmark = pytest.mark.asyncio

async def test_create_content_and_generate_markdown(client: AsyncClient):
    """
    Tests creating a content item and then generating a Markdown file from it.
    This is an end-to-end test for the core user flow.
    """
    # 1. Create a template to base the content on
    template_data = {
        "name": "Article",
        "description": "A template for news articles.",
        "fields": [
            {"name": "Headline", "data_type": "Text", "required": True},
            {"name": "Body", "data_type": "Rich Text", "required": True},
            {"name": "Author", "data_type": "Text", "required": True},
            {"name": "Is Published", "data_type": "Boolean", "required": True},
        ]
    }
    response = await client.post("/api/v1/templates/", json=template_data)
    assert response.status_code == 200, response.text
    template = response.json()
    template_id = template["id"]

    # Map field names to their IDs for creating the content item
    field_ids = {field["name"]: field["id"] for field in template["fields"]}

    # 2. Create a content item using the template
    content_data = {
        "title": "Big News!",
        "template_id": template_id,
        "values": [
            {"field_id": field_ids["Headline"], "value": "New System is Live"},
            {"field_id": field_ids["Body"], "value": "The new blog management system is now **live**."},
            {"field_id": field_ids["Author"], "value": "Jules"},
            {"field_id": field_ids["Is Published"], "value": False},
        ]
    }
    response = await client.post("/api/v1/content/", json=content_data)
    assert response.status_code == 200, response.text
    content_item = response.json()
    item_id = content_item["id"]
    assert content_item["title"] == "Big News!"

    # 3. Fetch the generated Markdown for the content item
    response = await client.get(f"/api/v1/content/{item_id}/markdown")
    assert response.status_code == 200, response.text
    markdown = response.text

    # 4. Validate the generated Markdown content
    assert markdown.startswith("---\n")
    assert markdown.endswith("---\n\n" + "The new blog management system is now **live**.")

    # Parse the YAML front matter to verify its contents
    front_matter_str = markdown.split("---")[1]
    front_matter = yaml.safe_load(front_matter_str)

    assert front_matter["title"] == "Big News!"
    assert "date" in front_matter
    assert front_matter["template_id"] == template_id
    assert front_matter["Headline"] == "New System is Live"
    assert front_matter["Author"] == "Jules"
    assert front_matter["Is Published"] is False
