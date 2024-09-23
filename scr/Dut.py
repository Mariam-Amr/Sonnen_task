
This file contains the code logic and the DUT class
"""
class DUT:
    def __init__(self):
        self.state = {}


    def set(self, key : str, value: int) -> bool:
        if value < 0:
            raise ValueError("Value cannot be negative.")
        self.state[key] = value
        return True


    def get(self, key: str) -> int:
        return self.state.get(key, 0)


def choose_action(pv_production: int , house_consumption: int) -> str:
    if pv_production > house_consumption :
        return "Charge with Surplus"
    elif pv_production < house_consumption:
        return "Storge will supply house with power"
    else:
        return "Nothing"
      
