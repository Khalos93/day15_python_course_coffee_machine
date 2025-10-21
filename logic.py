from util import (
    ValidUserInput,
    valid_user_options,
    are_resources_enough,
    collect_money,
    calculate_total_money_collected,
)
from datas import coffee_menu, machine_resources


def coffe_machine_manager(user_order: str, machine_money: float):

    if user_order == ValidUserInput.refill.value:

        machine_resources["water"] = 1000
        machine_resources["milk"] = 500
        machine_resources["coffee"] = 200

        print("Machine resources successfully refilled")

    elif user_order == ValidUserInput.report.value:

        print(
            f"Water: {machine_resources['water']}ml\nMilk: {machine_resources['milk']}ml\n"
            f"Coffe: {machine_resources['coffee']}gr\nMoney: £{machine_money}"
        )

    elif user_order == valid_user_options[user_order]:
        enough_resources = are_resources_enough(
            user_order, coffee_menu, machine_resources
        )
        if not enough_resources:
            print(
                "I am sorry, we don't have enough resources to complete your order."
                "\nPlease select a different option or refill me.."
            )

        else:
            while True:

                print(
                    f"To proceed with your order we need you to pay £{coffee_menu[user_order]['price']}"
                )
                money_collected = collect_money()
                total_money_value_collected = calculate_total_money_collected(
                    money_collected
                )

                if total_money_value_collected < coffee_menu[user_order]["price"]:
                    print(
                        "We are sorry, the coins insert do not reach the amount required. "
                    )
                    print(
                        f"Here is your refund amounting £{total_money_value_collected}"
                    )
                    continue

                else:
                    print(f"brrrrrrrrrrr ttccchhfff\nHere is your {user_order}, enjoy!")

                    for ingredient, amount in coffee_menu[user_order][
                        "ingredients"
                    ].items():
                        machine_resources[ingredient] -= amount

                    if total_money_value_collected == coffee_menu[user_order]["price"]:
                        machine_money += total_money_value_collected
                        return machine_money

                    else:
                        change = (
                            total_money_value_collected
                            - coffee_menu[user_order]["price"]
                        )
                        machine_money += coffee_menu[user_order]["price"]
                        print(f"Don't forget your change!\nHere is your £{change}")
                        return machine_money

