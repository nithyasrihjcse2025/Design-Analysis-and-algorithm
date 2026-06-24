
arr = [12, 25, 8, 45, 30, 18, 50]
target =8
found = False

for i in range(len(arr)):
    if arr[i] == target:
        print("Element  found at position:",i)
        found = True
        break

if not found:
    print("Element not found")