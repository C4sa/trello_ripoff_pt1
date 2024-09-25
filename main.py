class Task:
    def __init__(self, name, description=''):
        self.name = name
        self.description = description
        self.completed = False

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.name} - {self.description}"
    
    def complete(self):
        self.completed = True


class List:
    def __init__(self, name):
        self.name = name
        self.tasks = []
        
    def add_task(self, task_name, description=''):
        task = Task(task_name, description)
        self.tasks.append(task)

    def display_tasks(self):
        if not self.tasks:
            print(f"There are no tasks in list {self.name}")
        else:
            print(f"Tasks in list {self.name}:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].complete()
        else:
            print("Invalid task index!")


class Board:
    def __init__(self, name):
        self.name = name
        self.lists = []

    def add_list(self, list_name):
        new_list = List(list_name)
        self.lists.append(new_list)

    def display_lists(self):
        if not self.lists:
            print(f"No lists in board {self.name}")
        else:
            print(f"Lists in board {self.name}:")
            for i, lst in enumerate(self.lists, 1):
                print(f"{i}. {lst.name}")

    def get_list(self, list_index):
        if 0 <= list_index < len(self.lists):
            return self.lists[list_index]
        else:
            print("Invalid list index!")
            return None
        
class TrelloRipoff:
    def __init__(self):
        self.boards = []

    def add_board(self, board_name):
        board = Board(board_name)
        self.boards.append(board)

    def display_boards(self):
        if not self.boards:
            print("No boards available!")
        else:
            print("Available Boards:")
            for i, board in enumerate(self.boards, 1):
                print(f"[{i}] {board.name}")

    def get_board(self, board_index):
        if 0 <= board_index < len(self.boards):
            return self.boards[board_index]
        else:
            print("Invalid board index!")
            return None
        

def main():
    app = TrelloRipoff()

    while True:
        command = input("\n> ")

        if command == "mkboard":
            board_name = input("Name for new board: ")
            app.add_board(board_name)
            print(f"New board {board_name} created!")

        elif command == "mklist":
            app.display_boards()
            board_index = int(input("Board index for list: ")) - 1
            board = app.get_board(board_index)
            if board:
                list_name = input("Name for new list: ")
                board.add_list(list_name)
                print(f"New list {list_name} created!")

        elif command == "showboards":
            print("Board list:")
            app.display_boards()

        elif command == "showlists":
            app.display_boards()
            board_index = int(input("Select board index: ")) - 1
            board = app.get_board(board_index)
            if board:
                board.display_lists()

if __name__ == "__main__":
    main()