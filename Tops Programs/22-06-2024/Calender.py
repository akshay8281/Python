# For Particular Month only
'''
import calendar

yy = 2024
mm = 8

#Display the Output
print(calendar.month(yy,mm))
'''

# Full Year
'''
import calendar

yy = 2025
# mm = 8

#Display the Output
print(calendar.calendar(yy))
'''

# Date and Time
from datetime import date

today = date.today()

print("Current Day : ",today.day)
print("Current Month : ",today.month)
print("Current Year : ",today.year)
