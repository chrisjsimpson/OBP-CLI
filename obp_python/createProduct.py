import requests
import os
import json
from .init import get_config

def createProduct(bank_id=None, product_id=None, name=None, 
                 parent_product_code=None, category=None, 
                 family=None, super_family=None, more_info_url=None, 
                 details=None, description=None, meta_license_id="5", 
                 meta_license_name="Tesobe"):
  """
  Create a product in Open Product Project

  Requires role: 
  e.g. obp addrole --role-name 
  """

  payload = {
    "bank_id": bank_id,
    "name": name,
    "parent_product_code": parent_product_code,
    "category": category,
    "family": family,
    "super_family": super_family,
    "more_info_url": more_info_url,
    "details": details,
    "description": description,
    "meta": { 
      "license":{
        "id": meta_license_id,
        "name": meta_license_name
      }  
    }
  }
  
  url = get_config('OBP_API_HOST') + '/obp/v3.1.0/banks/{bank_id}/products/{product_id}'.format(bank_id=bank_id, product_id=product_id)
  
  authorization = 'DirectLogin token="{}"'.format(get_config('OBP_AUTH_TOKEN'))
  headers = {'Content-Type': 'application/json',
            'Authorization': authorization}
  req = requests.post(url, headers=headers, json=payload)

  if req.status_code == 403:
    print(req.text)
    exit(-1)

  return req
