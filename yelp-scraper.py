import requests
from lxml import html
import urllib.parse
import pandas as pd


data = []
def requesting(n):
    url = f"https://www.yelp.com/search?find_desc=Indian+restaurant&find_loc=San+Francisco%2C+CA&start={n}"
    token = "01ec000f2e124ec49386bcb1b6f0de1952c6dedd86a"
    targetUrl = urllib.parse.quote(url)
    customHeaders = "true"
    url = "http://api.scrape.do?token={}&url={}&customHeaders={}".format(token, targetUrl, customHeaders)
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en-IN;q=0.9,en;q=0.8,hi;q=0.7',
        'cache-control': 'max-age=0',
        'cookie': 'hl=en_US; wdi=2|9CB60CE4D03DDBC6|0x1.987a903d2622cp+30|b47f94a19925fffa; _ga=GA1.2.9CB60CE4D03DDBC6; _gcl_au=1.1.1801599402.1713284135; _pxvid=8e64d799-fc0c-11ee-8c19-4de392cac3c3; _scid=d2eadbfa-144c-4e7e-8bf7-25383289a5e9; __adroll_fpc=e76d7fb9e1b77b01822afe1df7298afa-1713284157008; _fbp=fb.1.1713284157508.901698835; _px3=b871325b3ee5fea9ac395795dc1436b74d364ca9af8946c301901f6ad16b252f:npigzVkT884l53AL3Fx5TkVNa0b1xBNWrx/5vCs4SMqxhA4w4hBQw+CCrGp0DZwA1KIH7wRpZmM0u6s7+Vkx4g==:1000:90NOftAgfjZlpFKAI+RXIMjQQhDFZs8mKHIUXPMibzxeGnz9xR7MNnuoAOyd65vQj91djRpj85//NoX0vzSSS2pitxkV2hLgQW4AQYYVIk08xMOpITMA8F5yUq+tCRr84knsUFD1AQOqDQPbwCMMcMUja/JXkt25n2tl0cWMJS+m8GqttBPJU+Rfdt9rRlBFJq4eawAPHW7Q7VhrKar+SE/j97QKK0JZ0F3oqjk2yFA=; g_state={"i_p":1716729822070,"i_l":3}; ndp_session_id=1310027e-dbfb-4d3d-8c1c-bfa3e0605716; _sctr=1%7C1716057000000; bse=53e8b494ceb64b05bb29357167ee8e53; spses.d161=*; _gid=GA1.2.1733293721.1716632186; rsp=%7B%22date%22%3A%222024-05-25%22%2C%22time%22%3A%221900%22%2C%22partySize%22%3A2%7D; recentlocations=; xcj=1|HEx7L-O1nAzUgV3mFnzp8ef-kecUB0oW-dostxhnwTA; _scid_r=d2eadbfa-144c-4e7e-8bf7-25383289a5e9; _uetsid=de3042801a7f11ef9139ffdb8a2c3aee; _uetvid=4636506090e111eea1e49d140947b0e4; _ga_K9Z2ZEVC8C=GS1.2.1716632185.13.1.1716632240.0.0.0; __ar_v4=BHPKS4B4ONEJJMGH4QCJZR%3A20240518%3A7%7CQB5JPFIKRZDSBOZSULG4YB%3A20240518%3A7%7C7YX6SJQ4RZAMPB6LZ7CHFF%3A20240518%3A7; bsi=1%7C6153db7e-a72c-4c57-bc8b-1d51f0c09a32%7C1716632282824%7C1716632179891; location=%7B%22country%22%3A+%22US%22%2C+%22state%22%3A+%22CA%22%2C+%22accuracy%22%3A+4%2C+%22zip%22%3A+%22%22%2C+%22latitude%22%3A+37.775123%2C+%22address1%22%3A+%22%22%2C+%22address2%22%3A+%22%22%2C+%22min_longitude%22%3A+-122.51781463623047%2C+%22city%22%3A+%22San+Francisco%22%2C+%22place_id%22%3A+%221237%22%2C+%22min_latitude%22%3A+37.706368356809776%2C+%22longitude%22%3A+-122.41932%2C+%22max_longitude%22%3A+-122.3550796508789%2C+%22unformatted%22%3A+%22San+Francisco%2C+CA%22%2C+%22provenance%22%3A+%22YELP_GEOCODING_ENGINE%22%2C+%22parent_id%22%3A+371%2C+%22display%22%3A+%22San+Francisco%2C+CA%22%2C+%22max_latitude%22%3A+37.81602226140252%2C+%22county%22%3A+%22San+Francisco+County%22%2C+%22location_type%22%3A+%22locality%22%2C+%22address3%22%3A+%22%22%2C+%22borough%22%3A+%22%22%2C+%22isGoogleHood%22%3A+false%2C+%22language%22%3A+null%2C+%22neighborhood%22%3A+%22%22%2C+%22polygons%22%3A+null%2C+%22usingDefaultZip%22%3A+false%2C+%22confident%22%3A+null%7D; spid.d161=5fca2f73-4236-4c6a-a830-3fb8c7856ecd.1713284115.24.1716632666.1716545951.3168ca28-ff98-4fc3-aa76-2eba623d1fe1.2dd914dd-556c-412c-9afe-056ec72f0b01.89f3b80c-5f56-41e5-93fe-ce9640d8dc82.1716632185710.22; OptanonConsent=isGpcEnabled=0&datestamp=Sat+May+25+2024+15%3A54%3A30+GMT%2B0530+(India+Standard+Time)&version=202403.1.0&browserGpcFlag=0&isIABGlobal=false&identifierType=Cookie+Unique+Id&hosts=&consentId=84bf6aa7-95de-43c1-a37a-3c741f6d6473&interactionCount=1&isAnonUser=1&landingPath=https%3A%2F%2Fwww.yelp.com%2Fsearch%3Ffind_desc%3DIndian+restaurant+%26find_loc%3DSan+Francisco%252C+CA&groups=BG122%3A1%2CC0003%3A1%2CC0002%3A1%2CC0001%3A1%2CC0004%3A1; bse=dadf9514571b4723841cfef4efab975d; bsi=1%7Cb5355f61-da2a-4af2-8894-62b6de1caae5%7C1716632886225%7C1716632886225; hl=en_US; location=%7B%22max_longitude%22%3A+-122.3550796508789%2C+%22provenance%22%3A+%22YELP_GEOCODING_ENGINE%22%2C+%22country%22%3A+%22US%22%2C+%22address1%22%3A+%22%22%2C+%22state%22%3A+%22CA%22%2C+%22latitude%22%3A+37.775123%2C+%22city%22%3A+%22San+Francisco%22%2C+%22location_type%22%3A+%22locality%22%2C+%22max_latitude%22%3A+37.81602226140252%2C+%22unformatted%22%3A+%22San+Francisco%2C+CA%22%2C+%22accuracy%22%3A+4%2C+%22address2%22%3A+%22%22%2C+%22display%22%3A+%22San+Francisco%2C+CA%22%2C+%22parent_id%22%3A+371%2C+%22zip%22%3A+%22%22%2C+%22min_latitude%22%3A+37.706368356809776%2C+%22place_id%22%3A+%221237%22%2C+%22min_longitude%22%3A+-122.51781463623047%2C+%22longitude%22%3A+-122.41932%2C+%22county%22%3A+%22San+Francisco+County%22%2C+%22address3%22%3A+%22%22%2C+%22borough%22%3A+%22%22%2C+%22isGoogleHood%22%3A+false%2C+%22language%22%3A+null%2C+%22neighborhood%22%3A+%22%22%2C+%22polygons%22%3A+null%2C+%22usingDefaultZip%22%3A+false%2C+%22confident%22%3A+null%7D; recentlocations=; wdi=2|40CE9C6BC01D5B1E|0x1.9946f4d8e6c7ap+30|d740db20a25d0c9b',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    response = requests.request("GET", url, headers=headers)
    return response



