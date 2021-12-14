# Create a class CALENDAR. Define methods for creating and working with a CALENDAR instances and overload operations^
# "+=, -=" - for adding and subtracting days, months, years to a given date
# "==, ! =, >, >=, <, <=" - for comparing dates.

class Calendar:
    def __init__(self, days, months, years):
        self.days = days
        self.months = months
        self.years = years

    def get_days(self):
        return self.days

    def set_days(self, days):
        self.days = days

    def get_months(self):
        return self.months

    def set_months(self, months):
        self.months = months

    def get_years(self):
        return self.years

    def set_years(self, years):
        self.years = years

    def checkLeap(Year):
        return (Year % 400 == 0) or (Year % 100 != 0) and (Year % 4 == 0)

    def amountOfDays(self):
        if self.months in {1, 3, 5, 7, 8, 10, 12}:
            return 31
        elif self.months == 2:
            if self.checkLeap():
                return 29
            else:
                return 28
        else:
            return 30

    def __iadd__(self, other):
        self.days += other.days
        self.months += other.months
        self.years += other.years
        if self.months > 12:
            self.months = self.months - 12
            self.years += 1
        if self.days > self.amountOfDays():
            self.days -= self.amountOfDays()
            self.months += 1
        if self.months > 12:
            self.months = self.months - 12
            self.years += 1
        return self

    def __isub__(self, other):
        self.days -= other.days
        self.months -= other.months
        self.years -= other.years
        if self.months < 1:
            self.months += 12
            self.years -= 1
        if self.days < 1:
            self.months -= 1
            if self.months == 0:
                self.months = 12
            self.days += self.amountOfDays()
        if self.months < 1:
            self.months += 12
            self.years -= 1
        return self

    def __eq__(self, other):
        if self.days == other.days and self.months == other.months and self.years == other.years:
            return True
        return False

    def __ne__(self, other):
        return not (self == other)

    def __gt__(self, other):
        if self.years > other.years:
            return True
        elif self.years < other.years:
            return False
        elif self.months > other.months:
            return True
        elif self.months < other.months:
            return False
        elif self.days > other.days:
            return True
        return False

    def __ge__(self, other):
        if self.years > other.years:
            return True
        elif self.years < other.years:
            return False
        elif self.months > other.months:
            return True
        elif self.months < other.months:
            return False
        elif self.days >= other.days:
            return True
        return False

    def __le__(self, other):
        return not (self > other)

    def __lt__(self, other):
        return not (self >= other)

    def print(self):
        print(str("Days: " + str(self.days) + " Months: " + str(self.months) + " Years: " + str(self.years)))


cal1 = Calendar(11, 10, 2003)
cal2 = Calendar(11, 11, 2021)
cal3 = Calendar(11, 3, 1987)
cal1 += cal3
cal1.print()
cal1 -= cal2
cal1.print()
print(cal1 != cal2)
print(cal1 > cal2)
print(cal1 >= cal2)
print(cal1 < cal2)
print(cal1 <= cal2)
