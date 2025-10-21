import pandas as pd
import matplotlib.pyplot as plt
import locale
import mpld3
locale.setlocale(locale.LC_TIME, "deu_deu")

class StatsClass:
    def __init__(self, path2csv):
        self.raw_data = pd.read_csv(path2csv)
        self.raw_data["Datum"] = pd.to_datetime(self.raw_data["Datum"], format="%d/%m/%Y")
        self.raw_data["Nat20"] = pd.to_numeric(self.raw_data["Nat20"])
        self.raw_data["Nat1"] = pd.to_numeric(self.raw_data["Nat1"])

    def sum_plot(self):
        html_total = []
        for name in pd.unique(self.raw_data["Spieler"]):
            df = self.raw_data[self.raw_data["Spieler"] == name]
            df = df.sort_values("Datum")
            df["Nat20_kum"] = df["Nat20"].cumsum()
            df["Nat1_kum"] = df["Nat1"].cumsum()
            fig, ax = plt.subplots(figsize=(6,4))
            ax.plot(df["Datum"], df["Nat20_kum"], "gx-", label="Nat20")
            ax.plot(df["Datum"], df["Nat1_kum"], "rx-", label="Nat1")
            ax.set_title(name)
            ax.set_ylabel("Anzahl")
            ax.grid(True)
            ax.legend()
            plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
            fig.tight_layout()
            #plt.show()
            html_str = mpld3.fig_to_html(fig)
            html_total.append(html_str)
        
        return html_total

    def current_pieChart(self):
        html_total = []
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

            fig, ax = plt.subplots(figsize=(5, 5))
            ax.pie(summen, labels=labels, colors=colors, autopct=autopct_abs, startangle=90)
            ax.set_title(f"Aktuelles Verhältnis Nat1/Nat20 für {name}")
            #plt.show()

            html_str = mpld3.fig_to_html(fig)
            html_total.append(html_str)
        return html_total

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

        fig, ax = plt.subplots(figsize=(5,5))
        ax.pie(total, labels=labels, autopct=autopct_abs)
        ax.set_title("Gesamte Würfelverteilung")
        #plt.show()

        html_str = mpld3.fig_to_html(fig)

        return html_str

    def total_barplot(self):
        df = self.raw_data
        df["Nat1_neg"] = -df["Nat1"]

        pivot_nat20 = df.pivot(index="Session", columns="Spieler", values="Nat20")
        pivot_nat1 = df.pivot(index="Session", columns="Spieler", values="Nat1_neg")


        fig, ax = plt.subplots(figsize=(9,6))

        pivot_nat20.plot(kind="bar", ax=ax, stacked=True)
        pivot_nat1.plot(kind="bar", ax=ax, stacked=True)

        #ax.axhline(0, color="black", linewidth=1, alpha=0.5, zorder=-1)
        ax.set_ylabel("Anzahl Würfe")
        ax.set_title("Nat20 (oben) und Nat1 (unten) pro Session und Spieler")
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles[:4], labels[:4])
        ax.set_xticklabels(pivot_nat20.index, rotation=45)
        plt.tight_layout()
        #plt.show()
        
        html_str = mpld3.fig_to_html(fig)
        
        return html_str

    def meanSessionIntervall_print(self):
        df = self.raw_data.sort_values("Datum")
        df["t_Delta"] = df["Datum"].diff()
        df_filt = df[df["t_Delta"] > pd.Timedelta(0)]
        print(df_filt)
        mean_t = df_filt["t_Delta"].mean()
        print(mean_t)


