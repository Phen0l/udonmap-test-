"""
Geocode addresses with the Geospatial Information Authority of Japan (GSI) API.
"""
import json, time, urllib.parse, urllib.request
from pathlib import Path

DATA = Path("data/data.json")
CACHE = Path("data/geocode-cache.json")
USER_AGENT = "my-udon-map-starter/1.0 (public hobby map)"

def main():
    shops = json.loads(DATA.read_text(encoding="utf-8"))
    cache = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {}
    changed = 0
    last_request = 0.0
    for shop in shops:
        if shop.get("lat") is not None and shop.get("lng") is not None:
            continue
        address = (shop.get("address") or "").strip()
        if not address:
            continue
        if address in cache:
            result = cache[address]
        else:
            delay = 1.1 - (time.time() - last_request)
            if delay > 0:
                time.sleep(delay)
            
            # 国土地理院の住所検索APIを使用
            url = "https://msearch.gsi.go.jp/address-search/AddressSearch?" + urllib.parse.urlencode({
                "q": address
            })
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            try:
                with urllib.request.urlopen(req, timeout=20) as resp:
                    found = json.loads(resp.read().decode("utf-8"))
                last_request = time.time()
                
                # 国土地理院APIは geometry.coordinates に [経度(lng), 緯度(lat)] の順で返す
                if found and "geometry" in found[0] and "coordinates" in found[0]["geometry"]:
                    coords = found[0]["geometry"]["coordinates"]
                    result = {"lng": float(coords[0]), "lat": float(coords[1])}
                else:
                    result = None
            except Exception as exc:
                print(f"Geocode failed for {shop.get('name')}: {exc}")
                continue
            
            cache[address] = result
            CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            
        if result and result.get("lat") is not None and result.get("lng") is not None:
            shop["lat"], shop["lng"] = result["lat"], result["lng"]
            changed += 1
            print(f"Located: {shop['name']}")
        else:
            print(f"No confident match: {shop['name']}")
            
    DATA.write_text(json.dumps(shops, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Coordinates added: {changed}")

if __name__ == "__main__":
    main()
