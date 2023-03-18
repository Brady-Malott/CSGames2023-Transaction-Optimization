import httpx
import datetime
import pandas as pd

def downloadStockCSV(symbos: list[str],
                     startDate: datetime.datetime,
                     endDate: datetime.datetime
                     ) -> list[pd.DataFrame]:
    url = 'https://query1.finance.yahoo.com/v7/finance/download/'
    frames = []
    #AAL?period1=1672531200&period2=1675209600&interval=1d&events=history&includeAdjustedClose=true
    for symbol in symbos:
        # construct download URL
        downloadSymbolURL = url + symbol

        # add start period
        downloadSymbolURL += f"?period1={startDate.strftime('%s')}"

        # add end period
        downloadSymbolURL += f"&period2={endDate.strftime('%s')}"

        downloadSymbolURL += "&interval=1d&events=history&includeAdjustedClose=true"

        print(downloadSymbolURL)

        # timeout of 5 seconds
        # we dont capture it because WE WANT IT TO FAIL IF CANNOT DOWNLOAD
        r = httpx.get(downloadSymbolURL, timeout=5)

        fName = f"{symbol}_history.csv"

        # quick and dirty open, write, close
        f = open(fName, 'wb')
        f.write(r.content)
        f.close()

        frames.append(pd.read_csv(fName))

    return frames

symbols = ["AAL", "DAL", "UAL", "LUV", "HA"]
start_date = datetime.datetime(2023, 1, 1)
end_date = datetime.datetime(2023, 2, 1)

stocks = downloadStockCSV(symbols, start_date, end_date)

print(stocks)
#requests.get('https://api.csgames2023.sandbox.croesusfin.cloud/CroesusValidation')

