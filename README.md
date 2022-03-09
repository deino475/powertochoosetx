# powertochoosetx

powertochoosetx is an unofficial Python library for interacting with the Power to Choose API.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install powertochoosetx.

```bash
pip install powertochoosetx
```

## Usage

```python
from powertochoosetx import get_electricity_plans
plans = get_electricity_plans("77002")
for plan in plans:
	print(f'{plan.plan_name}: {plan.get_average_price()} kwh')
	print(f'Percent renewable electricity: {plan.get_percent_renewable()}')
	print(f'Cancellation fee: {plan.get_cancellation_fee()}')

```

## License
[GNU GPL-V2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt)