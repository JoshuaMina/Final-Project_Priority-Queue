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