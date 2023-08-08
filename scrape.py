from network import NetworkRequest
from datetime import datetime
from utils import add_days, get_number_of_days_in_month, get_number_of_months, add_months_to_date
from data_handler import DataHandler
from db_handler import DatabaseConnector
from error_codes import NO_DATA
from payload_types import MERO_LAGANI
import sys
# import logging
# logger = logging.getLogger().setLevel(logging.INFO)

#month/date/year
# start_year = sys.argv[1]
# print(sys.argv[1])

def api_call_and_parse(str_date, page):
    #Fetch html data from the website, based on provided payload
    response = request.fetch_data(str_date, MERO_LAGANI, page)
    
    if response is not NO_DATA:

        #Parses html data using beautiful soup, if table is found, return a tuple of list
        return parser.parse_data(date, response)
    else:
        print(f"Data fetch error for {str_date}")
        return (NO_DATA, False, False)

if __name__ == "__main__":
    request =  NetworkRequest()
    parser = DataHandler()
    db_connector = DatabaseConnector()
    for year in range(2014, 2024, 1):
        # Convert the string start date to Date Type
        # year = 2023
        start_date = datetime.strptime(f"01/01/{year}", '%m/%d/%Y')


        #Loops through months in year 
        # for i in range(get_number_of_months()):
        for month in range(1, 12, 1):
            share_information = []

            #Add months to current date
            date = f"{month}/01/{year}"
            date = datetime.strptime(date, '%m/%d/%Y')

            # date = datetime.strptime(start_date, '%m/%d/%Y')
            # number_of_days_in_month = 2
            number_of_days_in_month = get_number_of_days_in_month(date.year, date.month)

            for day in range(number_of_days_in_month):
                str_date = date.strftime('%m/%d/%Y')

                page_2_present = False
                page_3_present = False

                #Fetch html data from the website, based on provided payload
                parsed_data, page_2_present, page_3_present = api_call_and_parse(str_date, 1)
                if parsed_data is not NO_DATA:
                    share_information += parsed_data

                if page_2_present:
                    parsed_data, _, _ = api_call_and_parse(str_date, 2)
                    if parsed_data is not NO_DATA:
                        share_information += parsed_data

                if page_3_present:
                    parsed_data, _, _ = api_call_and_parse(str_date, 3)
                    if parsed_data is not NO_DATA:
                        share_information += parsed_data

                # response = request.fetch_data(str_date, MERO_LAGANI)
                
                # if response is not NO_DATA:

                #     #Parses html data using beautiful soup, if table is found, return a tuple of list
                #     parsed_data, page_2_present, page_3_present = parser.parse_data(date, response)
                #     if parsed_data is not NO_DATA:
                #         #Merge previously extracted information with current information
                #         share_information += parsed_data
                #     else:
                #         print(f"Parse error {str_date}")
                # else:
                #     print(f"Data fetch error for {str_date}")
                date = add_days(date, 1)

            #Insert all data to database
            db_connector.insert(share_information)
            # print(share_information)
