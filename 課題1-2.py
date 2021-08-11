import os

SOURCE_CSV_PATH ="C:/Users/User/Desktop/米谷さん/source.csv"
DEFAULT_CHARACTORS=["ぜんいつ","たんじろう","ねずこ","いのすけ"]

if not os.path.exists(SOURCE_CSV_PATH):
    print(f"SOURCE_CSV_PATHが存在しません")
    with open(SOURCE_CSV_PATH, mode="w", encoding="utf-8_sig") as f:
        source =f.write("\n".join(DEFAULT_CHARACTORS))

while True:     

    word =input("鬼滅の登場人物の名前を入力してください")

    with open(SOURCE_CSV_PATH, mode="r", encoding="utf-8_sig") as f:
        if word in f.read().splitlines():
            print(f"{word}は存在します")
        else:
            print(f"{word}は存在しません")

            is_add = input("追加登録しますか？(n:しない　y:する)")

            # ここですが、この位置に書くと、else存在しませんの場合に、追加登録is_addが表示するようにできるのでしょうか？ 
            if is_add=="y":
                with open(SOURCE_CSV_PATH, mode="a", encoding="utf-8_sig") as f:
                    f.write("\n" + word)
