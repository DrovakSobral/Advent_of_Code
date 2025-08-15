input = open("2024/day_2/puzzle_input.txt")
raw_input = input.read().split("\n")

master_report_list = []
for report in raw_input:
    new_report = []
    temp_list = report.split()
    for level in temp_list:
        new_report.append(int(level))
    master_report_list.append(new_report)
master_report_list.remove(master_report_list[-1])

total_safe_report_counter = 0
unsafe_report_list = []
for report in master_report_list:
    descending = True
    ascending = True
    safe_gap = True
    for index in range(len(report)-1):
        if report[index] > report[index+1]:
            ascending = False
        if report[index] < report[index+1]:
            descending = False
        if report[index] == report[index+1]:
            safe_gap = False
        if (report[index] - report[index+1]) >= 4 :
            safe_gap = False
        if (report[index] - report[index+1]) <= -4 :
            safe_gap = False
    if safe_gap == True and (ascending == True or descending == True):
        total_safe_report_counter += 1
    else:
        unsafe_report_list.append(report)

problem_dampner_counter = 0
for report in unsafe_report_list:
    for level in range(len(report)):
        temp_report = report.copy()
        temp_report.pop(level)
        descending = True
        ascending = True
        safe_gap = True
        for index in range(len(temp_report)-1):
            if temp_report[index] > temp_report[index+1]:
                ascending = False
            if temp_report[index] < temp_report[index+1]:
                descending = False
            if temp_report[index] == temp_report[index+1]:
                safe_gap = False
            if (temp_report[index] - temp_report[index+1]) >= 4 :
                safe_gap = False
            if (temp_report[index] - temp_report[index+1]) <= -4 :
                safe_gap = False
        if safe_gap == True and (ascending == True or descending == True):
            problem_dampner_counter += 1
            break

safe_problem_dampned_report_total = total_safe_report_counter + problem_dampner_counter

print("Total amount of safe reports:", total_safe_report_counter)
print("Total amount of safe reports due to the problem dampner:", safe_problem_dampned_report_total)

#for each report, check if the levels are in ascending or descending order and if the difference between consecutive numbers is between 1 to 3