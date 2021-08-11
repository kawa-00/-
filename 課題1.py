### 検索ツールサンプル
### これをベースに課題の内容を追記してください
import os

# 検索ソース
# source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]
SOURCE_CSV_PATH ="source.csv"
DEFAULT_CHARACTORS=["ぜんいつ","たんじろう","ねずこ","いのすけ"]

# source.csvファイルが存在しなければ新規作成する
def read_source(csv_path:str):
    if not os.path.exists(csv_path):
        print(f"csv_path:{csv_path}が存在しません。新規作成します。")
        write_source(csv_path, DEFAULT_CHARACTORS)
    
    with open(csv_path, "r", encoding="shift-jis") as f:
        return f.read().splitlines()

def write_source(csv_path:str, source:list):
    with open(csv_path, mode="w", encoding="shift-jis") as f:
        f.write("\n".join(source))

### 検索ツール
def search():
    source =read_source(SOURCE_CSV_PATH)

    while True:
        word =input("鬼滅の登場人物の名前を入力してください >>> ")

        if word in source:
            print(f"「{word}」は登録されています。")
        else:
            print(f"「{word}」は未登録です。")

            is_add = input("追加登録しますか？(n:しない y:する)　＞＞")
            if is_add == "y":
                source.append(word)    

        write_source(SOURCE_CSV_PATH, source=source)

if __name__ == "__main__":
    search()