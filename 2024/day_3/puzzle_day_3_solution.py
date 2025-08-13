import re as re

input = open("2024/day_3/puzzle_input")
raw_input = input.read()
unucorrupted_memory_list = re.findall(r"mul\(\d\,\d\)|mul\(\d\,\d\d\)|mul\(\d\,\d\d\d\)|mul\(\d\d\,\d\)|mul\(\d\d\,\d\d\)|mul\(\d\d\,\d\d\d\)|mul\(\d\d\d\,\d\)|mul\(\d\d\d\,\d\d\)|mul\(\d\d\d\,\d\d\d\)|do\(\)|don\'t\(\)", raw_input)

total_result = 0
for instruction in unucorrupted_memory_list:
    both_numbers = re.findall(r"\d\d\d|\d\d|\d", instruction)
    if len(both_numbers) > 0:
        first_number = int(both_numbers[0])
        second_number = int(both_numbers[1])
        total_result += first_number * second_number

total_result_enabled = 0
multiplication = True
for instruction in unucorrupted_memory_list:
    if instruction[:3] == "do(":
        multiplication = True
    if instruction[:3] == "don":
        multiplication = False
    if instruction[:3] == "mul" and multiplication == True:
        both_numbers = re.findall(r"\d\d\d|\d\d|\d", instruction)
        first_number = int(both_numbers[0])
        second_number = int(both_numbers[1])
        total_result_enabled += first_number * second_number

print("Total result of all uncorrupted mul instructions:", total_result)
print("Total result of all uncorrupted and enabled mul instructions:", total_result_enabled)