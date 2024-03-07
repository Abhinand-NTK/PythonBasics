from datetime import datetime,timedelta

Test = datetime.today().date()
print(Test)

start_Date = datetime(2023,1,1).date()
End_Date = datetime(2023,11,1).date()
print(End_Date - start_Date)