crt.sh Python utility
========


This project aims at helping you to interact with [crt.sh](https://crt.sh) website. 

Git clone the repo. 

```bash
git clone https://github.com/PaulSec/crt.sh
```

Install the dependencies.

```bash
pip install -r requirements.txt
```

Then, you can start interacting with crt.sh this way: 

```python
from crtsh import crtshAPI
import json

print(json.dumps(crtshAPI().search('uber.com')))
```

The result is an array of dictionary items which looks like this: 

```json 
[
  {
    "crtsh_id": "201202462",
    "logged_at": "2017-08-29",
    "not_before": "2017-08-22",
    "domain": "lert.uber.com",
    "issuer": "C=US, O=DigiCert Inc, CN=DigiCert SHA2 Secure Server CA"
  },
  {
    "crtsh_id": "196687254",
    "logged_at": "2017-08-23",
    "not_before": "2017-08-23",
    "domain": "hatch.uber.com",
    "issuer": "C=US, O=Let's Encrypt, CN=Let's Encrypt Authority X3"
  },
  {
    "crtsh_id": "175522179",
    "logged_at": "2017-07-19",
    "not_before": "2017-07-11",
    "domain": "*.uber.com",
    "issuer": "C=US, O=DigiCert Inc, CN=DigiCert SHA2 Secure Server CA"
  },
  ....
]
```

License
========

I actually used some code from (the pretty cool) [Punter](https://github.com/nethunteros/punter/) project.
If any license applies on his side (it seems not), it will be his ones :) 