# -*- coding: UTF-8 -*-
from urllib import request
from lxml import etree

#最多72页
url = "https://www.javbus.com"
user_agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
referer="https://googleads.g.doubleclick.net/pagead/ads?client=ca-pub-7443704194229694&output=html&h=90&slotname=9826878184&adk=4171920228&adf=478900115&w=728&lmt=1521414700&loeid=10583696%2C38893312&format=728x90&url=https%3A%2F%2Fwww.qiushibaike.com%2F&flash=28.0.0&wgl=1&adsid=NT&dt=1521414700665&bpp=18&bdt=627&fdt=23&idt=131&shv=r20180312&cbv=r20170110&saldr=aa&correlator=1269135908771&frm=20&ga_vid=1105908403.1521414440&ga_sid=1521414701&ga_hid=1967102628&ga_fc=0&pv=2&iag=3&icsg=2&nhd=1&dssz=2&mdo=0&mso=0&u_tz=480&u_his=1&u_java=0&u_h=864&u_w=1536&u_ah=824&u_aw=1536&u_cd=24&u_nplug=5&u_nmime=7&adx=396&ady=13229&biw=1519&bih=735&abxe=1&scr_x=0&scr_y=0&eid=10593696%2C21060831%2C38893302%2C191880502%2C20040069&oid=3&ref=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DpQcHYknSFy4K-bLiAJOt8bDY3z8NTSt5_5YdxMHOlEoCwUBixZHGIStJP-fd8b1H%26wd%3D%26eqid%3Db5d16dab00021765000000025aaef22a&rx=0&eae=0&fc=528&brdim=0%2C0%2C0%2C0%2C1536%2C0%2C1536%2C824%2C1536%2C735&vis=1&rsz=%7C%7CeEbr%7C&abl=CS&ppjl=f&pfx=0&fu=24&bc=1&ifi=1&xpc=IswKClvwIF&p=https%3A//www.qiushibaike.com&dtd=252"
headers={'user-agent':user_agent,"referer":referer}
content=[]
list1 = []
for i in range(2, 3):
    temp = request.Request(url + str(i), None, headers=headers)
    a = request.urlopen(temp)
    html = a.read().decode()
    selector = etree.HTML(html)
    content.extend(selector.xpath('//*[@id="waterfall"]/div/a/@href'))
    print(content)