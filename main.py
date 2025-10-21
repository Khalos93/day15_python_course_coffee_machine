from util import (
    get_user_input,
    ValidUserInput,
)

from logic import coffe_machine_manager
from datas import machine_money


while True:
    user_order = get_user_input(
        "What would you like? ( espresso / capuccino / latte ):", ValidUserInput
    )
    if user_order == ValidUserInput.off.value:
        break
    else:
        machine_money = coffe_machine_manager(user_order, machine_money)



