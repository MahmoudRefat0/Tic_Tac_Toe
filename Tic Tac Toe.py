#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Tic_Tac_Toe

def display_board(board):
    num = 1
    for row in board:
        formatted_row = [str(num) if cell == ' ' else cell for cell in row]
        print(" | ".join(formatted_row))
        print("-" * 9)  # خط فاصل بين الصفوف
        num += 1

def check(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def main():
    while True:
        player_choice = input("Choose X or O: ").upper()
        if player_choice not in ['X', 'O']:
            print("Invalid choice. Choose X or O.")
            continue  # العودة لبداية الحلقة

        current, board = player_choice, [[' ']*3 for _ in range(3)]
        moves = []

        while True:
            display_board(board)  # عرض لوحة اللعب
            try:
                move = int(input(f"{current}, choose a number from 1 to 9: "))
                if 1 <= move <= 9:
                    r = (move - 1) // 3
                    c = (move - 1) % 3
                    if board[r][c] == ' ':
                        board[r][c] = current
                        moves.append(str(move))  # تسجيل الحركة في قائمة الحركات
                        if check(board, current):
                            display_board(board)  # عرض لوحة اللعب
                            print(f"{current} wins!")
                            formatted_moves = "\n".join(moves)  # تنسيق القائمة في صفوف منفصلة
                            print(formatted_moves)
                            break
                        elif all([s != ' ' for row in board for s in row]):
                            print("It's a draw!")
                            break
                        else:
                            current = 'O' if current == 'X' else 'X'
                    else:
                        print("Invalid move. The position is already occupied.")
                else:
                    print("Invalid input. Choose a number from 1 to 9.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        while play_again not in ['yes', 'no']:
            print("Invalid input. Enter 'yes' or 'no'.")
            play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == 'no':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()


# In[ ]:




