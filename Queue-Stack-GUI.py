import tkinter as tk

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[0]

    def size(self):
        return len(self.items)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

class StackQueueGUI:
    def __init__(self, master):
        self.master = master
        master.title("Stack and Queue GUI")

        self.stack = Stack()
        self.queue = Queue()

        self.stack_frame = tk.Frame(master)
        self.stack_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.stack_label = tk.Label(self.stack_frame, text="Stack")
        self.stack_label.pack()

        self.stack_listbox = tk.Listbox(self.stack_frame, width=20, height=10)
        self.stack_listbox.pack()

        self.stack_entry = tk.Entry(self.stack_frame)
        self.stack_entry.pack()

        self.stack_push_button = tk.Button(self.stack_frame, text="Push", command=self.stack_push)
        self.stack_push_button.pack(pady=5)

        self.stack_pop_button = tk.Button(self.stack_frame, text="Pop", command=self.stack_pop)
        self.stack_pop_button.pack()