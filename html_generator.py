from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import shutil


BASE_DIR = Path(__file__).parent
TEMPLATE_DIR = BASE_DIR
OUTPUT_DIR = BASE_DIR / "generated_portfolio"


def generate_portfolio(portfolio_data, profile_image=None):

    OUTPUT_DIR.mkdir(exist_ok=True)

    env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR)
    )

    template = env.get_template("template.html")

    html_content = template.render(
        **portfolio_data,
        profile_image=profile_image
    )

    output_file = OUTPUT_DIR / "index.html"

    output_file.write_text(
        html_content,
        encoding="utf-8"
    )

    style_file = BASE_DIR / "style.css"

    if style_file.exists():
        shutil.copy2(
            style_file,
            OUTPUT_DIR / "style.css"
        )

    old_image = OUTPUT_DIR / "profile.jpg"

    if profile_image:

        image_path = Path(profile_image)

        if image_path.exists():
            shutil.copy2(
                image_path,
                OUTPUT_DIR / "profile.jpg"
            )

    else:

        if old_image.exists():
            old_image.unlink()

    return str(output_file)