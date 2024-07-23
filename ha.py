import tkinter as tk
import random
def display_funny_messages():
    messages = [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "Parallel lines have so much in common. It’s a shame they’ll never meet.",
        "I threw a boomerang a few years ago. I now live in constant fear.",
        "Why don’t skeletons fight each other? They don’t have the guts."
    ]
    message = random.choice(messages)
    label.config(text=message)

#krijimi i window
root = tk.Tk()
root.title("Funny Messages App")
root.geometry("500x500")
root.configure(bg="#f0f0f0")

#krijimi i label
label = tk.Label(root, text="Click the button for a joke!", 
font=("Arial", 14), bg="#f0f0f0", fg="#c42d2d")
label.pack(pady=20)

#krijimi i butonit
button = tk.Button(root, text="Make me laugh!", command=display_funny_messages,
font=("Arial", 14), bg="#f0f0f0", fg="#c42d2d")
button.pack(pady=20)

root.mainloop()