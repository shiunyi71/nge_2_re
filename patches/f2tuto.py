#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

# Note:
# This file is a bit different to the section_*_translate files,
# in that the Japanese to be translated is BEFORE the ???.
# Put the translations in the ???
# \n is a linebreak
# \0 is the end of the string
# ' is a single quote
# \" is a double quote

# The number １ to ４ starting each entry is the number of pages
# it uses to display in-game. Keep them in SJIS format.

# Technical limits:
# Excluding the header line, (which is the # of pages and title),
# there is a limit of 5 lines per page.
# To end a page, use $n\n\n
#
# Text can't be more than 64 characters or else it crashes (counting \n as 1 character, excluding \0 in the count)
# Though only 54 characters (counting \n as 1 character) display on a line before being badly wrapped

translate_map = {
"３\nチュートリアルの使い方\n"
"このゲームは基本的なプレイは簡単ですが、より高度なプ\n"
"レイを行うためには、様々なシステムを把握し、使いこな\n"
"す必要があります。$n\n"
"しかし、まずはゲームに慣れて下さい。\n"
"そのプレイの中で、様々なシステムに関するより深い理解\n"
"が必要となるでしょう。$n\n"
"そのときに、このチュートリアルを活用して下さい。\n"
"はじめから全てを理解してプレイすることは不可能です。\n"
"まずは「はじめに」の項目に一通り目を通すだけでかまい\n"
"ません。\n\0":

"３\nHow to Use the Tutorial\n"
"While the basic gameplay is simple, various\n"
"systems need to be understood and mastered in\n"
"order to achieve a higher level of play.$n\n"
"That said, you should first familiarize yourself\n"
"with the game.\n"
"A deeper understanding of the various systems\n" 
"becomes necessary while you're playing it, after\n"
"all.$n\n" 
"At that time, please make use of this tutorial.\n"
"It's impossible for a new player to understand\n"
"everything right away.\n"
"So, to start with, concern yourself only with\n"
"skimming through the \"Introduction\" entries.\n\0",

##############################################################################

"３\nゲーム進行のヒント\n"
"このゲームでは、ゲームを進行させるために果たさなけれ\n"
"ばならない目的は、きわめて少ないゲームです。\n"
"特にシナリオ２以降では、ゲームを進行させるために必要\n"
"なおつかい、フラグ立てはほとんどありません。$n\n"
"使徒が出現するまでの時間を、プレイヤーが自由に使って\n"
"いいのです。\n"
"既存のゲームのように、何かをしないと先に進めなくなる\n"
"ことはありません。$n\n"
"シナリオ１では、シナリオを進行させるために特定の場所\n"
"へ移動したり、時間の経過を待つ箇所があります。\n"
"シナリオの進行が先に進まないと感じたら、いろんな場所\n"
"に移動してみましょう。\n\0":

"３\nHints for Game Progression\n"
"This game is light on objectives that must be\n"
"achieved in order to progress. Within Scenarios 2\n" 
"and up especially, there are almost no required\n"
"missions or flags to be raised.$n\n" 
"It's fine for the player to use the time freely up\n"
"until an Angel appears.\n"
"As in existing games, things keep moving ahead even\n"
"when you take no action.$n\n"
"Progressing in Scenario 1 may depend on things like\n"
"time elapsing or going to specific locations.\n"
"If you feel the scenario is not moving ahead, try\n"
"visiting different places.\n\0",

##############################################################################

"３\nゲームの目的\n"
"このゲームには、様々な目的、楽しみ方があります。\n"
"パイロットプレイで、日常生活と使徒との戦闘を楽しむ。\n"
"用意されたイベントをこなしてゆく。\n"
"お気に入りのキャラと仲良くなる。$n\n"
"裏方にまわり、パイロットとネルフをバックアップする。\n"
"目的もなく、第３新東京市での生活を楽しんでもよし。\n"
"それぞれの目的には、それぞれの攻略方法、面白さがあり\n"
"ます。$n\n"
"このゲームで出来る様々な行動を駆使、工夫して、あなた\n"
"の目的を達成して下さい。\n"
"最初は各シナリオのイベントをこなしていくのを目的にプ\n"
"レイするとよろしいでしょう。\n\0":

"３\nGameplay Goals\n"
"In this game, there are various objectives and\n" 
"many ways to have fun.\n"
"Enjoy both everyday life and fighting against the\n"
"Angels when playing as a pilot.\n"
"Stay on top of forthcoming events.\n"
"Befriend your favorite characters.$n\n"
"Backup the pilots and Nerv from behind the scenes.\n"
"You can also enjoy life in Tokyo-3 aimlessly.\n"
"Each objective has its own strategy and fun.$n\n"
"Through creative use of the various commands possible in the\n"
"game, go and achieve your goals!\n"
"At first it's probably best to play with a mind toward\n"
"completing each scenario's events.\n\0",

##############################################################################

"４\n生活パートの流れ\n"
"使徒との戦闘までのひととき、登場人物たちは第３新東京\n"
"市で生活を行います。\n"
"この第３新東京市での生活を、生活パートと呼びます。$n\n"
"生活パートでは、学生は学校に行き、ネルフの職員はネル\n"
"フで業務を行います。\n"
"そしてプレイヤーキャラは、夜の就寝時間まで活動可能で\n"
"す。$n\n"
"就寝時間が来ると、プレイヤーキャラは、その日の行動は\n"
"終了となり、翌日の朝まで就寝します。\n"
"この生活のサイクルが、使徒が出現するまで繰り返されま\n"
"す。$n\n"
"生活パートの時間の中で技能を上げたり、他のキャラとの\n"
"コミュニケーションを行ってください。\n"
"ΑΤを上昇させたり、インパルスを溜めるのも重要な行動\n"
"です。\n\0":

"４\nDaily Life Part\'s Flow\n"
"Up until the fight with an Angel, the characters\n"
"conduct their day-to-day lives in Tokyo-3.\n"
"This life in Tokyo-3 is called the Daily Life Part.$n\n"
"In the Daily Life Part, students go to school, and\n"
"Nerv personnel perform their duties at Nerv.\n"
"Furthermore, the player character can be active up\n"
"until their nightly bedtime.$n\n"
"When bedtime arrives, the player character's\n"
"daytime activities come to an end, and they retire\n"
"until the following morning.\n"
"This cycle is repeated until an Angel arrives.$n\n"
"To boost your abilities during the Daily Life Part,\n"
"you should engage in communications with other\n"
"characters.\n"
"It's also important to accumulate Impulse to make\n"
"your AT go up.\n\0",

##############################################################################

"４\nΑΤとインパルス\n"
"ΑΤとインパルスは、このゲームの中で最も重要なパラ\n"
"メータです。\n"
"これらのパラメータは画面下に表示され、刻々と変化する\n"
"様子を確認できます。$n\n"
"ΑΤとは、どれだけ心を開放しているかを表したパラメー\n"
"タです。\n"
"ΑΤが高いほど心が開いている状態で、ΑΤが低いほど心\n"
"が閉ざされている状態となります。$n\n"
"インパルスは行動衝動、いわば何かを行うときの行動力を\n"
"表したパラメータで、重要な行動はインパルスを消費する\n"
"ことで実行できます。$n\n"
"ΑΤが高く、インパルスも多い状態が、理想のコンディ\n"
"ションです。\n"
"ゲーム中では、常にこの状態を維持するよう、心がけてく\n"
"ださい。\n\0":

"４\nAT & Impulse\n"
"AT and Impulse are the most important parameters\n"
"in this game.\n"
"They are displayed at the bottom of the screen and\n"
"visibly change from one moment to the next.$n\n"
"AT shows how open someone's heart is.\n"
"The higher someone's AT, the more their heart\n"
"opens up. The lower the AT, the more their heart\n"
"closes off.$n/n"
"Impulse shows the urge to act, or the energy when\n"
"doing something. Consuming impulse makes important\n"
"actions possible.$n\n"
"A high AT and plentiful impulse are ideal.\n"
"Always try to maintain both while you're playing.\n\0",

##############################################################################

"４\nΑΤを上げるには\n"
"ΑΤは、楽しい出来事により上昇し、つらい出来事により\n"
"下降します。\n"
"出来事は記憶として蓄積され、その記憶からΑΤが算出さ\n"
"れるからです。$n\n"
"楽しい出来事、すなわちいい記憶が多いほど、ΑΤは高い\n"
"値が算出されることになります。\n"
"逆に、つらい出来事、すなわち悪い記憶が多いほど、ΑΤ\n"
"は低い値となります。$n\n"
"ΑΤに影響を与える記憶以外の要素に、体調があります。\n"
"体調が低いと、ΑΤの値が低い値に修正されます。\n"
"逆もあり、体調が高いと、ΑΤの値が高い値に修正されま\n"
"す。$n\n"
"他にも、庵野ＡＩによる影響などで、ΑΤの値に修正が加\n"
"わります。\n"
"ΑΤを上げるには、楽しい出来事を多く経験し、体調を高\n"
"く保つのがセオリーとなります。\n\0":

"４\nBoosting AT\n"
"AT goes up in response to positive experiences,\n" 
"while negative ones make it go down.\n"
"This is because day-to-day events are stored as\n" 
"memories, from which AT is calculated.$n\n"
"More frequent pleasant experiences, or good\n" 
"memories, will result in a higher AT value.\n"
"Conversely, more frequent harsh experiences, or\n" 
"bad memories, will result in a lower AT value.$n\n"
"Another element that influences AT is\n" 
"physical condition.\n"
"When physical condition is poor, the AT value\n" 
"plummets. Inversely, when physical condition is\n" 
"good, AT value escalates.$n\n"
"Additional shifts in AT value are imposed via the\n"
"effects of the Anno A.I.\n"
"To sum up, you boost AT by experiencing plenty of\n"
"positive events and maintaining good health.\n\0",

##############################################################################

"３\nインパルスを上げるには\n"
"インパルスは、キャラがつらい出来事を経験することで増\n"
"加し、溜まっていくパラメータです。\n"
"このときΑΤが低いほど、インパルス増加の量は大きくな\n"
"ります。\n"
"逆にΑΤが高いと、インパルスはなかなか増加しません。$n\n"
"また、インパルスはそのＭＡＸ値が増加するパラメータで\n"
"す。これは、インパルスをたくさん消費するほど、その\n"
"ＭＡＸ値は上がります。\n"
"インパルスのＭＡＸ値が上がるのは、朝、キャラが起床す\n"
"るタイミングです。$n\n"
"ΑΤが低いときに、インパルスを増加、消費することで、\n"
"ＭＡＸ値を上げるチャンスとなります。\n\0":

# [NOTE] Will fix the wording when I'm more certain what it's talking about, specifically the first and last sentences. -R
"３\nBoosting Impulse\n"
"Impulse is a parameter that increases and continues\n"
"accumulating when a character has trying\n" 
"experiences. At these times, the lower one's AT,\n"
"the larger the increase in impulse. Conversely, a\n"
"higher AT won't cause as much of an increase.$n\n"
"Impulse's maximum value can also go up. This\n"
"happens in the morning when a character gets out\n"
"of bed.\n" 
"The more impulse consumed the previous day, the more\n"
"the max value will grow.$n\n"
"When AT is low, there is a chance that the max\n"
"value will rise via the buildup and expenditure of\n"
"impulse.\n\0",

##############################################################################

"３\n様々な生活行動\n"
"このゲームでは、様々な行動を生活の中で実行することが\n"
"できます。\n"
"行動は大きく分けると、他の人物とのコミュニケーション、\n"
"特定場所での行動、一人で完結する行動に分けられます。$n\n"
"行動によっては、ΑΤの条件（ΑΤが低すぎる／高すぎる）\n"
"や、消費するインパルスが設定されており、その内容は行\n"
"動選択肢に表示され、実行できない行動は灰色表示となり\n"
"ます。$n\n"
"また、そのときの時間や場所、感情や相手との人間関係な\n"
"ど、様々なシチュエーションによっても実行可能な行動は\n"
"変化します。\n"
"いろんな場所で○ボタンを押して、いろんな行動を試して\n"
"みましょう。\n\0":

"３\nA Variety of Life Actions\n"
"In this game, various actions can be performed in the\n" 
"course of living.\n" 
"Dividing actions broadly, they can be sorted into\n"
"communications with other characters, actions at\n"
"specific places, and actions done solo.$n\n" 
"AT requirements (AT too low / too high), impulse\n"
"consumed, etc., vary from action to action. Such\n"
"details are displayed through the action selection;\n"
"any actions that aren't possible will be greyed out.\n$n"  
"Further, executable actions will change according to\n"
"various situations like current time and place,\n"
"emotions and interpersonal relationships with others,\n"
"and so on. Try pressing the ○ button at different\n"
"places to see the various actions possible.\n\0",

##############################################################################

"４\n人間関係\n"
"人間関係は、△ボタンでのシステムメニューの「人間関係」\n"
"にて確認できます。\n"
"人間関係は、相手への関心（横軸）と、相手への好意（縦\n"
"軸）で表現されます。$n\n"
"関心と好意は、相手へ何かしら行動を行うことで、その行\n"
"動に応じて変化します。\n"
"変化の様子は、人間関係の変化履歴としてポイントとして\n"
"残ります。$n\n"
"関心と好意は変化後、元の場所に戻ろうとします。\n"
"これは、人間関係の表に表示されている透明の楕円が、円\n"
"の形に戻ろうとするのにひきづられるためです。\n"
"人間関係はすぐに変化させることはできませんので、長い\n"
"スパンで仲良くなってください。$n\n"
"また関心と好意は、関心は無し、好意は普通のポイントへ\n"
"とゆっくり変化しています。\n"
"長いことコミュニケーションを行わないキャラとは疎遠に\n"
"なってしまうので注意してください。\n\0":

# [NOTE] Have no idea what second-to-last sentence means. Placeholder until I get more context and can fix. -R
"４\nInterpersonal Relationships\n",
"These can be be checked in \"Relationships\" in the △\n"
"button's system menu.\n"
"Relationships are represented by interest in the\n"
"person (horizontal axis) and regard for the person\n" 
"(vertical axis).$n\n" 
"Concern and regard change depending on the actions\n" 
"used that involve another person.\n" 
"Changing circumstances linger as points that\n" 
"represent the mutative history of a relationship.$n\n" 
"After a change, interest and regard try to return to\n" 
"their original placement.\n"  
"This is because the clear ellipse displayed on the\n" 
"relationship chart wants to revert to a more circular\n" 
"shape.$n\n" 
"??Also, regarding interest and regard, regard without\n" 
"interest changes slowly to a normal point.??\n" 
"You'll drift away from characters if you haven't\n" 
"talked in some time, so exercise caution.\n\0",

##############################################################################

"３\n時間の経過\n"
"生活パートでは、常に時間が経過し、特定の時間になると\n"
"使徒が出現します。\n"
"使徒が出現するまでの時間を、どのように過ごすかはプレ\n"
"イヤーにゆだねられます。$n\n"
"他人とのコミュニケーション、技能の訓練、ネルフでの業\n"
"務、アイテムの入手など、自由に行動してください。\n"
"学生のキャラであれば、ＡＭ０８：００〜ＰＭ０３：００\n"
"の間に登校することで、授業に参加できます。$n\n"
"なにもする事がなければ、さっさと就寝してかまいません。\n"
"就寝時間はキャラにより異なりますが、夜中の１時前後を\n"
"目安に行動してください。\n"
"起床時間もキャラにより異なります。就寝時間＋６時間が\n"
"起床時間となります。\n\0":

"３\nThe Passge of Time\n"
"During the daily life part, time continuously passes\n"
"until the specific moment when an Angel appears.\n"
"How to pass this time is left to the player's\n"
"discretion.$n\n"
"Do as you please, whether communicating with\n"
"others, honing your technical skills, performing\n"
"Nerv duties, acquiring items, etc.\n" 
"If you are a student character, you can attend\n"
"class from 8:00 AM to 3:00 PM.$n\n."
"If you have nothing to do, you may go to bed at any\n" 
"time. Bedtime varies by character, but a general\n" 
"yardstick to act by is for midnight +/- 1 hour.\n" 
"Wake-up time also differs between characters. You\n" 
"rise at Bedtime + 6 hours.\n\0",

##############################################################################

"３\nキャラの行動\n"
"プレイヤーキャラ以外のキャラも、プレイヤーキャラ同様\n"
"に行動しているのがこのゲームの特徴です。\n"
"これらのキャラは様々な「欲望」により行動内容を決定し\n"
"ています。$n\n"
"欲望にはトイレに行きたい欲望や、仕事をしたい欲望など\n"
"１６種類があり、それぞれ欲望の強さが異なります。\n"
"各欲望の強さは、現在の体調、時間、場所、相手、シチュ\n"
"エーション、などで複雑に変動します。$n\n"
"そして一番強い欲望が選択され、その欲望を満たす行動が\n"
"実行されます。\n"
"喉を潤したい欲望が選択されたら、自動販売機でジュース\n"
"を購入する、といった具合です。\n\0":

"???",

##############################################################################

"４\n記憶\n"
"キャラは行動を行うと、その行動の内容を記憶します。\n"
"このとき、行動の内容が楽しい出来事であるならば、いい\n"
"記憶が記憶され、結果ΑΤを上昇させます。\n"
"逆に、行動の内容が辛い出来事であるならば、悪い記憶が\n"
"記憶され、結果ΑΤを下降させます。$n\n"
"そして記憶は時間の経過とともに薄れていきます。\n"
"いい記憶も悪い記憶も、時間の経過で薄れることにより、\n"
"それによるΑΤの上昇、下降が和らぎます。\n"
"キャラが何もしていないのにΑΤの変動が発生するのはそ\n"
"のためです。$n\n"
"いい記憶、悪い記憶により変化したΑΤが、記憶が薄れる\n"
"ことにより、以前の値に近づくためです。$n\n"
"また、記憶された内容は、会話の中で話されることがあり\n"
"ます。\n"
"他のキャラに最近の出来事を聞いてみましょう。意外な出\n"
"来事が聞けるかも知れません。\n\0":

"???",

##############################################################################

"３\n感情の変化\n"
"キャラには２７の感情があり、行った行動、受けた行動に\n"
"よって感情は変化します。\n"
"感情の変化は会話後の人間関係変化情報で確認でき、シス\n"
"テムメニューのステータスでも確認できます。$n\n"
"感情は時間とともに「平穏」の感情に戻って行きます。\n"
"感情により、制限される行動、実行できるようになる行動\n"
"などがあります。$n\n"
"またプレイヤー以外のキャラは、感情によっても欲望に修\n"
"正が発生します。\n"
"感情が「怒り」のキャラにはしばらく話し掛けないなどの\n"
"配慮が必要です。\n\0":

"???",

##############################################################################

"４\n体調管理\n"
"体調には「空腹／水分／眠気／ＷＣ／風呂」の５つがあり、\n"
"システムメニューのステータスで確認できます。\n"
"体調は時間の経過で減少してゆき、食事をするなどの行動\n"
"で回復することができます。$n\n"
"体調が低いとΑΤが減少する修正が発生し、逆に、体調が\n"
"高いとΑΤが増加する修正が発生します。\n"
"ΑΤを高く維持するためにも、体調を高い状態で維持する\n"
"必要があります。$n\n"
"逆にΑΤを低くするために、体調を低いままにする手段も\n"
"あります。$n\n"
"またプレイヤー以外のキャラは、体調によっても欲望に修\n"
"正が発生します。\n"
"トイレに行きたいキャラ、お腹の空いたキャラには、嫌わ\n"
"れないためにも話し掛けないほうが無難です。\n\0":

"???",

##############################################################################

"４\n技能とその効果\n"
"技能には全員に共通する「事務技能／情報技能／白兵技能」\n"
"の３つの技能と、キャラにより「シンクロ技能／参謀技能\n"
"／開発技能／オペレート技能／諜報技能」があります。$n\n"
"技能は、システムメニューのステータスで確認できます。\n"
"技能が高いことで、特定の効果判定パルスが成功しやすく\n"
"なります。$n\n"
"またパイロットキャラの場合、白兵技能が高いと、戦闘補\n"
"助効果の時間が長くなり、シンクロ技能が高いと、移動速\n"
"度の向上、ヘイフリック回復速度の向上、チャージ時間の\n"
"短縮などが期待出来ます。$n\n"
"技能は訓練することにより、上昇させることができます。\n"
"ただし訓練のための効果判定パルスは、技能が高いほど成\n"
"功しにくくなるので注意が必要です。\n\0":

"???",

##############################################################################

"４\n判定パルス\n"
"判定パルスとは、プレイヤーが行った行動の結果判定を行\n"
"う反射ゲームです。\n"
"技能訓練や授業行動、特定の戦闘やイベントなど、ゲーム\n"
"の様々な場所で発生します。\n"
"判定パルスには、効果判定パルスと、成否判定パルスの二\n"
"つのタイプがあります。$n\n"
"判定パルスは、左右に伸縮する３本のバーに対応するボタ\n"
"ンを、バーの先端が成功領域に接触しているタイミングで\n"
"押せば成功となり、これを失敗するまで１０回行います。\n"
"違うボタンを押す、成功タイミングにボタンを押さない、\n"
"成功以外のタイミングにボタンを押すことで失敗となり、\n"
"その時点で判定パルスは終了となります。$n\n"
"効果判定パルスは、成功回数が多くなるほど、結果が良く\n"
"なっていきます。\n"
"成否判定パルスは、１０回全部成功することで、結果は成\n"
"功、そうでなければ失敗の結果となります。\n"
"また、効果判定パルスのほうが、伸縮バーの伸縮速度の増\n"
"加は大きいです。$n\n"
"成功領域の幅は、有利要素、不利要素、ΑΤの値で変化し\n"
"ます。\n"
"有利要素とΑΤの値が高いほど広がり、不利要素の値が高\n"
"いほど狭くなります。\n"
"判定パルスの難易度を下げるには、ΑΤの値を高く保つの\n"
"がセオリーです。\n\0":

"???",

##############################################################################

"３\n被災による影響\n"
"使徒との戦闘で、第３新東京市への被害が発生すると、そ\n"
"の被害の大きさにより影響が発生します。\n"
"コンビニの品揃えが悪くなったり、クラスメイトが疎開で\n"
"いなくなったりします。$n\n"
"被災が最も進むと、第３新東京市での生活は不可能となり、\n"
"民間人は全て疎開、生活の場もネルフ本部のみとなります。$n\n"
"第３新東京市で生活している人々のためにも、戦闘での都\n"
"市への被害は抑える努力が必要です。\n\0":

"???",

##############################################################################

"４\n庵野ＡＩ\n"
"庵野ＡＩは、プレイヤーのプレイ動向により、ゲームバラ\n"
"ンスへの介入を行う機能です。\n"
"前回の生活パートと戦闘パートのプレイ内容より、次の生\n"
"活パートへの影響を変化させます。$n\n"
"庵野ＡＩによるプレイ内容判断は、どんな行動を行ったか、\n"
"どんな場所にいたか、ΑΤの値はどうだったかなどです。$n\n"
"庵野ＡＩによる影響は、生活パート開始時に人間関係を変\n"
"化させたり、ΑΤや感情に対し常に修正を行うなどです。\n"
"影響の中には、大きくΑΤを減少させる影響などがあり、\n"
"ゲームの進行を困難にさせるものもあります。$n\n"
"戦闘中では、庵野ＡＩの条件満たせば、ΑΤが上昇する修\n"
"正が発生したりします。\n"
"※庵野ＡＩは、シナリオ１では機能しません。\n\0":

"???",

##############################################################################

"３\nデフコン\n"
"デフコンとは「ディフェンス・コンディション」の略で、\n"
"防衛体制を意味します。\n"
"このゲームでは、平時はデフコン５、使徒出現の直前でデ\n"
"フコン１となります。$n\n"
"画面左上の時計の隣にデフコンは表示されます（シナリオ\n"
"１では非表示）。\n"
"時間経過とともにデフコンがカウントダウンされていくの\n"
"で、戦闘開始までの時間の目安となります。$n\n"
"デフコンが１になるまでの生活パートの時間を有効に利用\n"
"してください。\n"
"※デフコンは、シナリオ１では機能しません。\n"
"※一部のイベントでは、デフコンには関係なく使徒が出現\n"
"　します。\n\0":

"???",

##############################################################################

"１\nパイロットの心得\n"
"パイロットキャラでプレイする場合、生活パートでは使徒\n"
"との戦闘に備えておく必要があります。\n"
"白兵技能の訓練、シンクロ技能の訓練、ΑΤとインパルス\n"
"を高く保つ、余裕があれば、他のパイロットのΑΤも高く\n"
"なるようにしてもいいでしょう。\n\0":

"???",

##############################################################################

"２\nお金の入手方法\n"
"お金は月に一度、学生キャラはお小遣いとして、大人キャ\n"
"ラは給与として、生活パート開始時に所持金が増加します。\n"
"シンジとアスカにおいては、ミサトに対して小遣いの要求\n"
"行動を実行する必要があります。$n\n"
"別なお金の入手方法は、他のキャラに対してお金をねだる\n"
"行動を行うことです。\n"
"ねだれる金額はキャラによって異なります。お金をたくさ\n"
"ん持っているキャラにねだりましょう。\n\0":

"???",

##############################################################################

"２\nアイテム入手方法\n"
"アイテムは、コンビニで購入することで入手できます。\n"
"他のキャラに「アイテムをねだる」や「アイテムの交換を\n"
"提案」を行い、入手することもできます。\n"
"他のキャラがアイテムをプレゼントしてくれる場合もあり\n"
"ます。$n\n"
"一部のアイテムは「弁当を作る」などで入手できます。\n\0":

"???",

##############################################################################

"２\nハーモニクステスト\n"
"パイロットキャラプレイの場合、ネルフ施設にてリツコか\n"
"マヤに「ハーモニクステストの依頼」を行い了承されれば、\n"
"ハーモニクステストを実行することができます。$n\n"
"ハーモニクステストでは効果判定パルスによる判定が行わ\n"
"れ、その結果によりΑΤの増減が発生します。\n\0":

"???",

##############################################################################

"２\nシンクロ技能訓練\n"
"パイロットキャラプレイの場合、ネルフ施設にてリツコか\n"
"マヤに「シンクロ技能訓練の依頼」を行い了承されれば、\n"
"シンクロ技能訓練を実行することができます。$n\n"
"シンクロ技能訓練では効果判定パルスによる判定が行われ、\n"
"その結果によりシンクロ技能が上昇します。\n\0":

"???",

##############################################################################

"４\n勝敗条件\n"
"戦闘に勝利するには、使徒の耐久力を０にして、これを殲\n"
"滅する必要があります。\n"
"戦闘に敗北となる条件は２つあり、一つ目はプレイヤー\n"
"キャラのエヴァの耐久力が０になる。二つ目はネルフ本部\n"
"が使徒の攻撃を受け、その耐久度が０になることです。$n\n"
"使徒は第３新東京市のゼロエリアを目指して侵攻し、ゼロ\n"
"エリア突破後はジオフロントを侵攻、ネルフ本部へと迫り\n"
"ます。\n"
"エヴァのパイロット達は、その前に使徒の侵攻を食い止め、\n"
"これを殲滅しなければなりません。$n\n"
"勝敗条件には直接関係しませんが、第３新東京市の被害も\n"
"重要です。\n"
"第３新東京市の迎撃施設が使徒の攻撃を受け、被害を受け\n"
"ることにより、\n"
"次の戦闘から、より不利な条件で戦うことになります。$n\n"
"使徒を倒し続けるためにも、エヴァと第３新東京市の被害\n"
"を最小限にしつつ、戦いを繰り返す必要があります。\n\0":

"???",

##############################################################################

"２\n使徒の出現\n"
"使徒の出現警報であるデフコンが１になると、使徒が第３\n"
"新東京市に出現し戦闘が開始されます。\n"
"戦闘開始前、使徒の正確な初期位置は確定しておらず、使\n"
"徒出現予想円の情報のみでエヴァの初期配置位置が設定さ\n"
"れます。$n\n"
"戦闘開始時、使徒の初期位置が判明、使徒はゼロエリアへ\n"
"と侵攻をはじめます。\n"
"※シナリオ１では、デフコンは機能していません。使徒は\n"
"　イベントに連動して出現します。\n\0":

"???",

##############################################################################

"４\nアンビリカルケーブル\n"
"エヴァは電力で駆動し、この電力は電源ビルからアンビリ\n"
"カルケーブルを通して供給されます。$n\n"
"アンビリカルケーブルは電源ビルとエヴァを繋ぐ有限の\n"
"ケーブルです。\n"
"アンビリカルケーブルが届く範囲内でしか電力を供給でき\n"
"ません。$n\n"
"エヴァがアンビリカルケーブルの範囲外で行動するには、\n"
"別の電源ビルのアンビリカルケーブルに繋ぎなおすか、ア\n"
"ンビリカルケーブルを切断して、エヴァの体内に残された\n"
"予備電源を消費することで、短時間だけアンビリカルケー\n"
"ブル無しで活動できます。$n\n"
"予備電源が切れるとエヴァは活動停止となり、一切の行動\n"
"が出来なくなります。\n"
"予備電源が切れる前に、アンビリカルケーブルを再接続す\n"
"る必要があります。\n\0":

"???",

##############################################################################

"３\n使徒の移動と索敵\n"
"使徒は移動中、強力な妨害電波を放っているため正確な位\n"
"置を特定することができません。\n"
"使徒の位置が判別できるのは、第３新東京市の迎撃施設の\n"
"索敵範囲内に使徒がいるときか、\n"
"他のエヴァの目視範囲に捕らえられている時だけです。$n\n"
"それ以外の時は、使徒の最終確認位置から推測される使徒\n"
"の予想侵攻ルートを頼りに、使徒の現在位置を予測する必\n"
"要があります。$n\n"
"第３新東京市の迎撃施設が数多く存在するほど、使徒の位\n"
"置が索敵しやすくなります。\n"
"このため、使徒との戦闘を有利に進めるためにも、迎撃施\n"
"設は重要な役割を果たします。\n\0":

"???",

##############################################################################

"４\n使徒への攻撃\n"
"使徒への攻撃は、エヴァの射程範囲に使徒が入った状態で\n"
"○ボタンを押し、攻撃コマンドを実行することで行われま\n"
"す。$n\n"
"エヴァの射程範囲は、エヴァ周囲にある半透明な扇状の範\n"
"囲です。\n"
"装備武器によりエヴァ前方にも半透明な範囲が発生し、こ\n"
"れもエヴァの射程範囲となります。$n\n"
"使徒への攻撃コマンドは、エヴァと使徒との位置によって\n"
"も変化します。\n"
"使徒を正面に位置しているならば、「プログナイフで突く」\n"
"が行え、使徒が横に位置しているならば、「ミドルキック」\n"
"が行えます。$n\n"
"使徒からの攻撃もエヴァ同様、使徒の射程範囲にエヴァが\n"
"入った状態で行われます。\n\0":

"???",

##############################################################################

"４\nより有利に戦うために\n"
"使徒との戦闘を有利に進めるために、いくつか基本的なテ\n"
"クニック、戦術があります。$n\n"
"＝戦闘補助コマンドを利用しましょう＝\n"
"「姿勢を構える」や「狙いをつける」などの戦闘補助コマ\n"
"ンドで、戦闘行動の効果を高めることができます。\n"
"戦闘補助コマンドを実行するには、インパルスを消費しま\n"
"す。インパルスの残量に注意してください。$n\n"
"＝エヴァ複数で同時に攻撃しましょう＝\n"
"使徒を囲むエヴァが多いほど、使徒のΑΤフィールドを中\n"
"和することが出来ます。\n"
"また、使徒のヘイフリックが回復しないうちに、複数のエ\n"
"ヴァで次々と攻撃することも重要です。$n\n"
"エヴァ複数で同時に攻撃するためにも、他のエヴァの行動\n"
"に注意しましょう。\n\0":

"???",

}
