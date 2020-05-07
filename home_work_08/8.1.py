from datetime import datetime


class Data:

    def __init__(self, date):
        self.date = date

    def __str__(self):
        return Data.to_int(self.date)
        # return f"{self.date}"
        # return ' '.join(i for i in self.date.split('-'))

    @classmethod
    def to_int(cls, date_str):
        date_list = date_str.split('-')
        try:
            for i in range(len(date_list)):
                date_list[i] = int(date_list[i])
            return cls.valid_date(date_str)
        except ValueError:
            return f"Введено некорректное значение"

    @staticmethod
    def valid_date(date_str):
        try:
            datetime.strptime(date_str, '%d-%m-%Y')
            return f"Корректная дата: {date_str}"
            # return f"Дата введена корректно"
        except ValueError:
            return f"Некорректная дата"


my_date = Data("14-02-2015")
print(my_date)
print(Data.to_int('12-12-2012'))
