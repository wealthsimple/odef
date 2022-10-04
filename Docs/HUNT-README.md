# The HUNT Library 

Welcome to the Threat Hunting HUNTS library :wave: 
#
## Goals

High-level goals for the HUNTS library: 
<ol>
  <li>Organize HUNTS in a structured format</li>
  <li>Provide audit/log trail</li>
  <li>Ensure continues vigilance for the covered TTPs</li>
  <li>Automate manual searching and reduce the operational effort</li>
  <li>Be the central repository of detections</li>
</ol>

## Hunt creation process

Standard as per the Sunrise phase:

```mermaid 
flowchart 
Research1(Opportunity Identification) -->Research2(Prioritize)
Research2 -->Research3(Develop Research Questions)
Research3 -->Research4(Information Gathering)
Research4 -->Research5(Collect Technical Context)
Research5 -->Prepare1(Identify Dataset)
Prepare1 -->Prepare2(Visibility Check)
Prepare2 -->Prepare3{Improve}
Prepare3 --> |yes| cis[Start visibility Improvement initiative]
Prepare3 --> |no| Build1(Detection Query Creation)
Build1 --> Build2(Manual Testing)
Build2 --> Build3(Baseline development)
Build3 --> Build4(Automated Unittest Development)
Build4 -->Build5(Enrich)
Build5 --> Build6(Document)
Build6 -->  Validate1(Confirm unittests) 
Validate1 -->val2(True/False Positive validation)
val2-->automate(Automation & deployment)
automate --> share(Socialize the new detection)
share -->share1(Update Sec Dependency Tree)
```
