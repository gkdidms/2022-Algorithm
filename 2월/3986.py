
n = int(input())
count = 0

for j in range(n):
    m = input()
    stack = []

    for i in range(len(m)):
        if stack and m[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(m[i])
    if not stack:
        count += 1
print(count)


# n = int(input())
# count = []
# for i in range(n):
#     m = input()
#     count.append(m)
#     if len(m) % 2 == 0:

#         print(m)
#         strings = [ j for j in range(len(m)) if "A" in m[j]]
#         if len(strings) > 1:
#             for j in range(len(strings)-1):
#                 if ((strings[j-1])-strings[j]) %2 == 0:
#                     count.pop()
#                     break
#         else:
#             count.pop()
#     else:
#         count.pop()
# print(len(count))