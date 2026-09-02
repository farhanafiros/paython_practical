squares =[]

for x in range(1,6):
    squares.append(x**2)
print(squares)

squares_comp = [x**2 for x in range(1,6)]
print(squares_comp)