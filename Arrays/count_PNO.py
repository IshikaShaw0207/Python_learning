arr= [-1,-2,0,4,7,2,5]

positive= negative = zero = 0

for num in arr:
    if num>0:
        positive+=1
    elif num<0:
        negative+=1
    else:
        zero+=1

print("positive:",positive)
print("Negative:",negative)
print("Zero:", zero)
