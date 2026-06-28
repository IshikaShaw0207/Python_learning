arr = list(map(int, input("enter numbers").split()))

min = arr[0]

for num in arr:
    if num< min:
        min=num

print("Minimum:", min)