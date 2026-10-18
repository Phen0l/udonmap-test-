import json
from pathlib import Path

def main():
    path = Path("data/data.json")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise SystemExit("data/data.json must be a JSON array")
    seen = set()
    errors = []
    for i, s in enumerate(data, 1):
        if not s.get("id") or not s.get("name"):
            errors.append(f"{i}: id/name missing")
        if s.get("id") in seen:
            errors.append(f"{i}: duplicate id {s.get('id')}")
        seen.add(s.get("id"))
        for k, lo, hi in (("lat",-90,90),("lng",-180,180)):
            v = s.get(k)
            if v is not None and (not isinstance(v,(int,float)) or not lo <= v <= hi):
                errors.append(f"{i}: invalid {k}")
        if (s.get("lat") is None) != (s.get("lng") is None):
            errors.append(f"{i}: lat/lng must both be null or both numeric")
    if errors:
        print("\\n".join(errors)); raise SystemExit(1)
    print(f"OK: {len(data)} shops")
if __name__ == "__main__":
    main()
