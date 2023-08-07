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
start_year = sys.argv[1]
# print(sys.argv[1])


if __name__ == "__main__":
    request =  NetworkRequest()
    parser = DataHandler()
    db_connector = DatabaseConnector()
    #Convert the string start date to Date Type
    start_date = datetime.strptime(f"01/01/{start_year}", '%m/%d/%Y')

    share_information = []

    #Loops through months in year 
    # for i in range(get_number_of_months()):
    for month in range(1, 13, 1):

        #Add months to current date
        date = f"{month}/01/{start_year}"
        date = datetime.strptime(date, '%m/%d/%Y')

        # date = datetime.strptime(start_date, '%m/%d/%Y')
        # number_of_days_in_month = 2
        number_of_days_in_month = get_number_of_days_in_month(date.year, date.month)

        for day in range(number_of_days_in_month):
            str_date = date.strftime('%m/%d/%Y')

            #Fetch html data from the website, based on provided payload
            response = request.fetch_data(str_date, MERO_LAGANI)
            if response is not NO_DATA:

                #Parses html data using beautiful soup, if table is found, return a tuple of list
                parsed_data = parser.parse_data(date, response)
                if parsed_data is not NO_DATA:
                    #Merge previously extracted information with current information
                    share_information += parsed_data
                else:
                    print(f"Parse error {str_date}")
            else:
                print(f"Data fetch error for {str_date}")
            date = add_days(date, 1)

        #Insert all data to database
        db_connector.insert(share_information)

            # record_for_month.append(ShareModel(date, ))
    # print(dt)
    # # datetime.datetime(2010, 2, 15, 0, 0)
    # print(dt.strftime('%d/%m/%Y'))