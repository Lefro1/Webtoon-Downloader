from pathlib import Path

root = Path(__file__).resolve().parent.parent

src = root / "webtoon_js_grabbers" / "webtoon_metadata_sep_2026"
dst = root / "helpers" / "webtoon_homepage.txt"

seen = set()
entries = []

for line in src.read_text(encoding="utf-8").splitlines():
    parts = line.split("|")
    if len(parts) < 4 or parts[0] == "title":
        continue

    title = parts[0].strip()
    url = parts[-1].strip()

    if not title or not url:
        continue

    entry = f"{title}|{url}"

    if entry not in seen:
        seen.add(entry)
        entries.append(entry)

entries.sort(key=lambda x: x.split("|", 1)[0].lower())

dst.write_text("\n".join(entries) + "\n", encoding="utf-8")
