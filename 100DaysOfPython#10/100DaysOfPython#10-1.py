leap_check = True

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("Leap year.")
        leap_check = True
      else:
        print("Not leap year.")
        leap_check = False
    else:
      print("Leap year.")
      leap_check = True
  else:
    print("Not leap year.")
    leap_check = False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (month == 2):
        is_leap(year)
        if leap_check == True: #윤년이면
            month_days[1] = 29
    return month_days[month-1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)