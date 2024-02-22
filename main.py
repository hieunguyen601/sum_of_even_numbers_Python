while True:
    target = int(input("Enter an even number between 0 and 1000: "))
    if target % 2 == 0 and 0 <= target <= 1000:
        break
    else:
        print("Invalid input. Please enter an even number between 0 and 1000.")

even_sum = 0
for number in range(2, target + 1, 2):  # Start from 2 and increment by 2 to ensure even numbers only
    even_sum += number

print("Sum of even numbers up to", target, "is:", even_sum)
