import requests

symbols = ["AAL", "DAL", "UAL", "LUV", "HA"]
start_date = datetime.datetime(2023, 1, 1)
end_date = datetime.datetime(2023, 2, 1)

requests.get('https://api.csgames2023.sandbox.croesusfin.cloud/CroesusValidation')


