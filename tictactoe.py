##########################################################################################
# Tic-Tac-Toe 
#
# This script implements a Tic-Tac-Toe game using tkinter for the GUI.
# I also added a customizable board size just for fun (normal tic-tac-toe gets boring after a while),
# which can be set by a prompt to the user. Enjoy playing!
#
# Author: Yash Uppot
##########################################################################################


import tkinter as tk
from tkinter import simpledialog, messagebox

class TicTacToe:
    def __init__(self, root, size):
        self.root = root
        self.size = size
        self.board = [' ' for _ in range(size * size)]  # Initialize the game board
        self.current_player = 'X'  # Initialize the current player
        self.buttons = [[None for _ in range(size)] for _ in range(size)]  # Initialize the button grid
        self.create_widgets()  # Create GUI widgets
        self.update_status()  # Update game status

    def create_widgets(self):
        # Create status label to display game status
        self.status_label = tk.Label(self.root, text="", font=('Helvetica', 20))
        self.status_label.pack()

        # Create frame to hold buttons
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        # Create buttons for the game grid
        for i in range(self.size):
            for j in range(self.size):
                # Create a button with a click event handler
                button = tk.Button(self.frame, text=' ', font=('Helvetica', 20), height=2, width=5,
                                   command=lambda row=i, col=j: self.handle_click(row, col))
                button.grid(row=i, column=j)  # Place the button in the grid layout
                self.buttons[i][j] = button  # Store button reference in the grid

        # Create reset button
        self.reset_button = tk.Button(self.root, text="Reset", font=('Helvetica', 14), command=self.reset_game)
        self.reset_button.pack()

    def handle_click(self, row, col):
        # Handle button click event
        index = row * self.size + col
        if self.board[index] == ' ':  # If the clicked cell is empty
            self.board[index] = self.current_player  # Update board with player symbol
            self.buttons[row][col].config(text=self.current_player)  # Update button text
            winner = self.who_won()  # Check for a winner
            if winner != '0':  # If there's a winner
                messagebox.showinfo("Game Over", f"Player {winner} wins!")  # Show winner message
                self.end_game()  # End the game
            elif self.draw():  # If it's a draw
                messagebox.showinfo("Game Over", "It's a tie!")  # Show draw message
                self.end_game()  # End the game
            else:  # If the game continues
                self.current_player = self.switch_player(self.current_player)  # Switch player
                self.update_status()  # Update game status
        else:
            messagebox.showwarning("Invalid Move", "This spot is already taken.")  # Show warning for invalid move

    def who_won(self):
        # Check for a winner
        # Check rows
        for i in range(self.size):
            if all(self.board[self.size * i + j] == self.board[self.size * i] != ' ' for j in range(self.size)):
                return self.board[self.size * i]

        # Check columns
        for i in range(self.size):
            if all(self.board[self.size * j + i] == self.board[i] != ' ' for j in range(self.size)):
                return self.board[i]

        # Check left diagonal
        if all(self.board[self.size * i + i] == self.board[0] != ' ' for i in range(self.size)):
            return self.board[0]

        # Check right diagonal
        if all(self.board[self.size * i + (self.size - i - 1)] == self.board[self.size - 1] != ' ' for i in range(self.size)):
            return self.board[self.size - 1]

        return '0'

    def draw(self):
        # Check for a draw
        if ' ' not in self.board and self.who_won() == '0':
            return True
        return False

    def switch_player(self, curr_player):
        # Switch player
        return 'O' if curr_player == 'X' else 'X'

    def update_status(self):
        # Update game status
        self.status_label.config(text=f"It's player {self.current_player}'s turn!")

    def end_game(self):
        # End the game
        for row in self.buttons:
            for button in row:
                button.config(state=tk.DISABLED)  # Disable buttons

    def reset_game(self):
        # Reset the game
        self.board = [' ' for _ in range(self.size * self.size)]  # Reset board
        self.current_player = 'X'  # Reset player
        for row in self.buttons:
            for button in row:
                button.config(text=' ', state=tk.NORMAL)  # Reset buttons
        self.update_status()  # Update game status

if __name__ == "__main__":
    root = tk.Tk()  # Create root window
    root.title("Tic Tac Toe")  # Set window title

    # Prompt user for board size
    size = simpledialog.askinteger("Input", "Enter the size of the board (integer between 3 and 10):", minvalue=3, maxvalue=10)
    if size:  # If user input is valid
        game = TicTacToe(root, size)  # Initialize TicTacToe object with given size
        root.mainloop()  # Start the Tkinter event loop