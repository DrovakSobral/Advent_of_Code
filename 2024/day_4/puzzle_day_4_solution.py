import re as re

input = open("2024/day_4/puzzle_input.txt")
raw_input = input.read().split()
horizontal_count = 0
vertical_count = 0
diagonal_count = 0

# Count every instance of the word "XMAS" both fowards and backwards on the horizontal axis
for line in raw_input:
    temp_list = re.findall("XMAS", line)
    horizontal_count += len(temp_list)
    temp_list = re.findall("SAMX", line)
    horizontal_count += len(temp_list)

# Count every instance of the word "XMAS" both fowards and backwards on the vertical axis
for line in range(len(raw_input)-3):
    for column in range(len(raw_input[0])):
        if raw_input[line][column] == "X" and raw_input[line+1][column] == "M" and raw_input[line+2][column] == "A" and raw_input[line+3][column] == "S":
            vertical_count += 1
        if raw_input[line][column] == "S" and raw_input[line+1][column] == "A" and raw_input[line+2][column] == "M" and raw_input[line+3][column] == "X":
            vertical_count += 1

# Count every instance of the word "XMAS" both fowards and backwards on the diagonal axis from left to right
for line in range(len(raw_input)-3):
    for column in range(len(raw_input[0])-3):
        if raw_input[line][column] == "X" and raw_input[line+1][column+1] == "M" and raw_input[line+2][column+2] == "A" and raw_input[line+3][column+3] == "S":
            diagonal_count += 1
        if raw_input[line][column] == "S" and raw_input[line+1][column+1] == "A" and raw_input[line+2][column+2] == "M" and raw_input[line+3][column+3] == "X":
            diagonal_count += 1

# Count every instance of the word "XMAS" both fowards and backwards on the diagonal axis from right to left
for line in range(len(raw_input)-3):
    for column in range(3, len(raw_input[0])):
        if raw_input[line][column] == "X" and raw_input[line+1][column-1] == "M" and raw_input[line+2][column-2] == "A" and raw_input[line+3][column-3] == "S":
            diagonal_count += 1
        if raw_input[line][column] == "S" and raw_input[line+1][column-1] == "A" and raw_input[line+2][column-2] == "M" and raw_input[line+3][column-3] == "X":
            diagonal_count += 1

xmas_count = 0
for line in range(len(raw_input)-2):
    for column in range(len(raw_input[0])-2):
        if raw_input[line][column] == "M" and raw_input[line][column+2] == "M" and raw_input[line+1][column+1] == "A" and raw_input[line+2][column] == "S" and raw_input[line+2][column+2] == "S":
            xmas_count += 1
        if raw_input[line][column] == "M" and raw_input[line][column+2] == "S" and raw_input[line+1][column+1] == "A" and raw_input[line+2][column] == "M" and raw_input[line+2][column+2] == "S":
            xmas_count += 1
        if raw_input[line][column] == "S" and raw_input[line][column+2] == "M" and raw_input[line+1][column+1] == "A" and raw_input[line+2][column] == "S" and raw_input[line+2][column+2] == "M":
            xmas_count += 1
        if raw_input[line][column] == "S" and raw_input[line][column+2] == "S" and raw_input[line+1][column+1] == "A" and raw_input[line+2][column] == "M" and raw_input[line+2][column+2] == "M":
            xmas_count += 1


total_count = horizontal_count + vertical_count + diagonal_count
print("Total amount of times the word \"XMAS\" shows up:", total_count)
print("Total amount of times the word \"MAS\" shows up in an x with itself:", xmas_count)
# 3022 is too high
# 1097 is too low