import json
from jinja2 import Template

with open("portfolio.json","r",encoding="utf-8") as file:
    data = json.load(file)

with open("template.html","r",encoding="utf-8") as file:
    template_content = file.read()

template = Template(template_content)

html = template.render(**data)

with open("portfolio.html","w",encoding="utf-8") as file:
    file.write(html)

print("portfolio generated successfully")
