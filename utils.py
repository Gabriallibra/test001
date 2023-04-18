from bs4 import BeautifulSoup
import requests


# 读取haier第一层数据
def read_haier1(haier_original_url):
    response1 = requests.get(haier_original_url)

    # 分离Sitemap
    url_list = response1.text.split("Sitemap: ")
    # print(url_list)  # 分离Sitemap的数据
    url_list1 = url_list[1:]

    # 去掉回车符,换行符
    new_list = []
    for i in url_list1:
        xml_url_list = i.split("\r\n")
        if len(xml_url_list) == 2:
            new_list.extend(xml_url_list[:-1])
        else:
            new_list.extend(xml_url_list[:-2])

    return new_list


# 读取<loc>内包含的xml数据,并组成数组,haier的第二层数据
def read_xml(xml_url):
    url_list2 = []
    url_text = requests.get(xml_url).text
    soup = BeautifulSoup(url_text, "xml")
    loc_list = soup.find_all("loc")
    for i in loc_list:
        url_list2.append(i.string)
    return url_list2


# 循环遍历第一层url,并获得第二层数据
def read_xml1(list1):
    url_data2 = []
    for i in list1:
        data2 = read_xml(i)
        if len(data2) != 0:
            for j in data2:
                url_data2.append(j)
    return url_data2


# 循环第二层数据,并获得第三层数据
def assemble_data(list2):
    url_data3 = []
    for i in list2:
        # 第二层数据包含xml文件,需要进一步解析
        if (i[-4:] == ".xml"):
            data3 = read_xml(i)
            # 第二层数据有可以直接访问的,直接组装数据
            for j in data3:
                url_data3.append(j)
        else:
            url_data3.append(i)
    return url_data3


if __name__ == '__main__':
    print(read_haier1("https://www.haier.com/robots.txt"))
    # print(read_xml("https://www.haier.com/cn/sitemap.xml"))