def card_data(links):
    print('started')
    for i in links:
        url = f"https://www.yelp.com{i}"
        token = "01ec000f2e124ec49386bcb1b6f0de1952c6dedd86a"
        payload = {}
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en-IN;q=0.9,en;q=0.8,hi;q=0.7',
            'cache-control': 'max-age=0',
            'cookie': 'hl=en_US; wdi=2|9CB60CE4D03DDBC6|0x1.987a903d2622cp+30|b47f94a19925fffa; _ga=GA1.2.9CB60CE4D03DDBC6; _gcl_au=1.1.1801599402.1713284135; _pxvid=8e64d799-fc0c-11ee-8c19-4de392cac3c3; _scid=d2eadbfa-144c-4e7e-8bf7-25383289a5e9; __adroll_fpc=e76d7fb9e1b77b01822afe1df7298afa-1713284157008; _fbp=fb.1.1713284157508.901698835; _px3=b871325b3ee5fea9ac395795dc1436b74d364ca9af8946c301901f6ad16b252f:npigzVkT884l53AL3Fx5TkVNa0b1xBNWrx/5vCs4SMqxhA4w4hBQw+CCrGp0DZwA1KIH7wRpZmM0u6s7+Vkx4g==:1000:90NOftAgfjZlpFKAI+RXIMjQQhDFZs8mKHIUXPMibzxeGnz9xR7MNnuoAOyd65vQj91djRpj85//NoX0vzSSS2pitxkV2hLgQW4AQYYVIk08xMOpITMA8F5yUq+tCRr84knsUFD1AQOqDQPbwCMMcMUja/JXkt25n2tl0cWMJS+m8GqttBPJU+Rfdt9rRlBFJq4eawAPHW7Q7VhrKar+SE/j97QKK0JZ0F3oqjk2yFA=; g_state={"i_p":1716729822070,"i_l":3}; ndp_session_id=1310027e-dbfb-4d3d-8c1c-bfa3e0605716; _sctr=1%7C1716057000000; bse=53e8b494ceb64b05bb29357167ee8e53; spses.d161=*; _gid=GA1.2.1733293721.1716632186; rsp=%7B%22date%22%3A%222024-05-25%22%2C%22time%22%3A%221900%22%2C%22partySize%22%3A2%7D; recentlocations=; xcj=1|HEx7L-O1nAzUgV3mFnzp8ef-kecUB0oW-dostxhnwTA; _scid_r=d2eadbfa-144c-4e7e-8bf7-25383289a5e9; _uetsid=de3042801a7f11ef9139ffdb8a2c3aee; _uetvid=4636506090e111eea1e49d140947b0e4; _ga_K9Z2ZEVC8C=GS1.2.1716632185.13.1.1716632240.0.0.0; __ar_v4=BHPKS4B4ONEJJMGH4QCJZR%3A20240518%3A7%7CQB5JPFIKRZDSBOZSULG4YB%3A20240518%3A7%7C7YX6SJQ4RZAMPB6LZ7CHFF%3A20240518%3A7; bsi=1%7C6153db7e-a72c-4c57-bc8b-1d51f0c09a32%7C1716632282824%7C1716632179891; location=%7B%22country%22%3A+%22US%22%2C+%22state%22%3A+%22CA%22%2C+%22accuracy%22%3A+4%2C+%22zip%22%3A+%22%22%2C+%22latitude%22%3A+37.775123%2C+%22address1%22%3A+%22%22%2C+%22address2%22%3A+%22%22%2C+%22min_longitude%22%3A+-122.51781463623047%2C+%22city%22%3A+%22San+Francisco%22%2C+%22place_id%22%3A+%221237%22%2C+%22min_latitude%22%3A+37.706368356809776%2C+%22longitude%22%3A+-122.41932%2C+%22max_longitude%22%3A+-122.3550796508789%2C+%22unformatted%22%3A+%22San+Francisco%2C+CA%22%2C+%22provenance%22%3A+%22YELP_GEOCODING_ENGINE%22%2C+%22parent_id%22%3A+371%2C+%22display%22%3A+%22San+Francisco%2C+CA%22%2C+%22max_latitude%22%3A+37.81602226140252%2C+%22county%22%3A+%22San+Francisco+County%22%2C+%22location_type%22%3A+%22locality%22%2C+%22address3%22%3A+%22%22%2C+%22borough%22%3A+%22%22%2C+%22isGoogleHood%22%3A+false%2C+%22language%22%3A+null%2C+%22neighborhood%22%3A+%22%22%2C+%22polygons%22%3A+null%2C+%22usingDefaultZip%22%3A+false%2C+%22confident%22%3A+null%7D; spid.d161=5fca2f73-4236-4c6a-a830-3fb8c7856ecd.1713284115.24.1716632666.1716545951.3168ca28-ff98-4fc3-aa76-2eba623d1fe1.2dd914dd-556c-412c-9afe-056ec72f0b01.89f3b80c-5f56-41e5-93fe-ce9640d8dc82.1716632185710.22; OptanonConsent=isGpcEnabled=0&datestamp=Sat+May+25+2024+15%3A54%3A30+GMT%2B0530+(India+Standard+Time)&version=202403.1.0&browserGpcFlag=0&isIABGlobal=false&identifierType=Cookie+Unique+Id&hosts=&consentId=84bf6aa7-95de-43c1-a37a-3c741f6d6473&interactionCount=1&isAnonUser=1&landingPath=https%3A%2F%2Fwww.yelp.com%2Fsearch%3Ffind_desc%3DIndian+restaurant+%26find_loc%3DSan+Francisco%252C+CA&groups=BG122%3A1%2CC0003%3A1%2CC0002%3A1%2CC0001%3A1%2CC0004%3A1; bse=dadf9514571b4723841cfef4efab975d; bsi=1%7Cb5355f61-da2a-4af2-8894-62b6de1caae5%7C1716632886225%7C1716632886225; hl=en_US; location=%7B%22max_longitude%22%3A+-122.3550796508789%2C+%22provenance%22%3A+%22YELP_GEOCODING_ENGINE%22%2C+%22country%22%3A+%22US%22%2C+%22address1%22%3A+%22%22%2C+%22state%22%3A+%22CA%22%2C+%22latitude%22%3A+37.775123%2C+%22city%22%3A+%22San+Francisco%22%2C+%22location_type%22%3A+%22locality%22%2C+%22max_latitude%22%3A+37.81602226140252%2C+%22unformatted%22%3A+%22San+Francisco%2C+CA%22%2C+%22accuracy%22%3A+4%2C+%22address2%22%3A+%22%22%2C+%22display%22%3A+%22San+Francisco%2C+CA%22%2C+%22parent_id%22%3A+371%2C+%22zip%22%3A+%22%22%2C+%22min_latitude%22%3A+37.706368356809776%2C+%22place_id%22%3A+%221237%22%2C+%22min_longitude%22%3A+-122.51781463623047%2C+%22longitude%22%3A+-122.41932%2C+%22county%22%3A+%22San+Francisco+County%22%2C+%22address3%22%3A+%22%22%2C+%22borough%22%3A+%22%22%2C+%22isGoogleHood%22%3A+false%2C+%22language%22%3A+null%2C+%22neighborhood%22%3A+%22%22%2C+%22polygons%22%3A+null%2C+%22usingDefaultZip%22%3A+false%2C+%22confident%22%3A+null%7D; recentlocations=; wdi=2|40CE9C6BC01D5B1E|0x1.9946f4d8e6c7ap+30|d740db20a25d0c9b',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
        }
        targetUrl = urllib.parse.quote(url)
        customHeaders = "true"
        url = "http://api.scrape.do?token={}&url={}&customHeaders={}".format(token, targetUrl, customHeaders)
        response = requests.request("GET", url, headers=headers, data=payload)

        hh = html.fromstring(response.text)
        try:
            title = hh.xpath('//div[@class="headingLight__09f24__N86u1 y-css-1j7tr06"]/h1/text()')[0]
        except:
            title = ""
        try:
            rating = hh.xpath('//div[@class="arrange-unit__09f24__rqHTg arrange-unit-fill__09f24__CUubG y-css-lbeyaq"]//span[@class=" y-css-kw85nd"]/text()[1]')[0]
        except:
            rating = ""
        try:
            address = hh.xpath('//section[@class="y-css-7hi8nk"]//p[@class=" y-css-dg8xxd"]/text()')[0]
        except:
            address = ""
        try:
            website = hh.xpath('(//section[@class="y-css-7hi8nk"]//p[@class=" y-css-1o34y7f"]/a/text())[1]')[0]
        except:
            website = ""
        try:
            phone = hh.xpath('(//section[@class="y-css-7hi8nk"]//p[@class=" y-css-1o34y7f"])[2]/text()')[0]
        except:
            phone = ""

        print(title,rating,address,website,phone)
        temp = {
          'Title':title,
          'Rating':rating,
          'Address': address,
          'Website':website,
          'Phone':phone
        }
        data.append(temp)



def main():
    t = 0
    for i in range(10):
        response = requesting(t)
        hh = html.fromstring(response.text)
        all_links = hh.xpath('//div[@class=" y-css-1he6azc"]//*[@class="y-css-hcgwj4"]/a/@href')
        card_data(all_links)
        t += 10
    pf = pd.DataFrame(data)
    pf.to_excel('yelp_data.xlsx')




if __name__ == "__main__":
    main()

