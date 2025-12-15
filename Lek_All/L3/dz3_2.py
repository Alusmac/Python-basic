#lis = [12, 3, 4, 10] # [10, 12, 3, 4]
#lis = [1] # [1]
lis = [] # []
#lis = [12, 3, 4, 10, 8] # [8, 12, 3, 4, 10

lis =[lis[-1]] + lis[:-1]
    if lis else []
print(lis)