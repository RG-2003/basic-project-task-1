# Define a list to store tasks
tasks = [
    {"description": "Buy groceries", "priority": "High"},
    {"description": "Complete project report", "priority": "Medium"},
    {"description": "Schedule a meeting with the team", "priority": "Low"},
    {"description": "Prepare presentation for the meeting", "priority": "Medium"},
    {"description": "Pay the bills", "priority": "High"},
    {"description": "Exercise", "priority": "Low"}
]

# Function to list all tasks
def list_tasks():
    if not tasks:
        print("No tasks found!")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['description']}: {task['priority']}")

# Main function to run the task management app
def main():
    while True:
        print("\nTask Management Menu:")
        print("1. List Tasks")
        print("2. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            list_tasks()
        elif choice == "2":
            print("Exiting Task Management App. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
