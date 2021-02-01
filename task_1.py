class Date:

    def __init__(self, date):
        self.__date = date

    @classmethod
    def convert(cls, date):
        return [int(x) for x in str(date).split('-')]

    @staticmethod
    def validate(v):
        day, month, year = v[0], v[1], v[2]
        return 0 < day < 32 and 0 < month < 13 and 0 < year < 2100

    @property
    def internal_date(self):
        return self.__date


d = Date('06-04-1987')
print(f'Date {d.internal_date}')
print(f'Convert {Date.convert(d.internal_date)}')
print(f'Is {d.internal_date} valid? {Date.validate(Date.convert(d.internal_date))}')

d2 = Date('15-04-77987')
print(f'Is {d2.internal_date} valid? {Date.validate(Date.convert(d2.internal_date))}')
