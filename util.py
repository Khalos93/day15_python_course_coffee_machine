from enum import Enum


class ValidUserInput(Enum):
    espresso = "espresso"
    capuccino = "capuccino"
    latte = "latte"
    report = "report"
    off = "off"
    refill = "refill"


valid_user_options = {
    "espresso": "espresso",
    "cappuccino": "cappuccino",
    "latte": "latte",
    "report": "report",
    "off": "off",
    "refill": "refill",
}


def get_user_input(sentence: str, valid_options) -> str:
    valid_values = [valid.value for valid in valid_options]
    while True:
        user_selection = str(input(sentence)).strip().lower().replace(" ", "")
        if user_selection in valid_values:
            return user_selection
        else:
            print("Invalid input")


def are_resources_enough(order: str, menu: dict, resources: dict) -> bool:
    enough_resources = True
    for ingredient in resources:
        if resources[ingredient] < menu[order]["ingredients"][ingredient]:
            enough_resources = False
            return enough_resources

    return enough_resources


def collect_money() -> list[int]:

    while True:
        try:
            five_pence = int(input("How many £0.05 coins are you paying with?"))
            ten_pence = int(input("How many £0.10 coins are you paying with?"))
            twenty_pence = int(input("How many £0.20 coins are you paying with?"))
            fifty_pence = int(input("How many £0.50 coins are you paying with?"))
            one_pound = int(input("How many £1 coins are you paying with?"))
            two_pound = int(input("How many £2 coins are you paying with?"))

            if any(
                n < 0
                for n in [
                    five_pence,
                    ten_pence,
                    twenty_pence,
                    fifty_pence,
                    one_pound,
                    two_pound,
                ]
            ):
                print("You cannot insert a negative number of coins. Try again.\n")
                continue

        except ValueError:
            print("Invalid input.")
            continue

        # total = (
        #     five_pence * 0.05
        #     + ten_pence * 0.1
        #     + twenty_pence * 0.20
        #     + fifty_pence * 0.5
        #     + one_pound
        #     + two_pound * 2
        # )
        money_collected = [
            five_pence,
            ten_pence,
            twenty_pence,
            fifty_pence,
            one_pound,
            two_pound,
        ]

        return money_collected


def calculate_total_money_collected(coins_collected: list[int]) -> float:
    if not isinstance(coins_collected, list):
        raise TypeError("coins_collected must be a list of integers.")

    if len(coins_collected) != 6:
        raise ValueError("coins_collected must contain exactly 6 elements.")

    total = (
        coins_collected[0] * 0.05
        + coins_collected[1] * 0.1
        + coins_collected[2] * 0.2
        + coins_collected[3] * 0.5
        + coins_collected[4]
        + coins_collected[5] * 2
    )

    return total
