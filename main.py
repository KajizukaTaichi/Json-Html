import json
import sys
import webbrowser as wb

def dict_html(struct: dict, indent: int) -> str:
    html_text = ""
    for (tag,value) in struct.items():    
        html_text += '\t'*indent + f"<{tag}>\n"
        if isinstance(value, dict):
            html_text += dict_html(value, indent+1)
        else:
            html_text += '\t'*indent + f"\t{value}\n"
        html_text += '\t'*indent + f"</{tag}>\n"
    return html_text

name = sys.argv[1]
file = open(name, mode="r", encoding="utf-8")
struct: dict = json.load(file)
html = dict_html(struct, 0)

name = f"{name.split('.')[0]}.html"
open(name, mode="w", encoding="utf-8").write(html)

wb.open(name)
