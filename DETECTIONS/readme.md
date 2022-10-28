# Significance of Using Terraform and How it will work.

## Prerequisites

At Wealthsimple, we use [Terragrunt](https://terragrunt.gruntwork.io/). Terragrunt us a light wrapper around Terraform which allows us to write more lean Terraform code and it takes care of some Terraform boilerplate for us.


Layout of terraform repository in here:

```
❯ tree .
.
├── README.md              # README.md file. (main repository read me)
├── account.hcl            # Account specific configuration file.
├── DETECTIONS             # This directory contains our detections. Detections are separated by directory.
│   ├── alert1             # Configuraton for alert1. (Name of the Alert)
│   │   ├── alerts.hcl     # Alert1 data.
│   │   └── terragrunt.hcl # Terragrunt configuration file.
│   │   └── README.md      # Read me of each alert.
│   ├── alert2
│   │   ├── alerts.hcl
│   │   └── terragrunt.hcl
│   │   └── README.md      # Read me of each alert.
│   └── alert3
│       ├── alerts.hcl
│       └── terragrunt.hcl
│   │   └── README.md      # Read me of each alert.
│   └── README.md          # This Doc
├── modules                # Our modules directory.
│   └── alert              # Alert module configuration directory.
│       ├── main.tf        # Configuration for our Terraform alert module.
│       └── variables.tf   # Variables used by our Terraform alert module.
├── terragrunt.hcl         # Root Terragrunt configuration file.

❯
```

## Setting Up a New Detection

after executing main.py file we need to take the following steps.
**Note:** These values might be slightly different depending on your local configuration.

1. open terminal, execute the following command:
```bash
python main.py
```
2. Select detection if we want to set up an alert in Splunk

   ![](../screenshots/Screen_Shot_2022-09-16_at_5.02.06_PM.png)
3. Select the type of detection

   ![](../screenshots/Screen_Shot_2022-09-16_at_5.02.20_PM.png)
4. Write detection like the sample example

   ![](../screenshots/Screen_Shot_2022-09-16_at_7.03.28_PM.png)
5. This will create an alert folder in the with a new detection under DETECTIONS.

# What to write in Detection
The prompt will ask a set of questions to set up the alert.hcl file listed below:
1. **"Enter detection name"** : It is the title of the detection/ alert that we want to set up. 
2. **"Enter author name"**: The author name will be the email of the person who intends to set up this alert. For intance *"shubhangi.upadhyay@wealthsimple.com"*
3. **"Select an Action Type"**: The prompt will give two options either to set an email notification if the alert goes off or do something else. We have to select something else in case to of logging an event to notable_dev/notable index.
4. **"Enter Search (spl)"**: We should put the query here and pipe it with the collect statement and it should have the following parameters
   1. **" | collect index= *index name* sourceType=*tag the field with the purpose it fulfils*"**
5. **"Enter MITRE ATT&CK Technique IDs related to the detection, comma delimited for multiple"**: We'll have to enter the TTP information that will be cover with the detection we intend to deploy.

[Crontab generator](https://crontab.cronhub.io/)