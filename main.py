from task_manager import TaskManager

def print_menu():
    print("\n-- Task Manager --")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

def main():
  
  task_manager = TaskManager()
  
  while True:

      print_menu()

      try:
          
        choice = input("Choose an option: ")

        match choice:
            case "1":
                description = input("Enter task description: ")
                task_manager.add_task(description)
            case "2":
                task_manager.list_tasks()
            case "3":
                id = int(input("Enter task ID to complete: "))
                task_manager.complete_task(id)
            case "4":
                id = int(input("Enter task ID to delete: "))
                task_manager.delete_task(id)
            case "5":
                print("Exiting Task Manager.")
                return
            case _:
                print("Invalid option. Please try again.")

      except Exception as e:
          print(f"An error occurred: {e}")

if __name__ == "__main__":
        main()