'''Your job is to write a program that allows you to mark a square on the map using a two-digit system.
The first digit is the vertical column number and the second digit is the horizontal row number. e.g.:
column 2, row 3 would be entered as: 23'''

row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
map = [row1, row2, row3]

position = input("Where do you want to put the treasure? ")
#23
vertical_column = int(position[0]) #2
horizontal_row = int(position[1])   #3

# selected_row = map[row - 1]
# selected_row[column - 1] = 'X'
print(map)
map[horizontal_row - 1][vertical_column - 1] = 'X'
print(map)
print(f"{row1}\n{row2}\n{row3}")
