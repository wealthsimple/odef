# The IOC Library 

Welcome to the Threat Hunting IOC library :wave:. The goal of the library is to provide an automated continuous vigilance for IOC of interest. 
#
## Goals

These are the goals of the IOC library on a high-level: 
<ol>
  <li>Organize IOC in a structured format</li>
  <li>Provide audit/log trail</li>
  <li>Ensure continues vigilance for the IOCs</li>
  <li>Automate manual searching and reduce the operational effort</li>
</ol>

#
## The *IOC_Library.yml* structure explained 
To add new IOC in the library you have to be familiar with the structure of the yml file. 

```
IOC_Library.yml
│   └───Actor_Name
│   |   | 
|   |   └───reporter: name of the person who reported the IOC
│   |   |
│   |   └─── sha1_hashes (one hash per line)
|   |   |   - hash1 
|   |   |   - hash2
│   |   └─── md5_hashes
|   |   |   - md5_hash
│   |   └─── sha256_hashes
|   |   |   - sha256hash
|   |   └─── domains
|   |   |   - domain
|   |   └─── ip addresses
|   |        - ip
|   |   
│   └─── Next actor ... 
```
:warning: If the IOC is not associated with a threat actor or a group you can just type **unassociated** or **custom** in the actor name field. 


#
## Implementation/Automation
Create an automation using your SOAR system to pick the IOC and search the data or use ci/cd to deploy the indicators to your SIEM.