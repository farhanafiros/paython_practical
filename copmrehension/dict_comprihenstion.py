squares_dict = { x: x**2 for x in range(5)}
print(squares_dict)

even_squares_dict = {x :x**2 for x in range(10) if x % 2 ==0 }
print(even_squares_dict)