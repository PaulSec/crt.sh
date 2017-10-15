from crtsh import crtshAPI
import sys
import json

if len(sys.argv) > 1:
    print(json.dumps(crtshAPI().search(sys.argv[1])))
else:
    pass
