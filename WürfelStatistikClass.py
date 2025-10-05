import pandas as pd
import matplotlib.pyplot as plt
import locale
locale.setlocale(locale.LC_TIME, "deu_deu")

class StatsClass:
    def __init__(self, path2csv):
        self.raw_data = pd.read_csv(path2csv)
        self.raw_data["Datum"] = pd.to_datetime(self.raw_data["Datum"], format="%d. %B %Y")
        self.raw_data["Nat20"] = pd.to_numeric(self.raw_data["Nat20"])
        self.raw_data["Nat1"] = pd.to_numeric(self.raw_data["Nat1"])

    def sum_plot(self):
        for name in pd.unique(self.raw_data["Spieler"]):
            df = self.raw_data[self.raw_data["Spieler"] == name]
            df = df.sort_values("Datum")
            df["Nat20_kum"] = df["Nat20"].cumsum()
            df["Nat1_kum"] = df["Nat1"].cumsum()
            plt.plot(df["Datum"], df["Nat20_kum"], "gx-", label="Nat20")
            plt.plot(df["Datum"], df["Nat1_kum"], "rx-", label="Nat1")
            plt.title(name)
            plt.legend()
            plt.xticks(rotation=45)
            plt.ylabel("Anzahl")
            plt.grid(True)
            plt.tight_layout()
            plt.show()

    def current_pieChart(self):
        for name in pd.unique(self.raw_data["Spieler"]):
            df = self.raw_data[self.raw_data["Spieler"] == name]
            summen = [
                df["Nat1"].sum(),
                df["Nat20"].sum()
            ]
            labels = ["Nat1", "Nat20"]
            colors = ["red", "green"]

            def autopct_abs(pct):
                total = sum(summen)
                absolute = int(round(pct * total / 100.0))
                return f"{pct:.1f}% ({absolute})"

            plt.figure(figsize=(5, 5))
            plt.pie(summen, labels=labels, colors=colors, autopct=autopct_abs, startangle=90)
            plt.title(f"Aktuelles Verhältnis Nat1/Nat20 für {name}")
            plt.show()



