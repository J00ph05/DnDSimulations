from collections import Counter
import matplotlib.pyplot as plt
import random

def wurf(dice):
    ergebnis = random.randint(1, abs(dice))
    if dice < 0:
        return -ergebnis
    return ergebnis

def wurf_summe(dices):
    summe = 0
    for dice in dices:
        summe += wurf(dice)
    return summe

def multiWuerfel_Simulation(*args):
    n = 1000000
    haeufigkeit = Counter()
    for _ in range(n):
        haeufigkeit[wurf_summe(args)] += 1

    relative_haeufigkeit = {wert: count / n * 100 for wert, count in haeufigkeit.items()}

    return relative_haeufigkeit

relative_haeufigkeit1 = multiWuerfel_Simulation(20, 3)
relative_haeufigkeit2 = multiWuerfel_Simulation(20)

plt.bar(relative_haeufigkeit1.keys(), relative_haeufigkeit1.values())
plt.bar(relative_haeufigkeit2.keys(), relative_haeufigkeit2.values())
plt.xlabel("Würfelwert")
plt.ylabel("rel. Häufigkeit [%]")
plt.show()