# coding: UTF-8
# ポーカーの収支を打ち込むだけで自動計算
a = input("第何回ですか？ : ")


chicchi = input("今までのちっちは？ : ")
chicchi = int(chicchi)

youhei = input("今までのようへいは？ : ")
youhei = int(youhei)

daiju = input("今までのだいじゅは？ : ")
daiju = int(daiju)

numa = input("今までのかずまは？ : ")
numa = int(numa)

dori = input("今までのけいじろうは？ : ")
dori = int(dori)

kamo = input("今までのカモは？ : ")
kamo = int(kamo)

fuji = input("今までのふじは？ : ")
fuji = int(fuji)

sizu = input("今までのうんちは？ : ")
sizu = int(sizu)


newchicchi = input("\n今日のちっちは？ : ")
newchicchi = int(newchicchi)

newyouhei = input("今日のようへいは？ : ")
newyouhei = int(newyouhei)

newdaiju = input("今日のだいじゅは？ : ")
newdaiju = int(newdaiju)

newnuma = input("今日のかずまは？ : ")
newnuma = int(newnuma)

newdori = input("今日のけいじろうは？ : ")
newdori = int(newdori)

newkamo = input("今日のカモは？ : ")
newkamo = int(newkamo)

newfuji = input("今日のふじは？ : ")
newfuji = int(newfuji)

newsizu = input("今日のうんちは？ : ")
newsizu = int(newsizu)


chicchi += newchicchi
youhei += newyouhei
daiju += newdaiju
numa += newnuma
dori += newdori
kamo += newkamo
fuji += newfuji
sizu += newsizu

sum = chicchi + youhei + daiju + numa + dori + kamo + fuji + sizu

print("\n第{}回".format(a))

print("ちっちは : {}".format(chicchi))
print("ようへいは : {}".format(youhei))
print("だいじゅは : {}".format(daiju))
print("かずまは : {}".format(numa))
print("けいじろうは : {}".format(dori))
print("カモは : {}".format(kamo))
print("ふじは : {}".format(fuji))
print("うんちは : {}".format(sizu))


if sum == 0:
    print("\nまたうんちがビリかぁ")
else:
    print("\n合計合わんやないか、そんなんだから負けんだよ")
