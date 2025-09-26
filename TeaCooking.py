import random
from collections import Counter
import matplotlib.pyplot as plt

WuerfelDict1 = {"Dice": [4, 6, 12, 20, 100],
               "Raise": [3, 5, 9, 17, 95],
               "Stay": [2, 2, 5, 11, 1]}

WuerfelDict2 = {"Dice": [4, 6, 12, 20, 100],
               "Raise": [3, 4, 9, 17, 95],
               "Stay": [2, 2, 5, 11, 1]}


def wurf(dice):
    return random.randint(1, dice)

def spiel(data):
    stufe = 1

    for _ in range(3):
        ergebnis = wurf(data["Dice"][stufe])

        if ergebnis < data["Stay"][stufe]:
            stufe -= 1
        elif ergebnis >= data["Raise"][stufe]:
            stufe += 1
        elif stufe == -1:
            break

    if stufe == 4:
        ergebnis = wurf(data["Dice"][stufe])
        if ergebnis >= 95:
            stufe += 1

    return stufe + 1

def TeaSimulation(n, wuerfelDict):
    haeufigkeit = Counter()
    for _ in range(n):
        haeufigkeit[spiel(wuerfelDict)] += 1

    relative_haeufigkeit = {wert: count / n * 100 for wert, count in haeufigkeit.items()}

    return relative_haeufigkeit

relative_haeufigkeit1 = TeaSimulation(1000000, WuerfelDict1)
relative_haeufigkeit2 = TeaSimulation(1000000, WuerfelDict2)

plt.bar(relative_haeufigkeit1.keys(), relative_haeufigkeit1.values())
plt.bar(relative_haeufigkeit2.keys(), relative_haeufigkeit2.values(), alpha = 0.3)
plt.xlabel("Seltenheit")
plt.ylabel("rel. Häufigkeit [%]")
plt.show()