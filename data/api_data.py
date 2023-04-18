import logging

import requests
import utils


class HaierData:
    def __init__(self):
        self.haier_url = "https://www.haier.com/robots.txt"
        self.learder_url = "https://www.leader.com.cn/sitemap.xml"
        self.casarte_url = "https://www.casarte.com/sitemap.xml"
        self.geappliances_url = "http://www.geappliances.cn/sitemap/sitemap.xml"
        self.haierschool_url = "https://www.haierschool.cn/sitemap/sitemap.xml"

    def haier_data(self):
        data1 = utils.read_haier1(self.haier_url)
        data2 = utils.read_xml1(data1)
        haier_data = utils.assemble_data(data2)
        return haier_data

    def leader_data(self):
        data1 = utils.read_xml(self.learder_url)
        leader_data = utils.assemble_data(data1)
        return leader_data

    def casarte_data(self):
        data1 = utils.read_xml(self.casarte_url)
        casarte_data = utils.assemble_data(data1)
        return casarte_data

    def geappliances_data(self):
        data1 = utils.read_xml(self.geappliances_url)
        geappliances_data = utils.assemble_data(data1)
        return geappliances_data

    def haierschool_data(self):
        data1 = utils.read_xml(self.learder_url)
        haierschool_data = utils.assemble_data(data1)
        return haierschool_data


if __name__ == '__main__':
    aa = HaierData()
    print(aa.haier_data())

