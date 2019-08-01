# sorted()除了对数字进行排序，也可以对字符串进行排序，字符串默认按照ASCII大小来比较

ls = [36, 5, 12, 9, 21]

# def reversed_cmp(x, y):
#     if x > y:
#         return -1
#     if x < y:
#         return 1
#     return 0

print(sorted(ls))
print(sorted(ls, reverse=False))
print(sorted(ls, reverse=True))
print()

students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
# 以年龄降序排序
rs = sorted(students, key=lambda student : student[2],reverse = True)
print('sort by age:', rs)

# 以分数升序排序
rs = sorted(students, key=lambda student : student[1])
print('sort by score:', rs)

# 以姓名升序排序
rs = sorted(students, key=lambda student : student[0])
print('sort by name:', rs)

