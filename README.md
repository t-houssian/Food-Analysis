# Food-Analysis
A Django App to allow interpretation of Global Food Prices.

Data Pulled From

https://data.humdata.org/dataset/wfp-food-prices

As a software Engineer I am trying to gain a larger breadth of programming knowledge and trying to learn to integrate different parts of software to create a complete system.

This a piece of software that took the https://data.humdata.org/dataset/wfp-food-prices dataset containing 1.7 million rows of data and creates a sqllite database from it using python (specically pandas). I then uses this database as the source of my data in a django app that allows visualization of the data and lets you choose any of the global foods in the database and select the ones you purchase the most. The app will then display which area of the world you should live based on the prices of the foods that you selected. You also are able to query by a date range to get data from 2000 to 2020.

Steps to run the software:
1. clone the repo
2. install anaconda (https://docs.anaconda.com/anaconda/install/)
3. run `conda create --name myenv --file spec-file.txt` to create the conda env
4. cd into django1 then into foodAnalysis
5. run `python manage.py migrate` in the terminal
6. run `python manage.py createsuperuser` in the terminal then create a user
7. run `python manage.py runserver` in the terminal than click on the development server link that pops up
8. log in using the credentials you created
9. click on the Food Analysis tab in the corner
10. select your date range to query by
11. select which foods you buy the most. (use ctrl to select multiple or shift to select a group of foods)
12. click the find best countries button
13. view which countries are best for you and if your a risky lad... head on your way!

The specific purpose of this project was to learn how to use sql and python together. And since I have experience with Django I thought it would be cool to bring the code to life and connect the database to a django app rather than just a text based app.

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of how created the Relational Database.}

[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

Database used: sqllite3
The database I created just has one table currently, the food_prices table:
food_prices:
            id integer PRIMARY KEY
            cm_name text NOT NULL - name of the good
            adm0_name text NOT NULL - name of the country
            um_name text NOT NULL - name of the unit of measurment
            mp_year text NOT NULL - year of the data
            mp_price integer NOT NULL - price of the data, average to create a single price unit

# Development Environment

For an exact copy of the env I used, See the spec-file.txt which allows you to recreate the conda env.

Language and tools used:
- Python
- Sqllite
- Django
- Pyviz Panel
- Pandas
- Holoviews
- Numpy
- datetime
- jupyter lab

# Useful Websites

* [dataset](https://data.humdata.org/dataset/wfp-food-prices)
* [conda env](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
* [pandas docs](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html)
* [pyviz panel](https://panel.holoviz.org/)
* [sqllite tutorial](https://www.sqlitetutorial.net/sqlite-python/creating-database/)

# Future Work

* Pull live data and update the database periodically
* Store results by user in a new table of the db
* Create new queries
* Style the site more
