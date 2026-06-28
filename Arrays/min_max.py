arr = list(map(int, input("Enter numbers:").split()))

max = arr[0]
min = arr[0]

for num in arr:
    if num>max:
        max=num
    if num<min:
        min=num
print("maximum=", max)
print("minimum=", min)