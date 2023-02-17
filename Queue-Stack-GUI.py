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
        master.title("Final Project - Stack and Queue GUI")
        self.master.config( bg="#16558f")

        self.stack = Stack()
        self.queue = Queue()

        self.stack_frame = tk.Frame(master,bg="#0583d2")
        self.stack_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.stack_label1 = tk.Label(self.stack_frame, text="Joshua Miña", font=("Times New Roman",18),bg="#0583d2")
        self.stack_label2 = tk.Label(self.stack_frame, text="Stack",font=("Arial",12),bg="#0583d2")
        self.stack_label1.pack()
        self.stack_label2.pack()


        self.stack_listbox = tk.Listbox(self.stack_frame, width=20, height=10,bg="#b8e3ff")
        self.stack_listbox.pack()

        self.stack_ask = tk.Label(self.stack_frame, text="Enter Element", font=("Arial", 12), bg="#0583d2")
        self.stack_ask.pack()
        self.stack_entry = tk.Entry(self.stack_frame,bg="#b8e3ff")
        self.stack_entry.pack()

        self.stack_push_button = tk.Button(self.stack_frame, text="Push", command=self.stack_push,bg="#61b0b7",font=("arial",10),width=10)
        self.stack_push_button.pack(pady=5)

        self.stack_pop_button = tk.Button(self.stack_frame, text="Pop", command=self.stack_pop,bg="#61b0b7",font=("arial",10),width=10)
        self.stack_pop_button.pack()

        self.queue_frame = tk.Frame(master,bg="#0583d2")
        self.queue_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        self.queue_label1 = tk.Label(self.queue_frame, text=" BSCOE 2-2",font=("Times New Roman",18), bg="#0583d2")
        self.queue_label2 = tk.Label(self.queue_frame, text="Queue",font=("Arial",12),bg="#0583d2")
        self.queue_label1.pack()
        self.queue_label2.pack()

        self.queue_listbox = tk.Listbox(self.queue_frame, width=20, height=10,bg="#b8e3ff")
        self.queue_listbox.pack()

        self.queue_ask = tk.Label(self.queue_frame, text="Enter Element", font=("Arial", 12), bg="#0583d2")
        self.queue_ask.pack()
        self.queue_entry = tk.Entry(self.queue_frame,bg="#b8e3ff")
        self.queue_entry.pack()

        self.queue_enqueue_button = tk.Button(self.queue_frame, text="Enqueue", command=self.queue_enqueue,bg="#61b0b7",font=("arial",10),width=10)
        self.queue_enqueue_button.pack(pady=5)

        self.queue_dequeue_button = tk.Button(self.queue_frame, text="Dequeue", command=self.queue_dequeue,bg="#61b0b7",font=("arial",10),width=10)
        self.queue_dequeue_button.pack()

    def stack_push(self):
        item = self.stack_entry.get()
        self.stack.push(item)
        self.stack_listbox.insert(tk.END, item)
        self.stack_entry.delete(0, tk.END)

    def stack_pop(self):
        item = self.stack.pop()
        self.stack_listbox.delete(0,tk.END)
        self.stack_entry.delete(0, tk.END)
        self.stack_listbox.insert(tk.END, self.stack.items)


    def queue_enqueue(self):
        item = self.queue_entry.get()
        self.queue.enqueue(item)
        self.queue_listbox.insert(tk.END, item)
        self.queue_entry.delete(0, tk.END)

    def queue_dequeue(self):
        item = self.queue.dequeue()
        self.queue_listbox.delete(0,tk.END)
        self.queue_listbox.insert(tk.END, self.queue.items)
        self.queue_entry.delete(0, tk.END)

root = tk.Tk()
app = StackQueueGUI(root)
root.mainloop()
