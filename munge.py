def changetemp(c):
    f = c / 100 * 1.8
    return format(f, ".1f")

f = open("data.txt", "r")
csv_file = open("clean_data.csv", "w")

s = f.readline()

while "Year" not in s:
    s = f.readline()

clean_s = ",".join(s.split()[:-1]) + "\n"
csv_file.write(clean_s)

s = f.readline()

while True:
    if s != "":
        if s.split(" ")[0].isnumeric():
            not_clean_lst = s.split()[:-1]
            for i in range(1, len(not_clean_lst)):
                if "*" in not_clean_lst[i]:
                    not_clean_lst[i] = "NaN"
                else:
                    not_clean_lst[i] = changetemp(int(not_clean_lst[i]))
            clean_s = ",".join(not_clean_lst) + "\n"
            csv_file.write(clean_s)
            s = f.readline()
        else:
            s = f.readline()
            continue
    else:
        break

csv_file.close()
