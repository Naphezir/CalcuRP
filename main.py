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

insulin_switch = False


def insulin():
    global insulin_switch
    insulin_entry.grid()
    insulin_label.grid()
    dose_label.config(text="Podaj ilość jednostek we wkładzie:")
    usage_label.config(text="Podaj liczbę jednostek, jaką pacjent stosuje na dzień:")
    smallest_box_label.grid_remove()
    amount_bought_label.config(text="Podaj liczbę wkładów, jaka została wtedy wykupiona:")
    insulin_switch = True
    show_smallest_box_entry()


def pills():
    global insulin_switch
    insulin_entry.grid_remove()
    insulin_label.grid_remove()
    dose_label.config(text="Podaj ilość sztuk w opakowaniu:")
    usage_label.config(text="Podaj liczbę sztuk, jaką pacjent stosuje na dzień:")
    amount_bought_label.config(text="Podaj liczbę sztuk, jaka została wtedy wykupiona:")
    insulin_switch = False
    show_smallest_box_entry()


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


# def calculate_insulin_yearly():
#     message = ""
#     issue_day = int(day_entry.get().replace(',', '.'))
#     issue_month = int(month_entry.get().replace(',', '.'))
#     issue_year = int(year_entry.get().replace(',', '.'))
#     issue_date = datetime.datetime(year=issue_year, month=issue_month, day=issue_day)
#     number_of_boxes = float(boxes_entry.get().replace(',', '.'))
#     number_of_fills_in_box = int(insulin_entry.get().replace(',', '.'))
#     number_of_fills_left = int(number_of_boxes * number_of_fills_in_box)
#     fills_lost = 0
#     number_of_units_in_fill = float(dose_entry.get().replace(',', '.'))
#     units_taken_daily = float(usage_entry.get().replace(',', '.'))
#     days_passed_since_issue = (datetime.datetime.now() - issue_date).days
#     if days_passed_since_issue > 30:
#         fills_lost = int((days_passed_since_issue * units_taken_daily) // number_of_units_in_fill)
#         result_text.configure(state=tkinter.NORMAL)
#         result_text.delete("1.0", tkinter.END)
#         message += f"Przepadło {fills_lost} wkładów.\n"
#         result_text.configure(state=tkinter.DISABLED, bg=BACKGROUND_COLOR)
#         number_of_fills_left = (number_of_boxes * number_of_fills_in_box) - fills_lost
#
#     fills_to_give = int((units_taken_daily * 120) // number_of_units_in_fill)
#     if fills_to_give >= number_of_fills_left:
#         if fills_lost:
#             message = f"Można wydać wszystkie pozostałe {fills_to_give} wkłady,\nczyli {fills_to_give/number_of_fills_in_box} op."
#         else:
#             message = f"Można wydać wszystkie op."
#     else:
#         days_of_therapy_3_4 = int((fills_to_give * number_of_units_in_fill / units_taken_daily) * 3 / 4)
#         next_buy_date= (datetime.datetime.now() + datetime.timedelta(days=days_of_therapy_3_4)).strftime('%d.%m.%Y')
#         message = (f"Można wydać {fills_to_give} wkładów,\nczyli {fills_to_give / number_of_fills_in_box}op."
#                    f"\nReszta najwcześniej po {next_buy_date}!")
#         if number_of_fills_left > fills_to_give + fills_lost:
#             next_portion_box_number = fills_to_give*2 + 1
#             message += (f"\nPozostała ilość począwszy od {next_portion_box_number}. wkładu.\n po {days_of_therapy_3_4}"
#                         f"dniach od {fills_to_give+1}. wkładu.")
#
#     result_text.configure(state=tkinter.NORMAL, bg=BACKGROUND_COLOR)
#     result_text.delete("1.0", tkinter.END)
#     result_text.insert("1.0", message)
#     result_text.configure(state=tkinter.DISABLED)
#     return

