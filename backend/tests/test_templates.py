import pytest
from httpx import AsyncClient

pytestmark = pytest.mark.asyncio

async def test_create_and_read_template(client: AsyncClient):
    """
    Tests creating a new page template and then reading it back.
    """
    # 1. Define the template data
    template_data = {
        "name": "Blog Post",
        "description": "A standard blog post template.",
        "fields": [
            {"name": "Title", "data_type": "Text", "required": True},
            {"name": "Content", "data_type": "Rich Text", "required": True},
            {"name": "Author", "data_type": "Text", "required": False},
        ]
    }

    # 2. Create the template via the API
    response = await client.post("/api/v1/templates/", json=template_data)
    assert response.status_code == 200, response.text
    created_template = response.json()

    # 3. Assert the created template is correct
    assert created_template["name"] == "Blog Post"
    assert len(created_template["fields"]) == 3
    template_id = created_template["id"]

    # 4. Read the template back from the API
    response = await client.get(f"/api/v1/templates/{template_id}")
    assert response.status_code == 200, response.text
    read_template = response.json()

    # 5. Assert the retrieved template is correct
    assert read_template["name"] == "Blog Post"
    assert read_template["description"] == "A standard blog post template."
    assert len(read_template["fields"]) == 3
    assert read_template["fields"][0]["name"] == "Title"

async def test_create_duplicate_template_fails(client: AsyncClient):
    """
    Tests that creating a template with a duplicate name fails.
    """
    template_data = {"name": "Duplicate Template", "description": "First one", "fields": []}

    # Create the first template
    response = await client.post("/api/v1/templates/", json=template_data)
    assert response.status_code == 200, response.text

    # Attempt to create a second template with the same name
    response = await client.post("/api/v1/templates/", json=template_data)
    assert response.status_code == 400, response.text
    assert "already exists" in response.json()["detail"]
