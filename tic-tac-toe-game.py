import tkinter as tk
from tkinter import messagebox

# check winner

def check_winner():
    global winner
    combos =[
        [0,1,2],[3,4,5],[6,7,8], 
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for a,b,c in combos:
        ta = buttons[a]["text"]
        tb = buttons[b]["text"]
        tc = buttons[c]["text"]

        # check three-in-a-row and not empty 
        if ta == tb == tc != "":
            winner = True
            buttons[a].config(bg="lightgreen")
            buttons[b].config(bg="lightgreen")
            buttons[c].config(bg="lightgreen")
            messagebox.showinfo("tic - tac -toe", f"Player {ta} wins!")
            # optionally disable board so no further clicks allowed
            for btn in buttons:
                btn.config(state=tk.DISABLED)
            return
         # draw check: if no empty buttons and no winner
    if not winner and all(button["text"] != "" for button in buttons):
        messagebox.showinfo("tic - tac -toe", "It's a draw!")
        for btn in buttons:
            btn.config(state=tk.DISABLED)

def button_click(index):
    global current_player
    if buttons[index]["text"] == "" and not winner:
        buttons[index].config(text=current_player)   # use config (safer)
        check_winner()
        if not winner:                                # toggle only if game not finished
            toggle_player()
        

def toggle_player():
   global current_player 
   current_player = "X" if current_player == "O" else "O"
   label.config(text=f"player {current_player}'s turn")

root =tk.Tk()
root.title("tic-tac-toe")

buttons =[tk.Button(root, text="", font=("normal",25), width=6, height=2, command=lambda i=i: button_click(i)) for i in range(9)]

for i, button in enumerate(buttons):
   button.grid(row=i // 3, column= i % 3)

current_player = "X"
winner = False
label = tk.Label(root, text=f"player {current_player}'s turn",font=("normal",16))
label.grid(row=3,column=0 ,columnspan=3)

root.mainloop()









