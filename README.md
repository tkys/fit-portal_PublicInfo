# fit-portal_PublicInfo
再生可能エネルギー発電事業の認定情報サイトからのデータセット構築

## 0.準備
データセットは[事業計画認定情報　公表用ウェブサイト](https://www.fit-portal.go.jp/PublicInfo)から別途取得しておく

---
>＜お知らせ＞
>　令和5年5月22日
>　再生可能エネルギー電気の利用の促進に関する特別措置法第９条第６項に基づき、
>　再生可能エネルギー発電事業計画の認定情報について公表いたします。
>　なお、今回、公表する認定情報は、4月30日時点にて新規認定を受けている又は新制度への移行手続が完了した
>　再生可能エネルギー発電設備（太陽光20kW未満を除く）に係る情報であり（ただし今回は紙媒体での新規申請、変更認定申請、
>　事前変更届出、事後変更届出、廃止届出は1月31日時点の情報となっております。）、
>　当該日時点において、新規認定申請中の案件及び新制度への移行手続が完了していない案件（電源接続案件募集プロセス等、
>　事業計画の提出が猶予されている案件を含む。）は公表対象になっておらず、今後、認定手続が完了したものについては、
>　一ヶ月ごとに情報を更新し、公表してまいります。
>
>【説明】
> - 事業計画の認定情報は、１ヵ月ごとに情報を更新して公表します。
> - 都道府県ごとにファイルが分かれているので、閲覧したいファイルをクリックしてダウンロードしてください。
> - 設備の所在地については、代表地番のみと全ての地番を表記したシートの２種類があります。
>   ただし、代表地番のみのシートで筆数の列が「０」と記載されている設備は、申請書に全ての地番が記載されておらず、
>   「他○筆」と記載されていたものであり、全ての地番が情報として登録されていないものです。
> - 廃棄等費用について、運転開始前のもの、現時点で定期報告の提出が確認されないもの、公表に同意が得られなかったものは、
>   それぞれ「運転開始前」「－」「開示不同意」と表示されています。定期報告が提出されてからデータが反映されるまでには、
>　　１～２ヶ月程度（電子報告の場合）を要します。
>
----
## 1.データ配置
都道府県ごとの.xlsxファイルは `./dataset`に保存しておく

## 2.merge
 `python main.py`
 
 marge_data_YYYYmm.csvが生成される
