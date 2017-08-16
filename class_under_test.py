class Calendar:

    def __init__(self, year: int, month: int, day: int) -> None:
        self._year = year
        self._month = month
        self._day = day

    @property
    def year(self) -> int:
        return self._year

    @property
    def month(self) -> int:
        return self._month

    @property
    def day(self) -> int:
        return self._day


# Пример некорректного использования Calendar
calendar = Calendar('2017', '06', '11')
