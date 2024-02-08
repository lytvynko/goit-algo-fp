items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_calories = 0
    selected_items = []
    
    for item, info in sorted_items:
        if budget >= info['cost']:
            budget -= info['cost']
            total_calories += info['calories']
            selected_items.append(item)
    
    return selected_items, total_calories

def dynamic_programming(items, budget):
    item_names = list(items.keys())
    n = len(item_names)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            cost = items[item_names[i-1]]['cost']
            calories = items[item_names[i-1]]['calories']
            
            if cost <= w:
                dp[i][w] = max(calories + dp[i-1][w-cost], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(item_names[i-1])
            w -= items[item_names[i-1]]['cost']
    
    selected_items.reverse()
    total_calories = dp[n][budget]
    
    return selected_items, total_calories

# Приклад використання
budget = 100
greedy_result = greedy_algorithm(items, budget)
dynamic_result = dynamic_programming(items, budget)

print("Greedy Algorithm Result:", greedy_result)
print("Dynamic Programming Result:", dynamic_result)