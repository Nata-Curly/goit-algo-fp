def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )

    total_cost = 0
    total_calories = 0
    selected_items = []

    for item in sorted_items:
        name, properties = item
        if total_cost + properties["cost"] <= budget:
            selected_items.append(name)
            total_cost += properties["cost"]
            total_calories += properties["calories"]

    return selected_items, total_calories, total_cost


def dynamic_programming(items, budget):
    names = list(items.keys())
    n = len(names)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        name = names[i - 1]
        cost = items[name]["cost"]
        calories = items[name]["calories"]
        for j in range(budget + 1):
            if cost > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + calories)

    total_calories = dp[n][budget]
    total_cost = 0
    selected_items = []
    j = budget
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            name = names[i - 1]
            selected_items.append(name)
            total_cost += items[name]["cost"]
            j -= items[name]["cost"]

    return selected_items, total_calories, total_cost


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}

budget = 100

selected_items, total_calories, total_cost = greedy_algorithm(items, budget)
print("\nGreedy algorithm")
print("-" * 50)
print("Selected items:", selected_items)
print("Total calories:", total_calories)
print("Total cost:", total_cost)

selected_items, total_calories, total_cost = dynamic_programming(items, budget)
print("\nDynamic programming")
print("-" * 50)
print("Chosen items:", selected_items)
print("Total calories:", total_calories)
print("Total cost:", total_cost)
