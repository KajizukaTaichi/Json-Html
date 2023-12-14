import json
import sys
import webbrowser as wb

def dict_html(struct: dict) -> str:
    html_text = ""
    for (tag,value) in struct.items():    
        html_text += f"<{tag}>"
        if isinstance(value, dict):
            html_text += dict_html(value)
        else:
            html_text += value
        html_text += f"</{tag}>"
    return html_text

name = sys.argv[1]
file = open(name, mode="r", encoding="utf-8")
struct: dict = json.load(file)
html = dict_html(struct)

name = f"{name.split('.')[0]}.html"
open(name, mode="w", encoding="utf-8").write(html)

wb.open(name)
