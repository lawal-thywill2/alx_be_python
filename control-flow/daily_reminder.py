task = input("Enter your task: ")
priority = input("Priority (High/Medium/Low): ").strip().lower()
time_bound = input("Is it time-bound? (Yes/No): ").strip().lower()

match priority :
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today.")
        elif time_bound == "no":
            print(f"Reminder: '{task}' is a high priority task. Please address it as soon as possible.")
        else:
            print(f"Reminder: '{task}' has an unrecognized priority level.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be completed soon.")
        elif time_bound == "no":
            print(f"Reminder: '{task}' is a medium priority task. Please plan to complete it in due time.")
        else:
            print(f"Reminder: '{task}' has an unrecognized priority level.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that can be done at your convenience.")
        elif time_bound == "no":
            print(f"Reminder: '{task}' is a low priority task. Feel free to complete it whenever possible.")
        else:
            print(f"Reminder: '{task}' has an unrecognized priority level.")