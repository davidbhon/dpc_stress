#!/bin/env python3
import certifi, os, sys, datetime as dt
from io import BytesIO

# kinda PEP 8 style
pep8url = 'https://peps.python.org/pep-0008/'

try:
  import pycurl
except:
  print("need conda install or pip install of pycurl...")
  sys.exit()

pycurlio = 'http://pycurl.io/'
dpcsbx = 'https://sandbox.dpc.cms.gov/'
dpcprod = 'dpc.cms.gov/api'

def dpc_curl(url, ver='v1', id=None):
  """
  Curl REST DPC API via version and Id
  code based on http://pycurl.io/docs/latest/quickstart.html
  Comments moved into this docstring
  Body is a byte string.
  We have to know the encoding in order to print it to a text file
  such as standard output.
  """
  endpoint = url + '/api/' + ver + '/'
  if(id): endpoint +=  id

  buffer = BytesIO()
  c = pycurl.Curl()
  c.setopt(c.URL, endpiont)
  c.setopt(c.WRITEDATA, buffer)
  c.setopt(c.CAINFO, certifi.where())
  c.perform()
  c.close()
  body = buffer.getvalue()
  content = body.decode('iso-8859-1') ; print(content)
  return content

def main():
  """
  Main entry to DPC API testing via pycurl module
  """
  print("Hello DPC v1 and v2")
  # test v1 defaults
  conv1 = dpc_curl(pycurlio) 
  # test v2
  conv2 = dpc_curl(pycurlio, 'v2') 

if __name__ == "__main__":
    main()
