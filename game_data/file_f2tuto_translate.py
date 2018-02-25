#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

# Note:
# This file is a bit different to the section_*_translate files,
# in that the Japanese to be translated is BEFORE the ???.
# Put the translations in the ???
# \n is a linebreak
# \0 is the end of the string
# \' is a single quote

translate_map = {
"３\nチュートリアルの使い方\nこのゲームは基本的なプレイは簡単ですが、より高度なプ\nレイを行うためには、様々なシステムを把握し、使いこな\nす必要があります。$n\nしかし、まずはゲームに慣れて下さい。\nそのプレイの中で、様々なシステムに関するより深い理解\nが必要となるでしょう。$n\nそのときに、このチュートリアルを活用して下さい。\nはじめから全てを理解してプレイすることは不可能です。\nまずは「はじめに」の項目に一通り目を通すだけでかまい\nません。\n\0\0\0\0":
'???',

"３\nゲーム進行のヒント\nこのゲームでは、ゲームを進行させるために果たさなけれ\nばならない目的は、きわめて少ないゲームです。\n特にシナリオ２以降では、ゲームを進行させるために必要\nなおつかい、フラグ立てはほとんどありません。$n\n使徒が出現するまでの時間を、プレイヤーが自由に使って\nいいのです。\n既存のゲームのように、何かをしないと先に進めなくなる\nことはありません。$n\nシナリオ１では、シナリオを進行させるために特定の場所\nへ移動したり、時間の経過を待つ箇所があります。\nシナリオの進行が先に進まないと感じたら、いろんな場所\nに移動してみましょう。\n\0\0\0\0":
'???',

"３\nゲームの目的\nこのゲームには、様々な目的、楽しみ方があります。\nパイロットプレイで、日常生活と使徒との戦闘を楽しむ。\n用意されたイベントをこなしてゆく。\nお気に入りのキャラと仲良くなる。$n\n裏方にまわり、パイロットとネルフをバックアップする。\n目的もなく、第３新東京市での生活を楽しんでもよし。\nそれぞれの目的には、それぞれの攻略方法、面白さがあり\nます。$n\nこのゲームで出来る様々な行動を駆使、工夫して、あなた\nの目的を達成して下さい。\n最初は各シナリオのイベントをこなしていくのを目的にプ\nレイするとよろしいでしょう。\n\0\0":
'???',

"４\n生活パートの流れ\n使徒との戦闘までのひととき、登場人物たちは第３新東京\n市で生活を行います。\nこの第３新東京市での生活を、生活パートと呼びます。$n\n生活パートでは、学生は学校に行き、ネルフの職員はネル\nフで業務を行います。\nそしてプレイヤーキャラは、夜の就寝時間まで活動可能で\nす。$n\n就寝時間が来ると、プレイヤーキャラは、その日の行動は\n終了となり、翌日の朝まで就寝します。\nこの生活のサイクルが、使徒が出現するまで繰り返されま\nす。$n\n生活パートの時間の中で技能を上げたり、他のキャラとの\nコミュニケーションを行ってください。\nΑΤを上昇させたり、インパルスを溜めるのも重要な行動\nです。\n\0\0\0":
'???',

"４\nΑΤとインパルス\nΑΤとインパルスは、このゲームの中で最も重要なパラ\nメータです。\nこれらのパラメータは画面下に表示され、刻々と変化する\n様子を確認できます。$n\nΑΤとは、どれだけ心を開放しているかを表したパラメー\nタです。\nΑΤが高いほど心が開いている状態で、ΑΤが低いほど心\nが閉ざされている状態となります。$n\nインパルスは行動衝動、いわば何かを行うときの行動力を\n表したパラメータで、重要な行動はインパルスを消費する\nことで実行できます。$n\nΑΤが高く、インパルスも多い状態が、理想のコンディ\nションです。\nゲーム中では、常にこの状態を維持するよう、心がけてく\nださい。\n\0\0\0":
'???',

"４\nΑΤを上げるには\nΑΤは、楽しい出来事により上昇し、つらい出来事により\n下降します。\n出来事は記憶として蓄積され、その記憶からΑΤが算出さ\nれるからです。$n\n楽しい出来事、すなわちいい記憶が多いほど、ΑΤは高い\n値が算出されることになります。\n逆に、つらい出来事、すなわち悪い記憶が多いほど、ΑΤ\nは低い値となります。$n\nΑΤに影響を与える記憶以外の要素に、体調があります。\n体調が低いと、ΑΤの値が低い値に修正されます。\n逆もあり、体調が高いと、ΑΤの値が高い値に修正されま\nす。$n\n他にも、庵野ＡＩによる影響などで、ΑΤの値に修正が加\nわります。\nΑΤを上げるには、楽しい出来事を多く経験し、体調を高\nく保つのがセオリーとなります。\n\0\0\0\0":
'???',

"３\nインパルスを上げるには\nインパルスは、キャラがつらい出来事を経験することで増\n加し、溜まっていくパラメータです。\nこのときΑΤが低いほど、インパルス増加の量は大きくな\nります。\n逆にΑΤが高いと、インパルスはなかなか増加しません。$n\nまた、インパルスはそのＭＡＸ値が増加するパラメータで\nす。これは、インパルスをたくさん消費するほど、その\nＭＡＸ値は上がります。\nインパルスのＭＡＸ値が上がるのは、朝、キャラが起床す\nるタイミングです。$n\nΑΤが低いときに、インパルスを増加、消費することで、\nＭＡＸ値を上げるチャンスとなります。\n\0\0":
'???',

"３\n様々な生活行動\nこのゲームでは、様々な行動を生活の中で実行することが\nできます。\n行動は大きく分けると、他の人物とのコミュニケーション、\n特定場所での行動、一人で完結する行動に分けられます。$n\n行動によっては、ΑΤの条件（ΑΤが低すぎる／高すぎる）\nや、消費するインパルスが設定されており、その内容は行\n動選択肢に表示され、実行できない行動は灰色表示となり\nます。$n\nまた、そのときの時間や場所、感情や相手との人間関係な\nど、様々なシチュエーションによっても実行可能な行動は\n変化します。\nいろんな場所で○ボタンを押して、いろんな行動を試して\nみましょう。\n\0":
'???',

"４\n人間関係\n人間関係は、△ボタンでのシステムメニューの「人間関係」\nにて確認できます。\n人間関係は、相手への関心（横軸）と、相手への好意（縦\n軸）で表現されます。$n\n関心と好意は、相手へ何かしら行動を行うことで、その行\n動に応じて変化します。\n変化の様子は、人間関係の変化履歴としてポイントとして\n残ります。$n\n関心と好意は変化後、元の場所に戻ろうとします。\nこれは、人間関係の表に表示されている透明の楕円が、円\nの形に戻ろうとするのにひきづられるためです。\n人間関係はすぐに変化させることはできませんので、長い\nスパンで仲良くなってください。$n\nまた関心と好意は、関心は無し、好意は普通のポイントへ\nとゆっくり変化しています。\n長いことコミュニケーションを行わないキャラとは疎遠に\nなってしまうので注意してください。\n\0":
'???',

"３\n時間の経過\n生活パートでは、常に時間が経過し、特定の時間になると\n使徒が出現します。\n使徒が出現するまでの時間を、どのように過ごすかはプレ\nイヤーにゆだねられます。$n\n他人とのコミュニケーション、技能の訓練、ネルフでの業\n務、アイテムの入手など、自由に行動してください。\n学生のキャラであれば、ＡＭ０８：００〜ＰＭ０３：００\nの間に登校することで、授業に参加できます。$n\nなにもする事がなければ、さっさと就寝してかまいません。\n就寝時間はキャラにより異なりますが、夜中の１時前後を\n目安に行動してください。\n起床時間もキャラにより異なります。就寝時間＋６時間が\n起床時間となります。\n\0\0\0":
'???',

"３\nキャラの行動\nプレイヤーキャラ以外のキャラも、プレイヤーキャラ同様\nに行動しているのがこのゲームの特徴です。\nこれらのキャラは様々な「欲望」により行動内容を決定し\nています。$n\n欲望にはトイレに行きたい欲望や、仕事をしたい欲望など\n１６種類があり、それぞれ欲望の強さが異なります。\n各欲望の強さは、現在の体調、時間、場所、相手、シチュ\nエーション、などで複雑に変動します。$n\nそして一番強い欲望が選択され、その欲望を満たす行動が\n実行されます。\n喉を潤したい欲望が選択されたら、自動販売機でジュース\nを購入する、といった具合です。\n\0\0":
'???',

"４\n記憶\nキャラは行動を行うと、その行動の内容を記憶します。\nこのとき、行動の内容が楽しい出来事であるならば、いい\n記憶が記憶され、結果ΑΤを上昇させます。\n逆に、行動の内容が辛い出来事であるならば、悪い記憶が\n記憶され、結果ΑΤを下降させます。$n\nそして記憶は時間の経過とともに薄れていきます。\nいい記憶も悪い記憶も、時間の経過で薄れることにより、\nそれによるΑΤの上昇、下降が和らぎます。\nキャラが何もしていないのにΑΤの変動が発生するのはそ\nのためです。$n\nいい記憶、悪い記憶により変化したΑΤが、記憶が薄れる\nことにより、以前の値に近づくためです。$n\nまた、記憶された内容は、会話の中で話されることがあり\nます。\n他のキャラに最近の出来事を聞いてみましょう。意外な出\n来事が聞けるかも知れません。\n\0\0\0\0":
'???',

"３\n感情の変化\nキャラには２７の感情があり、行った行動、受けた行動に\nよって感情は変化します。\n感情の変化は会話後の人間関係変化情報で確認でき、シス\nテムメニューのステータスでも確認できます。$n\n感情は時間とともに「平穏」の感情に戻って行きます。\n感情により、制限される行動、実行できるようになる行動\nなどがあります。$n\nまたプレイヤー以外のキャラは、感情によっても欲望に修\n正が発生します。\n感情が「怒り」のキャラにはしばらく話し掛けないなどの\n配慮が必要です。\n\0\0\0":
'???',

"４\n体調管理\n体調には「空腹／水分／眠気／ＷＣ／風呂」の５つがあり、\nシステムメニューのステータスで確認できます。\n体調は時間の経過で減少してゆき、食事をするなどの行動\nで回復することができます。$n\n体調が低いとΑΤが減少する修正が発生し、逆に、体調が\n高いとΑΤが増加する修正が発生します。\nΑΤを高く維持するためにも、体調を高い状態で維持する\n必要があります。$n\n逆にΑΤを低くするために、体調を低いままにする手段も\nあります。$n\nまたプレイヤー以外のキャラは、体調によっても欲望に修\n正が発生します。\nトイレに行きたいキャラ、お腹の空いたキャラには、嫌わ\nれないためにも話し掛けないほうが無難です。\n\0\0":
'???',

"４\n技能とその効果\n技能には全員に共通する「事務技能／情報技能／白兵技能」\nの３つの技能と、キャラにより「シンクロ技能／参謀技能\n／開発技能／オペレート技能／諜報技能」があります。$n\n技能は、システムメニューのステータスで確認できます。\n技能が高いことで、特定の効果判定パルスが成功しやすく\nなります。$n\nまたパイロットキャラの場合、白兵技能が高いと、戦闘補\n助効果の時間が長くなり、シンクロ技能が高いと、移動速\n度の向上、ヘイフリック回復速度の向上、チャージ時間の\n短縮などが期待出来ます。$n\n技能は訓練することにより、上昇させることができます。\nただし訓練のための効果判定パルスは、技能が高いほど成\n功しにくくなるので注意が必要です。\n\0\0\0":
'???',

"４\n判定パルス\n判定パルスとは、プレイヤーが行った行動の結果判定を行\nう反射ゲームです。\n技能訓練や授業行動、特定の戦闘やイベントなど、ゲーム\nの様々な場所で発生します。\n判定パルスには、効果判定パルスと、成否判定パルスの二\nつのタイプがあります。$n\n判定パルスは、左右に伸縮する３本のバーに対応するボタ\nンを、バーの先端が成功領域に接触しているタイミングで\n押せば成功となり、これを失敗するまで１０回行います。\n違うボタンを押す、成功タイミングにボタンを押さない、\n成功以外のタイミングにボタンを押すことで失敗となり、\nその時点で判定パルスは終了となります。$n\n効果判定パルスは、成功回数が多くなるほど、結果が良く\nなっていきます。\n成否判定パルスは、１０回全部成功することで、結果は成\n功、そうでなければ失敗の結果となります。\nまた、効果判定パルスのほうが、伸縮バーの伸縮速度の増\n加は大きいです。$n\n成功領域の幅は、有利要素、不利要素、ΑΤの値で変化し\nます。\n有利要素とΑΤの値が高いほど広がり、不利要素の値が高\nいほど狭くなります。\n判定パルスの難易度を下げるには、ΑΤの値を高く保つの\nがセオリーです。\n\0\0":
'???',

"３\n被災による影響\n使徒との戦闘で、第３新東京市への被害が発生すると、そ\nの被害の大きさにより影響が発生します。\nコンビニの品揃えが悪くなったり、クラスメイトが疎開で\nいなくなったりします。$n\n被災が最も進むと、第３新東京市での生活は不可能となり、\n民間人は全て疎開、生活の場もネルフ本部のみとなります。$n\n第３新東京市で生活している人々のためにも、戦闘での都\n市への被害は抑える努力が必要です。\n\0\0\0\0":
'???',

"４\n庵野ＡＩ\n庵野ＡＩは、プレイヤーのプレイ動向により、ゲームバラ\nンスへの介入を行う機能です。\n前回の生活パートと戦闘パートのプレイ内容より、次の生\n活パートへの影響を変化させます。$n\n庵野ＡＩによるプレイ内容判断は、どんな行動を行ったか、\nどんな場所にいたか、ΑΤの値はどうだったかなどです。$n\n庵野ＡＩによる影響は、生活パート開始時に人間関係を変\n化させたり、ΑΤや感情に対し常に修正を行うなどです。\n影響の中には、大きくΑΤを減少させる影響などがあり、\nゲームの進行を困難にさせるものもあります。$n\n戦闘中では、庵野ＡＩの条件満たせば、ΑΤが上昇する修\n正が発生したりします。\n※庵野ＡＩは、シナリオ１では機能しません。\n\0":
'???',

"３\nデフコン\nデフコンとは「ディフェンス・コンディション」の略で、\n防衛体制を意味します。\nこのゲームでは、平時はデフコン５、使徒出現の直前でデ\nフコン１となります。$n\n画面左上の時計の隣にデフコンは表示されます（シナリオ\n１では非表示）。\n時間経過とともにデフコンがカウントダウンされていくの\nで、戦闘開始までの時間の目安となります。$n\nデフコンが１になるまでの生活パートの時間を有効に利用\nしてください。\n※デフコンは、シナリオ１では機能しません。\n※一部のイベントでは、デフコンには関係なく使徒が出現\n　します。\n\0\0\0":
'???',

"１\nパイロットの心得\nパイロットキャラでプレイする場合、生活パートでは使徒\nとの戦闘に備えておく必要があります。\n白兵技能の訓練、シンクロ技能の訓練、ΑΤとインパルス\nを高く保つ、余裕があれば、他のパイロットのΑΤも高く\nなるようにしてもいいでしょう。\n\0":
'???',

"２\nお金の入手方法\nお金は月に一度、学生キャラはお小遣いとして、大人キャ\nラは給与として、生活パート開始時に所持金が増加します。\nシンジとアスカにおいては、ミサトに対して小遣いの要求\n行動を実行する必要があります。$n\n別なお金の入手方法は、他のキャラに対してお金をねだる\n行動を行うことです。\nねだれる金額はキャラによって異なります。お金をたくさ\nん持っているキャラにねだりましょう。\n\0\0\0\0":
'???',

"２\nアイテム入手方法\nアイテムは、コンビニで購入することで入手できます。\n他のキャラに「アイテムをねだる」や「アイテムの交換を\n提案」を行い、入手することもできます。\n他のキャラがアイテムをプレゼントしてくれる場合もあり\nます。$n\n一部のアイテムは「弁当を作る」などで入手できます。\n\0\0\0\0":
'???',

"２\nハーモニクステスト\nパイロットキャラプレイの場合、ネルフ施設にてリツコか\nマヤに「ハーモニクステストの依頼」を行い了承されれば、\nハーモニクステストを実行することができます。$n\nハーモニクステストでは効果判定パルスによる判定が行わ\nれ、その結果によりΑΤの増減が発生します。\n\0\0\0":
'???',

"２\nシンクロ技能訓練\nパイロットキャラプレイの場合、ネルフ施設にてリツコか\nマヤに「シンクロ技能訓練の依頼」を行い了承されれば、\nシンクロ技能訓練を実行することができます。$n\nシンクロ技能訓練では効果判定パルスによる判定が行われ、\nその結果によりシンクロ技能が上昇します。\n\0":
'???',

"４\n勝敗条件\n戦闘に勝利するには、使徒の耐久力を０にして、これを殲\n滅する必要があります。\n戦闘に敗北となる条件は２つあり、一つ目はプレイヤー\nキャラのエヴァの耐久力が０になる。二つ目はネルフ本部\nが使徒の攻撃を受け、その耐久度が０になることです。$n\n使徒は第３新東京市のゼロエリアを目指して侵攻し、ゼロ\nエリア突破後はジオフロントを侵攻、ネルフ本部へと迫り\nます。\nエヴァのパイロット達は、その前に使徒の侵攻を食い止め、\nこれを殲滅しなければなりません。$n\n勝敗条件には直接関係しませんが、第３新東京市の被害も\n重要です。\n第３新東京市の迎撃施設が使徒の攻撃を受け、被害を受け\nることにより、\n次の戦闘から、より不利な条件で戦うことになります。$n\n使徒を倒し続けるためにも、エヴァと第３新東京市の被害\nを最小限にしつつ、戦いを繰り返す必要があります。\n\0":
'???',

"２\n使徒の出現\n使徒の出現警報であるデフコンが１になると、使徒が第３\n新東京市に出現し戦闘が開始されます。\n戦闘開始前、使徒の正確な初期位置は確定しておらず、使\n徒出現予想円の情報のみでエヴァの初期配置位置が設定さ\nれます。$n\n戦闘開始時、使徒の初期位置が判明、使徒はゼロエリアへ\nと侵攻をはじめます。\n※シナリオ１では、デフコンは機能していません。使徒は\n　イベントに連動して出現します。\n\0\0\0":
'???',

"４\nアンビリカルケーブル\nエヴァは電力で駆動し、この電力は電源ビルからアンビリ\nカルケーブルを通して供給されます。$n\nアンビリカルケーブルは電源ビルとエヴァを繋ぐ有限の\nケーブルです。\nアンビリカルケーブルが届く範囲内でしか電力を供給でき\nません。$n\nエヴァがアンビリカルケーブルの範囲外で行動するには、\n別の電源ビルのアンビリカルケーブルに繋ぎなおすか、ア\nンビリカルケーブルを切断して、エヴァの体内に残された\n予備電源を消費することで、短時間だけアンビリカルケー\nブル無しで活動できます。$n\n予備電源が切れるとエヴァは活動停止となり、一切の行動\nが出来なくなります。\n予備電源が切れる前に、アンビリカルケーブルを再接続す\nる必要があります。\n\0\0\0":
'???',

"３\n使徒の移動と索敵\n使徒は移動中、強力な妨害電波を放っているため正確な位\n置を特定することができません。\n使徒の位置が判別できるのは、第３新東京市の迎撃施設の\n索敵範囲内に使徒がいるときか、\n他のエヴァの目視範囲に捕らえられている時だけです。$n\nそれ以外の時は、使徒の最終確認位置から推測される使徒\nの予想侵攻ルートを頼りに、使徒の現在位置を予測する必\n要があります。$n\n第３新東京市の迎撃施設が数多く存在するほど、使徒の位\n置が索敵しやすくなります。\nこのため、使徒との戦闘を有利に進めるためにも、迎撃施\n設は重要な役割を果たします。\n\0\0":
'???',

"４\n使徒への攻撃\n使徒への攻撃は、エヴァの射程範囲に使徒が入った状態で\n○ボタンを押し、攻撃コマンドを実行することで行われま\nす。$n\nエヴァの射程範囲は、エヴァ周囲にある半透明な扇状の範\n囲です。\n装備武器によりエヴァ前方にも半透明な範囲が発生し、こ\nれもエヴァの射程範囲となります。$n\n使徒への攻撃コマンドは、エヴァと使徒との位置によって\nも変化します。\n使徒を正面に位置しているならば、「プログナイフで突く」\nが行え、使徒が横に位置しているならば、「ミドルキック」\nが行えます。$n\n使徒からの攻撃もエヴァ同様、使徒の射程範囲にエヴァが\n入った状態で行われます。\n\0\0":
'???',

"４\nより有利に戦うために\n使徒との戦闘を有利に進めるために、いくつか基本的なテ\nクニック、戦術があります。$n\n＝戦闘補助コマンドを利用しましょう＝\n「姿勢を構える」や「狙いをつける」などの戦闘補助コマ\nンドで、戦闘行動の効果を高めることができます。\n戦闘補助コマンドを実行するには、インパルスを消費しま\nす。インパルスの残量に注意してください。$n\n＝エヴァ複数で同時に攻撃しましょう＝\n使徒を囲むエヴァが多いほど、使徒のΑΤフィールドを中\n和することが出来ます。\nまた、使徒のヘイフリックが回復しないうちに、複数のエ\nヴァで次々と攻撃することも重要です。$n\nエヴァ複数で同時に攻撃するためにも、他のエヴァの行動\nに注意しましょう。\n\0\0\0\0":
'???',

}