def calculate_insulin_yearly():
    message = ""
    issue_day = int(day_entry.get().replace(',', '.'))
    issue_month = int(month_entry.get().replace(',', '.'))
    issue_year = int(year_entry.get().replace(',', '.'))
    issue_date = datetime.datetime(year=issue_year, month=issue_month, day=issue_day)
    number_of_boxes = float(boxes_entry.get().replace(',', '.'))
    number_of_fills_in_box = int(insulin_entry.get().replace(',', '.'))
    number_of_fills_left = int(number_of_boxes * number_of_fills_in_box)
    fills_lost = 0
    number_of_units_in_fill = float(dose_entry.get().replace(',', '.'))
    units_taken_daily = float(usage_entry.get().replace(',', '.'))
    days_passed_since_issue = (datetime.datetime.now() - issue_date).days
    if days_passed_since_issue > 30:
        fills_lost = int((days_passed_since_issue * units_taken_daily) // number_of_units_in_fill)
        result_text.configure(state=tkinter.NORMAL)
        result_text.delete("1.0", tkinter.END)
        message += f"Przepadło {fills_lost} wkładów.\n"
        result_text.configure(state=tkinter.DISABLED, bg=BACKGROUND_COLOR)
        number_of_fills_left = (number_of_boxes * number_of_fills_in_box) - fills_lost

    fills_to_give = int((units_taken_daily * 120) // number_of_units_in_fill)
    if fills_to_give >= number_of_fills_left:
        if fills_lost:
            message = f"Można wydać wszystkie pozostałe {fills_to_give} wkłady,\nczyli {fills_to_give/number_of_fills_in_box} op."
        else:
            message = f"Można wydać wszystkie op."
    else:
        fills_left_after_first_buy = number_of_fills_left - fills_to_give
        days_of_therapy_3_4 = int((fills_to_give * number_of_units_in_fill / units_taken_daily) * 3 / 4)
        next_buy_date = (datetime.datetime.now() + datetime.timedelta(days=days_of_therapy_3_4)).strftime('%d.%m.%Y')
        next_portion = fills_left_after_first_buy
        if next_portion > fills_to_give:
            next_portion = fills_to_give
        message = (f"Można wydać {fills_to_give} wkładów, czyli {fills_to_give / number_of_fills_in_box}op."
                   f"\nKolejne {next_portion} wkł. czyli {next_portion/number_of_fills_in_box} op. najwcześniej po {next_buy_date}!")
        if fills_left_after_first_buy > 0:
            next_portion_fill_number = fills_to_give + next_portion + 1
            message += (f"\nPozostała ilość począwszy od {next_portion_fill_number}. wkładu\npo {days_of_therapy_3_4} "
                        f"dniach od {fills_to_give+1}. wkładu.")
        if number_of_boxes > (fills_lost/number_of_fills_in_box) + (fills_to_give/number_of_fills_in_box) + (next_portion/number_of_fills_in_box):
            maximum_amount_to_give = int((units_taken_daily*360) // number_of_units_in_fill)
            if maximum_amount_to_give < number_of_fills_left:
                message += f"\nMaksymalnie łącznie można wydać {maximum_amount_to_give} wkł. czyli {maximum_amount_to_give/number_of_fills_in_box} op."
    result_text.configure(state=tkinter.NORMAL, bg=BACKGROUND_COLOR)
    result_text.delete("1.0", tkinter.END)
    result_text.insert("1.0", message)
    result_text.configure(state=tkinter.DISABLED)
    return


def calculate_pills_yearly():
    message = ""
    issue_day = int(day_entry.get().replace(',', '.'))
    issue_month = int(month_entry.get().replace(',', '.'))
    issue_year = int(year_entry.get().replace(',', '.'))
    issue_date = datetime.datetime(year=issue_year, month=issue_month, day=issue_day)
    initial_number_of_boxes = float(boxes_entry.get().replace(',', '.'))
    number_of_boxes_left = initial_number_of_boxes
    boxes_lost = 0
    number_of_doses_in_box = float(dose_entry.get().replace(',', '.'))
    doses_taken_daily = float(usage_entry.get().replace(',', '.'))
    days_passed_since_issue = (datetime.datetime.now() - issue_date).days
    if days_passed_since_issue > 30:
        boxes_lost = int((days_passed_since_issue * doses_taken_daily) // number_of_doses_in_box)
        message += f"Przepadło {boxes_lost} op.\n"
        number_of_boxes_left = initial_number_of_boxes - boxes_lost

    boxes_to_give = int((doses_taken_daily * 120) // number_of_doses_in_box)
    if boxes_to_give == 0:
        boxes_to_give = 1
    if boxes_to_give >= number_of_boxes_left:
        if boxes_lost:
            message = f"Można wydać pozostałe {number_of_boxes_left} op."
        else:
            message = f"Można wydać wszystkie op."
    else:
        boxes_left_after_first_buy = number_of_boxes_left - boxes_to_give
        days_of_therapy_3_4 = int((boxes_to_give * number_of_doses_in_box / doses_taken_daily) * 3 / 4)
        next_buy_date = (datetime.datetime.now() + datetime.timedelta(days=days_of_therapy_3_4)).strftime('%d.%m.%Y')
        next_portion = boxes_left_after_first_buy
        if next_portion > boxes_to_give:
            next_portion = boxes_to_give
        message = f"Można wydać {boxes_to_give} op.\nKolejne {next_portion} op. może być wydane\nnajwcześniej po {next_buy_date}!"
        if boxes_left_after_first_buy > 0:
            next_portion_box_number = boxes_to_give + next_portion + 1
            message += (f"\nPozostała ilość począwszy od {next_portion_box_number}. op.\npo {days_of_therapy_3_4} "
                        f"dniach od {boxes_to_give+1}. op.")
        if initial_number_of_boxes > boxes_lost + boxes_to_give + next_portion:
            maximum_amount_to_give = int((doses_taken_daily*360) // number_of_doses_in_box)
            if maximum_amount_to_give < number_of_boxes_left:
                message += f"\nMaksymalnie łącznie można wydać {maximum_amount_to_give} op."

    result_text.configure(state=tkinter.NORMAL, bg=BACKGROUND_COLOR)
    result_text.delete("1.0", tkinter.END)
    result_text.insert("1.0", message)
    result_text.configure(state=tkinter.DISABLED)
    return


def calculate_insulin_monthly():
    message = ""
    issue_day = int(day_entry.get().replace(',', '.'))
    issue_month = int(month_entry.get().replace(',', '.'))
    issue_year = int(year_entry.get().replace(',', '.'))
    issue_date = datetime.datetime(year=issue_year, month=issue_month, day=issue_day)
    number_of_boxes = float(boxes_entry.get().replace(',', '.'))
    number_of_fills_in_box = int(insulin_entry.get().replace(',', '.'))
    number_of_fills_left = int(number_of_boxes * number_of_fills_in_box)
    number_of_units_in_fill = float(dose_entry.get().replace(',', '.'))
    units_taken_daily = float(usage_entry.get().replace(',', '.'))
    days_passed_since_issue = (datetime.datetime.now() - issue_date).days
    if days_passed_since_issue > 30:
        result_text.configure(state=tkinter.NORMAL)
        result_text.delete("1.0", tkinter.END)
        result_text.insert("1.0", "RECEPTA PRZETERMINOWANA")
        result_text.configure(state=tkinter.DISABLED, bg="red")
        return

    fills_to_give = int((units_taken_daily * 120) // number_of_units_in_fill)
    if fills_to_give >= number_of_fills_left:
        message = f"Można wydać wszystkie op."
    else:
        message = f"Można wydać {fills_to_give} wkładów,\nczyli {fills_to_give/number_of_fills_in_box}op.\nReszta przepada!"

    result_text.configure(state=tkinter.NORMAL, bg=BACKGROUND_COLOR)
    result_text.delete("1.0", tkinter.END)
    result_text.insert("1.0", message)
    result_text.configure(state=tkinter.DISABLED)


def calculate_pills_monthly():
    message = ""
    issue_day = int(day_entry.get().replace(',', '.'))
    issue_month = int(month_entry.get().replace(',', '.'))
    issue_year = int(year_entry.get().replace(',', '.'))
    issue_date = datetime.datetime(year=issue_year, month=issue_month, day=issue_day)
    number_of_boxes = float(boxes_entry.get().replace(',', '.'))
    number_of_doses_in_box = float(dose_entry.get().replace(',', '.'))
    doses_taken_daily = float(usage_entry.get().replace(',', '.'))
    days_passed_since_issue = (datetime.datetime.now() - issue_date).days
    if days_passed_since_issue > 30:
        result_text.configure(state=tkinter.NORMAL)
        result_text.delete("1.0", tkinter.END)
        result_text.insert("1.0", "RECEPTA PRZETERMINOWANA")
        result_text.configure(state=tkinter.DISABLED, bg="red")
        return
    boxes_to_give = int((doses_taken_daily * 120) // number_of_doses_in_box)
    if boxes_to_give == 0:
        boxes_to_give = 1
    print(type(boxes_to_give))
    if boxes_to_give >= number_of_boxes:
        message = f"Można wydać wszystkie op."
    else:
        message = f"Można wydać {boxes_to_give} op.\nReszta przepada!"
    result_text.configure(state=tkinter.NORMAL, bg=BACKGROUND_COLOR)
    result_text.delete("1.0", tkinter.END)
    result_text.insert("1.0", message)
    result_text.configure(state=tkinter.DISABLED)


def choose_calculate_yearly():
    if insulin_switch:
        calculate_insulin_yearly()
    else:
        calculate_pills_yearly()


def choose_calculate_monthly():
    if insulin_switch:
        calculate_insulin_monthly()
    else:
        calculate_pills_monthly()


def check_data_completion():
    try:
        number_of_boxes = float(boxes_entry.get().replace(',', '.'))
        number_of_doses_in_box = float(dose_entry.get().replace(',', '.'))
        doses_taken_daily = float(usage_entry.get().replace(',', '.'))
        if insulin_switch:
            number_of_fills = float(insulin_entry.get().replace(',', '.'))
        return True
    except ValueError:
        result_text.configure(state=tkinter.NORMAL)
        result_text.delete("1.0", tkinter.END)
        result_text.insert("1.0", "PODANO BŁĘDNE\nLUB NIEKOMPLETNE DANE")
        result_text.configure(state=tkinter.DISABLED, bg="red")
        return False


def check_date_correctness():
    try:
        issue_day = int(day_entry.get().replace(',', '.'))
        issue_month = int(month_entry.get().replace(',', '.'))
        issue_year = int(year_entry.get().replace(',', '.'))
        if issue_day < 1 or issue_day > 31 or issue_month < 1 or issue_month > 12 or issue_year < 2023:
            show_wrong_date()
            return
        else:
            issue_date = datetime.datetime(year=issue_year, month=issue_month, day=issue_day)
            days_passed_since_issue = (datetime.datetime.now() - issue_date).days
        if days_passed_since_issue < 0:
            show_wrong_date()
            return False
        else:
            date_issued_label.config(text="Podaj datę wystawienia:", bg=BACKGROUND_COLOR2)
    except ValueError:
        show_wrong_date()
        return False
    return True


def show_wrong_date():
    date_issued_label.config(text="PODANO BŁĘDNĄ DATĘ", bg="red")
    result_text.configure(state=tkinter.NORMAL, bg=BACKGROUND_COLOR)
    result_text.delete("1.0", tkinter.END)
    result_text.configure(state=tkinter.DISABLED)


def calculate_results():
    if not check_data_completion():
        return
    if not check_date_correctness():
        return
    if prescription_type.get():  # 1 - roczna
        choose_calculate_yearly()
    else:
        choose_calculate_monthly()  # 0 - miesięczna
# def calculate_results():
#     global insulin_switch
#     if insulin_switch:
#         calculate_insulin()
#         return
#     message = ""
#     try:
#         issue_day = int(day_entry.get().replace(',', '.'))
#         issue_month = int(month_entry.get().replace(',', '.'))
#         issue_year = int(year_entry.get().replace(',', '.'))
#         issue_date = datetime.datetime(year=issue_year, month=issue_month, day=issue_day)
#         number_of_boxes = float(boxes_entry.get().replace(',', '.'))
#         number_of_boxes_left = number_of_boxes
#         boxes_lost = 0
#         number_of_doses_in_box = float(dose_entry.get().replace(',', '.'))
#         doses_taken_daily = float(usage_entry.get().replace(',', '.'))
#         days_passed_since_issue = (datetime.datetime.now() - issue_date).days
#
#         if days_passed_since_issue > 30:
#             boxes_lost = int((days_passed_since_issue * doses_taken_daily)//number_of_doses_in_box)
#             result_text.configure(state=tkinter.NORMAL)
#             result_text.delete("1.0", tkinter.END)
#             message += f"Przepadło {boxes_lost} op.\n"
#             result_text.configure(state=tkinter.DISABLED, bg=BACKGROUND_COLOR)
#             number_of_boxes_left = number_of_boxes - boxes_lost
#
#         if days_passed_since_issue < 0:
#             date_issued_label.config(text="PODANO BŁĘDNĄ DATĘ", bg="red")
#             result_text.configure(state=tkinter.NORMAL, bg=BACKGROUND_COLOR)
#             result_text.delete("1.0", tkinter.END)
#             result_text.configure(state=tkinter.DISABLED)
#             return
#         else:
#             date_issued_label.config(text="Podaj datę wystawienia:", bg=BACKGROUND_COLOR2)
#
#         boxes_to_give = int((float(doses_taken_daily)*120)//float(number_of_doses_in_box))
#         if boxes_to_give >= number_of_boxes_left:
#             boxes_to_give = int(number_of_boxes_left)
#
#         result_text.configure(state=tkinter.NORMAL, bg=BACKGROUND_COLOR)
#         result_text.delete("1.0", tkinter.END)
#         message += f"Można wydać {boxes_to_give} op.\n"
#
#         if number_of_boxes_left > boxes_to_give:
#             days_of_therapy_covered = int((boxes_to_give*number_of_doses_in_box/doses_taken_daily)*3/4)
#             message += f"Reszta najwcześniej po {(datetime.datetime.now() + datetime.timedelta(days=days_of_therapy_covered)).strftime('%d.%m.%Y')} <<<<"
#
#         result_text.insert("1.0", message)
#         result_text.configure(state=tkinter.DISABLED)
#
#     except ValueError:
#         result_text.configure(state=tkinter.NORMAL)
#         result_text.delete("1.0", tkinter.END)
#         result_text.insert("1.0", "PODANO BŁĘDNE\nLUB NIEKOMPLETNE DANE")
#         result_text.configure(state=tkinter.DISABLED, bg="red")
#
#
# def calculate_insulin():
#     message = ""
#     try:
#         issue_day = int(day_entry.get().replace(',', '.'))
#         issue_month = int(month_entry.get().replace(',', '.'))
#         issue_year = int(year_entry.get().replace(',', '.'))
#         issue_date = datetime.datetime(year=issue_year, month=issue_month, day=issue_day)
#         number_of_boxes = float(boxes_entry.get().replace(',', '.'))
#         number_of_fills_in_box = int(insulin_entry.get().replace(',', '.'))
#         number_of_fills_left = number_of_boxes * number_of_fills_in_box
#         fills_lost = 0
#         number_of_units_in_fill = float(dose_entry.get().replace(',', '.'))
#         units_taken_daily = float(usage_entry.get().replace(',', '.'))
#         days_passed_since_issue = (datetime.datetime.now() - issue_date).days
#
#         if days_passed_since_issue > 30:
#             fills_lost = int((days_passed_since_issue * units_taken_daily) // number_of_units_in_fill)
#             result_text.configure(state=tkinter.NORMAL)
#             result_text.delete("1.0", tkinter.END)
#             message += f"Przepadło {fills_lost} wkładów.\n"
#             result_text.configure(state=tkinter.DISABLED, bg=BACKGROUND_COLOR)
#             number_of_fills_left = (number_of_boxes * number_of_fills_in_box) - fills_lost
#
#         if days_passed_since_issue < 0:
#             date_issued_label.config(text="PODANO BŁĘDNĄ DATĘ", bg="red")
#             result_text.configure(state=tkinter.NORMAL, bg=BACKGROUND_COLOR)
#             result_text.delete("1.0", tkinter.END)
#             result_text.configure(state=tkinter.DISABLED)
#             return
#         else:
#             date_issued_label.config(text="Podaj datę wystawienia:", bg=BACKGROUND_COLOR2)
#
#         fills_to_give = int((float(units_taken_daily) * 120) // float(number_of_units_in_fill))
#         if fills_to_give >= number_of_fills_left:
#             fills_to_give = int(number_of_fills_left)
#
#         result_text.configure(state=tkinter.NORMAL, bg=BACKGROUND_COLOR)
#         result_text.delete("1.0", tkinter.END)
#         message += f"Można wydać {fills_to_give} wkładów, czyli {fills_to_give/number_of_fills_in_box} op.\n"
#
#         if number_of_fills_left > fills_to_give:
#             days_of_therapy_covered = int((fills_to_give * number_of_units_in_fill / units_taken_daily) * 3 / 4)
#             message += f"Reszta najwcześniej po {(datetime.datetime.now() + datetime.timedelta(days=days_of_therapy_covered)).strftime('%d.%m.%Y')} <<<<"
#
#         result_text.insert("1.0", message)
#         result_text.configure(state=tkinter.DISABLED)
#
#     except ValueError:
#         result_text.configure(state=tkinter.NORMAL)
#         result_text.delete("1.0", tkinter.END)
#         result_text.insert("1.0", "PODANO BŁĘDNE\nLUB NIEKOMPLETNE DANE")
#         result_text.configure(state=tkinter.DISABLED, bg="red")


result_text = tkinter.Text(background=BACKGROUND_COLOR, fg="#280274", font=FONT, width=50, height=6)
result_text.configure(state=tkinter.DISABLED)
result_text.grid(row=0, column=0, sticky="nw")

prescription_type_frame = tkinter.Frame(bg=BACKGROUND_COLOR)
prescription_type_frame.grid(row=0, column=1, sticky="nw")


def show_smallest_box_entry():
    if smallest_box.get():
        smallest_box_entry.grid()
        smallest_box_label.grid()
    else:
        smallest_box_entry.grid_remove()
        smallest_box_label.grid_remove()


prescription_type = tkinter.IntVar()
yearly = tkinter.Radiobutton(prescription_type_frame, text="Rp roczna", variable=prescription_type, value=1, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, font=FONT2)
yearly.grid(row=0, column=0, sticky="nw")
monthly = tkinter.Radiobutton(prescription_type_frame, text="Rp miesięczna", variable=prescription_type, value=0, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, font=FONT2)
monthly.grid(row=1, column=0, sticky="nw")
smallest_box = tkinter.BooleanVar()
smallest_box_button = tkinter.Checkbutton(prescription_type_frame, text="(Naj)mniejsze\nrefundowane\nopakowanie?", variable=smallest_box, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, font=FONT2, command=show_smallest_box_entry)
smallest_box_button.grid(row=2, column=0, sticky="nw")

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
smallest_box_label.grid_remove()
smallest_box_entry = tkinter.Entry(width=10, font=FONT)
smallest_box_entry.grid(row=9, column=1, sticky="w", padx=3)
smallest_box_entry.grid_remove()

calculate_button = tkinter.Button(text="PRZELICZ", width=10, height=5, background="#294B29", font=FONT, command=calculate_results, activebackground="#294B29")
calculate_button.grid(row=6, column=2, rowspan=3)

exit_button = tkinter.Button(text="WYJDŹ", command=exit, width=10, height=5, fg="red", background="#F3CCF3", font=FONT, activebackground="#F3CCF3")
exit_button.grid(row=0, column=2)

insulin_button = tkinter.Button(text="INSULINA", command=insulin, background=BACKGROUND_COLOR2, font=FONT2, activebackground=BACKGROUND_COLOR2)
insulin_button.grid(row=4, column=2)

pills_button = tkinter.Button(text="TABLETKI ITP.", command=pills, background=BACKGROUND_COLOR2, font=FONT2, activebackground=BACKGROUND_COLOR2)
pills_button.grid(row=3, column=2)

previous_buy_button = tkinter.Button(text="Wcześniejsze\nrealizacje", command=previous_buys, background=BACKGROUND_COLOR2, font=FONT2, activebackground=BACKGROUND_COLOR2)
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

bought_button = tkinter.Button(text="Dodaj\nrealizację", background=BACKGROUND_COLOR2, font=FONT2, activebackground=BACKGROUND_COLOR2)
bought_button.grid(row=14, column=2)
bought_button.grid_remove()

window.mainloop()
