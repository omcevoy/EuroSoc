# EuroSoc

### CIS 451 (Database Processing) Final Project

For the final project my group (Nicholas Fay & myself) decided that we would model European Soccer. This repository includes the python scripts I wrote to scrape data off the internet, scripts to import data from a csv file to the sql database, and the csv files themselves, and of course the sql file. Unfortunately, due to time restrictions, not all of the data is accurate. Fake data was generated to populate the managers table and fake data will be generated to populate the rest of the player data. Eventually, I will try to populate the database with exclusively real data. 
------------------------------------------------------------------------------------------------------------------------------
# Link
http://ix.cs.uoregon.edu/~omcevoy/final.html
# Tables
                                                  
**player**  : conID (pk), name, position, age, weekly_wage, club_name, country_of_birth

**manager** : conID (pk), fname, lname, age, cob, club

**country** : country_code (pk), country_name

**city**    : city_code (pk), city_name, country_code, population

**stadium** : stad_name (pk), city_code, capacity, year_built

**league**  : league_code (pk), league_name, founding_date

**club**    : club_name (pk), city_code, league_code, stadium

**refs**    : conID (pk), fname, lname, league_code

**eurocup** : cupID (pk), cupName, champion

**owners**  : club_name (pk), fname, lname, managers_lname

**sponsors**: club_name (pk), kit_sponsor, drink_sponsor
               
    
------------------------------------------------------------------------------------------------------------------------------
