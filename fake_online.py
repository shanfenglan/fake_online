import re
import time
import requests

def heartbeat():
    url = "http://192.168.186.133:333/activity"
    headers = {
            'Cookie': 'IgyzGuIX0Jra5Ht45ZLYKyXWBnxfkNI3m6BOvExEPdWCuAv8fnY6HXKTygBOVdE34sDYusoDIjzHr/QR32mKsoVPb5NFMCHAtC7FLQUdSsZdufXjsd2dSqkGDcaZkcQYD1BssyjGZHTy42lT8oDpga3y1z5FMGRjobeksgaMX7M=',
            'Host': '192.168.186.133:333',
            'Accept': '*/*',
            'Connection': 'Keep-Alive',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727)'
        }
    resp = requests.get(url=url,headers=headers)
    text = resp.content.hex()
    return text

x = True
while x:
    text = heartbeat()
    lengs = len(text)
    # print(lengs, "    ", text)

    if '2f4320' in text and '000041' in text:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

        commeds = re.findall(r'2f4320(.*?)000041', text)
        for comm in commeds:
            commed = bytes.fromhex(comm).decode('utf-8')
            print(commed)
    time.sleep(5)
