import sys

line_arr = []
for line in sys.stdin:
    line_arr.append([x.strip() for x in line.split('/')])

new_line_arr = filter(lambda x: x[1] == line_arr[-1][0], line_arr[:-1])
for line in sorted(new_line_arr, key=lambda x: -x[0]):
    print(line[0])
