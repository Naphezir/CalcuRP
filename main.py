import tkinter
import datetime

BACKGROUND_COLOR = "#FFBB64"
BACKGROUND_COLOR2 = "#FFEAA7"
FONT = ("Liberation Serif", 20, "normal")
FONT2 = ("Liberation Serif", 13, "normal")

window = tkinter.Tk()
version = "PL"
window.title("Kalkulator E-recepty")
window.config(height=500, width=1000, padx=10, pady=10, bg=BACKGROUND_COLOR)

# canvas = tkinter.Canvas(height=500, width=1000)
# canvas.grid(row=0, column=0)
# canvas.create_text(10, 10,text="Hello")


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


def previous_buys():
    date_bought_label.grid()
    buyday_label.grid()
    buyday_entry.grid()
    buymonth_label.grid()
    buymonth_entry.grid()
    buyyear_label.grid()
    buyyear_entry.grid()
    amount_bought_label.grid()
    amount_bought_entry.grid()
    bought_button.grid()
    previous_buy_button.config(command=hide_previous_buys)


def hide_previous_buys():
    date_bought_label.grid_remove()
    buyday_label.grid_remove()
    buyday_entry.grid_remove()
    buymonth_label.grid_remove()
    buymonth_entry.grid_remove()
    buyyear_label.grid_remove()
    buyyear_entry.grid_remove()
    amount_bought_label.grid_remove()
    amount_bought_entry.grid_remove()
    bought_button.grid_remove()
    previous_buy_button.config(command=previous_buys)


