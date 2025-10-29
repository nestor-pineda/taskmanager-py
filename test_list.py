from task_manager import TaskManager

print("Testing Task Manager...")
tm = TaskManager()
print(f"Loaded {len(tm.tasks)} tasks")

if tm.tasks:
    print("Tasks found:")
    for task in tm.tasks:
        print(f"  Task {task.id}: {task.description} - {'Done' if task.completed else 'Pending'}")
else:
    print("No tasks found")

print("\nCalling list_tasks():")
tm.list_tasks()
print("Done.")