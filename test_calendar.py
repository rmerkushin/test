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
    (Calendar(2017, 13, 5))   # несуществующий месяц
]


@pytest.mark.parametrize('cl', td_positive)
def test_positive_calendar(cl):
    datetime.date(cl.get_year, cl.get_month, cl.get_day)


@pytest.mark.parametrize('cl', td_negative)
def test_negative_calendar(cl):
    with pytest.raises(ValueError):
        datetime.date(cl.get_year, cl.get_month, cl.get_day)
