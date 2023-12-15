import os
import json
import argparse as ap
import webbrowser as wb

parser = ap.ArgumentParser(description='jsonデータからHTMLを作成するツール')
parser.add_argument('input_file', help='入力するjsonファイル')
parser.add_argument('-o', '--open', action='store_true', help='作成したHTMLをブラウザで開きます')
args = parser.parse_args()


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


def change_extension(file_path, new_extension):
    base_path, old_extension = os.path.splitext(file_path)
    new_file_path = base_path + new_extension    
    return new_file_path

path: str = args.input_file
file = open(path, mode="r", encoding="utf-8")
struct: dict = json.load(file)
html = dict_html(struct, 0)

new_path = change_extension(path, ".html")
open(new_path, mode="w", encoding="utf-8").write(html)

is_open = args.open
if is_open:
    wb.open(new_path)
