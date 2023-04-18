import requests


class HaierAPI:
    def haier_api(self, haier_url):
        return requests.get(haier_url)

    def leader_api(self, leader_url):
        return requests.get(leader_url)

    def casarte_api(self, casarte_url):
        return requests.get(casarte_url)

    def geappliances_api(self,geappliances_url):
        return requests.get(geappliances_url)

    def haierschool_api(self, haierschool_url):
        return requests.get(haierschool_url)
