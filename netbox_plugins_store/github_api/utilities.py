import markdown
import requests

def markdown_to_html(markdown)
    # Get raw markdown from GitHub and convert to HTML
    html = markdown.markdown(
        requests.get(markdown).text
    )
    return html