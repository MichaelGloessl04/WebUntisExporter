import tkinter as tk
import databank
from datetime import datetime


class GUI:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.geometry('350x200')
        t = databank.model.TimetableHandler("C:/Code/WebUntisExporter/databank/databank.db")
        s = databank.model.SubjectHandler("C:/Code/WebUntisExporter/databank/databank.db")
        table = t.To_Dict

        weekday_buttons = []
        weekday_labels = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

        scrollbar = tk.Scrollbar(self.window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        listbox = tk.Listbox(self.window, yscrollcommand=scrollbar.set)
        for i in range(len(table['id'])):
            label_text = f"""{s.get_where("short_name", table['subject'][i])[0][0]},
                             {datetime.fromtimestamp(table['start'][i])},
                             {datetime.fromtimestamp(table['end'][i])}"""
            listbox.insert(tk.END, label_text)
        listbox.pack(fill=tk.BOTH)

        scrollbar.config(command=listbox.yview)

        for i in range(5):
            btn = tk.Button(self.window, text=weekday_labels[i])
            weekday_buttons.append(btn)

        self.window.mainloop()
