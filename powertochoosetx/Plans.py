import re

class Plan:
    def __init__(self, data):
        #Unique plan id
        self.id = data.get('plan_id')
        self.zip_code = data.get('zip_code')

        #Unique company id
        self.company_id = data.get('company_id')
        #Unique ID for each company from the TDU
        self.company_tdu_id = data.get('company_tdu_id')

        #The name of the company providiing the plan from the TDU
        self.company_tdu_name = data.get('company_tdu_name')

        #The name of the company providing this plan
        self.company_name = data.get('company_name')

        #The link to the company logo
        self.company_logo = data.get('company_logo')

        #The website to sign up for plan
        self.website = data.get('website')

        #The name of the plan
        self.plan_name = data.get('plan_name')
        self.plan_details = data.get('plan_details')

        #Whether the plan is fixed rate (1) or variable rate (0)
        self.plan_type = data.get('plan_type')
        self.special_terms = data.get('special_terms')

        #Whether the plan is a fixed rate or variable rate
        self.rate_type = data.get('rate_type')

        #The number of months the plan lasts for
        self.term_value = data.get('term_value')
        self.price_kwh500 = data.get('price_kwh500')
        self.price_kwh1000 = data.get('price_kwh1000')
        self.price_kwh2000 = data.get('price_kwh2000')
        self.detail_kwh500 = data.get('detail_kwh500')
        self.detail_kwh1000 = data.get('detail_kwh1000')
        self.detail_kwh2000 = data.get('detail_kwh2000')

        #Whether the plan is a prepaid plan or not
        self.prepaid = data.get('prepaid')
        self.time_of_use = data.get('timeofuse')
        self.pricing_details = data.get('pricing_details')
        self.fact_sheet = data.get('fact_sheet')
        self.terms_of_service = data.get('terms_of_service')
        self.go_to_plan = data.get('go_to_plan')
        self.promotions = data.get('promotions')
        self.prepaid_url = data.get('prepaid_url')
        self.yrac_url = data.get('yrac_url')
        self.enroll_phone = data.get('enroll_phone')
        self.renewable_energy_id = data.get('renewable_energy_id')
        self.renewable_energy_description = data.get('renewable_energy_description')
        self.rating_total = data.get('rating_total')
        self.rating_count = data.get('rating_count')
        self.jdp_rating = data.get('jdp_rating')
        self.jdp_rating_year = data.get('jdp_rating_year')
        self.simple_plan = data.get('simple_plan')
        self.new_customer = data.get('new_customer')
        self.minimum_usage = data.get('minimum_usage')

    def get_average_price(self, kwh = "1000"):
        '''
        This function takes in a KwH usage and returns the averager price per Kw
        '''
        if kwh == "500":
            return self.price_kwh500
        elif kwh == "2000":
            return self.price_kwh2000
        return self.price_kwh1000

    def get_percent_renewable(self):
        '''
        This function returns the percent of electricity produced by renewable energy sources.
        '''
        return self.renewable_energy_id / 100.0

    def get_cancellation_fee(self):
        '''
        This function retrieves the cancellation fee and whether it is a monthly fee or one-time fee
        '''
        if 'Cancellation Fee:' in self.pricing_details:
            price_list = re.findall("\$[0-9]+\.?[0-9]*", self.pricing_details)
            if len(price_list) == 0:
                return {
                    'cancellation_fee' : None,
                    'type' : 'unknown'
                }
            price = price_list[0].replace('$','')
            if 'month' in self.pricing_details:
                return {
                    'cancellation_fee' : float(price),
                    'type' : 'per_month'
                }
            return {
                'cancellation_fee' : float(price),
                'type' : 'one_time'
            }
        return {
            'cancellation_fee' : None,
            'type' : 'unknown'
        }






