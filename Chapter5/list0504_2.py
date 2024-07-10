import random
ALP = ["A", "B", "C", "D", "E", "F", "G"]
r = random.choice(ALP)
arp = " "
for i in ALP:
    if i != r:
        arp = arp + i
print(arp)
