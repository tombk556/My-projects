import pandas_datareader as web
import datetime as dt
import pandas as pd

class Extraction:
    end = dt.datetime.now()
    data = []
    
    def __init__(self, ticker: str, name: str, year: int, month: int, day: int):
        
        # Run a validation before instanciate the attributes
        
        assert year >= 0 and year <= Extraction.end.year, f"Year {year} is not greater than or equal to zero!" 
        # Checks if the year is between the past and now
        
        assert month >= 1 and month <= 12, f"Month {month} is not in the correct time-frame!"
        # Checks if the month is between januanry and december and not in the future
        
        assert day >= 1 and day <=31, f"Day {day} is not in the correct time-frame!"
        # Checks if the day is between the first or the 31th of the month and not in the future
        
        #Assing to self object
        
        self.ticker = ticker
        self.name = name
        self.year = year
        self.month = month
        self.day = day
        
        # Action to execute and store all the data into a list called data
        Extraction.data.append(self)

    def extract_data(self):
        stock_data = web.DataReader(self.ticker, 'yahoo', dt.datetime(self.year, self.month, self.day)).sort_values(['Date'], ascending= False )
        stock_data = pd.DataFrame(stock_data)
        return stock_data
    


