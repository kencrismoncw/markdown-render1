import json
import pystache
import sys

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

def main():
  templatefile = sys.argv[1]
  jsonfile = sys.argv[2]
  markdownfile = sys.argv[3]

  print(f"Template file: {templatefile}")
  print(f"JSON file: {jsonfile}")
  print(f"Markdown file: {markdownfile}")

  template_path = templatefile
  json_path = jsonfile
  output_path = markdownfile

  render_markdown(template_path, json_path, output_path)

if __name__ == "__main__":
  main()

  # Next steps
  # - Consume all aspects from command shell JSON input, Template input, output destination.
  # - Embed this into an Action.
