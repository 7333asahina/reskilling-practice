### memo (作業メモ)

>Docker version 29.9.2, build a82e528

□ python3 --version（Windows は py --version）が Python 3.13.17 を返す
□ VS Code で reskilling フォルダが開けていて、左に .venv が見える
□ VS Code の中のターミナルで py hello.py（Mac は python3 hello.py）が「こんにちは」を返す

user.name asahina_tomonori
user.email=t.asahina@teamtech.by-works.net

git config --global user.name "asahina_tomonori"
git config --global user.email "t.asahina@teamtech.by-works.net"

https://github.com/7333asahina/-reskilling-practice.git
ミスでリポ作った。
---
day 2
ブラウザ型 

エディタ型　併用：前の現場でこれだったので。
```
#hello.py
print("こんにちは")
print("今日から15日間、よろしくお願いします")
print("お手数かけます。")
```
A:挨拶と15日間の開始あいさつ、およびお礼を表示します。

ーーーーーーーーーーーーー
文字列の変数   18 行目（例: date = sys.argv[1]）
    ```
    path = Path(__file__).resolve().parent / "schedule.json"
    ```
数の変数       62 行目（例: len(todays)）
   ```
   events = filter_by_date(schedule, date)
   ```
リストの変数   30 行目（例: events = json.load(f)）
    ```
    filtered = [
        event
        for event in schedule
        if datetime.fromisoformat(event["start"]).date().isoformat() == date
    ]
    ```
ーーーーーーーーーーーーー
関数1  名前: load_schedule  受け取るもの: 無し　　  返すもの: json.load(file)（JSON）  役割: JSONファイルを読み込んで、予定のリストとして返す
関数2  名前: filter_by_date 受け取るもの: schedule（用事）, date（日時）  返すもの: filtered（予定）  役割: 開始日時の日付が指定された日付と一致する予定だけを集める（日付順に）
関数3  名前: format_event  受け取るもの: event（できごと）  返すもの:line（合成文字列） 役割: ISO形式の日時から、表示用の時刻を取り出す、ロケーション付与
 ーーーー
```
 (.venv) PS C:\Users\user\reskilling> py -c "ev={'title':'朝会'}; print(ev.get('location','なし')); print(ev['location'])"
なし
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    ev={'title':'朝会'}; print(ev.get('location','なし')); print(ev['location'])
                                                                 ~~^^^^^^^^^^^^
KeyError: 'location'   
```

□ AI コーディングツールを1つ決めて、日本語で答えが返る
□ 自分の schedule.py が GitHub にある（午前）
□ schedule.py の3つの関数について、役割を1行ずつ書いた（memo.md）
□ review-target.py の誤りを3つ、行番号と理由つきで書いた（review.md）