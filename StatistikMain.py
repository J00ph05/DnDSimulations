from WürfelStatistikClass import StatsClass
import tkinter as tk
from tkinter import filedialog

def choose_file():
    root = tk.Tk()
    root.withdraw()                # Hauptfenster verbergen
    path = filedialog.askopenfilename(title="Datei auswählen")
    root.destroy()
    return path

if __name__ == "__main__":
    # Beispiel: wahlweise Datei oder Ordner
    file_path = choose_file()
    data = StatsClass(file_path)
    print(data.raw_data)
    html_sumplot = data.sum_plot()
    html_pieplot = data.current_pieChart()
    html_pietotal = data.total_pieChart()
    data.meanSessionIntervall_print()
    html_barplot = data.total_barplot()

    rows = []
    for pie_plot, sum_plot in zip(html_pieplot, html_sumplot):
        rows.append(f"""
        <div class="row">
            <div class="plot">{pie_plot}</div>
            <div class="plot">{sum_plot}</div>
        </div>
        """)

    single_rows = []
    single_rows.append(f"""
    <div class="row single">
        <div class="plot">{html_pietotal}</div>
    </div>
    """)
    single_rows.append(f"""
    <div class="row single">
        <div class="plot">{html_barplot}</div>
    </div>
    """)

    # Gesamtes HTML
    full_html = f"""
    <html>
    <head>
    <meta charset="utf-8">
    <title>Würfel-Analyse</title>
    <style>
    body {{
      font-family: sans-serif;
      margin: 60px;
    }}
    .row {{
      display: flex;
      flex-wrap: nowrap;
      justify-content: left;
      align-items: flex-start;
      margin-bottom: 30px;
    }}
    .plot {{
      flex: 0 0 auto;
      width: 440px;
      margin: 0 15px;
    }}
    </style>
    </head>
    <body>
    {''.join(single_rows)}
    {''.join(rows)}
    </body>
    </html>
    """


    with open("report.html", "w", encoding="utf-8") as f:
        # f.write(html_barplot)
        # f.write(html_pietotal)
        f.write(full_html)

