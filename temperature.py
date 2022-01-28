import requests
from selectorlib import Extractor
class Temperature :
# Screper uses an yml file to read the full xpath of a value that extracts from web site
    headers = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    base_url = 'https://www.timeanddate.com/weather/'
    yml_path = 'temp.yaml'

# replacing spaces with - simbol ( North Korea , North-Korea )
    def __init__(self,country,city) :
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")
# bulding url adding country and city to the base url
    def _build_url(self):
        url = self.base_url + self.country + "/" + self.city
        return url
# extracting the value from yml file and returning it
    def _scrape(self):
        url = self._build_url()
        extracor = Extractor.from_yaml_file(self.yml_path)
        r = requests.get(url, headers=self.headers)
        full_content = r.text
        extracor.extract(full_content)
        return extracor.extract(full_content)
# cleaing the output to get float, and using stip metod to remove all spaces around the number
    def get(self):

        scraped_content=self._scrape()
        return float(scraped_content['temp'].replace("°C", "").strip())
# if __name__ == __main__ ( if the script is executed as the main script, than executed lines below, oderwise dont.
if __name__ == "__main__":

    temperature = Temperature(country="serbia", city="belgrade")

    print(temperature.get())
