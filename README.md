# README file update 7-16-17

# Capstone Project Proposal

Capstone idea \#3 


## Problem

Assessing Cancer incidence and mortality in the United States


## Client Description and Potential Usage

Policy makers, public health planners and others may be interested in how cancer affects mortality rates geographically. 
Having this detailed report would allow them to monitor the burden of disease and to implement cancer prevention and control 
programs.


## Data Acquisition

The first Datasets for the incidence and mortality rates in the US are located at cancer.gov. This will point you to the state profile site: 

https://statecancerprofiles.cancer.gov/incidencerates/index.php?stateFIPS=99&cancer=001&race=00&sex=0&age=001&type=incd&sortVariableName=rate&sortOrder=default

You need to provide the proper filters to download the Mortality rates (death.csv)and Incidence (incd.csv).

Centers for disease control:
(https://www.cdc.gov/cancer/npcr/uscs/download_data.htm) 
The dates available are from 1999-2013. Data are from selected statewide and metropolitan area cancer registries that meet the 
data quality criteria for all invasive cancer sites combined. Rates cover approximately 99% of the U.S. population.CDC WONDER is a public service developed and operated by the Centers for Disease Control and Prevention, an agency of United States federal government. This data has the breakdown by State only and does not include the FIPS column.

The public web site at http://wonder.cdc.gov is in the public domain, and only provides access to public 
use data and information. You may access the information freely, and use, copy, distribute or publish this information 
without additional or explicit permission. Please do provide a citation to credit the authors and/or data providers. When referring to a written article or document, please cite the item as you would any other document on the world wide web.


Also the datasets from HDW (HRSA Data Warehouse) Health Resources and Services Administration (HRSA)

https://datawarehouse.hrsa.gov/data/datadownload.aspx

can be used by sorting by Healthcare Facilities and then under 
served medical locations. Checking for areas that are potentially high risk from being under served medically. 


## Approach

Data acquistion: current data detailed above
Data wrangling: CDC - Creation of data 
frames from flat text files, editing, creating and cross referencing variables from mulitple datasets and potential location based data integrated from HRSA. After evaluating datasets it was determined that the FIPS column https://en.wikipedia.org/wiki/Federal_Information_Processing_Standard_state_code was needed to compare Incidence and Mortality against the specific county in each state (not just the state fromm the first CDC dataset). This is needed to correlate with the HRSA/MUA dataset. 
    
Exploratory data analysis: Statistically and Visually tell the data story...


## Deliverables

GitHub: Code for the project in R markdown including documentation.
Paper explaining the problem, the approach and conclusions,Slide deck covering the same material as the final report.

Present the project to the online springboard community either in an office hour or online video.