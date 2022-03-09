#THIRD PARTY LIBRARIES
import requests

#CUSTOM FILES
from powertochoosetx.data import TX_ZIP_CODES
from powertochoosetx.Plans import Plan

def get_electricity_plans(
	zip_code
):
	plans = []
	if zip_code not in TX_ZIP_CODES:
		raise Exception('This is not a valid TX zip code.')
	url = f'http://api.powertochoose.org/api/PowerToChoose/plans?zip_code={zip_code}'
	r = requests.get(url)
	data = r.json()
	for plan_data in data['data']:
		new_plan = Plan(plan_data)
		plans.append(new_plan)

	return plans