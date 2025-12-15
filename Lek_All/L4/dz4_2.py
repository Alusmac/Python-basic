lst =[1, 3, 5] #=> 30
#lst = [6] #=> 36
#lst = [] #=> 0

answer = sum(lst[::2]) * lst[-1] if lst else 0
print(answer)