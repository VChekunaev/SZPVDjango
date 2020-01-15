
"""
Definition of methods.
"""

import requests
import xmltodict
import json

# Create your models here.


def get_mq_version(*wsdl):
    result = []
    for w in wsdl:
        url = w
        body = """
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/">
           <soapenv:Header/>
           <soapenv:Body>
              <tem:GetVersion/>
           </soapenv:Body>
        </soapenv:Envelope>
        """
        headers = {'content-type': 'text/xml','SOAPAction': 'http://tempuri.org/IMqService/GetVersion'}
        response = requests.post(url,data=body,headers=headers)
        o = xmltodict.parse(response.text)
        j = json.loads(json.dumps(o))
        vers = j["s:Envelope"]["s:Body"]["GetVersionResponse"]["GetVersionResult"]["a:ServiceVersion"]
        result.append(vers)
    return result