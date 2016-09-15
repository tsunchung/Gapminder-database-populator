## Gapminder-database-populator
Done Nov 2013.  
Developed a script to parse Gapminder CSV files in order to generate SQL statements to populate the Gapminder database.

Source: Free material from [https://www.gapminder.org/data/](https://www.gapminder.org/data/)

### How to Run
	python parser.py
Output: gapminder\_load.sql  
gapminder\_schema.sql for reference.  

### Approach

Since each CSV file begins with a line consisting of all the years for each type of
data, we took the first line of each CSV file and inserted all the years into 
a list when creating each respective table.  

We then traversed each line of the CSV files while matching with our year list in order to maintain 
data integrity in creating our insert statements.   

A special case had to made 
for the country, Cote d'Ivoire, because of its apostrophe (single quote), so 
whenever we hit Cote d'Ivoire in creating our insert statements, we added an 
extra single quote after the initial one to escape it.