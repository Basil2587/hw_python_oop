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
          date_now = dt.datetime.now().date()
          sum_day = sum([notes.amount for notes in self.records if notes.date == date_now])      
          return sum_day

     def get_week_stats(self):
          date_now = dt.datetime.now().date()
          timedelta = date_now - dt.timedelta(6)
          sum_week = sum([notes.amount for notes in self.records if timedelta <= notes.date <= date_now])         
          return sum_week
          
class CashCalculator(Calculator):
     USD_RATE = 63.0
     EURO_RATE = 68.7
                  
     def get_today_cash_remained(self, currency=None):
          total = self.get_today_stats()
          exchange = {'rub': (1.0, 'руб'),
                      'usd': (self.USD_RATE, 'USD'),
                      'eur': (self.EURO_RATE, 'Euro'),
          }
          rate, coin = exchange[currency] 
          money = round((self.limit-total)/rate,2)
          if total < self.limit:
               answer = f'На сегодня осталось {money} {coin}'
          elif total == self.limit: 
               answer = 'Денег нет, держись'
          else:
               if money < 0:
                    money = abs(money)
                    answer = f'Денег нет, держись: твой долг - {money} {coin}'     
          return answer


class CaloriesCalculator(Calculator):
          
     def get_calories_remained(self):
          lim_calories = self.limit-self.get_today_stats()
          if lim_calories > 0:
               answer = f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {lim_calories} кКал'
          else:
               answer = 'Хватит есть!'
          return answer