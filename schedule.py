import json
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


def load_schedule():
    path = Path(__file__).resolve().parent / "schedule.json"
    if not path.exists():
        print(f"schedule.json が見つかりません。{path} に配置してください。")
        return None

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def filter_by_date(schedule, date):
    filtered = [
        event
        for event in schedule
        if datetime.fromisoformat(event["start"]).date().isoformat() == date
    ]
    return sorted(filtered, key=lambda event: datetime.fromisoformat(event["start"]))


def format_event(event):
    start = datetime.fromisoformat(event["start"])
    end = datetime.fromisoformat(event["end"])
    line = f'{start.strftime("%H:%M")}-{end.strftime("%H:%M")}  {event["title"]}'
    location = event.get("location") or "（場所なし）"
    line += f"  @{location}"
    return line


def main():
    if len(sys.argv) > 1:
        date = sys.argv[1]
    else:
        date = datetime.now(ZoneInfo("Asia/Tokyo")).date().isoformat()

    schedule = load_schedule()
    if schedule is None:
        return

    events = filter_by_date(schedule, date)
    print(f"{date} の予定 {len(events)} 件")
    for event in events:
        print(format_event(event))


if __name__ == "__main__":
    main()
