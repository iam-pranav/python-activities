# 🥤 THE GREAT JUICE SWAP GAME! (For Grades 6-8) 🥤
# Imagine you have two cups:
# Cup A has Apple Juice 🍎
# Cup B has Blueberry Juice 🫐
# How do you swap them without mixing them up? You need a third "temporary" empty cup! 🏆

def swap_numbers(cup_a, cup_b):
    print(f"\n🟢 BEFORE SWAP:")
    print(f"Cup A has: {cup_a}")
    print(f"Cup B has: {cup_b}")
    
    # Step 1: Pour Cup A into our temporary empty cup
    temp_cup = cup_a
    
    # Step 2: Now that Cup A is empty, pour Cup B into Cup A
    cup_a = cup_b
    
    # Step 3: Pour the juice from the temporary cup into Cup B
    cup_b = temp_cup
    
    print(f"\n🔵 AFTER SWAP:")
    print(f"Cup A now has: {cup_a}")
    print(f"Cup B now has: {cup_b}")
    return cup_a, cup_b

# Let's play!
try:
    number_1 = float(input("Enter your first number (Cup A): "))
    number_2 = float(input("Enter your second number (Cup B): "))
    
    swap_numbers(number_1, number_2)
except ValueError:
    print("Please enter actual numbers to play the game!")
