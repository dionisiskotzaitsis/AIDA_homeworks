import urllib.request
import re
import ssl



if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context
    site=str(input("Give me your website\n"))
    page = urllib.request.urlopen(site).read().decode('utf-8')
    title = re.compile('<title>(.*?)</title>', re.IGNORECASE | re.DOTALL)
    results = re.findall(title, page)
    for i in results:
        print(i)
    dates1=re.compile('([\d]{4})[-/](0[1-9]|1[0-2])[-/](0[1-9]|[12][0-9]|3[01])', re.IGNORECASE | re.DOTALL)
    dates2=re.compile('(0[1-9]|[12][0-9]|3[01])[-/](0[1-9]|1[0-2])[-/]([\d]{4})', re.IGNORECASE | re.DOTALL)
    results1 = re.findall(dates1, page)
    results2 = re.findall(dates2, page)
    for i in results1:
        print("{0}-{1}-{2}".format(*i))
        #print(i)
    for i in results2:
        print("{0}-{1}-{2}".format(*i))
        #print(i)
    money=re.compile('\d+[\.\,]*\d*[\.\,]*\d*[\.\,]*\d*\s*[£€]|[£€$]\s*\d+[\.\,]*\d*[\.\,]*\d*[\.\,]*\d*', re.IGNORECASE | re.DOTALL)
    results=re.findall(money,page)
    for i in results:
        print(i)