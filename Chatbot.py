import tkinter as tk
from tkinter import scrolledtext


def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "You: " + user_input + "\n")
    entry.delete(0, tk.END)

  
    response = get_bot_response(user_input)
    chat_window.insert(tk.END, "Bot: " + response + "\n\n")
    chat_window.config(state=tk.DISABLED)
    chat_window.see(tk.END)

def get_bot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"
    elif "your name" in user_input:
        return "I'm a Python Chatbot!"
    elif "how are you" in user_input:
        return "I'm doing great, thank you!"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that."

root = tk.Tk()
root.title("Simple Chatbot")
root.geometry("400x500")
root.resizable(False, False)

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=30, font=("Arial", 12))
entry.pack(side=tk.LEFT, padx=(10, 5))
entry.focus()

send_button = tk.Button(frame, text="Send", command=send_message)
send_button.pack(side=tk.LEFT)

root.mainloop()