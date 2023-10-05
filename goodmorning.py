import time
name = input("Enter your name: ").title()
hour = int(time.strftime('%H'))
if 4<= hour < 12:
    print("Good Morning", name)
elif 12<= hour < 17:
    print("Good Afternoon", name)
elif 17<= hour < 20:
    print("Good Evening", name)
else:
    print("Good Night")