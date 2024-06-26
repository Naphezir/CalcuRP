import math
import tkinter
import datetime
from prescription import Prescription

BACKGROUND_COLOR = "#FFBB64"
BACKGROUND_COLOR2 = "#FFEAA7"
BACKGROUND_COLOR3 = "#DCFFB7"
FONT = ("Liberation Serif", 15, "normal")
FONT2 = ("Liberation Serif", 10, "normal")

window = tkinter.Tk()
version = "PL"
window.title("Kalkulator E-recepty")
window.config(bg=BACKGROUND_COLOR)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1, minsize=100)
window.columnconfigure(2, weight=1, minsize=100)
window.rowconfigure(0, weight=1, minsize=120)
# insulin_switch = False
# previous_buys_present = False
# previous_buys_list = []
# TODO /\ zmienić te rzeczy i przenieść do klasy
the_current_prescription = Prescription()


def insulin(current_prescription):
    insulin_entry.grid()
    insulin_label.grid()
    dose_label.config(text="Podaj ilość jednostek we wkładzie:")
    usage_label.config(text="Podaj, ile jednostek pacjent bierze na dzień:")
    smallest_box_label.grid_remove()
    amount_bought_label.config(text="Podaj liczbę wkładów, jaka została wykupiona:")
    current_prescription.insulin_switch = True
    show_smallest_box_entry()
    smallest_box_entry.grid_remove()
    smallest_box_label.grid_remove()
    smallest_box_button.grid_remove()
    return


def pills(current_prescription):
    insulin_entry.grid_remove()
    insulin_label.grid_remove()
    dose_label.config(text="Podaj ilość sztuk w opakowaniu:")
    usage_label.config(text="Podaj liczbę sztuk, jaką pacjent stosuje na dzień:")
    amount_bought_label.config(text="Podaj liczbę sztuk, jaka została wtedy wykupiona:")
    current_prescription.insulin_switch = False
    show_smallest_box_entry()
    smallest_box_button.grid()
    return


def previous_buys(current_prescription):

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
    previous_buy_button.config(command=lambda: hide_previous_buys(current_prescription))
    current_prescription.previous_buys_present = True
    previous_buys_label.grid()
    return


def hide_previous_buys(current_prescription):
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
    previous_buy_button.config(command=lambda: previous_buys(current_prescription))
    current_prescription.previous_buys_present = False
    current_prescription.previous_buys_list = []
    previous_buys_label.config(text="")
    previous_buys_label.grid_remove()
    return


def get_smallest_box(box):
    if smallest_box.get():
        smallest_box_label.config(text="Jakie jest najmniejsze refundowane opakowanie:", background=BACKGROUND_COLOR2)
        try:
            if box > int(smallest_box_entry.get()) > 0:
                return int(smallest_box_entry.get())
            else:
                smallest_box_label.config(text="To opakowanie nie jest mniejsze", bg="red")
        except ValueError:
            smallest_box_label.config(text="Błędna wielkość najmniejszego op. refund.", bg="red")
            return 0
    else:
        return 0


