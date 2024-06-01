import datetime
import math


class Prescription:
    def __init__(self):
        self.issue_date = datetime.datetime.now()
        self.initial_number_of_doses = None
        self.initial_number_of_boxes = None
        self.initial_number_of_fills = None
        self.number_of_doses_in_box = None
        self.number_of_fills_in_box = None
        self.number_of_units_in_fill = None
        self.units_taken_daily = None
        self.doses_lost = 0
        self.fills_lost = 0
        self.number_of_doses_left = None
        self.number_of_fills_left = None
        self.days_passed_since_issue = None
        self.number_of_doses_in_box = None
        self.doses_taken_daily = None
        self.doses_in_smallest_box = None
        self.smallest_box_present = False
        self.yearly = False
        self.maximum_doses_to_give_once = None
        self.maximum_doses_overall = None
        self.maximum_units_to_give_once = None
        self.maximum_units_overall = None
        self.maximum_fills_to_give_once = None
        self.maximum_fills_overall = None
        self.restarting_period = None
        self.counting_date = None
        self.insulin_switch = False
        self.previous_buys_present = False
        self.previous_buys_list = []
        self.units_to_give = None
        self.fills_to_give = None
        self.days_of_therapy_3_4 = None

    def set_issue_date(self, d, m, y):
        self.issue_date = datetime.datetime(year=y, month=m, day=d)
        self.days_passed_since_issue = (datetime.datetime.now() - self.issue_date).days

    def set_number_of_doses_in_box(self, n):
        self.number_of_doses_in_box = n

    def set_initial_number_of_boxes(self, n):
        self.initial_number_of_boxes = n

    def set_initial_number_of_doses(self):
        self.initial_number_of_doses = self.number_of_doses_in_box * self.initial_number_of_boxes

    def set_doses_lost(self, n):
        self.doses_lost += n

    def set_number_of_doses_left(self, n):
        if n:
            self.number_of_doses_left = n
        else:
            self.number_of_doses_left = self.initial_number_of_doses
            if self.number_of_doses_left > self.maximum_doses_overall:
                self.number_of_doses_left = self.maximum_doses_overall

    def set_maximum_doses_to_give_once(self):
        self.maximum_doses_to_give_once = self.doses_taken_daily * 120

    def set_maximum_doses_overall(self):
        self.maximum_doses_overall = self.doses_taken_daily * 360

    def set_yearly(self):
        self.yearly = True

    def check_restarting_period(self, date):
        if not date:
            self.counting_date = datetime.datetime.now()
        if (datetime.datetime.now() - self.counting_date).days > self.maximum_doses_to_give_once:
            self.counting_date = date

    def set_number_of_fills_in_box(self, n):
        self.number_of_fills_in_box = n

    def set_number_of_units_in_fill(self, n):
        self.number_of_units_in_fill = n

    def set_units_taken_daily(self, n):
        self.units_taken_daily = n

    def set_initial_number_of_fills(self):
        self.initial_number_of_fills = self.initial_number_of_boxes * self.number_of_fills_in_box

    def set_number_of_fills_left(self, n):
        if n:
            self.number_of_fills_left = n
        else:
            self.number_of_fills_left = self.initial_number_of_fills

    def set_maximum_units_to_give_once(self):
        self.maximum_units_to_give_once = self.units_taken_daily * 120

    def set_maximum_units_overall(self):
        self.maximum_units_overall = self.units_taken_daily * 360

    def set_maximum_fills_to_give_once(self):
        self.maximum_fills_to_give_once = self.maximum_units_to_give_once // self.number_of_units_in_fill

    def set_maximum_fills_overall(self):
        self.maximum_fills_overall = int(self.maximum_units_overall // self.number_of_units_in_fill)

    def set_fills_lost(self):
        self.fills_lost = int((self.days_passed_since_issue * self.units_taken_daily) // self.number_of_units_in_fill)

    def set_units_to_give(self):
        self.units_to_give = (self.maximum_units_to_give_once // self.number_of_units_in_fill) * self.number_of_units_in_fill

    def set_fills_to_give(self):
        self.fills_to_give = int(self.units_to_give // self.number_of_units_in_fill)

    def set_days_of_therapy_3_4(self):
        self.days_of_therapy_3_4 = math.ceil((self.fills_to_give * self.number_of_units_in_fill / self.units_taken_daily) * 3 / 4)