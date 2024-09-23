# Sonnen-s-Task
# Energy Management Task

## Overview

This project implements a function to determine the appropriate action based on photovoltaic (PV) production and household consumption. The function evaluates different scenarios to decide whether to charge with surplus energy, discharge, or take no action.

## Functionality

The main function, `choose_action`, takes two parameters:
- `pv_production`: The amount of energy produced by the solar panels (in kWh).
- `house_consumption`: The amount of energy consumed by the household (in kWh).

### Possible Actions
- **Charge with Surplus**: If PV production exceeds household consumption.
- **Storge will supply house with power**: If household consumption exceeds PV production.
- **Nothing**: If both values are equal.

## Usage

To use the function, simply call it with the desired parameters. Here’s an example:

```python
from Sonnen_task.src.Dut import choose_action

result = choose_action(10, 5)
print(result)  # Output: Charge with Surplus
