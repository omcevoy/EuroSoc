# Scrape

For my CIS 451 (Database Processing) final project, I am modeling european soccer. 

This repository includes the python scripts I wrote to scrape data off the internet, python scripts to import data from a csv file to the sql database, the csv files themselves, and of course the sql file.  Eventually, this repo will include a few php files as well as a link to the website. Unfortunately, due to time restrictions, not all of the data is accurate. Fake data was generated to populate the managers table and fake data will be generated to populate the rest of the player data. Eventually, I will try to populate them with exclusively real data.

------------------------------------------------------------------------------------------------------------------------------

# Tables
                                                  
**player** : playerID (pk), name, position, age, weekly_wage, club_name, country_of_birth

**manager**: managerID (pk), fname, lname, age, cob, club

**country**: country_code (pk), country_name

**city**   : city_code (pk), city_name, country_code, population

**stadium**: stad_name (pk), city_code, capacity, year_built

**league** : league_code (pk), league_name, founding_date

**club**   : club_name (pk), city_code, league_code, stadium
               
               
------------------------------------------------------------------------------------------------------------------------------
