class ToDoList:
    def __init__(self):
        self.tasks = {}
        self.task_id_counter = 1

    def add_task(self, description):
        task_id = self.task_id_counter
        self.tasks[task_id] = {'description': description, 'completed': False}
        self.task_id_counter += 1
        print(f'Task {task_id} added: {description}')

    def mark_task_completed(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id]['completed'] = True
            print(f'Task {task_id} marked as completed.')
        else:
            print(f'Task {task_id} not found.')

    def update_task_description(self, task_id, new_description):
        if task_id in self.tasks:
            self.tasks[task_id]['description'] = new_description
            print(f'Task {task_id} description updated: {new_description}')
        else:
            print(f'Task {task_id} not found.')

    def remove_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            print(f'Task {task_id} removed.')
        else:
            print(f'Task {task_id} not found.')

    def display_tasks(self):
        if not self.tasks:
            print('No tasks found.')
        else:
            print('Tasks:')
            for task_id, task_info in self.tasks.items():
                status = 'Completed' if task_info['completed'] else 'Not Completed'
                print(f'{task_id}: {task_info["description"]} - {status}')


def main():
    todo_list = ToDoList()

    while True:
        print('\n1. Add Task')
        print('2. Mark Task as Completed')
        print('3. Update Task Description')
        print('4. Remove Task')
        print('5. Display Tasks')
        print('6. Quit')

        choice = input('Enter your choice (1-6): ')

        if choice == '1':
            description = input('Enter task description: ')
            todo_list.add_task(description)
        elif choice == '2':
            task_id = int(input('Enter task ID to mark as completed: '))
            todo_list.mark_task_completed(task_id)
        elif choice == '3':
            task_id = int(input('Enter task ID to update description: '))
            new_description = input('Enter new task description: ')
            todo_list.update_task_description(task_id, new_description)
        elif choice == '4':
            task_id = int(input('Enter task ID to remove: '))
            todo_list.remove_task(task_id)
        elif choice == '5':
            todo_list.display_tasks()
        elif choice == '6':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 6.')
if __name__ == '__main__':
    main()
