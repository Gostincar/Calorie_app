import requests
from selectorlib import Extractor
class gen() :
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

    base_url = 'https://www.google.com/search?q=random+number+generator+&sxsrf=AOaemvJzxytG7pUKDBTrFPrA_uQqJTUOfw%3A1641945744490&ei=kBreYaysHenorgSM5IfwBg&ved=0ahUKEwistNzG9Kr1AhVptIsKHQzyAW4Q4dUDCA4&uact=5&oq=random+number+generator+&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBAgjECcyBAgjECcyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBOgcIIxCwAxAnOgcIABBHELADSgQIQRgASgQIRhgAULwCWLwCYLsEaAFwAngAgAF_iAF_kgEDMC4xmAEAoAEByAEKwAEB&sclient=gws-wiz'
    yml_path = 'temp.yaml'





    def _build_url(self):
        url = self.base_url
        return url


    def _scrape(self):
        url = self._build_url()
        extracor = Extractor.from_yaml_file(self.yml_path)
        r = requests.get(url, headers=self.headers)
        full_content = r.text
        extracor.extract(full_content)
        return extracor.extract(full_content)
    def get(self):

        scraped_content=self._scrape()
        return float(scraped_content)
