import random


def roll_dice():
    return random.randint(1, 6)


def simulate_dice_rolls(num_rolls):
    results = {}
    for _ in range(num_rolls):
        roll1 = roll_dice()
        roll2 = roll_dice()
        total = roll1 + roll2
        if total in results:
            results[total] += 1
        else:
            results[total] = 1

    probabilities = {k: v / num_rolls * 100 for k, v in results.items()}
    return probabilities


def print_probabilities(probabilities):
    print("Сума\tІмовірність")
    print("-" * 20)
    sorted_probabilities = sorted(probabilities.items())
    for total, probability in sorted_probabilities:
        print(f"{total}\t{probability:.2f}% ({probability/100:.2f})")


def main():
    num_rolls = 100000  
    probabilities = simulate_dice_rolls(num_rolls)
    print(f"\nДля {num_rolls} кидків кубиків:\n")
    print_probabilities(probabilities)


if __name__ == "__main__":
    main()
