import os
import json
secret = dict(os.environ)
json_secrets = json.dumps(secret)
print(secret)
print(json_secrets)
