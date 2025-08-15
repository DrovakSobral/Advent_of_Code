input = open("2024/day_1/puzzle_input.txt")
combined_list_raw = input.read().split()
list_1 = []
list_2 = []
for index in range(len(combined_list_raw)):
    if (index % 2) == 0:
        list_2.append(int(combined_list_raw[index]))
    else:
        list_1.append(int(combined_list_raw[index]))

list_1.sort()
list_2.sort()
total_distance = 0
for index in range(len(list_1)):
    if list_2[index] > list_1[index]:
        total_distance += (list_2[index] - list_1[index])
    else:
        total_distance += (list_1[index] - list_2[index])

total_similarity_score = 0
for index_A in range(len(list_1)):
    counter = 0
    for index_B in range(len(list_2)):
        if list_1[index_A] == list_2[index_B]:
            counter += 1
    total_similarity_score += (list_1[index_A] * counter)

print("total distance:", total_distance)
print("total similarity score:", total_similarity_score)