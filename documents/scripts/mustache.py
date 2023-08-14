import json
import pystache

def render_markdown(template_path, json_path, output_path):
  """Renders a Markdown file from a mustache template and a JSON file.

  Args:
    template_path: The path to the mustache template file.
    json_path: The path to the JSON file that contains the context data.
    output_path: The path to the output Markdown file.
  """

  with open(template_path) as f:
    template_text = f.read()

  with open(json_path) as f:
    context = json.load(f)

  renderer = pystache.Renderer()
  rendered_markdown = renderer.render(template_text, context)

  with open(output_path, "w") as f:
    f.write(rendered_markdown)

if __name__ == "__main__":
  template_path = "../templates/doctemplate.tpl"
  json_path = "../json/doc1.json"
  output_path = "output.md"

  render_markdown(template_path, json_path, output_path)
