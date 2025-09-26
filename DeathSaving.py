import random


def wurf():
    """Wirft zwei W20 und gibt das höhere Ergebnis zurück."""
    return max(random.randint(1, 20), random.randint(1, 20))


def ein_spiel():
    erfolge = 0
    fehlschlaege = 0

    while erfolge < 3 and fehlschlaege < 3:
        ergebnis = wurf()
        if ergebnis >= 10:
            erfolge += 1
        else:
            fehlschlaege += 1

    return erfolge == 3  # True = Erfolg, False = Fehlschlag


def monte_carlo_simulation(anzahl=1000000):
    erfolge = sum(ein_spiel() for _ in range(anzahl))
    fehlschlaege = anzahl - erfolge
    print(f"Gesamtanzahl Simulationen: {anzahl}")
    print(f"Erfolge: {erfolge} ({erfolge / anzahl:.2%})")
    print(f"Fehlschläge: {fehlschlaege} ({fehlschlaege / anzahl:.2%})")


monte_carlo_simulation()