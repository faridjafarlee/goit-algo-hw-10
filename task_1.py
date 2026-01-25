from pulp import LpMaximize, LpProblem, LpStatus, LpVariable, value


def main() -> None:
    lemonade = LpVariable("Lemonade", lowBound=0, cat="Integer")
    juice = LpVariable("FruitJuice", lowBound=0, cat="Integer")

    model = LpProblem("Beverage_Production_Optimization", LpMaximize)

    model += lemonade + juice, "Total_Produced"

    model += 2 * lemonade + 1 * juice <= 100, "Water"
    model += 1 * lemonade <= 50, "Sugar"
    model += 1 * lemonade <= 30, "LemonJuice"
    model += 2 * juice <= 40, "FruitPuree"

    model.solve()

    print("Status:", LpStatus[model.status])
    print("Lemonade:", int(value(lemonade)))
    print("Fruit juice:", int(value(juice)))
    print("Total:", int(value(model.objective)))

    used_water = 2 * int(value(lemonade)) + 1 * int(value(juice))
    used_sugar = int(value(lemonade))
    used_lemon = int(value(lemonade))
    used_puree = 2 * int(value(juice))

    print("\nUsed resources:")
    print(f"Water: {used_water}/100")
    print(f"Sugar: {used_sugar}/50")
    print(f"Lemon juice: {used_lemon}/30")
    print(f"Fruit puree: {used_puree}/40")


if __name__ == "__main__":
    main()
