import requests

url = "http://localhost:8000/RPC2"

payload="<?xml version='1.0'?> \
        <methodCall> \
            <methodName>add</methodName>\
            <params> \
                <param> \
                    <int>2</int> \
                </param> \
                <param> \
                    <int>3</int> \
                </param> \
            </params> \
        </methodCall>"
        
headers = {
  'Content-Type': 'application/xml'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
