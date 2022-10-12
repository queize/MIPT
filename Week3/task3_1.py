# Программа считывает натуральное число. 
# По данному натуральному числу найдите минимальное натуральное число, 
# состоящее из тех же цифр, что и данное, и выведите его на экран.

# Важно! Число не может начинаться с 0.

# 123412345

nums = int(input())

while nums > 0:
    num_list.append(nums % 10)
    nums //= 10
num_list = num_list[::-1]

num_list.sort()

for i in range(len(num_list)):
    if num_list[i] != 0:
        num_list[0], num_list[i] = num_list[i], num_list[0]
        break
print(num_list)