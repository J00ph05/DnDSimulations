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
    # data.sum_plot()
    # data.current_pieChart()
    # data.total_pieChart()
    # data.meanSessionIntervall_print()
    data.total_barplot()