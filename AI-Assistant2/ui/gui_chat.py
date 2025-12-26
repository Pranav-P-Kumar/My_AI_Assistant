# ui/gui_chat.py
import tkinter as tk
from tkinter import scrolledtext

class GUIChat:
    def __init__(self, get_response_fn):
        self.get_response = get_response_fn

        self.window = tk.Tk()
        self.window.title("Student AI Assistant")

        self.chat_box = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, state=tk.DISABLED, width=80, height=20)
        self.chat_box.pack(padx=10, pady=10)

        self.input_var = tk.StringVar()
        self.input_box = tk.Entry(self.window, textvariable=self.input_var, width=70)
        self.input_box.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))
        self.input_box.bind("<Return>", self.on_enter)

        self.send_btn = tk.Button(self.window, text="Send", command=self.on_enter)
        self.send_btn.pack(side=tk.LEFT, padx=(5, 10), pady=(0, 10))

        self.window.protocol("WM_DELETE_WINDOW", self.window.destroy)

    def on_enter(self, event=None):
        user_text = self.input_var.get().strip()
        if not user_text:
            return
        self.input_var.set("")
        self.append(f"You: {user_text}\n")

        response = self.get_response(user_text)
        self.append(f"Assistant: {response}\n")

    def append(self, text: str):
        self.chat_box.config(state=tk.NORMAL)
        self.chat_box.insert(tk.END, text + "\n")
        self.chat_box.see(tk.END)
        self.chat_box.config(state=tk.DISABLED)

    def run(self):
        self.window.mainloop()
