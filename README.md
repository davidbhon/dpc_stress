# dpc_stress

Misc. stuff along with bash and python gists related to the dpc-app.
Python and optionally Bash (via CLI history) scripts to curl DPC REST v1 and v2 endpoints, which may be ported to Go-lang or Swift-lang for
better performance.

Refs. listed below. More TBD.

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
    
---

Ubuntu Linux CLI extract CUI cover sheet template (page 20) from DoD PDF:

    pdftk A=N_PR_2810_0007_.pdf cat A20 output CUI_1.pdf

Sadly the Python PDF module(s) did not fully install successfully. However, consider groovy scripts that import this awesome-ness:

[Awesome JVM PDF tools](https://pdfbox.apache.org) 

---


