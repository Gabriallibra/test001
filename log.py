import logging

import pytest
from api.haier_api import HaierAPI
from data.api_data import HaierData


class TestHaierAPI:
    def setup_class(self):
        self.haierAPI = HaierAPI()

    def teardown_class(self):
        pass

    @pytest.mark.haier
    @pytest.mark.parametrize("haier_url", HaierData().haier_data())
    def test_haier_api(self, haier_url):
        response = self.haierAPI.haier_api(haier_url)
        assert 200 == response.status_code
        logging.info("url:{}在测试时的响应状态码为:{}".format(haier_url, response.status_code))

    @pytest.mark.leader
    @pytest.mark.parametrize("leader_url", HaierData().leader_data())
    def test_leader_api(self, leader_url):
        response = self.haierAPI.haier_api(leader_url)
        assert 200 == response.status_code
        logging.info("url:{}在测试时的响应状态码为:{}".format(leader_url, response.status_code))

    @pytest.mark.casarte
    @pytest.mark.skip(reason="数据处理有问题")
    @pytest.mark.parametrize("casarte_url", HaierData().casarte_data())
    def test_casarte_api(self, casarte_url):
        response = self.haierAPI.haier_api(casarte_url)
        assert 200 == response.status_code
        logging.info("url:{}在测试时的响应状态码为:{}".format(casarte_url, response.status_code))

    @pytest.mark.geappliances
    @pytest.mark.parametrize("geappliances_url", HaierData().geappliances_data())
    def test_geappliances_api(self, geappliances_url):
        response = self.haierAPI.haier_api(geappliances_url)
        assert 200 == response.status_code
        logging.info("url:{}在测试时的响应状态码为:{}".format(geappliances_url, response.status_code))

    @pytest.mark.haierschool
    @pytest.mark.parametrize("haierschool_url", HaierData().haierschool_data())
    def test_haierschool_api(self, haierschool_url):
        response = self.haierAPI.haier_api(haierschool_url)
        assert 200 == response.status_code
        logging.info("url:{}在测试时的响应状态码为:{}".format(haierschool_url, response.status_code))


if __name__ == '__main__':
    pytest.main()