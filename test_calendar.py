import pytest
import datetime

from class_under_test import Calendar

td_positive = [
    (Calendar(2000, 2, 29)),  # 29 февраля в високосном году
    (Calendar(2001, 2, 28)),  # 28 февраля в не високосном году
    (Calendar(2017, 1, 31)),  # 31 дней в месяце
    (Calendar(2017, 4, 30)),  # 30 дней в месяце
    (Calendar(1970, 1, 1)),   # 1 день в году + UNIX TIME дата отсчета :)
    (Calendar(2017, 12, 31))  # последний день в году
]

td_negative = [
    (Calendar(2000, 2, 30)),  # 30 февраля в високосном году
    (Calendar(2001, 2, 29)),  # 29 февраля в не високосном году
    (Calendar(2017, 1, 32)),  # 32 дней в месяце
    (Calendar(2017, 4, 31)),  # 31 дней в месяце
    (Calendar(2017, 13, 5)),  # несуществующий месяц
    (Calendar(2017, 4, 0)),   # некорректный формат
    (Calendar(2017, 0, 13)),
    (Calendar(0, 5, 29)),
    (Calendar(0, 0, 0)),
    (Calendar(2017, 4, None)),
    (Calendar(2017, None, 13)),
    (Calendar(None, 5, 29)),
    (Calendar(None, None, None))
]


@pytest.mark.parametrize('calendar', td_positive)
def test_positive_calendar(calendar):
    datetime.date(calendar.year, calendar.month, calendar.day)


@pytest.mark.parametrize('calendar', td_negative)
def test_negative_calendar(calendar):
    with pytest.raises(Exception):
        datetime.date(calendar.year, calendar.month, calendar.day)
