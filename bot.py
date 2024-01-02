import tkinter as tk
from tkinter import Scrollbar, Text, Frame, Button, Entry

qa_pairs = {
    "Tell me about Python basics.": "Python basics cover fundamental concepts such as variables, data types (integers, floats, strings), control flow statements (if, else, loops), and functions.",
    "Explain data structures in Python.": "Python supports various data structures. Lists are ordered and mutable, tuples are ordered and immutable, dictionaries are key-value pairs, and sets are unordered collections of unique elements.",
    "Discuss Python functions.": "Functions in Python are defined using the 'def' keyword. They can take parameters, return values, and are reusable blocks of code. You can define and call functions to modularize your code and make it more readable.",
    "Tell me about Python modules and libraries.": "In Python, modules are individual files containing Python code. Libraries are collections of modules that provide additional functionality. Popular libraries include NumPy for numerical computing, Pandas for data manipulation, and Matplotlib for data visualization.",
    "How does Python handle exceptions?": "Python uses a try-except block to handle exceptions. Code inside the 'try' block is executed, and if an exception occurs, the code inside the 'except' block is executed to handle the exception.",
    "What is list comprehension in Python?": "List comprehension is a concise way to create lists in Python. It provides a more readable and compact syntax for creating lists by specifying the expression to evaluate and the input sequence to iterate over.",
    "Explain object-oriented programming (OOP) in Python.": "Python is an object-oriented programming language. OOP is a programming paradigm that uses objects, which bundle data and methods that operate on the data. In Python, you can create classes and objects to implement OOP concepts.",
    "How does Python handle memory management?": "Python uses a built-in garbage collector to manage memory. It automatically deallocates memory occupied by objects that are no longer in use, freeing up resources and preventing memory leaks.",
}

chatbot_name = "Mystic"

class ChatBotApp:
    def __init__(self, root):
        self.root = root
        self.root.title(f"{chatbot_name}'s Python Interview ChatBot")
        self.root.geometry("600x400")

        self.create_widgets()

    def create_widgets(self):
        self.create_chat_log()
        self.create_input_box()
        self.create_ask_button()
        self.create_topic_buttons()

    def create_chat_log(self):
        self.chat_log = Text(self.root, wrap="word", state="disabled", font=("Arial", 12), bg="aqua")  # Set new background color
        self.chat_log.pack(fill="both", expand=True)

        scrollbar = Scrollbar(self.root, command=self.chat_log.yview)
        scrollbar.pack(side="right", fill="y")
        self.chat_log.config(yscrollcommand=scrollbar.set)

    def create_input_box(self):
        self.input_box = Entry(self.root, bg="#ffffcc", font=("Arial", 12), justify="center", insertwidth=4)
        self.input_box.pack(fill="both", expand=True, pady=5)

        # Set a placeholder text
        self.input_box.insert(0, "Type here...")

        # Bind the function to clear the placeholder on focus
        self.input_box.bind("<FocusIn>", self.clear_placeholder)

    def create_ask_button(self):
        ask_button = Button(self.root, text="Ask", command=self.ask_question, bg="#4caf50", fg="#ffffff", font=("Arial", 12))
        ask_button.pack(pady=5)

    def create_topic_buttons(self):
        topics_frame = Frame(self.root)
        topics_frame.pack()

        topic_buttons = [
            ("Python Basics", "Tell me about Python basics."),
            ("Data Structures", "Explain data structures in Python."),
            ("Functions", "Discuss Python functions."),
            ("Modules and Libraries", "Tell me about Python modules and libraries."),
            ("Exceptions", "How does Python handle exceptions?"),
            ("List Comprehension", "What is list comprehension in Python?"),
            ("OOP in Python", "Explain object-oriented programming (OOP) in Python."),
            ("Memory Management", "How does Python handle memory management?"),
        ]

        for topic, question in topic_buttons:
            Button(topics_frame, text=topic, command=lambda q=question: self.ask_question(q), 
                   bg="#2196F3", fg="#ffffff", font=("Arial", 10)).pack(side="left", padx=5, pady=5)

    def clear_placeholder(self, event):
        # Clear the placeholder text when the user clicks on the input box
        if self.input_box.get() == "Type here...":
            self.input_box.delete(0, tk.END)

    def ask_question(self, custom_question=None):
        user_question = custom_question if custom_question else self.input_box.get().strip().lower()
        self.input_box.delete(0, 'end')  # Clear the input box

        response = qa_pairs.get(user_question, " I don't have an answer for that question.")
        
        self.chat_log.config(state="normal")
        self.chat_log.insert("end", f"User: {user_question}\n", "user")
        self.chat_log.insert("end", f"{chatbot_name}: {response}\n", "chatbot")
        self.chat_log.tag_config("user", foreground="black")  # Set user text color (navy blue)
        self.chat_log.tag_config("chatbot", foreground="red")  # Set chatbot text color (dark green)
        self.chat_log.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatBotApp(root)
    root.mainloop()
