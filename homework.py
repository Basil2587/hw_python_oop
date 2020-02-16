import datetime as dt

class Record:
     def __init__(self, amount, comment, date=None):
          date_format = '%d.%m.%Y'
          self.amount = amount
          self.date =  dt.datetime.strptime(date, date_format).date() if date else dt.date.today()
          self.comment = comment

class Calculator:
     def __init__(self, limit):
          self.limit = limit
          self.records = []

     def add_record(self, Record):
          self.records.append(Record)

     def get_today_stats(self):
          sum_day = 0
          date_now = dt.datetime.now().date()
          for notes in self.records:
               if notes.date == date_now:
                   sum_day = sum_day + int(notes.amount)    
          return sum_day
     def get_week_stats(self):
          sum_week = 0
          date_now = dt.datetime.now().date()
          timedelta = date_now - dt.timedelta(6)
          for notes in self.records:
               if timedelta <= notes.date <= date_now:
                    sum_week = sum_week + int(notes.amount)
          return sum_week

class CashCalculator(Calculator):
     USD_RATE = 63.0
     EURO_RATE = 68.7
                  
     def __init__(self, limit):
          super().__init__(limit)

     def get_today_cash_remained(self, currency=None):
          total = self.get_today_stats()
          exchange = {"rub": 1.0, "usd": self.USD_RATE, "eur": self.EURO_RATE} 
          valuta = {"rub": 'руб', "usd": 'USD', "eur": 'Euro'}
          money = round((self.limit - total)/exchange[currency],2)         
          if total < self.limit:     
               answer = F'На сегодня осталось {money} {valuta[currency]}'
          elif total == self.limit: 
               answer = 'Денег нет, держись'         
          else:
               if money < 0:
                    money = money*(-1)
                    answer = F'Денег нет, держись: твой долг - {money} {valuta[currency]}'     
          return answer


class CaloriesCalculator(Calculator):
     def __init__(self, limit):
          super().__init__(limit)
          
     def get_calories_remained(self):
          lim_calories = self.limit - self.get_today_stats()
          if lim_calories > 0 :
               answer = F'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {lim_calories} кКал'
          else:
               answer = 'Хватит есть!'
          return answer           




