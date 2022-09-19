## Import libraries 
from datetime import datetime 

BirthDate = input("Enter Birthday (dd/mm/yyyy): ") ## input your birthday. Example: 10/12/2000

SplitBirthDate = BirthDate.split("/") ## Splits your birthday. Example: ['10', '12', '2000']

BirthYear = int(SplitBirthDate[2]) ## Gets year from split birthday and turns it from string to int. Example: '2000' to 2000

BirthMonth = int(SplitBirthDate[1]) ## Gets month from split birthday and turns it from string to int. Example: '12' to 12

BirthDay = int(SplitBirthDate[0]) ## Gets day from split birthday and turns it from string to int. Example: '12' to 12

DateTimeBirthday = datetime(day=BirthDay, month=BirthMonth, year=BirthYear) ## your birthday to datetime

YourAge = round((datetime.now() - DateTimeBirthday).total_seconds() / 86400, 3) ## Read Below
## Line above gets current date - your birthday than turns it into seconds / 86400 (Days) than rounds the number to 3 decimals 

print(f"You are {int(YourAge/365)} years old.\nYou were born {YourAge} days ago.") ## Prints results
