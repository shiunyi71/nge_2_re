#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

# Note:
# This file contains section-specific untranslated strings
# Put the translations in the ???
# \n is a linebreak
# \0 is the end of the string
# \' is a single quote

from support import *

section_data = AppSection('.data', 0x001DAA00, 0x000793FC, AppSectionFlag.Allocated | AppSectionFlag.Writable,
{
    # PreRelocationAddress: Data(Type, Size, Value, Comment)
    0x001E6460: Data(DataType.String, 44, '???', "＝心の補完観察＝\n観察対象を選択して下さい。\0"),
    0x001E66D0: Data(DataType.String, 24, '0123456789\0', "０１２３４５６７８９\0"),
    0x001ED874: Data(DataType.String, 72, 'You can configure the rate at which time passes in-game.\n The speed of battles is unaffected.\n\0
', "ゲーム中の時間経過速度を設定できます。\n戦闘の速度には関係ありません。\n\0"),
    0x001ED8BC: Data(DataType.String, 40, 'Switch character graphics on/off.\n\0', "キャラの立ち絵の有／無を設定します。\n\0"),
    0x001ED8E4: Data(DataType.String, 40, 'Switch character voices on/off.\n\0', "キャラボイスの有／無を設定できます。\n\0"),
    0x001ED90C: Data(DataType.String, 76, '???', "方向キーの挙動を設定します。\n%1i%2i%3i%4iに方向キーの同位置が対応します。\n\0"),
    0x001ED958: Data(DataType.String, 76, '???', "オプション設定を、現在の設定状態に変更し、\nタイトルメニューに戻ります。\n\0"),
    0x001ED9A4: Data(DataType.String, 72, '???', "オプション設定を、現在の設定状態に変更し、\nゲームプレイに戻ります。\n\0"),
    0x0023980C: Data(DataType.String, 80, '???', "奥へと通路が伸びている。\n通路の脇には巨大なダクトが\n並行して設置してある…。\0"),
    0x0023985C: Data(DataType.String, 76, '???', "通路の傾斜が弱くなってきた。\n照明が弱く、足元の配線に\n足を取られそうだ…。\0"),
    0x002398A8: Data(DataType.String, 64, '???', "だんだん空気が冷たくなってきた。\n通路は幅が広くなってゆく…。\0"),
    0x002398E8: Data(DataType.String, 80, '???', "照明の明るい回廊へと抜けた。\n天井も高く、機材運搬の\nリフトが移動している…。\0"),
    0x00239938: Data(DataType.String, 80, '???', "通路を左折した先の、狭いハッチを\nくぐると、ネズミが足元を走り\n抜けていった…。\0"),
    0x00239988: Data(DataType.String, 76, '???', "通路を右折すると、通路は瓦礫に\n覆われていた。\n瓦礫を避けて先へと進む…。\0"),
    0x002399D4: Data(DataType.String, 96, '???', "さほど長くも無い梯子を登ると\nハッチをあけ、別区画に移動した。\n周囲を確認し、ハッチを閉める…。\0"),
    0x00239A34: Data(DataType.String, 88, '???', "長い梯子を降りきると、そこは\n巨大な暗い空間であった。\nぐるり見渡し、行く先を探す…。\0"),
    0x00239A8C: Data(DataType.String, 96, '???', "脇にあった扉を無視して進むと、\n天井が低い通路に出くわした。\nしばらく中腰で先へと歩を進めた。\0"),
    0x00239AEC: Data(DataType.String, 60, '???', "%sを差し込むと、\n軽い機械音が響き、扉のロックが\n外れた…。\0"),
    0x00239B28: Data(DataType.String, 80, '???', "%sを差し込むと、\n認証に時間がかかったものの、\n無事ロックが外れ、扉が開いた…。\0"),
    0x00239B78: Data(DataType.String, 80, '???', "ゼーレの刻印があるカードリーダー\nに%sを通した。\n静かに巨大な扉が開いていく…。\0"),
    0x00239BF8: Data(DataType.String, 20, '???', "通路に沿って進む\0"),
    0x00239C0C: Data(DataType.String, 16, 'Proceed underground\0', "地下方向へ進む\0"),
    0x00239C1C: Data(DataType.String, 16, 'Head toward darkness', "薄暗い方へ進む\0"),
    0x00239C2C: Data(DataType.String, 24, 'Head toward sound of machinery\0', "機械音がする方向へ進む\0"),
    0x00239C44: Data(DataType.String, 20, 'Turn left at next corner\0', "次の角を左に曲がる\0"),
    0x00239C58: Data(DataType.String, 20, 'Turn right at next corner\0', "次の角を右に曲がる\0"),
    0x00239C6C: Data(DataType.String, 12, 'Climb ladder\0', "梯子を登る\0"),
    0x00239C78: Data(DataType.String, 16, 'Descend ladder\0', "梯子を降りる\0"),
    0x00239C88: Data(DataType.String, 20, 'Ignore door and proceed\0', "扉を無視して進む\0"),
    0x00239C9C: Data(DataType.String, 28, 'Open security door\0', "セキュリティー扉を開ける\0"),
    0x00239CB8: Data(DataType.String, 24, 'Open Warning Type Two door\0', "第二級警戒扉を開ける\0"),
    0x00239CD0: Data(DataType.String, 24, 'Open Warning Type One door\0', "第一級警戒扉を開ける\0"),
    0x00239D18: Data(DataType.String, 68, '???', "駄目だ、今所有するＩＤカードでは\nこの扉のロックは解除できない…。\0"),
    0x00239D5C: Data(DataType.String, 28, '???', "行き止まりだ、引き返そう。\0"),
    0x00239D78: Data(DataType.String, 28, '???', "あれ、こんなとこに出た。\0"),
    0x00239D94: Data(DataType.String, 28, 'Huh, you emerged outside.\0', "ありゃ、外に出ちゃった。\0"),
    0x00239DB0: Data(DataType.String, 100, '???', "行き止まりの空間には、複雑な配線が\nむき出しになっており、マギへの\n直接端末も含まれているようだ…。\0"),
    0x00239E14: Data(DataType.String, 84, '???', "空間が開けると、そこには\n廃棄された射撃場がある…。\n実銃と実弾も完備されてるが…。\0"),
    0x002406C8: Data(DataType.String, 64, '???', "　　　事務　%02d\n　　　情報　%02d\n　　　白兵　%02d\n%s　%02d\n\0"),
    0x00240708: Data(DataType.String, 52, '???', "　　　事務　%02d\n　　　情報　%02d\n　　　白兵　%02d\n\0"),
    0x002504F4: Data(DataType.String, 12, 'Cancel\0', "キャンセル\0"),
    0x00250500: Data(DataType.String, 28, 'Attach Umbilical Cable\0', "アンビリカルケーブル接続\0"),
    0x0025051C: Data(DataType.String, 16, 'Equip weapon', "武器を装備する\0"),
    0x0025052C: Data(DataType.String, 24, 'View Map\0', "全域マップを確認する\0"),
    0x00250544: Data(DataType.String, 20, 'Middle Kick\0', "ミドルキックで攻撃\0"),
    0x00250558: Data(DataType.String, 20, 'Prog. Knife Stab\0', "ブログナイフで突く\0"),
    0x00250570: Data(DataType.String, 16, 'Chop\0', "チョップ攻撃\0"),
    0x00250580: Data(DataType.String, 20, 'Prog. Knife Cut\0', "プログナイフで切る\0"),
    0x00250598: Data(DataType.String, 24, 'Front Kick\0', "フロントキックで攻撃\0"),
    0x002505B4: Data(DataType.String, 12, 'Sword Swing\0', "剣を振るう\0"),
    0x002505C0: Data(DataType.String, 24, 'A.T. Field Attack\0', "ΑΤフィールドアタック\0"),
    0x002505D8: Data(DataType.String, 20, 'Two Platoon Kick\0', "ツープラトンキック\0"),
    0x002505EC: Data(DataType.String, 24, 'Pallet Rifle Shot\0', "パレットライフルで射撃\0"),
    0x00250604: Data(DataType.String, 24, 'Maguroku Sword Slash\0', "マゴロクソードで斬る\0"),
    0x0025061C: Data(DataType.String, 24, 'Maguroku Sword Thrust\0', "マゴロクソードで突く\0"),
    0x00250634: Data(DataType.String, 16, 'Rifle Shot\0', "ライフルで射撃\0"),
    0x00250644: Data(DataType.String, 28, 'Positron Rifle Shot\0', "ポジトロンライフルで射撃\0"),
    0x00250660: Data(DataType.String, 24, 'Positron Sniper Shot\0', "ポジトロン・Ｓで射撃\0"),
    0x00250678: Data(DataType.String, 20, 'Sever Cable\0', "ケーブルを切断する\0"),
    0x0025068C: Data(DataType.String, 16, '???', "装備を実行する\0"),
    0x0025069C: Data(DataType.String, 16, '???', "作戦確認終了\0"),
    0x002506B0: Data(DataType.String, 24, '???', "退屈しのぎに何か話す\0"),
    0x002506C8: Data(DataType.String, 16, 'How\s it going?\0', "調子はどう？\0"),
    0x002506D8: Data(DataType.String, 20, 'How will you fight?\0', "どうやって戦う？\0"),
    0x002506EC: Data(DataType.String, 20, 'What do you think of %s?\0', "%sのことどう思う？\0"),
    0x00250700: Data(DataType.String, 16, 'Discard equipment', "装備を破棄する\0"),
    0x00250710: Data(DataType.String, 12, 'Pick up sword\0', "剣を拾う\0"),
    0x0025071C: Data(DataType.String, 16, 'Mastema Shot\0', "マステマで射撃\0"),
    0x0025072C: Data(DataType.String, 16, 'Mastema Cut\0', "マステマで切る\0"),
    0x0025073C: Data(DataType.String, 16, 'N. Missile Strike\0', "Νミサイル攻撃\0"),
    0x0025074C: Data(DataType.String, 20, 'Dual Saw Strike\0', "デュアルソーで攻撃\0"),
    0x00250760: Data(DataType.String, 20, 'Prog. Dagger Stab\0', "プログダガーで突く\0"),
    0x00250774: Data(DataType.String, 20, 'Prog. Dagger Cut\0', "プログダガーで切る\0"),
    0x00250788: Data(DataType.String, 20, 'Impact Bolt\0', "インパクトボルト\0"),
    0x0025079C: Data(DataType.String, 20, 'Hyper Chop\0', "ハイパーチョップ\0"),
    0x002507B0: Data(DataType.String, 20, 'Interact with Tabris\0', "タブリスと対話する\0"),
    0x002507C4: Data(DataType.String, 20, 'Pilot Instruction\0', "パイロットに指示\0"),
    0x002507D8: Data(DataType.String, 16, 'Neural connection cut\0', "神経接続切断\0"),
    0x002507E8: Data(DataType.String, 12, 'Status\0', "ステータス\0"),
    0x002507F4: Data(DataType.String, 16, '%s, change location.\0', "%sは移動して\0"),
    0x00250804: Data(DataType.String, 20, '%s, go on standby.\0', "%sはその場で待機\0"),
    0x00250818: Data(DataType.String, 16, '%s, take cover.\0', "%sは退避して\0"),
    0x00250828: Data(DataType.String, 16, '%s, start firing.\0', "%sは射撃開始\0"),
    0x00250838: Data(DataType.String, 16, '%s, engage the enemy up close.\0', "%sは接近戦よ\0"),
    0x00250848: Data(DataType.String, 24, '%s, fire from a distance.\0', "%sは距離をとって射撃\0"),
    0x00250860: Data(DataType.String, 12, 'Battle Results\0', "作戦決定\0"),
    0x0025086C: Data(DataType.String, 28, '???', "パイロット選択からやり直す\0"),
    0x00250888: Data(DataType.String, 20, 'Use Dummy Plug\0', "ダミープラグを使え\0"),
    0x0025089C: Data(DataType.String, 24, 'Use Spear of Longinus\0', "ロンギヌスの槍を使え\0"),
    0x002508B4: Data(DataType.String, 20, 'Cut neural connection\0', "神経接続を切断する\0"),
    0x002508C8: Data(DataType.String, 20, 'Dummy Plug overrides %s', "%sにダミープラグだ\0"),
    0x002508DC: Data(DataType.String, 12, 'Punch\0', "パンチ攻撃\0"),
    0x002508E8: Data(DataType.String, 16, 'Return to Nerv\0', "ネルフに戻る\0"),
    0x002508F8: Data(DataType.String, 12, '???', "関係ないや\0"),
    0x00250904: Data(DataType.String, 12, 'Deploy\0', "配置する\0"),
    0x00250910: Data(DataType.String, 20, 'Put both Evas on standby\0', "両機はその場で待機\0"),
    0x00250924: Data(DataType.String, 28, 'Sever Umbilical Cable\0', "アンビリカルケーブル切断\0"),
    0x00250950: Data(DataType.String, 24, 'View %s\'s attack list\0', "%sの攻撃リストを見る\0"),
    0x00250968: Data(DataType.String, 16, 'Deploy %s\0', "%sを配置する\0"),
    0x00250978: Data(DataType.String, 16, '???', "%sに武装する\0"),
    0x00250988: Data(DataType.String, 20, 'Deploy UN army\0', "国連軍を配置する\0"),
    0x0025099C: Data(DataType.String, 24, '???', "出撃パイロットの再選\0"),
    0x002509B4: Data(DataType.String, 24, '???', "作戦立案終了、次に進む\0"),
    0x002509CC: Data(DataType.String, 16, '???', "%sに移動指示\0"),
    0x002509DC: Data(DataType.String, 28, 'Instruct Pilot\0', "パイロットに指示を与える\0"),
    0x002509F8: Data(DataType.String, 8, 'Yes\0', "はい\0"),
    0x00250A00: Data(DataType.String, 8, 'No\0', "いいえ\0"),
    0x00250A18: Data(DataType.String, 20, '???', "出撃メンバーは\n%s\0"),
    0x00250A2C: Data(DataType.String, 48, '???', "出撃メンバーは\n%s$n入院中の%s\n無理は承知の上よ\0"),
    0x00250A5C: Data(DataType.String, 64, '???', "出撃メンバーは全員入院中だけど…\nやらなきゃ…どの道、終わりよ\0"),
    0x00250A9C: Data(DataType.String, 16, '???', "%sの装備は%s\0"),
    0x00250AAC: Data(DataType.String, 28, '???', "各機の配置はこんな感じよ\0"),
    0x00250ACC: Data(DataType.String, 40, 'You can sortie up\n to three Evas\0', "ＥＶＡは３体までしか\n出撃できません。\0"),
    0x00250AF4: Data(DataType.String, 48, '???', "%sはシンクロ率が低すぎて\nＥＶＡを動かせません。\0"),
    0x00250B24: Data(DataType.String, 28, '???', "それでも出撃させますか？\0"),
    0x00250B40: Data(DataType.String, 112, '???', "神経接続を切断しますか？$n一定時間、パイロットへのダメージ\nがカットされる代わり、エヴァは\n行動不能になります。\0"),
    0x00250BB0: Data(DataType.String, 56, '???', "新型エヴァは、ダミーシステムを\n使用する事が出来ません。\0"),
    0x00250BE8: Data(DataType.String, 48, 'Please select Eva pilots to sortie\0', "出撃するエヴァのパイロットを\n選んでください。\0"),
    0x00250C18: Data(DataType.String, 60, '???', "%sは、委員会から凍結命令が\n降りているため、出撃出来ません。\0"),
    0x00250C54: Data(DataType.String, 48, '???', "現在、パイロットが欠番のため\n出撃出来ません。\0"),
    0x00250C84: Data(DataType.String, 36, '???', "%sは消失したため、\n出撃出来ません。\0"),
    0x00250CA8: Data(DataType.String, 64, '???', "%sの\n残弾数が０になりました。\n使用出来ないため、破棄します。\0"),
    0x00250CE8: Data(DataType.String, 32, '???', "この位置には配置できません。\0"),
    0x00250D08: Data(DataType.String, 72, '???', "ここにエヴァを配置すると、\n%s分間しか活動出来ません。\n配置しますか？\0"),
    0x00250D50: Data(DataType.String, 88, '???', "エヴァを複数同時に活動させるための\n電源が確保できません。\n他の場所に配置してください。\0"),
    0x00250DA8: Data(DataType.String, 48, 'New Eva-01 model\n cannot carry out "Equipping."\0', "新型初号機は、\n「装備」を行うことは出来ません。\0"),
    0x00250DD8: Data(DataType.String, 56, '???', "%sは\n%sが装備しています。\n外して、%sに装備しますか？\0"),
    0x00252958: Data(DataType.String, 20, 'A.T. Field held out\0', "ＡＴフィールド持続\0"),
    0x0025298C: Data(DataType.String, 8, '???', "定数\0"),
    0x002529BC: Data(DataType.String, 8, '???', "定数\0"),
    0x00252A40: Data(DataType.String, 20, 'Resist mental contamination\0', "精神汚染への抵抗\0"),
    0x00252A74: Data(DataType.String, 20, 'Get closer to Angel\0', "使徒への接近距離\0"),
    0x00252AA4: Data(DataType.String, 8, '???', "定数\0"),
    0x00252C40: Data(DataType.String, 16, 'Open Gaghiel\'s mouth\0', "ガギエルの開口\0"),
    0x00252C74: Data(DataType.String, 16, 'Eva-02\'s stamina\0', "弐号機の耐久力\0"),
    0x00252CA4: Data(DataType.String, 8, '???', "定数\0"),
    0x00252D20: Data(DataType.String, 20, 'Retrieve submerged Eva\0', "沈降エヴァの救出\0"),
    0x00252D54: Data(DataType.String, 16, 'Eva\'s stamina\0', "エヴァの耐久力\0"),
    0x00252D84: Data(DataType.String, 8, '???', "定数\0")
})
