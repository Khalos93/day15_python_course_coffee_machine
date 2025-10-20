from util import (
    get_user_input,
    ValidUserInput,
    valid_user_options,
    are_resources_enough,
    collect_money,
    calculate_total_money_collected,
)
from datas import coffee_menu, machine_resources, machine_money


while True:
    user_order = get_user_input(
        "What would you like? ( espresso / capuccino / latte ):", ValidUserInput
    )

    if user_order == ValidUserInput.off.value:
        break

    elif user_order == ValidUserInput.refill.value:

        machine_resources["water"] = 1000
        machine_resources["milk"] = 500
        machine_resources["coffee"] = 200

        print("Machine resources successfully refilled")

    elif user_order == ValidUserInput.report.value:
        money_total = (
            machine_money["0.05"] * 0.05
            + machine_money["0.10"] * 0.1
            + machine_money["0.20"] * 0.20
            + machine_money["0.50"] * 0.5
            + machine_money["1.00"]
            + machine_money["2.00"] * 2
        )
        print(
            f"Water: {machine_resources['water']}ml\nMilk: {machine_resources['milk']}ml\n"
            f"Coffe: {machine_resources['coffee']}gr\nMoney: £{money_total}"
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
            print(
                f"To proceed with your order we need you to pay £{coffee_menu[user_order]['price']}"
            )
            money_collected = collect_money()
            total_money_value_collocted = calculate_total_money_collected(
                money_collected
            )

            if total_money_value_collocted < coffee_menu[user_order]["price"]:
                print(
                    "We are sorry, the coins insert do not reach the amount required. "
                )
                print(f"Here your refund amounting £{money_collected}")

            else:
                print(f"brrrrrrrrrrr ttccchhfff\nHere your {user_order}, enjoy!")

                # if total_money_value_collocted > coffee_menu[user_order]['price']:
                #     change = total_money_value_collocted - coffee_menu[user_order]['price']
                #
                #     print(f"Don't forget your change!\nHere is your £{change}")
                #     money_collected -= change
                #     machine_money += money_collected
