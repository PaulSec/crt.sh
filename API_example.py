from crtsh import crtshAPI
import json

print(json.dumps(crtshAPI().search('uber.com')))