# dpc_stress

Misc. info and prototype scripts related to the dpc-app tests and Data Point of Care (DPC) PDF documents.

Python and optionally Bash (via CLI history) scripts to curl or wget DPC REST v1 and v2 endpoints, which may be ported to Go-lang or Swift-lang for
better performance.

Python scripts using PyPDF2 to inspect and concat PDFs. Debug python scripts via "python3 -m pdb script.py".

Refs. listed below.

---

### Controlled Unclassified Information

[NASA CUI Site](https://www.nasa.gov/content/controlled-unclassified-information)

[NASA CUI PDF](https://nodis3.gsfc.nasa.gov/OPD_docs/NID_2810_135_.pdf)

---

### Data Point of Care

[DPC-2226](https://jira.cms.gov/browse/DPC-2226)
    
[Draft DPC Pilot Roadmap](https://confluence.cms.gov/pages/viewpage.action?spaceKey=DAPC&title=DRAFT+DPC+Pilot+Roadmap)
    
[DPC V2 Impl Guide](https://confluence.cms.gov/display/DAPC/DPC+Version+2+Implementation+Guide)
    
[DPC V2 Tech Specs](https://confluence.cms.gov/display/DAPC/DPC+Version+2+Technical+Specification#DPCVersion2TechnicalSpecification-APIService)

[DPC V1 Tech Specs](https://dpc.cms.gov/docsV1)

---

Ubuntu Linux CLI extract CUI cover sheet template (page 20) from DoD PDF:

    pdftk A=N_PR_2810_0007_.pdf cat A20 output CUI_1.pdf

[Python PDF module: pip install pypdf2](https://pypi.org/project/PyPDF2)

[Python file magic number module: pip install puremagic](https://pypi.org/project/puremagic/)

[Python Debugger: python3 -m pdb script.py](https://docs.python.org/3/library/pdb.html)

---

Also consider groovy scripts that import this groovy awesomeness:

[Awesome JVM PDF tools](https://pdfbox.apache.org)

[Download Groovy shell](https://groovy.apache.org/download.html)

---

Cloud tools to consider:

[AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/create-sample-projects.html)

[Google Big Data Stats](https://cloud.google.com/bigquery)

[Elastic Log Monitoring and Search](https://www.elastic.co/observability/log-monitoring)

[Telemtry Logging](https://opentelemetry.io/)

---

CCSDS and NASA Refs:

[CCSDS Standards](https://public.ccsds.org/default.aspx)

[NASA Systems Engineering](https://www.nasa.gov/connect/ebooks/nasa-systems-engineering-handbook)

More TBD

---

