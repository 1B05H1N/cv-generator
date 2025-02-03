import os
import sys
import argparse
import json
import jinja2
from weasyprint import HTML, CSS

def ensure_output_directory(directory):
    """Ensure the 'output' directory exists before saving files."""
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")
    except Exception as e:
        print(f"Error: Could not create directory '{directory}'. {e}")
        sys.exit(1)

def delete_existing_files(output_html, output_pdf):
    """Delete existing output HTML and PDF files if they exist."""
    for file in [output_html, output_pdf]:
        try:
            if os.path.exists(file):
                os.remove(file)
                print(f"Deleted existing file: {file}")
        except Exception as e:
            print(f"Warning: Could not delete {file}. {e}")

def render_html(template_file, data, output_html):
    """Render the HTML template with provided data."""
    try:
        template_dir, template_name = os.path.split(os.path.abspath(template_file))
        env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

        # Ensure template exists
        if not os.path.exists(template_file):
            print(f"Error: Template file '{template_file}' not found.")
            sys.exit(1)

        template = env.get_template(template_name)

        ensure_output_directory(os.path.dirname(output_html))  # Ensure output directory exists

        with open(output_html, 'w', encoding='utf-8') as f:
            f.write(template.render(data))
        print(f"Generated HTML: {output_html}")

    except jinja2.TemplateNotFound:
        print(f"Error: Template file '{template_file}' could not be loaded.")
        sys.exit(1)
    except jinja2.TemplateSyntaxError as e:
        print(f"Error: Syntax error in the template '{template_file}' at line {e.lineno}: {e.message}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error while rendering HTML: {e}")
        sys.exit(1)

def generate_pdf_from_html(html_file, output_pdf, css_file):
    """Convert HTML file to PDF using WeasyPrint, ensuring proper CSS formatting."""
    try:
        ensure_output_directory(os.path.dirname(output_pdf))  # Ensure directory exists

        # Ensure HTML file exists
        if not os.path.exists(html_file):
            print(f"Error: HTML file '{html_file}' not found. Cannot generate PDF.")
            sys.exit(1)

        # Ensure CSS file exists
        if not os.path.exists(css_file):
            print(f"Warning: CSS file '{css_file}' not found. Resume may not be styled correctly.")
            HTML(html_file).write_pdf(output_pdf)
        else:
            HTML(html_file).write_pdf(output_pdf, stylesheets=[CSS(css_file)])

        print(f"PDF generated successfully: {output_pdf}")

    except Exception as e:
        print(f"Error generating PDF: {e}")
        sys.exit(1)

def load_json(file_path):
    """Load JSON data from file with error handling."""
    try:
        if not os.path.exists(file_path):
            print(f"Error: JSON data file '{file_path}' not found.")
            sys.exit(1)

        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON file '{file_path}' at line {e.lineno}, column {e.colno}: {e.msg}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error while loading JSON: {e}")
        sys.exit(1)

def main():
    """Main function to generate an ATS-optimized resume."""
    parser = argparse.ArgumentParser(description="Generate an ATS-optimized resume.")
    parser.add_argument('--template', default='cv_template.html', help='HTML template file')
    parser.add_argument('--css', default='cv_template.css', help='CSS stylesheet for formatting')
    parser.add_argument('--data', default='data.json', help='JSON data file')
    args = parser.parse_args()

    try:
        data = load_json(args.data)
        output_dir = "output"
        output_html = os.path.join(output_dir, "output.html")
        output_pdf = os.path.join(output_dir, f"{data['name'].replace(' ', '_')}_Resume.pdf")

        ensure_output_directory(output_dir)
        delete_existing_files(output_html, output_pdf)

        render_html(args.template, data, output_html)
        generate_pdf_from_html(output_html, output_pdf, args.css)

    except KeyError as e:
        print(f"Error: Missing expected key in JSON data: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
