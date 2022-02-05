'''Your job is to write a program that allows you to mark a square on the map using a two-digit system.
The first digit is the vertical column number and the second digit is the horizontal row number. e.g.:'''

# row1 = ["a", "b", "c"]
# row2 = ["d", "e", "f"]
# row3 = ["j", "i", "k"]

row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
map = [row1, row2, row3]
print(map)
# print(map[0][0])
# print(map[0][1])
# print(map[0][2])
# print(map[1][0])
# print(map[1][1])
# print(map[1][2])
# print(map[2][0])
# print(map[2][1])
# print(map[2][2])
# print(type(map))
position = input("Where do you want to put the treasure? ")
position_convert = list(position[1] + position[0])
print(position_convert)
if position_convert == ['1', '1']:
    map[0][0] = 'x'
elif position_convert == ['1', '2']:
    map[0][1] = 'x'
elif position_convert == ['1', '3']:
    map[0][2] = 'x'
elif position_convert == ['2', '1']:
    map[1][0] = 'x'
elif position_convert == ['2', '2']:
    map[1][1] = 'x'
elif position_convert == ['2', '3']:
    map[1][2] = 'x'
elif position_convert == ['3', '1']:
    map[2][0] = 'x'
elif position_convert == ['3', '2']:
    map[2][1] = 'x'
elif position_convert == ['3', '3']:
    map[2][2] = 'x'

print(f"{row1}\n{row2}\n{row3}")
