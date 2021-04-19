# W4-geospatial-data-project

This is the fourth project I do at the Data Analytics bootcamp in Ironhack.

## Purpose
The purpose of this project is to determine where is the best location to establish a videogame company we have created, taking into account some employee requirements:
- Designers like to go to design talks and share knowledge. There must be some nearby companies that also do design.
- 30% of the company staff have at least 1 child - nearby nurseries.
- Executives like Starbucks A LOT. Ensure there's a starbucks not too far.
- Account managers need to travel a lot - nearby airport/helipad.
- Everyone in the company is between 25 and 40, give them some place to go party.
- Employees like to look smart and neet - we will ensure there is hairdresser nearby.

## Method
To do so, we use a dataset with over 18.000 companies, including names, category code, founding dates, number of employees, acquisition information and many others.
United States is among the top countries in the videogame industry and since NYC is one of my favourite cities, we have decided to locate the company here.
1. We have filtered using MongoDB Compass following the next criteria:
- Country: USA
- Founded year: after 2000
- Name/coordinates: we have removed all the null values
- Number of employees: between 10 and 500
- Category: Videogame

2. Once we determine our headquarters, we need to fulfill our employee requirements by following criteria we previusly explained and look for:
- Airports
- Starbucks
- Nurseries
- Nightclubs
- Hairdresser

3. Once we have met all the requirements we create a map using folium, showing the most nearby establishements to make our employees happy.

## Conclusion
As shown in the map, the location of the company is perfect since all the establishements that make the employees happy are very near to the office.