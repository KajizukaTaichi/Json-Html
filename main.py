import os
import json
import argparse as ap
import webbrowser as wb

# コマンドライン引数の設定
parser = ap.ArgumentParser(description='jsonデータからHTMLを作成するツール')
parser.add_argument('input_file', help='入力するjsonファイル')
parser.add_argument('-o', '--open', action='store_true', help='作成したHTMLをブラウザで開きます')
args = parser.parse_args()

def dict_html(struct: dict, indent: int) -> str:
    '''
    辞書データをHTMLテキストに変換します。    
    '''

    html_text = ""
    for (tag, value) in struct.items():    
        html_text += '\t'*indent + f"<{tag}>\n"
        if isinstance(value, dict):
            # 再帰的に呼び出す
            html_text += dict_html(value, indent+1)
        else:
            html_text += '\t'*indent + f"\t{value}\n"
        html_text += '\t'*indent + f"</{tag.split(' ')[0]}>\n"
    return html_text


def change_extension(file_path: str, new_extension: str):
    '''
    ファイルの拡張子を変更します
    '''
    base_path, _ = os.path.splitext(file_path)
    new_file_path = base_path + new_extension    
    return new_file_path

def main():
    path: str = args.input_file

    # ファイルの存在確認
    if not os.path.exists(path):
        print("指定されたファイルは存在しません。")
        return
    
    # ファイルがJSON形式かどうか確認
    try:
        with open(path, mode="r", encoding="utf-8") as file:
            struct: dict = json.load(file)
    except json.JSONDecodeError as e:
        print("JSON形式のファイルではありません。")
        return
    
    html = dict_html(struct, 0)

    new_path = change_extension(path, ".html")
    with open(new_path, mode="w", encoding="utf-8") as html_file:
        html_file.write(html)

    is_open = args.open
    if is_open:
        wb.open(new_path)


if __name__ == "__main__":
    main()