def calculate_insulin_yearly(current_prescription):
    message = ""
    issue_day = int(day_entry.get().replace(',', '.'))
    issue_month = int(month_entry.get().replace(',', '.'))
    issue_year = int(year_entry.get().replace(',', '.'))
    current_prescription.set_initial_number_of_boxes(float(boxes_entry.get().replace(',', '.')))
    current_prescription.set_number_of_fills_in_box(int(insulin_entry.get().replace(',', '.')))
    current_prescription.set_number_of_units_in_fill(float(dose_entry.get().replace(',', '.')))
    current_prescription.set_units_taken_daily(float(usage_entry.get().replace(',', '.')))

    current_prescription.set_issue_date(issue_day, issue_month, issue_year)
    current_prescription.set_number_of_fills_left()
    # days_passed_since_issue = (datetime.datetime.now() - issue_date).days <<< zrobione przy set_issue_date

    current_prescription.set_maximum_units_to_give_once()
    current_prescription.set_maximum_fills_to_give_once()
    if current_prescription.maximum_fills_to_give_once == 0:
        current_prescription.maximum_fills_to_give_once = 1
    current_prescription.set_maximum_units_overall()
    current_prescription.set_maximum_fills_overall()
    if current_prescription.maximum_fills_overall == 0:
        current_prescription.maximum_fills_overall = 1
    if current_prescription.number_of_fills_left > current_prescription.maximum_fills_overall:
        current_prescription.number_of_fills_left = current_prescription.maximum_fills_overall
        message += f"Maksymalnie można wydać łącznie {int(current_prescription.maximum_fills_overall)} wkładów, (tj. {(current_prescription.maximum_fills_overall / current_prescription.number_of_fills_in_box)} op.)\n"

    if current_prescription.days_passed_since_issue > 30:
        current_prescription.set_fills_lost()
        if current_prescription.fills_lost == 0:
            current_prescription.fills_lost = 1
        message += f"Przepadło {int(current_prescription.fills_lost)} wkładów.\n"
        current_prescription.set_number_of_fills_left(current_prescription.number_of_fills_left - current_prescription.fills_lost)

    if current_prescription.maximum_fills_to_give_once >= current_prescription.number_of_fills_left:
        if current_prescription.fills_lost and current_prescription.number_of_fills_left > 0:
            message += f"Można wydać pozostałe {current_prescription.number_of_fills_left} wkłady/ów, czyli {(current_prescription.number_of_fills_left / current_prescription.number_of_fills_in_box)} op."
        elif current_prescription.number_of_fills_left <= 0:
            message = "Przepadło wszystko."
        else:
            message += f"Dziś można wydać {current_prescription.number_of_fills_left} wkł."
    else:
        current_prescription.set_units_to_give()
        current_prescription.set_fills_to_give()
        if current_prescription.fills_to_give == 0:
            current_prescription.fills_to_give = 1
        current_prescription.set_days_of_therapy_3_4()
        next_buy_date = (datetime.datetime.now() + datetime.timedelta(days=current_prescription.days_of_therapy_3_4)).strftime('%d.%m.%Y')
        message += f"Dziś można wydać {current_prescription.fills_to_give} wkłady/ów, czyli {current_prescription.fills_to_give / current_prescription.number_of_fills_in_box} op."
        current_prescription.set_number_of_fills_left(current_prescription.number_of_fills_left - current_prescription.fills_to_give)

        while current_prescription.number_of_fills_left > 0:
            if current_prescription.number_of_fills_left < current_prescription.maximum_fills_to_give_once:
                message += f"\nOstatnie {int(current_prescription.number_of_fills_left)} wkłady/ów, (czyli {current_prescription.number_of_fills_left / current_prescription.number_of_fills_in_box} op.), może być wydane\nnajwcześniej po {next_buy_date} <<<<"
                break
            elif current_prescription.number_of_fills_left == current_prescription.maximum_fills_to_give_once:
                message += f"\nOstatnie 1 op. ({current_prescription.number_of_fills_left} wkł.) może być wydane najwcześniej po {next_buy_date} <<<<"
                break
            elif current_prescription.number_of_fills_left > current_prescription.maximum_fills_to_give_once:
                current_prescription.units_to_give = int(current_prescription.maximum_fills_to_give_once * current_prescription.number_of_units_in_fill)
                current_prescription.set_fills_to_give()
                # if fills_to_give == 0:
                #     fills_to_give = 1
                message += f"\nKolejne {current_prescription.fills_to_give} wkłady/ów, (czyli {current_prescription.fills_to_give / current_prescription.number_of_fills_in_box} op.), może być wydane\nnajwcześniej po {next_buy_date} <<<<"
                current_prescription.set_days_of_therapy_3_4()
                next_buy_date = (datetime.datetime.strptime(next_buy_date, '%d.%m.%Y') + datetime.timedelta(
                    days=current_prescription.days_of_therapy_3_4)).strftime(
                    '%d.%m.%Y')
                current_prescription.set_number_of_fills_left(current_prescription.number_of_fills_left - current_prescription.fills_to_give)

    result_text.configure(state=tkinter.NORMAL, bg=BACKGROUND_COLOR3)
    result_text.delete("1.0", tkinter.END)
    result_text.insert("1.0", message)
    result_text.configure(state=tkinter.DISABLED)
    return


def calculate_pills_yearly(current_prescription):
    number_of_doses_in_box = float(dose_entry.get().replace(',', '.'))
    the_smallest_box = get_smallest_box(number_of_doses_in_box)
    if the_smallest_box:
        calculate_pills_yearly_with_smallest_box()
    else:
        calculate_pills_yearly_without_smallest_box()
    return
# TODO ==================================\/=========================

