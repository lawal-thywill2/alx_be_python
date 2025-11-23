task = input("Enter your task: ")
priority = input("Priority (High/Medium/Low): ")
time_bound = input("Is it time-bound? (Yes/No): ")

if time_bound == "yes":
    if priority == "high":
        print(f"Reminder: {task} is a high priority task that requires immediate attention today.")
    elif priority == "medium":
        print(f"Reminder: {task} is a medium priority task. Please ensure to complete it within the next two days.")
    elif priority == "low":
        print(f"Reminder: {task} is a low priority task. You can schedule it for later this week.")
    else:
        print("Invalid priority level entered.")
elif time_bound == "no":
    if priority == "high":
        print(f"Reminder: {task} is a high priority task. Please plan to complete it as soon as possible.")
    elif priority == "medium":
        print(f"Reminder: {task} is a medium priority task. Try to get to it within the week.")
    elif priority == "low":
        print(f"Reminder: {task} is a low priority task. Consider completing it when you have free time.")
    else:
        print("Invalid priority level entered.")
else:
    print("Invalid time-bound response entered.")