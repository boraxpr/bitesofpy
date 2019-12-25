from datetime import datetime

NOW = datetime.now()

# print(datetime.strptime("11-11-2018", "%d-%m-%Y")-NOW)


class Promo:

    def __init__(self, name, expiredate):
        self.name = name
        self.expiredate = expiredate.strftime("%d/%m/%Y")
        self._expired = self.expired

    @property
    def expired(self):
        return datetime.strptime(self.expiredate, "%d/%m/%Y") < NOW

    @expired.setter
    def expired(self, expiredate):
        if expiredate-NOW < 0:
            self.expired = 1
        else:
            self.expired = 0


# print(Promo("dead", "22/12/2020").expired)