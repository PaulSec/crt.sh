"""
This is the (unofficial) Python API for crt.sh website.

Using this code, you can retrieve subdomains.
"""

from bs4 import BeautifulSoup
import requests


class crtshAPI(object):
    """crtshAPI main handler."""

    def search(self, domain, wildcard=True):
        """
        Search crt.sh for the given domain.

        domain -- Domain to search for
        wildcard -- Whether or not to prepend a wildcard to the domain
                    (default: True)

        Return a list of objects, like so:

        {
            "crtsh_id": "201202462",
            "pem_url": "https://crt.sh/?d=201202462",
            "logged_at": "2017-08-29",
            "not_before": "2017-08-22",
            "domain": "lert.uber.com",
            "issuer": "C=US, O=DigiCert Inc, CN=DigiCert SHA2 Secure Server CA"
        }
        """
        subdomain_list = []

        base_url = "https://crt.sh/?q="
        if wildcard:
            base_url += "%25."
        base_url += domain

        ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 ' + \
            'Firefox/40.1'
        r = requests.get(url=base_url, headers={'User-Agent': ua})

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
                            'pem_url': 'https://crt.sh/?d=' + cells[0].text,
                            'logged_at': cells[1].text,
                            'not_before': cells[2].text,
                        }

                        if wildcard:
                            tmp['domain'] = cells[3].text
                            tmp['issuer'] = cells[4].text
                        else:
                            tmp['domain'] = domain,
                            tmp['issuer'] = cells[3].text

                        subdomain_list.append(tmp)
            except IndexError:
                print("Error retrieving information.")

        return subdomain_list
