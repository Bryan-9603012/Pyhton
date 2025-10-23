# for迴圈
# for i in range(11):
#     print(i)

# while迴圈
# i=0
# while i < 11:
#     print(i)
#     i+=1

# for i in range(1,8):
#     print("#"*i)

# for i in range(1,8):
#     print("#"*8)

# for i in range(11):
#     print(i,"*",i,"=",i*i)

# a=['Python','Numpy','Pandas','Django','Flask']
# for i in range(5):
#     print(a[i])

# a=0
# for i in range(1,101,1):
#     a+=i
#     print(a)

# import sys

# i=0
# a=0
# for i in range(1,101):
#   a+=i
#   sys.stdout.write(str(i))  # 覆蓋同一行
#       sys.stdout.flush()
# print()
# print(a)

import sys

i=0
a=0
for i in range(1,101):
    if i%2==1:
        a+=i
        sys.stdout.write(str(i))  # 覆蓋同一行
        sys.stdout.flush()
        print()
print(a)