def calculate_pills_yearly_without_smallest_box(current_prescription):
    message = ""
    issue_day = int(day_entry.get().replace(',', '.'))
    issue_month = int(month_entry.get().replace(',', '.'))
    issue_year = int(year_entry.get().replace(',', '.'))
    initial_number_of_boxes = float(boxes_entry.get().replace(',', '.'))
    number_of_doses_in_box = float(dose_entry.get().replace(',', '.'))
    doses_taken_daily = float(usage_entry.get().replace(',', '.'))

    issue_date = datetime.datetime(year=issue_year, month=issue_month, day=issue_day)
    doses_lost = 0
    initial_number_of_doses = initial_number_of_boxes * number_of_doses_in_box
    number_of_doses_left = initial_number_of_doses
    days_passed_since_issue = (datetime.datetime.now() - issue_date).days

    maximum_doses_to_give_once = doses_taken_daily * 120
    maximum_doses_overall = doses_taken_daily * 360

    if number_of_doses_left > maximum_doses_overall:
        number_of_doses_left = maximum_doses_overall
        message += f"Maksymalnie można wydać łącznie {int(maximum_doses_overall)} szt. (tj. {int(maximum_doses_overall // number_of_doses_in_box)} op.)\n"

    if days_passed_since_issue > 30:
        doses_lost = int(
            ((days_passed_since_issue * doses_taken_daily) // number_of_doses_in_box) * number_of_doses_in_box)
        boxes_lost = doses_lost // number_of_doses_in_box
        if boxes_lost == 0:
            boxes_lost = 1
            doses_lost = number_of_doses_in_box
        message += f"Przepadło {int(boxes_lost)} op.\n"
        number_of_doses_left -= doses_lost

    previous_buys_calculations = check_previous_buys(issue_date, maximum_doses_to_give_once, number_of_doses_left,
                                                     doses_taken_daily)
    if previous_buys_calculations:
        # issue_date = previous_buys_calculations[0]
        number_of_doses_left = previous_buys_calculations[1]
        if previous_buys_calculations[2]:
            message += previous_buys_calculations[2]
    else:
        return

    if maximum_doses_to_give_once >= number_of_doses_left:
        if (doses_lost or previous_buys_present) and number_of_doses_left > 0:
            message += f"Można wydać pozostałe {int(number_of_doses_left // number_of_doses_in_box)} op."
        elif number_of_doses_left <= 0:
            message = "Przepadło wszystko."
        else:
            message = "Można wydać wszystkie op."
    else:
        doses_to_give = (maximum_doses_to_give_once // number_of_doses_in_box) * number_of_doses_in_box
        if doses_to_give == 0:
            doses_to_give = number_of_doses_in_box
        if previous_buys_calculations and previous_buys_calculations[3]:
            doses_to_give -= previous_buys_calculations[3]
            days_of_therapy_3_4 = math.ceil(
                ((doses_to_give + previous_buys_calculations[3]) / doses_taken_daily) * 3 / 4)
            next_buy_date = (previous_buys_calculations[0] + datetime.timedelta(days=days_of_therapy_3_4)).strftime(
                '%d.%m.%Y')
        else:
            days_of_therapy_3_4 = math.ceil((doses_to_give / doses_taken_daily) * 3 / 4)
            next_buy_date = (datetime.datetime.now() + datetime.timedelta(days=days_of_therapy_3_4)).strftime(
                '%d.%m.%Y')
        message += f"Dziś można wydać {int(doses_to_give // number_of_doses_in_box)} op."
        number_of_doses_left -= doses_to_give

        while number_of_doses_left > 0:
            if number_of_doses_left < number_of_doses_in_box:
                message += f"\nPozostanie {int(number_of_doses_left)} szt. Jeśli tak się da, może to być wydane najwcześniej po {next_buy_date} <<<<"
                break
            elif number_of_doses_left == number_of_doses_in_box:
                message += f"\nKolejne 1 op. może być wydane najwcześniej po {next_buy_date} <<<<"
                break
            else:
                if maximum_doses_to_give_once >= number_of_doses_left:
                    doses_to_give = int(
                        (number_of_doses_left // number_of_doses_in_box) * number_of_doses_in_box)  # always > 0
                    message += f"\nKolejne {int(doses_to_give // number_of_doses_in_box)} op. może być wydane najwcześniej po {next_buy_date} <<<<"
                    days_of_therapy_3_4 = math.ceil((doses_to_give / doses_taken_daily) * 3 / 4)
                    next_buy_date = (datetime.datetime.strptime(next_buy_date, '%d.%m.%Y') + datetime.timedelta(
                        days=days_of_therapy_3_4)).strftime(
                        '%d.%m.%Y')
                    number_of_doses_left -= doses_to_give
                else:
                    doses_to_give = int((maximum_doses_to_give_once // number_of_doses_in_box) * number_of_doses_in_box)
                    message += f"\nKolejne {int(doses_to_give // number_of_doses_in_box)} op. może być wydane najwcześniej po {next_buy_date} <<<<"
                    days_of_therapy_3_4 = math.ceil((doses_to_give / doses_taken_daily) * 3 / 4)
                    next_buy_date = (datetime.datetime.strptime(next_buy_date, '%d.%m.%Y') + datetime.timedelta(
                        days=days_of_therapy_3_4)).strftime(
                        '%d.%m.%Y')
                    number_of_doses_left -= doses_to_give

    result_text.configure(state=tkinter.NORMAL, bg=BACKGROUND_COLOR3)
    result_text.delete("1.0", tkinter.END)
    result_text.insert("1.0", message)
    result_text.configure(state=tkinter.DISABLED)
    return


def calculate_pills_yearly_with_smallest_box(current_prescription):
    message = ""
    issue_day = int(day_entry.get().replace(',', '.'))
    issue_month = int(month_entry.get().replace(',', '.'))
    issue_year = int(year_entry.get().replace(',', '.'))
    initial_number_of_boxes = float(boxes_entry.get().replace(',', '.'))
    number_of_doses_in_box = float(dose_entry.get().replace(',', '.'))
    doses_taken_daily = float(usage_entry.get().replace(',', '.'))
    doses_in_smallest_box = get_smallest_box(number_of_doses_in_box)

    issue_date = datetime.datetime(year=issue_year, month=issue_month, day=issue_day)
    doses_lost = 0
    initial_number_of_doses = initial_number_of_boxes * number_of_doses_in_box
    number_of_doses_left = initial_number_of_doses
    days_passed_since_issue = (datetime.datetime.now() - issue_date).days

    maximum_doses_to_give_once = doses_taken_daily * 120
    maximum_doses_overall = doses_taken_daily * 360
    if number_of_doses_left > maximum_doses_overall:
        number_of_doses_left = maximum_doses_overall
        boxes_left = int(number_of_doses_left // number_of_doses_in_box)
        smallest_boxes_left = int(
            (number_of_doses_left - (boxes_left * number_of_doses_in_box)) // doses_in_smallest_box)
        message += f"Maksymalnie można wydać łącznie {int(maximum_doses_overall)} szt. (tj. {int(maximum_doses_overall // number_of_doses_in_box)} op.)"
        if smallest_boxes_left:
            message += f" oraz {smallest_boxes_left} op. x {doses_in_smallest_box} szt.\n"
        else:
            message += "\n"
    if days_passed_since_issue > 30:
        initial_doses_lost = int(days_passed_since_issue * doses_taken_daily)
        doses_lost_from_boxes = int((initial_doses_lost // number_of_doses_in_box) * number_of_doses_in_box)
        doses_lost_from_smallest_boxes = int(
            ((initial_doses_lost - doses_lost_from_boxes) // doses_in_smallest_box) * doses_in_smallest_box)
        doses_lost = doses_lost_from_boxes + doses_lost_from_smallest_boxes
        boxes_lost = doses_lost_from_boxes // number_of_doses_in_box
        smallest_boxes_lost = doses_lost_from_smallest_boxes // doses_in_smallest_box
        if boxes_lost == 0 and smallest_boxes_lost == 0:
            smallest_boxes_lost = 1
            doses_lost = doses_in_smallest_box
        if boxes_lost > 0:
            message += f"Przepadło {int(boxes_lost)} op. x {number_of_doses_in_box} szt."
            if smallest_boxes_lost > 0:
                message += f" oraz {int(smallest_boxes_lost)} op. x {doses_in_smallest_box} szt.\n"
            else:
                message += "\n"
        elif smallest_boxes_lost > 0:
            message += f"Przepadło {int(smallest_boxes_lost)} op. x {doses_in_smallest_box} szt.\n"
        number_of_doses_left -= doses_lost

    previous_buys_calculations = check_previous_buys(issue_date, maximum_doses_to_give_once, number_of_doses_left,
                                                     doses_taken_daily)
    if previous_buys_calculations:
        # issue_date = previous_buys_calculations[0]
        number_of_doses_left = previous_buys_calculations[1]
        if previous_buys_calculations[2]:
            message += previous_buys_calculations[2]
    else:
        return

    if maximum_doses_to_give_once >= number_of_doses_left:
        if doses_lost and number_of_doses_left > 0:
            boxes_to_give = (number_of_doses_left // number_of_doses_in_box)
            smallest_boxes_to_give = (number_of_doses_left - (
                    boxes_to_give * number_of_doses_in_box)) // doses_in_smallest_box
            if boxes_to_give > 0:
                message += f"Można wydać pozostałe {int(number_of_doses_left // number_of_doses_in_box)} op. x {number_of_doses_in_box} szt."
                if smallest_boxes_to_give > 0:
                    message += f" oraz {int(smallest_boxes_to_give)} op. x {doses_in_smallest_box} szt.\n"
                else:
                    message += "\n"
            elif smallest_boxes_to_give > 0:
                message += f"Można wydać pozostałe {int(smallest_boxes_to_give)} op. x {doses_in_smallest_box} szt.\n"
        elif number_of_doses_left <= 0:
            message = "Przepadło wszystko."
        else:
            message = "Można wydać wszystkie op."
    else:
        if previous_buys_calculations and previous_buys_calculations[3]:
            doses_left_after_previous_buys = maximum_doses_to_give_once - previous_buys_calculations[3]
            doses_to_give_from_boxes = int(
                (doses_left_after_previous_buys // number_of_doses_in_box) * number_of_doses_in_box)
            doses_to_give_from_smallest_boxes = int(((
                                                                 doses_left_after_previous_buys - doses_to_give_from_boxes) // doses_in_smallest_box) * doses_in_smallest_box)
            doses_to_give = doses_to_give_from_boxes + doses_to_give_from_smallest_boxes
            days_of_therapy_3_4 = math.ceil((doses_to_give + previous_buys_calculations[3] / doses_taken_daily) * 3 / 4)
            next_buy_date = (previous_buys_calculations[0] + datetime.timedelta(days=days_of_therapy_3_4)).strftime(
                '%d.%m.%Y')
        else:
            doses_to_give_from_boxes = int(
                (maximum_doses_to_give_once // number_of_doses_in_box) * number_of_doses_in_box)
            doses_to_give_from_smallest_boxes = int(((
                                                                 maximum_doses_to_give_once - doses_to_give_from_boxes) // doses_in_smallest_box) * doses_in_smallest_box)
            doses_to_give = doses_to_give_from_boxes + doses_to_give_from_smallest_boxes
            days_of_therapy_3_4 = math.ceil((doses_to_give / doses_taken_daily) * 3 / 4)
            next_buy_date = (datetime.datetime.now() + datetime.timedelta(days=days_of_therapy_3_4)).strftime(
                '%d.%m.%Y')
        boxes_to_give = doses_to_give_from_boxes // number_of_doses_in_box
        smallest_boxes_to_give = doses_to_give_from_smallest_boxes // doses_in_smallest_box
        if boxes_to_give > 0:
            message += f"Dziś można wydać {int(boxes_to_give)} op. x {number_of_doses_in_box} szt."
            if smallest_boxes_to_give > 0:
                message += f" oraz {int(smallest_boxes_to_give)} op. x {doses_in_smallest_box} szt.\n"
            else:
                message += "\n"
        elif smallest_boxes_to_give > 0:
            message += f"Dziś można wydać {int(smallest_boxes_to_give)} op. x {doses_in_smallest_box} szt.\n"
        number_of_doses_left -= doses_to_give

        while number_of_doses_left > 0:
            if number_of_doses_left < doses_in_smallest_box:
                message += f"Pozostanie {int(number_of_doses_left)} szt. które muszą przepaść."
                break
            elif number_of_doses_left == doses_in_smallest_box:
                message += f"\nKolejne 1 op. x {doses_in_smallest_box} szt. może być wydane najwcześniej po {next_buy_date} <<<<"
                break
            else:
                if number_of_doses_left <= maximum_doses_to_give_once:
                    doses_to_give_from_boxes = int(
                        (number_of_doses_left // number_of_doses_in_box) * number_of_doses_in_box)
                    doses_to_give_from_smallest_boxes = int(((
                                                                     number_of_doses_left - doses_to_give_from_boxes) // doses_in_smallest_box) * doses_in_smallest_box)
                    doses_to_give = doses_to_give_from_boxes + doses_to_give_from_smallest_boxes
                    boxes_to_give = doses_to_give_from_boxes // number_of_doses_in_box
                    smallest_boxes_to_give = doses_to_give_from_smallest_boxes // doses_in_smallest_box
                    if boxes_to_give > 0:
                        message += f"Kolejne {int(boxes_to_give)} op. x {number_of_doses_in_box} szt."
                        if smallest_boxes_to_give > 0:
                            message += f" oraz {int(smallest_boxes_to_give)} op. x {doses_in_smallest_box} szt. może być wydane\nnajwcześniej po {next_buy_date} <<<<\n"
                        else:
                            message += f" może być wydane najwcześniej po {next_buy_date} <<<<\n"
                    elif smallest_boxes_to_give > 0:
                        message += f"Kolejne {int(smallest_boxes_to_give)} op. x {doses_in_smallest_box} szt. może być wydane najwcześniej po {next_buy_date} <<<<\n"
                    days_of_therapy_3_4 = math.ceil((doses_to_give / doses_taken_daily) * 3 / 4)
                    next_buy_date = (datetime.datetime.strptime(next_buy_date, '%d.%m.%Y') + datetime.timedelta(
                        days=days_of_therapy_3_4)).strftime(
                        '%d.%m.%Y')
                    number_of_doses_left -= doses_to_give
                else:
                    doses_to_give_from_boxes = int(
                        (maximum_doses_to_give_once // number_of_doses_in_box) * number_of_doses_in_box)
                    doses_to_give_from_smallest_boxes = int(
                        ((
                                 maximum_doses_to_give_once - doses_to_give_from_boxes) // doses_in_smallest_box) * doses_in_smallest_box)
                    doses_to_give = doses_to_give_from_boxes + doses_to_give_from_smallest_boxes
                    boxes_to_give = doses_to_give_from_boxes // number_of_doses_in_box
                    smallest_boxes_to_give = doses_to_give_from_smallest_boxes // doses_in_smallest_box
                    if boxes_to_give > 0:
                        message += f"Kolejne {int(boxes_to_give)} op. x {number_of_doses_in_box} szt."
                        if smallest_boxes_to_give > 0:
                            message += f" oraz {int(smallest_boxes_to_give)} op. x {doses_in_smallest_box} szt. może być wydane\nnajwcześniej po {next_buy_date} <<<<\n"
                        else:
                            message += f" może być wydane najwcześniej po {next_buy_date} <<<<\n"
                    elif smallest_boxes_to_give > 0:
                        message += f"Kolejne {int(smallest_boxes_to_give)} op. x {doses_in_smallest_box} szt. może być wydane najwcześniej po {next_buy_date} <<<<\n"
                    days_of_therapy_3_4 = math.ceil((doses_to_give / doses_taken_daily) * 3 / 4)
                    next_buy_date = (datetime.datetime.strptime(next_buy_date, '%d.%m.%Y') + datetime.timedelta(
                        days=days_of_therapy_3_4)).strftime(
                        '%d.%m.%Y')
                    number_of_doses_left -= doses_to_give

    result_text.configure(state=tkinter.NORMAL, bg=BACKGROUND_COLOR3)
    result_text.delete("1.0", tkinter.END)
    result_text.insert("1.0", message)
    result_text.configure(state=tkinter.DISABLED)
    return


def calculate_insulin_monthly(current_prescription):
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
        message = f"Można wydać {fills_to_give} wkładów,\nczyli {fills_to_give / number_of_fills_in_box}op.\nReszta przepada!"

    result_text.configure(state=tkinter.NORMAL, bg=BACKGROUND_COLOR3)
    result_text.delete("1.0", tkinter.END)
    result_text.insert("1.0", message)
    result_text.configure(state=tkinter.DISABLED)


def calculate_pills_monthly(current_prescription):
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
    # print(type(boxes_to_give))
    if boxes_to_give >= number_of_boxes:
        message = f"Można wydać wszystkie op."
    else:
        message = f"Można wydać {boxes_to_give} op.\nReszta przepada!"
    result_text.configure(state=tkinter.NORMAL, bg=BACKGROUND_COLOR3)
    result_text.delete("1.0", tkinter.END)
    result_text.insert("1.0", message)
    result_text.configure(state=tkinter.DISABLED)


def check_previous_buys(issue_date, maximum_doses_to_give_once, number_of_doses_left, doses_taken_daily,
                        current_prescription):
    if previous_buys_present and previous_buys_list:
        previously_bought_amount = 0
        previously_bought_portion = 0
        first_buy_date = previous_buys_list[0]["date"]
        for index, buy in enumerate(previous_buys_list):
            if buy["date"] < issue_date:
                result_text.configure(state=tkinter.NORMAL)
                result_text.delete("1.0", tkinter.END)
                result_text.insert("1.0", "PODANO BŁĘDNĄ DATĘ\nPOPRZEDNIEGO WYKUPIENIA")
                result_text.configure(state=tkinter.DISABLED, bg="red")
                return 0
            previously_bought_amount += buy["amount"]
            previously_bought_portion += buy["amount"]
            if buy["amount"] > maximum_doses_to_give_once or previously_bought_amount > number_of_doses_left:
                result_text.configure(state=tkinter.NORMAL)
                result_text.delete("1.0", tkinter.END)
                result_text.insert("1.0", "WYDANO ZA DUŻO ! !\nKONIECZNA KOREKTA ! !")
                result_text.configure(state=tkinter.DISABLED, bg="red")
                return 0
            if previously_bought_portion > maximum_doses_to_give_once:
                if (buy["date"] - first_buy_date).days < math.ceil(
                        maximum_doses_to_give_once / doses_taken_daily * 3 / 4):
                    result_text.configure(state=tkinter.NORMAL)
                    result_text.delete("1.0", tkinter.END)
                    result_text.insert("1.0", "WYDANO ZA DUŻO ! !\nKONIECZNA KOREKTA ! !")
                    result_text.configure(state=tkinter.DISABLED, bg="red")
                    return 0
                else:
                    first_buy_date = buy["date"]
                    previously_bought_portion = 0

        issue_date = previous_buys_list[-1]["date"]
        # print(issue_date)
        number_of_doses_left -= previously_bought_amount
        message = f"Wcześniej wykupiono {previously_bought_amount} szt.\nPozostało więc {number_of_doses_left} szt.\n"
        result = (issue_date, number_of_doses_left, message, previously_bought_portion)
        return result
    else:
        result = (issue_date, number_of_doses_left, 0, 0)
        return result


def choose_calculate_yearly(current_prescription):
    if insulin_switch:
        calculate_insulin_yearly()
    else:
        calculate_pills_yearly()


def choose_calculate_monthly(current_prescription):
    if insulin_switch:
        calculate_insulin_monthly()
    else:
        calculate_pills_monthly()


def check_data_completion(current_prescription):
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


def check_date_correctness(current_prescription):
    try:
        issue_day = int(day_entry.get().replace(',', '.'))
        issue_month = int(month_entry.get().replace(',', '.'))
        issue_year = int(year_entry.get().replace(',', '.'))
        if issue_day < 1 or issue_day > 31 or issue_month < 1 or issue_month > 12 or issue_year < 2023:
            # TODO add every month correctness check like in add_previous_buy()
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


def show_wrong_previous_date():
    date_bought_label.config(text="PODANO BŁĘDNE DANE", bg="red")
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


def show_smallest_box_entry():
    if smallest_box.get():
        smallest_box_entry.grid()
        smallest_box_label.grid()
    else:
        smallest_box_entry.grid_remove()
        smallest_box_label.grid_remove()


def add_previous_buy(current_prescription):
    try:
        day = int(buyday_entry.get())
        month = int(buymonth_entry.get())
        year = int(buyyear_entry.get())
        amount = int(amount_bought_entry.get())
        if not 0 < day < 32:
            show_wrong_previous_date()
            return
        if not 0 < month < 13:
            show_wrong_previous_date()
            return
        if year < datetime.datetime.now().year - 1 or year > datetime.datetime.now().year:
            show_wrong_previous_date()
            return
        if amount < 0:
            show_wrong_previous_date()
            return
        if month in [4, 6, 9, 11] and day > 30:
            show_wrong_previous_date()
            return
        if month == 2 and day > 29:
            show_wrong_previous_date()
            return
        # TODO add leap year
    except ValueError:
        show_wrong_previous_date()
        return
    else:
        global previous_buys_list
        previous_buys_list.append({
            "date": datetime.datetime(day=day, month=month, year=year),
            "amount": amount,
        })
        previous_buys_list = sorted(previous_buys_list, key=lambda x: x["date"])
        # print(previous_buys_list)
        # print(len(previous_buys_list))
        # print(previous_buys_list[0]["date"])
        date_bought_label.config(text="Podaj datę wykupienia:", bg=BACKGROUND_COLOR2)
        result_text.configure(state=tkinter.NORMAL, bg=BACKGROUND_COLOR)
        result_text.delete("1.0", tkinter.END)
        result_text.configure(state=tkinter.DISABLED)
        buys = ""
        for buy in previous_buys_list:
            buys += f'{buy["date"].strftime("%d.%m.%Y")} zostało wykupione {buy["amount"]} szt.\n'
        previous_buys_label.config(text=buys, font=FONT)


result_text = tkinter.Text(background=BACKGROUND_COLOR, fg="#280274", font=FONT, width=65, height=7)
result_text.configure(state=tkinter.DISABLED)
result_text.grid(row=0, column=0)

prescription_type_frame = tkinter.Frame(bg=BACKGROUND_COLOR)
prescription_type_frame.grid(row=0, column=1)
prescription_type = tkinter.IntVar()

yearly = tkinter.Radiobutton(prescription_type_frame, text="Rp roczna", variable=prescription_type, value=1,
                             bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, font=FONT2)
yearly.grid(row=0, column=0, sticky="nw")
monthly = tkinter.Radiobutton(prescription_type_frame, text="Rp miesięczna", variable=prescription_type, value=0,
                              bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, font=FONT2)
monthly.grid(row=1, column=0, sticky="nw")
smallest_box = tkinter.BooleanVar()
smallest_box_button = tkinter.Checkbutton(prescription_type_frame, text="(Naj)mniejsze\nrefundowane\nopakowanie?",
                                          variable=smallest_box, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR,
                                          font=FONT2, command=show_smallest_box_entry)
smallest_box_button.grid(row=2, column=0, sticky="nw")

# right_canvas = tkinter.Canvas(background=BACKGROUND_COLOR, width=20, height=600, highlightthickness=0)
# right_canvas.grid(row=0, column=3, rowspan=20)
# bottom_canvas = tkinter.Canvas(background=BACKGROUND_COLOR, width=200, height=10, highlightthickness=0)
# bottom_canvas.grid(row=20, column=0, columnspan=4)

boxes_label = tkinter.Label(text="Podaj ilość zapisanych opakowań:", background=BACKGROUND_COLOR2, font=FONT)
boxes_label.grid(row=1, column=0, sticky="e")
boxes_entry = tkinter.Entry(width=10, font=FONT)
boxes_entry.grid(row=1, column=1)

insulin_label = tkinter.Label(text="Podaj ilość wkładów w opakowaniu:", background=BACKGROUND_COLOR2, font=FONT)
insulin_label.grid(row=2, column=0, sticky="e")
insulin_label.grid_remove()
insulin_entry = tkinter.Entry(width=10, font=FONT)
insulin_entry.grid(row=2, column=1)
insulin_entry.grid_remove()

dose_label = tkinter.Label(text="Podaj ilość sztuk w opakowaniu:", background=BACKGROUND_COLOR2, font=FONT)
dose_label.grid(row=3, column=0, sticky="e")
dose_entry = tkinter.Entry(width=10, font=FONT)
dose_entry.grid(row=3, column=1)

usage_label = tkinter.Label(text="Podaj liczbę sztuk, jaką pacjent stosuje na dzień:", background=BACKGROUND_COLOR2,
                            font=FONT)
usage_label.grid(row=4, column=0, sticky="e")
usage_entry = tkinter.Entry(width=10, font=FONT)
usage_entry.grid(row=4, column=1)

date_issued_label = tkinter.Label(text="Podaj datę wystawienia:", bg=BACKGROUND_COLOR2, font=FONT)
date_issued_label.grid(row=5, column=0, sticky="e")
day_label = tkinter.Label(text="dzień:", bg=BACKGROUND_COLOR2, font=FONT)
day_label.grid(row=6, column=0, sticky="e")
day_entry = tkinter.Entry(width=10, font=FONT)
day_entry.grid(row=6, column=1)
day_entry.insert(0, str(datetime.datetime.now().day))
month_label = tkinter.Label(text="miesiąc:", bg=BACKGROUND_COLOR2, font=FONT)
month_label.grid(row=7, column=0, sticky="e")
month_entry = tkinter.Entry(width=10, font=FONT)
month_entry.grid(row=7, column=1)
month_entry.insert(0, str(datetime.datetime.now().month))
year_label = tkinter.Label(text="rok:", bg=BACKGROUND_COLOR2, font=FONT)
year_label.grid(row=8, column=0, sticky="e")
year_entry = tkinter.Entry(width=10, font=FONT)
year_entry.grid(row=8, column=1)
year_entry.insert(0, str(datetime.datetime.now().year))

smallest_box_label = tkinter.Label(text="Jakie jest najmniejsze refundowane opakowanie:", background=BACKGROUND_COLOR2,
                                   font=FONT)
smallest_box_label.grid(row=9, column=0, sticky="e")
smallest_box_label.grid_remove()
smallest_box_entry = tkinter.Entry(width=10, font=FONT)
smallest_box_entry.grid(row=9, column=1)
smallest_box_entry.grid_remove()

calculate_button = tkinter.Button(text="PRZELICZ", height=4, background="#294B29", font=FONT, command=calculate_results,
                                  activebackground="#294B29")
calculate_button.grid(row=6, column=2, rowspan=3, sticky="w")

exit_button = tkinter.Button(text="WYJDŹ", command=window.destroy, width=8, height=4, fg="red", background="#F3CCF3",
                             font=FONT, activebackground="#F3CCF3")
exit_button.grid(row=0, column=2, sticky="w")

insulin_button = tkinter.Button(text="INSULINA", command=lambda: insulin(the_current_prescription), background=BACKGROUND_COLOR2, font=FONT2,
                                activebackground=BACKGROUND_COLOR2)
insulin_button.grid(row=4, column=2, sticky="w")

pills_button = tkinter.Button(text="TABLETKI ITP.", command=lambda: pills(the_current_prescription), background=BACKGROUND_COLOR2, font=FONT2,
                              activebackground=BACKGROUND_COLOR2)
pills_button.grid(row=3, column=2, sticky="w")

previous_buy_button = tkinter.Button(text="Wcześniejsze\nrealizacje", command=lambda: previous_buys(the_current_prescription),
                                     background=BACKGROUND_COLOR2, font=FONT2, activebackground=BACKGROUND_COLOR2)
previous_buy_button.grid(row=9, column=2, sticky="w")

line_canvas = tkinter.Canvas(background="#6C22A6", width=880, height=10, highlightthickness=0)
line_canvas.grid(row=10, column=0, columnspan=3)

date_bought_label = tkinter.Label(text="Podaj datę wykupienia:", bg=BACKGROUND_COLOR2, font=FONT)
date_bought_label.grid(row=11, column=0, sticky="e")
date_bought_label.grid_remove()
buyday_label = tkinter.Label(text="dzień:", bg=BACKGROUND_COLOR2, font=FONT)
buyday_label.grid(row=12, column=0, sticky="e")
buyday_label.grid_remove()
buyday_entry = tkinter.Entry(width=10, font=FONT)
buyday_entry.grid(row=12, column=1)
buyday_entry.grid_remove()
buymonth_label = tkinter.Label(text="miesiąc:", bg=BACKGROUND_COLOR2, font=FONT)
buymonth_label.grid(row=13, column=0, sticky="e")
buymonth_label.grid_remove()
buymonth_entry = tkinter.Entry(width=10, font=FONT)
buymonth_entry.grid(row=13, column=1)
buymonth_entry.grid_remove()
buyyear_label = tkinter.Label(text="rok:", bg=BACKGROUND_COLOR2, font=FONT)
buyyear_label.grid(row=14, column=0, sticky="e")
buyyear_label.grid_remove()
buyyear_entry = tkinter.Entry(width=10, font=FONT)
buyyear_entry.grid(row=14, column=1)
buyyear_entry.grid_remove()

amount_bought_label = tkinter.Label(text="Podaj liczbę sztuk, jaka została wtedy wykupiona:",
                                    background=BACKGROUND_COLOR2, font=FONT)
amount_bought_label.grid(row=15, column=0, sticky="e")
amount_bought_label.grid_remove()
amount_bought_entry = tkinter.Entry(width=10, font=FONT)
amount_bought_entry.grid(row=15, column=1)
amount_bought_entry.grid_remove()

bought_button = tkinter.Button(text="Dodaj\nrealizację", command=lambda: add_previous_buy(the_current_prescription),
                               background=BACKGROUND_COLOR2,
                               font=FONT2, activebackground=BACKGROUND_COLOR2)
bought_button.grid(row=13, column=2, rowspan=2, sticky="w")
bought_button.grid_remove()

previous_buys_frame = tkinter.Frame(bg=BACKGROUND_COLOR)
previous_buys_frame.grid(row=16, column=0, sticky="nw")
previous_buys_label = tkinter.Label(previous_buys_frame, text="", font=FONT2, bg=BACKGROUND_COLOR,
                                    activebackground=BACKGROUND_COLOR2)
previous_buys_label.grid(row=0, column=0)

window.mainloop()
