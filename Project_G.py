# Sort table

numbers = []

number_of_cells = int(input("Enter the number of cells you want: "))

for i in range(number_of_cells):
    cell = int(input(f"Enter the cell number {i+1}: "))
    numbers.append(cell)

print(f" this is your list: {numbers}")

for i in range(number_of_cells - 1):
    min_pos = i
    min = numbers[min_pos]

    for j in range (i+1, number_of_cells):
        if numbers[j] < min:
            min_pos = j
            min = numbers[min_pos]

    numbers[min_pos] = numbers[i]
    numbers[i] = min

print("Let me sort this list .....")
print(f"This is the ordered list: {numbers}")