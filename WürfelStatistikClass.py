import pandas as pd
import matplotlib.pyplot as plt
import locale
locale.setlocale(locale.LC_TIME, "deu_deu")

class StatsClass:
    def __init__(self, path2csv):
        self.raw_data = pd.read_csv(path2csv)
        self.raw_data["Datum"] = pd.to_datetime(self.raw_data["Datum"], format="%d/%m/%Y")
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

    def total_pieChart(self):
        labels = []
        total = []

        for name in pd.unique(self.raw_data["Spieler"]):
            df = self.raw_data[self.raw_data["Spieler"] == name]
            total.append(df["Nat1"].sum() + df["Nat20"].sum())
            labels.append(name)

        def autopct_abs(pct):
            totale = sum(total)
            absolute = int(round(pct * totale / 100.0))
            return f"{pct:.1f}% ({absolute})"

        plt.figure(figsize=(5,5))
        plt.pie(total, labels=labels, autopct=autopct_abs)
        plt.title("Gesamte Würfelverteilung")
        plt.show()

    def total_barplot(self):
        df = self.raw_data
        df["Nat1_neg"] = -df["Nat1"]

        pivot_nat20 = df.pivot(index="Session", columns="Spieler", values="Nat20")
        pivot_nat1 = df.pivot(index="Session", columns="Spieler", values="Nat1_neg")


        fig, ax = plt.subplots(figsize=(9,6))

        pivot_nat20.plot(kind="bar", ax=ax, stacked=True)
        pivot_nat1.plot(kind="bar", ax=ax, stacked=True)

        ax.axhline(0, color="black", linewidth=1)
        ax.set_ylabel("Anzahl Würfe")
        ax.set_title("Nat20 (oben) und Nat1 (unten) pro Session und Spieler")
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles[:4], labels[:4])
        ax.set_xticklabels(pivot_nat20.index, rotation=45)
        plt.tight_layout()
        plt.show()

    def meanSessionIntervall_print(self):
        df = self.raw_data.sort_values("Datum")
        df["t_Delta"] = df["Datum"].diff()
        df_filt = df[df["t_Delta"] > pd.Timedelta(0)]
        print(df_filt)
        mean_t = df_filt["t_Delta"].mean()
        print(mean_t)


