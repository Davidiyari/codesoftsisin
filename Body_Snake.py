#Codewars 309 snake
import tkinter as tk

def generate_snake_matrix():
    matrix = [[' ' for _ in range(3)] for _ in range(3)]

    # Posiciones 
    matrix[0][1] = 'H'  # Cabeza en la posición (0,1)
    matrix[1][0] = 'X'  # Cuerpo en (1,0)
    matrix[1][1] = 'X'  # Cuerpo en (1,1)
    matrix[2][0] = 'X'  # Cuerpo en (2,0)
    matrix[2][1] = 'X'  # Cuerpo en (2,1)
    matrix[2][2] = 'T'  # Cola en (2,2)

    return matrix

def draw_snake_matrix(matrix, cell_size=60):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    window = tk.Tk()
    window.title("Serpiente en matriz 3x3")
    canvas = tk.Canvas(window, width=cols * cell_size, height=rows * cell_size, bg="white")
    canvas.pack()

    for r in range(rows):
        for c in range(cols):
            x1 = c * cell_size
            y1 = r * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size

            canvas.create_rectangle(x1, y1, x2, y2, outline="black", width=2)
            text = matrix[r][c]
            if text != ' ':
                canvas.create_text(x1 + cell_size // 2, y1 + cell_size // 2, text=text, font=("Arial", 20, "bold"))

    window.mainloop()

matrix = generate_snake_matrix()

for row in matrix:
    print(row)

draw_snake_matrix(matrix)
