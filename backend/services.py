import yaml
import models

def generate_markdown_from_item(item: models.ContentItem) -> str:
    """
    Generates a Markdown string with YAML front matter from a ContentItem.
    """
    front_matter = {
        "title": item.title,
        "date": item.created_at.isoformat(),
        "template_id": item.template_id,
    }
    main_content = ""

    # This function expects that item.values and value.field have been eagerly loaded.
    for value in item.values:
        # Simple convention: a field with data_type 'Rich Text' is the main content.
        if value.field.data_type == "Rich Text":
            # Ensure value is a string, as it's stored as JSON
            main_content = str(value.value) if value.value is not None else ""
        else:
            # Add other fields to the front matter.
            front_matter[value.field.name] = value.value

    # Use yaml.dump to create the front matter string.
    # sort_keys=False preserves the order of the fields.
    front_matter_yaml = yaml.dump(front_matter, default_flow_style=False, sort_keys=False, allow_unicode=True)

    # Combine front matter and main content into a single string.
    markdown_output = f"---\n{front_matter_yaml}---\n\n{main_content}"

    return markdown_output
