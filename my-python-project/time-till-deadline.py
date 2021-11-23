from datetime import datetime

user_input = input("Enter your goal with a deadline, separated by a colon \n")
input_list = user_input.split(":")
goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")

# Calculate how many days till deadline

today_date = datetime.today()
calculated_time = deadline_date - today_date
print(f"Dear user, time remaining for your goal: {goal} is {calculated_time.days} days")
