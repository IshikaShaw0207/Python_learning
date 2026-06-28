arr = list(map(int, input("Enter numbers:").split()))

max = arr[0]
for num in arr:
    if num > max:
        max = num

print("Maximum =", max)