# Place code below to do the analysis part of the assignment.
import csv

num_rows = 0

for row in open("clean_data.csv", "r"):
    num_rows += 1

csvfile = open("clean_data.csv", "r")

l = csvfile.readline()

while num_rows != 1:
    l = csvfile.readline()
    lst = l.split(",")
    avg_lst = [0 for i in range(len(lst))]
    divisor = [10 for i in range(len(lst))]
    avg_lst[0] = str(lst[0]) + " to "
    if num_rows >= 10:
        for i in range(10):
            for j in range(1, len(lst)):
                if "NaN" in lst[j]:
                    divisor[j] -= 1
                else:
                    avg_lst[j] += float(lst[j])
            if lst[0][3] != "9":
                l = csvfile.readline()
                lst = l.split(",")
        num_rows -= 10
    else:
        num_rows -= 1
        divisor = [num_rows for i in range(len(lst))]
        for i in range(num_rows):
            for j in range(1, len(lst)):
                if "NaN" in lst[j]:
                    divisor[j] -= 1
                else:
                    avg_lst[j] += float(lst[j])
            if num_rows != 1:
                l = csvfile.readline()
                lst = l.split(",")
                num_rows -= 1

    avg_lst[0] += str(lst[0])
    for k in range(1, len(lst)):
        avg_lst[k] = str(format(avg_lst[k] / divisor[k], ".1f"))
    final = avg_lst[0] + ": " + ", ".join(avg_lst[1:])
    print(final)
    


