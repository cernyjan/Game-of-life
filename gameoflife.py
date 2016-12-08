import random
from time import sleep
import cell
import turtle


def init_matrix(x_range, y_range):
        matrix = []
        for x in range(x_range):
                temp = []
                for y in range(y_range):
                        if random.random() > 0.5:
                                temp.append(cell.Cell(True))
                        else:
                                temp.append(cell.Cell(False))
                matrix.append(temp)  
        return matrix

def count_neighbors(matrix, x_range, y_range):
        for y in range(y_range):
                for x in range(x_range):
                        neighbors = 0
                        if is_valid(x-1, y-1, x_range, y_range):
                                if matrix[x-1][y-1].get_life() == True:
                                        neighbors = neighbors + 1
                        if is_valid(x, y-1, x_range, y_range):
                                if matrix[x][y-1].get_life() == True:
                                        neighbors = neighbors + 1
                        if is_valid(x+1, y-1, x_range, y_range):
                                if matrix[x+1][y-1].get_life() == True:
                                        neighbors = neighbors + 1
                        if is_valid(x-1, y, x_range, y_range):
                                if matrix[x-1][y].get_life() == True:
                                        neighbors = neighbors + 1
                        if is_valid(x+1, y, x_range, y_range):
                                if matrix[x+1][y].get_life() == True:
                                        neighbors = neighbors + 1
                        if is_valid(x-1, y+1, x_range, y_range):
                                if matrix[x-1][y+1].get_life() == True:
                                        neighbors = neighbors + 1
                        if is_valid(x, y+1, x_range, y_range):
                                if matrix[x][y+1].get_life() == True:
                                        neighbors = neighbors + 1
                        if is_valid(x+1, y+1, x_range, y_range):
                                if matrix[x+1][y+1].get_life() == True:
                                        neighbors = neighbors + 1
                        matrix[x][y].set_neighbors(neighbors)
        return matrix

def refresh_life(matrix, x_range, y_range):
        for y in range(y_range):
                for x in range(x_range):
                        if matrix[x][y].get_life() == True and (matrix[x][y].get_neighbors() > 3 or matrix[x][y].get_neighbors() < 2):
                                        matrix[x][y].set_life(False)
                        else: 
                                if matrix[x][y].get_neighbors() == 3:
                                        matrix[x][y].set_life(True)      
        return matrix

def is_valid(x, y, x_range, y_range):
        return (0 <= x < x_range) and (0 <= y < y_range)

def draw(matrix, w, t, x_range, y_range):
        w.reset()
        t.hideturtle()
        t.tracer(0, 0)
        for y in range(y_range):
                for x in range(x_range):
                        if matrix[x][y].get_life() == True:
                                t.color('#72BF44')
                        else:
                                t.color('#fef6f6')
                        t.penup()
                        t.setpos(x*10, 190 + y*(-10))
                        t.pendown()
                        t.begin_fill()
                        for i in range(4):
                                t.forward(9)
                                t.left(90)
                        t.end_fill()    
        w.update()

def write_text(text, w, t, x, y, color, size, finish = False):
        t.hideturtle()
        t.penup()
        t.setpos(x, y)
        t.color(color)
        t.write(text, font=("Arial", size, "normal"))
        w.update()
        if finish:
                turtle.done()


def main():
        cell_size = 10
        xpixels = 300
        ypixels = 200
        x_range = int(xpixels/cell_size)
        y_range = int(ypixels/cell_size)
        
        w = turtle.Screen()
        t = turtle.Turtle()

        w.title('Game Of Life')
        w.setup(xpixels+cell_size, ypixels+cell_size, 0, 0)
        w.screensize(xpixels+cell_size, ypixels+cell_size)
        w.setworldcoordinates(0, 0, xpixels+cell_size, ypixels+cell_size)

        loop = True
        level = 0
        
        matrix = init_matrix(x_range, y_range) 

        draw(matrix, w, t, x_range, y_range)

        while loop:
                write_text("level: " + str(level), w, t, 5, 5, "black", "10")
                if sum(sum(m.get_life() == True for m in l) for l in matrix) == 0:
                        loop = False
                        write_text("Game Over", w, t, 100, 100, "red", "16", True)
                        continue
                matrix = count_neighbors(matrix, x_range, y_range)
                matrix = refresh_life(matrix, x_range, y_range)
                draw(matrix, w, t, x_range, y_range)
                level = level + 1
                
                

        
if __name__ == '__main__':
        main()
