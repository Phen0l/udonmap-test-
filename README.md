# 讃岐うどんマップ（AI generated）

このZIPには、初期店舗データ **50 店**を入れています。店舗名・住所は公開されている店舗一覧や紹介ページ等を参照してまとめた候補データです。最新営業状況を全店で個別確認したものではないため、`status: unverified` とし、営業時間・定休日は未確認のままにしています。麺・出汁タグも未確認を基本にし、一部は公開紹介文に基づく初期分類です。

## GitHubへの設置

1. ZIPをダウンロードし、PCで展開します。
2. GitHubで `my-udon-map` という Public repository を作ります。
3. `Add file` → `Upload files` で、展開したフォルダーの中身をアップロードしてコミットします（ZIP自体を置くだけでは動きません）。
4. `Settings` → `Pages` → `Build and deployment` → `Source` を `GitHub Actions` にします。
5. `Actions` タブで `Deploy map to GitHub Pages` の成功を確認します。

## 座標の設定

データ内の `lat` / `lng` は、誤った位置を表示しないよう初期状態では `null` です。GitHubの `Actions` タブで `Geocode missing shop coordinates` → `Run workflow` を実行すると、住所からOpenStreetMapのNominatimで座標取得を試みます。Nominatimの利用条件を守るため、リクエスト間隔を空け、結果をキャッシュします。検索結果が見つからない店舗は座標未設定のままです。結果は地図上で確認してください。

## 初期データの出典

- 香川県観光協会「うどん県旅ネット」: https://www.my-kagawa.jp/udon/list
- 本場さぬきうどん協同組合 店舗一覧: https://www.honba-sanukiudon.jp/shoplist/
- 一般社団法人日本うどん協会 会員リスト: https://japanudon.com/member/
- 高松観光コンベンション・ビューロー うどん食べ歩きマップ: https://www.takamatsu.or.jp/udon/
- 香川県産農畜水産物応援ポータル「讃岐の食」: https://sanukinoshoku.jp/

## 免責・データ利用

掲載情報は参考情報であり、実際の営業状況、営業時間、定休日、所在地等と一致しない場合があります。来店前に店舗の公式情報をご確認ください。誤りを見つけた場合は修正してください。店舗情報の取得・再公開は各情報源の利用条件を確認してください。

地図タイルおよび座標検索にはOpenStreetMap関連サービスを利用します。表示にはOpenStreetMap contributorsの帰属表示が必要です。Nominatimの利用条件は変更される場合があるため、実行前に最新のポリシーを確認してください。
