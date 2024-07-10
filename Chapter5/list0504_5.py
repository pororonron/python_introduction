import random
import datetime
ALP = ["A", "B", "C", "D", "E", "F", "G",
       "H", "I", "J", "K", "L", "M", "N",
       "O", "P", "Q", "R", "S", "T", "U",
       "V", "W", "X", "Y", "Z"]
r = random.choice(ALP)
arp = " "
for i in ALP:
    if i != r:
        arp = arp + i
print(arp)
st = datetime.datetime.now()
ans = input("抜けているアルファベットは？")
if ans == r:
    print("正解です")
    et = datetime.datetime.now()
    print(str((et - st).seconds) + "秒かかりました")
else:
    print("違います")
