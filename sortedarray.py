# Initialize the array
arr = [45, 12, 78, 33, 11, 20, 30]

print("Original Array:", arr)

print("\nPress:")
print("1 - Ascending Order")
print("2 - Descending Order")

choice = input("Enter your choice: ")

if choice == "1":
    arr.sort()
    print("Ascending Order:", arr)

elif choice == "2":
    arr.sort(reverse=True)
    print("Descending Order:", arr)

else:
    print("Invalid Choice!")