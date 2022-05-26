class Person:
    count = 0

    def __init__(self, first_name: str, last_name: str, year: int, month: int, day: int) -> None:
        self.name = f'{last_name} {first_name}'
        self._year = year
        self._month = month
        self._day = day
        Person.count += 1

    @name.setter
    def name(self, new_name):
        self.name = new_name

    @month.setter
    def month(self, month):
        self.month = month

    @year.setter
    def year(self, year):
        self._year = year

    @day.setter
    def day(self, day):
        self.day = day

    @property
    def month(self):
        return self._month

    @property
    def day(self):
        return self._day

    @property
    def year(self):
        return self._year

    @property
    def name(self):
        return self.name

    @month.deleter
    def month(self):
        del self._month

    @day.deleter
    def day(self):
        del self._day

    @year.deleter
    def year(self):
        del self._year


    @classmethod
    def get_Id(Id):
        return Id.count

    def __del__(self):
        Person.count -= 1