def calculate_results():
    try:
        issue_day = day_entry.get().replace(',', '.')
        issue_month = month_entry.get().replace(',', '.')
        issue_year = year_entry.get().replace(',', '.')
        number_of_boxes = boxes_entry.get().replace(',', '.')
        number_of_doses_in_box = dose_entry.get().replace(',', '.')
        doses_taken_daily = usage_entry.get().replace(',', '.')

        boxes_to_give = int((float(doses_taken_daily)*120)//float(number_of_doses_in_box))
        if boxes_to_give >= float(number_of_boxes):
            boxes_to_give = "wszystkie"
        result_label.configure(state=tkinter.NORMAL)
        result_label.delete("1.0", tkinter.END)
        result_label.insert("1.0", f"Można wydać {boxes_to_give} op.")
    except ValueError:
        result_label.configure(state=tkinter.NORMAL)
        result_label.delete("1.0", tkinter.END)
        result_label.insert("1.0", "PODANO BŁĘDNE\nLUB NIEKOMPLETNE DANE")


result_label = tkinter.Text( background=BACKGROUND_COLOR, fg="#280274", font=FONT, width=50, height=6)
result_label.configure(state=tkinter.DISABLED)
result_label.grid(row=0, column=0, sticky="nw")

right_canvas = tkinter.Canvas(background=BACKGROUND_COLOR, width=20, height=1000, highlightthickness=0)
right_canvas.grid(row=0, column=3, rowspan=20)
bottom_canvas = tkinter.Canvas(background=BACKGROUND_COLOR, width=1000, height=10, highlightthickness=0)
bottom_canvas.grid(row=20, column=0, columnspan=4)

boxes_label = tkinter.Label(text="Podaj ilość zapisanych opakowań:", background=BACKGROUND_COLOR2, font=FONT)
boxes_label.grid(row=1, column=0, sticky="e")
boxes_entry = tkinter.Entry(width=10, font=FONT)
boxes_entry.grid(row=1, column=1, sticky="w", padx=3)

insulin_label = tkinter.Label(text="Podaj ilość wkładów w opakowaniu:", background=BACKGROUND_COLOR2, font=FONT)
insulin_label.grid(row=2, column=0, sticky="e")
insulin_label.grid_remove()
insulin_entry = tkinter.Entry(width=10, font=FONT)
insulin_entry.grid(row=2, column=1, sticky="w", padx=3)
insulin_entry.grid_remove()

dose_label = tkinter.Label(text="Podaj ilość sztuk w opakowaniu:", background=BACKGROUND_COLOR2, font=FONT)
dose_label.grid(row=3, column=0, sticky="e")
dose_entry = tkinter.Entry(width=10, font=FONT)
dose_entry.grid(row=3, column=1, sticky="w", padx=3)

usage_label = tkinter.Label(text="Podaj liczbę sztuk, jaką pacjent stosuje na dzień:", background=BACKGROUND_COLOR2, font=FONT)
usage_label.grid(row=4, column=0, sticky="e")
usage_entry = tkinter.Entry(width=10, font=FONT)
usage_entry.grid(row=4, column=1, sticky="w", padx=3)

date_issued_label = tkinter.Label(text="Podaj datę wystawienia:", bg=BACKGROUND_COLOR2, font=FONT)
date_issued_label.grid(row=5, column=0, sticky="e")
day_label = tkinter.Label(text="dzień:", bg=BACKGROUND_COLOR2, font=FONT)
day_label.grid(row=6, column=0, sticky="e")
day_entry = tkinter.Entry(width=10, font=FONT)
day_entry.grid(row=6, column=1, padx=3, sticky="w")
day_entry.insert(0, str(datetime.datetime.now().day))
month_label = tkinter.Label(text="miesiąc:", bg=BACKGROUND_COLOR2, font=FONT)
month_label.grid(row=7, column=0, sticky="e")
month_entry = tkinter.Entry(width=10, font=FONT)
month_entry.grid(row=7, column=1, padx=3, sticky="w")
month_entry.insert(0, str(datetime.datetime.now().month))
year_label = tkinter.Label(text="rok:", bg=BACKGROUND_COLOR2, font=FONT)
year_label.grid(row=8, column=0, sticky="e")
year_entry = tkinter.Entry(width=10, font=FONT)
year_entry.grid(row=8, column=1, padx=3, sticky="w")
year_entry.insert(0, str(datetime.datetime.now().year))

smallest_box_label = tkinter.Label(text="Jakie jest najmniejsze refundowane opakowanie:", background=BACKGROUND_COLOR2, font=FONT)
smallest_box_label.grid(row=9, column=0, sticky="e")
smallest_box_entry = tkinter.Entry(width=10, font=FONT)
smallest_box_entry.grid(row=9, column=1, sticky="w", padx=3)

calculate_button = tkinter.Button(text="PRZELICZ", width=10, height=5, background="#294B29", font=FONT, command=calculate_results)
calculate_button.grid(row=6, column=2, rowspan=3)

exit_button = tkinter.Button(text="WYJDŹ", command=exit, width=10, height=5, fg="red", background="#F3CCF3", font=FONT)
exit_button.grid(row=0, column=2)

insulin_button = tkinter.Button(text="INSULINA", command=insulin, background=BACKGROUND_COLOR2, font=FONT2)
insulin_button.grid(row=4, column=2)

pills_button = tkinter.Button(text="TABLETKI ITP.", command=pills, background=BACKGROUND_COLOR2, font=FONT2)
pills_button.grid(row=3, column=2)

previous_buy_button = tkinter.Button(text="Wcześniejsze\nrealizacje", command=previous_buys, background=BACKGROUND_COLOR2, font=FONT2)
previous_buy_button.grid(row=9, column=2)

line_canvas = tkinter.Canvas(background="#6C22A6", width=1000, height=10, highlightthickness=0)
line_canvas.grid(row=10, column=0, columnspan=4)

date_bought_label = tkinter.Label(text="Podaj datę wykupienia:", bg=BACKGROUND_COLOR2, font=FONT)
date_bought_label.grid(row=11, column=0, sticky="e")
date_bought_label.grid_remove()
buyday_label = tkinter.Label(text="dzień:", bg=BACKGROUND_COLOR2, font=FONT)
buyday_label.grid(row=12, column=0, sticky="e")
buyday_label.grid_remove()
buyday_entry = tkinter.Entry(width=10, font=FONT)
buyday_entry.grid(row=12, column=1, padx=3, sticky="w")
buyday_entry.grid_remove()
buymonth_label = tkinter.Label(text="miesiąc:", bg=BACKGROUND_COLOR2, font=FONT)
buymonth_label.grid(row=13, column=0, sticky="e")
buymonth_label.grid_remove()
buymonth_entry = tkinter.Entry(width=10, font=FONT)
buymonth_entry.grid(row=13, column=1, padx=3, sticky="w")
buymonth_entry.grid_remove()
buyyear_label = tkinter.Label(text="rok:", bg=BACKGROUND_COLOR2, font=FONT)
buyyear_label.grid(row=14, column=0, sticky="e")
buyyear_label.grid_remove()
buyyear_entry = tkinter.Entry(width=10, font=FONT)
buyyear_entry.grid(row=14, column=1, padx=3, sticky="w")
buyyear_entry.grid_remove()

amount_bought_label = tkinter.Label(text="Podaj liczbę sztuk, jaka została wtedy wykupiona:", background=BACKGROUND_COLOR2, font=FONT)
amount_bought_label.grid(row=14, column=0, sticky="e")
amount_bought_label.grid_remove()
amount_bought_entry = tkinter.Entry(width=10, font=FONT)
amount_bought_entry.grid(row=14, column=1, sticky="w")
amount_bought_entry.grid_remove()

bought_button = tkinter.Button(text="Dodaj\nrealizację", background=BACKGROUND_COLOR2, font=FONT2)
bought_button.grid(row=14, column=2)
bought_button.grid_remove()

window.mainloop()
