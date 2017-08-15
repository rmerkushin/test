class Calendar:

    def __init__(self, year, month, day):
        self._year = year
        self._month = month
        self._day = day

    @property
    def get_year(self):
        return self._year

    @property
    def get_month(self):
        return self._month

    @property
    def get_day(self):
        return self._day
