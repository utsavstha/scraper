from bs4 import BeautifulSoup
from error_codes import NO_DATA
from share_model import ShareModel
# from 
class DataHandler:
    def parse_data(self, date, html_content)->[]:
        soup = BeautifulSoup(html_content, 'html.parser')
        table = soup.find('table', class_='table table-bordered table-striped table-hover sortable')
        if table:
            rows = table.find_all('tr')
            data = []

            # Extract headers
            # headers = [th.get_text().strip() for th in rows[0].find_all('th')]

            # Extract data from the rows
            for row in rows[1:]:
                row_data = [td.get_text().strip().replace(",", "") for td in row.find_all('td')]
                model = ShareModel(date=date,
                                        symbol=row_data[1], 
                                        ltp=row_data[2], 
                                        change=row_data[3],
                                        high=row_data[4],
                                        low=row_data[5],
                                        open=row_data[6],
                                        qty=row_data[7],
                                        turnover=row_data[8])
                data.append(model.toSQL())
            return data
        else:
            return NO_DATA