numbers = [-4,-3,-2,-1,0,2,4,6]
positive_number = []
negative_number = []
for num in numbers:
    if num > 0:
        positive_number.append(num)
    else:
        negative_number.append(num)
print("正數有:",len(positive_number),"個",positive_number)
print("負數有",len(negative_number),"個",negative_number)