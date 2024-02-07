def greedy_algorithm(items, budget):
    # Сортуємо словник предметів за спаданням коефіцієнта калорійності до вартості
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )
    selected_items = []  
    total_cost = 0  
    total_calories = 0  

    # Проходимося по відсортованим предметам
    for item_name, item_data in sorted_items:
        # Якщо додавання вартості поточного предмета не перевищує бюджет
        if total_cost + item_data["cost"] <= budget:
            selected_items.append(item_name)  
            total_cost += item_data["cost"]  
            total_calories += item_data["calories"]  
    return {
        "selected_items": selected_items,
        "total_cost": total_cost,
        "total_calories": total_calories,
    }


def dynamic_programming(items, budget):
    # Ініціалізуємо матрицю dp для вирішення задачі динамічного програмування
    dp = [[0 for _ in range(budget + 1)] for _ in range(len(items) + 1)]

    # Заповнюємо матрицю dp
    for i in range(1, len(items) + 1):
        item_name, item_data = list(items.items())[i - 1]
        for j in range(1, budget + 1):
            if item_data["cost"] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i - 1][j - item_data["cost"]] + item_data["calories"],
                )

    # Відновлюємо обрані предмети з матриці dp
    selected_items = []
    i, j = len(items), budget
    while i > 0 and j > 0:
        item_name, item_data = list(items.items())[i - 1]
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(item_name)
            j -= item_data["cost"]
        i -= 1

    # Обчислюємо загальну вартість та калорійність обраних предметів
    total_cost = sum(items[item]["cost"] for item in selected_items)
    total_calories = sum(items[item]["calories"] for item in selected_items)
    return {
        "selected_items": selected_items,
        "total_cost": total_cost,
        "total_calories": total_calories,
    }


if __name__ == "__main__":
    # Список предметів з їх вартістю та калорійністю
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }

    budget = 100  

    # Виклик жадібного алгоритму та алгоритму динамічного програмування
    selected_items_greedy = greedy_algorithm(items, budget)
    selected_items_dp = dynamic_programming(items, budget)

    # Виведення результатів на екран
    print("Greedy Algorithm Result:")
    print(
        "{'selected_items':",
        selected_items_greedy["selected_items"],
        ", 'total_cost':",
        selected_items_greedy["total_cost"],
        ", 'total_calories':",
        selected_items_greedy["total_calories"],
        "}",
    )
    print("\nDynamic Programming Result:")
    print(
        "{'selected_items':",
        selected_items_dp["selected_items"],
        ", 'total_cost':",
        selected_items_dp["total_cost"],
        ", 'total_calories':",
        selected_items_dp["total_calories"],
        "}",
    )
