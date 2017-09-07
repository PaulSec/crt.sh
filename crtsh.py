"""
This is the (unofficial) Python API for crt.sh Website.
Using this code, you can retrieve subdomains

"""
import requests
from bs4 import BeautifulSoup


class crtshAPI(object):

    """cstshAPI Main Handler"""

    def __init__(self, verbose=False):
        self.verbose = verbose


    def search(self, domain):

        subdomain_list = []
        base_url = "https://crt.sh/?q=%25." + domain

        r = requests.get(url=base_url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'})

        if r.ok:
            soup = BeautifulSoup(r.content, 'html.parser')
            try:
                table = soup.findAll('table')[2]
                rows = table.find_all(['tr'])
                for row in rows:
                    cells = row.find_all('td', limit=5)
                    if cells:
                        tmp = {
                            'crtsh_id': cells[0].text,
                            'logged_at': cells[1].text,
                            'not_before': cells[2].text,
                            'domain': cells[3].text,
                            'issuer': cells[4].text
                        }
                        # name = cells[3].text
                        subdomain_list.append(tmp)
            except:
                print("error retriving information")
        return subdomain_list