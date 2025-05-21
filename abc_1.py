def double_until_match(odd_number, target):
    sequence = []
    while odd_number < target + 2:
        sequence.append(odd_number)
        if odd_number in (target - 1, target, target + 1):
            print(f"{odd_number} match")
            break
        odd_number *= 2
    return sequence

# User input
target_number = int(input("Enter the target number: "))
while True:
    odd_number = int(input("Enter an odd number: "))
    if odd_number % 2 != 0:
        break
    print("Please enter a valid odd number.")

result = double_until_match(odd_number, target_number)

if result:
    print("\n".join(map(str, result)))
    if result[-1] == target_number - 1:
        print(f"Closest match: {target_number - 1}")
    elif result[-1] == target_number + 1:
        print(f"Closest match: {target_number + 1}")
else:
    print("No valid sequence generated. The starting number was too large.")
