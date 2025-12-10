import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def is_valid_move(x, y, board):
    if x >= 0 and y >= 0 and x < len(board) and y < len(board):
        return board[x][y] == -1
    return False

def count_valid_moves(x, y, x_moves, y_moves, board):
    count = 0
    for i in range(8):
        new_x, new_y = x + x_moves[i], y + y_moves[i]
        if is_valid_move(new_x, new_y, board):
            count += 1
    return count

def get_warnsdorff_moves(x, y, x_moves, y_moves, board):
    move_list = []
    for i in range(8):
        new_x, new_y = x + x_moves[i], y + y_moves[i]
        if is_valid_move(new_x, new_y, board):
            count = count_valid_moves(new_x, new_y, x_moves, y_moves, board)
            move_list.append((count, new_x, new_y))
    move_list.sort(key=lambda x: x[0])
    return [(x, y) for _, x, y in move_list]

def solve_knight_tour(board, x, y, move_count, x_moves, y_moves, path, is_closed, max_iterations):
    
    if move_count == len(board) * len(board):
        if is_closed:
            start_x, start_y = path[0]
            for i in range(8):
                if x + x_moves[i] == start_x and y + y_moves[i] == start_y:
                    path.append((start_x, start_y))
                    return True
            return False
        else:
            path.append((x, y))  
            return True
        return False
    
    move_list = get_warnsdorff_moves(x, y, x_moves, y_moves, board)
    
    for (new_x, new_y) in move_list:
        board[new_x][new_y] = move_count
        path.append((new_x, new_y))
        if solve_knight_tour(board, new_x, new_y, move_count + 1, x_moves, y_moves, path, is_closed, max_iterations):
            return True        
        board[new_x][new_y] = -1
        path.pop()
    return False


def animate_knight(path, size):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xticks(np.arange(-0.5, size, 1))
    ax.set_yticks(np.arange(-0.5, size, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(True)
    ax.set_xlim(-0.5, size - 0.5)
    ax.set_ylim(size - 0.5, -0.5)  
    knight_pos, = ax.plot([], [], marker="o", markersize=8, color="blue", linestyle="-", linewidth=2)

    def update_frame(frame):
        x_vals, y_vals = zip(*path[:frame+1])  
        knight_pos.set_data(x_vals, y_vals)
        return knight_pos,
    ani = FuncAnimation(fig, update_frame, frames=len(path), interval=500, blit=True, repeat=False)
    ani.event_source.stop()  
    plt.title(f"Knight's Tour - TeoriGrafB11")
    plt.show()

def visualize_knight_tour(path, size):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xticks(np.arange(-0.5, size, 1))
    ax.set_yticks(np.arange(-0.5, size, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(True)

    
    ax.set_xlim(-0.5, size - 0.5)
    ax.set_ylim(size - 0.5, -0.5)  

    
    x_vals, y_vals = zip(*path)
    ax.plot(x_vals, y_vals, marker="o", markersize=8, color="blue", linestyle="-", linewidth=2)

    plt.title(f"Knight's Tour - TeoriGrafB11")
    plt.show()


def knight_tour():
    size = 8
    tour_type = input("Enter the type of tour ('open' or 'closed'): ").strip().lower()
    board = [[-1 for _ in range(size)] for _ in range(size)]
    x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
    y_moves = [1, 2, 2, 1, -1, -2, -2, -1]
    start_pos = input(f"Enter the starting position (e.g., 'A1', 'H8'): ").strip().lower()
    start_x = ord(start_pos[0]) - ord('a')
    start_y = 8 - int(start_pos[1])
    
    board[start_x][start_y] = 0
    path = [(start_x, start_y)]
    
    max_iterations = 5000  
    if solve_knight_tour(board, start_x, start_y, 1, x_moves, y_moves, path, is_closed=(tour_type == 'closed'), max_iterations=max_iterations):
        print("Knight's Tour Found!")
        print("The path of the knight is:")
        for move in path:
            print(move)        
        animate_knight(path, size)
    else:
        print("No solution found!")

if __name__ == "__main__":
    knight_tour()
