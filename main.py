import tkinter
import datetime

BACKGROUND_COLOR = "#FFBB64"
BACKGROUND_COLOR2 = "#FFEAA7"
FONT = ("Liberation", 20, "normal")

window = tkinter.Tk()
version = "PL"
window.title("Kalkulator E-recepty")
window.config(height=500, width=1000, padx=50, pady=50, bg=BACKGROUND_COLOR)


def insulin():
    insulin_entry.grid()
    insulin_label.grid()
    dose_label.config(text="Podaj ilość jednostek we wkładzie:")
    usage_label.config(text="Podaj liczbę jednostek, jaką pacjent stosuje na dzień:")
    smallest_box_label.grid_remove()
    smallest_box_entry.grid_remove()


def pills():
    insulin_entry.grid_remove()
    insulin_label.grid_remove()
    dose_label.config(text="Podaj ilość sztuk w opakowaniu:")
    usage_label.config(text="Podaj liczbę sztuk, jaką pacjent stosuje na dzień:")
    smallest_box_label.grid()
    smallest_box_entry.grid()


boxes_label = tkinter.Label(text="Podaj ilość zapisanych opakowań:", background=BACKGROUND_COLOR2, font=FONT)
boxes_label.grid(row=1, column=0)
boxes_entry = tkinter.Entry(width=10, font=FONT)
boxes_entry.grid(row=1, column=1)

insulin_label = tkinter.Label(text="Podaj ilość wkładów w opakowaniu:", background=BACKGROUND_COLOR2, font=FONT)
insulin_label.grid(row=2, column=0)
insulin_label.grid_remove()
# insulin_label.grid()
insulin_entry = tkinter.Entry(width=10, font=FONT)
insulin_entry.grid(row=2, column=1)
insulin_entry.grid_remove()
# insulin_entry.grid()

dose_label = tkinter.Label(text="Podaj ilość sztuk w opakowaniu:", background=BACKGROUND_COLOR2, font=FONT)
dose_label.grid(row=3, column=0)
dose_entry = tkinter.Entry(width=10, font=FONT)
dose_entry.grid(row=3, column=1)

usage_label = tkinter.Label(text="Podaj liczbę sztuk, jaką pacjent stosuje na dzień:", background=BACKGROUND_COLOR2, font=FONT)
usage_label.grid(row=4, column=0)
usage_entry = tkinter.Entry(width=10, font=FONT)
usage_entry.grid(row=4, column=1)

date_issued_label = tkinter.Label(text="Podaj datę wystawienia:", bg=BACKGROUND_COLOR2, font=FONT)
date_issued_label.grid(row=5, column=1)
day_label = tkinter.Label(text="dzień:", bg=BACKGROUND_COLOR2, font=FONT)
day_label.grid(row=6, column=0)
day_entry = tkinter.Entry(justify="left", font=FONT)
day_entry.grid(row=6, column=1)
day_entry.insert(0, str(datetime.datetime.now().day))
month_label = tkinter.Label(text="miesiąc:", bg=BACKGROUND_COLOR2, font=FONT)
month_label.grid(row=7, column=0)
month_entry = tkinter.Entry(justify="left", font=FONT)
month_entry.grid(row=7, column=1)
month_entry.insert(0, str(datetime.datetime.now().month))
year_label = tkinter.Label(text="rok:", bg=BACKGROUND_COLOR2, font=FONT)
year_label.grid(row=8, column=0)
year_entry = tkinter.Entry(justify="left", font=FONT)
year_entry.grid(row=8, column=1)
year_entry.insert(0, str(datetime.datetime.now().year))

smallest_box_label = tkinter.Label(text="Jakie jest najmniejsze refundowane opakowanie?", background=BACKGROUND_COLOR2, font=FONT)
smallest_box_label.grid(row=9, column=0)
smallest_box_entry = tkinter.Entry(width=10, font=FONT)
smallest_box_entry.grid(row=9, column=1)

exit_button = tkinter.Button(text="WYJDŹ", command=exit, width=10, height=5, fg="red", background="#F3CCF3", font=FONT)
exit_button.grid(row=0, column=2, columnspan=2)

insulin_button = tkinter.Button(text="INSULINA", borderwidth=10, command=insulin, background=BACKGROUND_COLOR2, font=FONT)
insulin_button.grid(row=3, column=2)

insulin_button = tkinter.Button(text="TABLETKI ITP.", borderwidth=10, command=pills, background=BACKGROUND_COLOR2, font=FONT)
insulin_button.grid(row=4, column=2)


window.mainloop()
