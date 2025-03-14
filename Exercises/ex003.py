# Your Student ID: 240543604
# Your Name and Surname: Aylin-P-Saatlou

from datetime import datetime

now = datetime.now()

current_date = now.strftime("%Y-%m-%d")
current_time = now.strftime("%H:%M:%S")

print("Current date: ", current_date)
print("Current time: ", current_time)
print("Current date and time: ", current_date ,current_time)