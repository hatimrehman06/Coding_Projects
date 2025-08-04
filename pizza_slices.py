# List of pizza toppings
topping = ("pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms")

# Prices for each topping (in the same order as topping list)
prices = (2, 6, 1, 3, 2, 7, 2)

# Count how many pizzas cost exactly $2
num_two_dollar_slices = prices.count(2)

# Count how many different pizza types we have
num_pizzas = len(topping)

# Print how many different types of pizzas we sell
print("We sell", num_pizzas, "different kinds of pizza!")

# Combine prices and toppings into one list (list of lists)
pizza_and_prices = [
    [2, "pepperoni"],
    [6, "pineapple"],
    [1, "cheese"],
    [3, "sausage"],
    [2, "olives"],
    [7, "anchovies"],
    [2, "mushrooms"]
]

# Print the combined list of pizzas and their prices
print(pizza_and_prices)

# Sort pizzas by price (lowest to highest)
pizza_and_prices.sort()

# Get the cheapest pizza (first item after sorting)
cheapest_pizza = pizza_and_prices[0]

# Get the most expensive pizza (last item after sorting)
priciest_pizza = pizza_and_prices[6]

# Remove the last pizza from the list (the priciest one)
pizza_and_prices.pop()

# Add a new pizza with price 2.5 and topping "peppers"
pizza_and_prices.append([2.5, "peppers"])

# Get the three cheapest pizzas after changes
three_cheapest = pizza_and_prices[:3]

# Print the three cheapest pizzas
print(three_cheapest)
