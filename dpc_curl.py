#!/bin/env python3
import certifi, os, sys, datetime as dt
from io import BytesIO
from threading import Thread

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

def thrd_curls(cnt=10):
  """
  Use standard thread module to kick off a bunch of asyncio curls
  See https://www.pythontutorial.net/advanced-python/python-threading/
  """
  threads = []
  for n in range(1,cnt+1):
    tv1 = Thread(target=dpc_curl, args=(url, 'v1')) ; threads.append(tv1) ; tv1.start()
    tv2 = Thread(target=dpc_curl, args=(url, 'v2')) ; threads.append(tv2) ; tv2.start()

  for t in threads: t.join()

def fetch_endpoints(ver='all', yml=None, json=None, xml=None):
  """
  Return tuples or lists of all REST endpoints for v1 or v2
  Default list hadr-coded here, and can be reset via optional yaml or json or xml input file
  """
  v1 = ['v1', 'hard', 'coded', 'default', 'list', 'optionally', 'read', 'from json or xml file')
  v2 = ['v2', 'hard', 'coded', 'default', 'list', 'optionally', 'read', 'from json or xml file')
  return (v1, v2)

def main():
  """
  Main entry to DPC API testing via pycurl module
  Relevant docs:
    https://confluence.cms.gov/pages/viewpage.action?spaceKey=DAPC&title=V2+Comparison
    https://jira.cms.gov/browse/DPC-2226?jql=sprint%20%3D%2019023
    https://nodis3.gsfc.nasa.gov/OPD_docs/NID_2810_135_.pdf
    https://www.governmentattic.org/43docs/TreasuryDP80-08CUI_2018.pdf
    https://confluence.cms.gov/pages/viewpage.action?spaceKey=DAPC&title=DRAFT+DPC+Pilot+Roadmap
    https://confluence.cms.gov/display/DAPC/DPC+Version+2+Technical+Specification#DPCVersion2TechnicalSpecification-APIService
    Note V2 Endpoints table in above and also
    https://confluence.cms.gov/display/DAPC/DPC+Version+2+Implementation+Guide
  """
  print("Hello DPC v1 and v2")
  # test v1 defaults
  conv1 = dpc_curl(pycurlio) 
  # test v2
  conv2 = dpc_curl(pycurlio, 'v2') 

if __name__ == "__main__":
    main()
