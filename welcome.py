from datetime import datetime

current_time = datetime.now().time()
name = input("Enter your name: \n" )
hour = current_time.hour

if hour >= 5 and hour < 12:
    print("Good Moring " + name)
elif hour >= 12 and hour < 17:
    print("Good Afternoon " + name)
else:
    print("Good Evening " + name)