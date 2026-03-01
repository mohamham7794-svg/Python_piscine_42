# EXERCISE 5: ft_count_harvest_recursive.py
# by : mohhammo


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def count_helper(current, max_days):
        if current <= max_days:
            print(f"Day {current}")
            count_helper(current + 1, max_days)
    count_helper(1, days)
    print("Harvest time!")
