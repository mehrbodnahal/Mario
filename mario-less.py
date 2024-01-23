def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error input")


height = get_int("Height: ")


while height < 1 or height > 8:
    height = get_int("Height: ")


for i in range(1, height + 1):
    print(" " * (height - i) + "#" * i)
