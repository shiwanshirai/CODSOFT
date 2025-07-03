import random
import tkinter as tk
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")
item_list = ["Rock", "Paper", "Scissors"]
tk.Label(root, text="Choose your move", font=("Comic Sans MS", 16)).pack(pady=20)

def play_game(user_move):
    
    comp_move = random.choice(item_list)

    result = f"Your move: {user_move}\nComputer's move: {comp_move}\n"

    if user_move == comp_move:
        result += "Tie 🤝"
    elif user_move == "Rock":
        if comp_move == "Paper":
            result += "Computer Wins 🤖"
        else:
            result += "You Win 🥳"
    elif user_move == "Paper":
        if comp_move == "Rock":
            result += "You Win 🥳"
        else:
            result += "Computer Wins 🤖"
    elif user_move == "Scissors":
        if comp_move == "Rock":
            result += "Computer Wins 🤖"
        else:
            result += "You Win 🥳"
    else:
        result = "Invalid input."

    result_window = tk.Toplevel(root)
    result_window.title("Game Result")
    result_window.geometry("300x200")
    tk.Label(result_window, text=result, font=("Comic Sans MS", 12)).pack(pady=20)



tk.Button(root, text="Rock", width=20, height=2, font=("Comic Sans MS", 12), bg="lightgreen", fg="black", command=lambda: play_game("Rock")).pack(pady=5)
tk.Button(root, text="Paper", width=20, height=2, font=("Comic Sans MS", 12), bg="lightgreen", fg="black", command=lambda: play_game("Paper")).pack(pady=5)
tk.Button(root, text="Scissors", width=20, height=2, font=("Comic Sans MS", 12), bg="lightgreen", fg="black", command=lambda: play_game("Scissors")).pack(pady=5)

tk.Button(root, text="Exit", width=20, height=2, command=root.quit).pack(pady=20)

root.mainloop()