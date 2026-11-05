"""予定表プログラム（第2回・正しい版）

使い方:
    py schedule.py 2026-10-02     指定した日の予定を時刻順に表示する
    py schedule.py                今日（日本時間）の予定を表示する

同じフォルダの schedule.json を読む。
"""
import json
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


def load_schedule():
    # schedule.py と同じフォルダにある予定表を探す
    path = Path(__file__).resolve().parent / "schedule.json"
    try:
        # JSONファイルを読み込んで、予定のリストとして返す
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"エラー: {path} が見つかりません。同じフォルダに置いてください。")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"エラー: {path} の中身が JSON として読めません（{e.lineno} 行目あたり）")
        sys.exit(1)
        
def filter_by_date(schedule, date):
    # 開始日時の日付が指定された日付と一致する予定だけを集める
    filtered = [
        event
        for event in schedule
        if datetime.fromisoformat(event["start"]).date().isoformat() == date
    ]
    # 開始日時順に並べ替える
    return sorted(filtered, key=lambda event: datetime.fromisoformat(event["start"]))


def format_event(event):
    # ISO形式の日時から、表示用の時刻を取り出す
    start = datetime.fromisoformat(event["start"])
    end = datetime.fromisoformat(event["end"])
    line = f'{start.strftime("%H:%M")}-{end.strftime("%H:%M")}  {event["title"]}'
    # 場所が無ければ、代わりに「場所なし」を表示する
    location = event.get("location") or "（場所なし）"
    line += f"  @{location}"
    return line


def main():
    # 日付の引数があればそれを使い、なければ日本時間の今日を使う
    if len(sys.argv) > 1:
        date = sys.argv[1]
    else:
        date = datetime.now(ZoneInfo("Asia/Tokyo")).date().isoformat()

    # ファイルを読み込み、予定を指定した日付で絞り込む
    schedule = load_schedule()
    if schedule is None:
        return

    events = filter_by_date(schedule, date)
    # 件数と、絞り込んだ予定を1件ずつ表示する
    print(f"{date} の予定 {len(events)} 件")
    for event in events:
        print(format_event(event))


if __name__ == "__main__":
    main()
