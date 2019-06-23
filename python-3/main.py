import numpy as np
from _datetime import datetime, date

class ManagerDates:
    def date_is_valid(self, date):
        try:
            datetime.strptime(date, '%d/%m/%Y')
            return True

        except ValueError:
            return False

    def date_weekday(self, date):
        week_days = {0: 'Monday',
                     1: 'Tuesday',
                     2: 'Wednesday',
                     3: 'Thursday',
                     4: 'Friday',
                     5: 'Saturday',
                     6: 'Sunday'}
        return week_days[date.weekday()]

    def convert_string_to_date(self, date_str):
        try:
            return datetime.strptime(date_str, '%d/%m/%Y')
        except:
            try:
                return datetime.strptime(date_str, '%d-%m-%Y')
            except:
                try:
                    return datetime.strptime(date_str, '%d%m%Y')
                except:
                    return False

    def get_all_dates(self, month, year):
        start_date = date(int(year), int(month), 1)
        end_date = date(int(year), int(month) + 1, 1)

        return np.arange(start_date, end_date)

    def count_days_mounth(self, month, year):
        start_date = date(int(year), int(month), 1)
        end_date = date(int(year), int(month) + 1, 1)

        return np.busday_count(start_date, end_date)

    def get_first_monday(self, year):
        date_ = np.busday_offset(str(year)+'-05',  0, roll='forward', weekmask='Mon')
        return "{:02d}/{:02d}/{:d}".format(
            date_.astype('datetime64[D]').astype(object).day,
            date_.astype('datetime64[M]').astype(object).month,
            date_.astype('datetime64[Y]').astype(object).year,
            )
