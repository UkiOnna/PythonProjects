import bs4
import requests
import urllib3

#py -m pip install -U --user requests
cookie="is_returning=0; ssid=c75jutcj6llovq6jfq2osus63u; kid2=d841111d21c4dc746e9212605f43f778e58bb449; _ga=GA1.2.2085872712.1571924040; _gid=GA1.2.888432297.1571924040; _ym_uid=1571924040996650385; _ym_d=1571924040; _ym_isad=2; dd_user.anonymousId=eff157f0-f662-11e9-a212-73013d375c53; dd__persistedKeys=[%22user.anonymousId%22]; __gads=ID=cde7d51f2e3ffb66:T=1571924043:S=ALNI_MZFNKej0SMlfTNx3yp_ddmxZasF_g; _hjid=3beb5fb0-a736-46b2-b068-a09cd8ff7b64; old_ssid=c75jutcj6llovq6jfq2osus63u; kl_cdn_host=//astkt-kz.kcdn.online; _ym_visorc_10095472=b; _ym_visorc_49456615=b; _ym_visorc_50600908=w; gh_show=1; _gat=1; _gat_UA-20095517-9=1; __tld__=null"
host='kolesa.kz'
url_name="https://kolesa.kz/cars/"
referer="https://kolesa.kz/cars/"
links=[]
names=[]
prices=[]
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
s=requests.Session()
headers = {
        'cookie': cookie,
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': referer,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': host,
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'X-V': '8Z58MSE7PR968W0T'
    }
r=requests.get(url_name,headers=headers,timeout=40,verify=False)
soup = bs4.BeautifulSoup(r.text, 'html.parser')
for link in soup.find_all("a", {"class": "list-link ddl_product_link"}):
    links.append(link.get('href'))
    if(link.text.startswith('ещё')==False):
        print(link.text)
print(links)