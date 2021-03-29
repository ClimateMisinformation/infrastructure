# Infrastructure
The repository  contains the configuration and code used by our infrastructure. 

There are  three main dirs for scraping code.

1) cloud_functions
This contains the work we  are doing to migrate the  scrape scripts to  a serverless architecture. Google cloud 
functions run a scraping script and save the  output to  a bigquery table.   Because google maintain the
infrastructure it is expected to require the least upkeep by the team. For that reason it is our favoured 
option. 

2) containers
This contains the  work done to migrate  the  scrape scripts to  docker containers. It was paused to investigate 
serverless motivated by the  difficulty  of maintaining dependencies for all the containers and the need to 
run the containers regularly  CRONJOB and maintain permanent data stores of the results without duplicates. 
Some containers are large because of the script dependencies they  use. 
They  run on your machine  after installing docker and are portable between different cloud env. 

3) scrape-scripts
These are the original scripts. They run on your machine, they  work and they save to a CSV file.

##  The scraping code
Each directory and source has its own scraping scripts.  There is an aim to rationalise these into one 
python package. This will be located at 

https://github.com/ClimateMisinformation/scraper 


## The sources
The aim is to scrape all these sources daily and save the articles in a format  usable by the  data science
team.

https://docs.google.com/spreadsheets/d/1S_pv0cFsYCdrJFp8M-Tc_Vbk221PvhtnCe-QaBr8rQw/edit#gid=0


## The  data storage
Each directory and source has its own way  fo storing the results.