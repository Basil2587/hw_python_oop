import datetime as dt

class Record:
     def __init__(self, amount, comment, date = ''):
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
          sumDay = 0
          datenow = dt.datetime.now().date()
          for Notes in self.records:
               if Notes.date == datenow:
                   sumDay = sumDay + int(Notes.amount)    
          return sumDay
     def get_week_stats(self):
          sumWeek = 0
          datenow = dt.datetime.now().date()
          timedelta = datenow - dt.timedelta(7)
          for Notes in self.records:
               if timedelta <= Notes.date <= datenow:
                    sumWeek = sumWeek + int(Notes.amount)
          return sumWeek

class CashCalculator(Calculator):
     USD_RATE = 63.0
     EURO_RATE = 68.7
     N = 1.0
               
     def __init__(self, limit):
          super().__init__(limit)

     def get_today_cash_remained(self, currency):
          total = self.get_today_stats()
          if currency == 'usd':
               cur = 'USD'
               money = round((self.limit - total)/self.USD_RATE,2)
          elif currency == 'eur':
               cur = 'Euro'
               money = round((self.limit - total)/self.EURO_RATE,2)
          else:
               cur = 'руб'
               money = round((self.limit - total)/self.N,2)
          if total < self.limit:     
               answer = ('На сегодня осталось ' + str(money) + ' ' + cur)
          elif total == self.limit: 
               answer = 'Денег нет, держись'         
          else:
               if money < 0:
                    money = money * (-1)
               answer = ('Денег нет, держись: твой долг - '+ str(money) + ' ' + cur)     
          return answer


class CaloriesCalculator(Calculator):
     def __init__(self, limit):
          super().__init__(limit)
          
     def get_calories_remained(self):
          LimitCalor = self.limit - self.get_today_stats()
          if LimitCalor > 0 :
               answer = ('Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более ' + str(LimitCalor) + ' кКал') 
          else:
               answer = 'Хватит есть!'
          return answer           




