from urllib.request import urlretrieve

data_url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
file_name = "data/raw/owid-covid-data.csv"
urlretrieve(data_url, file_name)

