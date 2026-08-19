from pathlib import Path
from jinja2 import Template


BASE_DIR = Path(__file__).parent


def generate_portfolio(portfolio_data, profile_path):

    template_file = BASE_DIR / "template.html"
    output_file = BASE_DIR / "portfolio.html"

    with open(
        template_file,
        "r",
        encoding="utf-8"
    ) as file:
        template_content = file.read()

    template = Template(template_content)

    portfolio_data["image"] = "profile.jpg"

    html = template.render(
        **portfolio_data
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:
        file.write(html)

    return str(output_file)