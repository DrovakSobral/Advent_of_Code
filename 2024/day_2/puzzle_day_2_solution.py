input = open("/home/drovak/Programming_Projects/GitHub_Repos/Advent_of_Code/2024/day_2/puzzle_input")
raw_input = input.read().split("\n")

master_report_list = []
for report in raw_input:
    new_report = []
    temp_list = report.split()
    for level in temp_list:
        new_report.append(int(level))
    master_report_list.append(new_report)
master_report_list.remove(master_report_list[-1])

#for each report, check if the levels are in ascending or descending order and if the difference between consecutive numbers is between 1 to 3