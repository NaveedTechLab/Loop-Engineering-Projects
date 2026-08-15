#!/usr/bin/env python3
"""
brief.py — the Morning Brief.

Fetches today's top Hacker News stories and reports only the ones that
weren't in yesterday's (or the last run's) top list. Uses seen-stories.txt
as its spine: read first, written last. Delete that file and every story
looks "new" again — that is "no spine, no loop."

No API key needed. The Hacker News API is free and public.
"""

import json
import sys
import urllib.request
from pathlib import Path

TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"
HOW_MANY = 10

STATE_FILE = Path(__file__).resolve().parents[4] / "seen-stories.txt"


def fetch_json(url: str):
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        print(f"ERROR: could not reach Hacker News: {e}", file=sys.stderr)
        sys.exit(1)


def fetch_top_stories() -> list[dict]:
    ids = fetch_json(TOP_STORIES_URL)
    if not ids:
        print("ERROR: no story IDs returned", file=sys.stderr)
        sys.exit(1)

    stories = []
    for story_id in ids[:HOW_MANY]:
        item = fetch_json(ITEM_URL.format(story_id))
        if item and item.get("title"):
            stories.append(
                {
                    "id": story_id,
                    "title": item.get("title", "(no title)"),
                    "score": item.get("score", 0),
                    "url": item.get("url", f"https://news.ycombinator.com/item?id={story_id}"),
                }
            )
    return stories


def read_seen_ids() -> set[str]:
    if not STATE_FILE.exists():
        return set()
    return set(STATE_FILE.read_text().strip().splitlines())


def write_seen_ids(ids: list[str]) -> None:
    STATE_FILE.write_text("\n".join(ids) + "\n")


def main() -> None:
    stories = fetch_top_stories()
    seen_ids = read_seen_ids()

    new_stories = [s for s in stories if str(s["id"]) not in seen_ids]
    is_first_run = len(seen_ids) == 0

    print("  📰  MORNING BRIEF — Hacker News Top Stories")
    print("  " + "─" * 56)

    if is_first_run:
        print("     (first run — showing today's full top 10)")
        to_show = stories
    elif not new_stories:
        print("     ✓  Nothing new since last brief. All caught up.")
        to_show = []
    else:
        print(f"     {len(new_stories)} new stor{'y' if len(new_stories)==1 else 'ies'} since last brief:")
        to_show = new_stories

    for s in to_show:
        print(f"     • {s['title']}")
        print(f"       {s['score']} points — {s['url']}")

    print("  " + "─" * 56)

    write_seen_ids([str(s["id"]) for s in stories])


if __name__ == "__main__":
    main()
