arr = list(map(int,input("enter numbers:").split()))

largest=second=float('-inf')

for num in arr:
    if num>largest:
        second=largest
        largest=num
    elif largest> num > second:
        second = num
    
print("Second largest:", second)
