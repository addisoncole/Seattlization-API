# Seattlization-API
_Back-end API for Seattlization project [Built with Django/Python]_

### About
This is a project built with Python 3.7.2, Django 2.1.4 and Postgres and serves as the backend API of the [Seattlization Project](https://github.com/addisoncole/Seattlization "Seattlization"). 

The data one can access at the endpoints of this API is made up of publicly accessed data on income, housing, homelessness and inequality in Seattle, WA.
This data was attained through data scraping public data from nonprofits, U.S. Census Bureau data, public records requests and the use of local governmental data and APIs.

## ENDPOINTS

### Yearly Homeless Counts
```
GET /homelesscounts/
```
Returns a list of yearly homeless counts for King County and demographics of individuals counted.

```
GET /homelesscounts/:year
```
Returns the homeless count for that year.

## IN DEVELOPMENT

Additonal Endpoints desired: yearly city budgets, yearly distribution of incomes, yearly housing development with percentages of low income housing built, number of death per year of individuals living on the street,  yearly data on stock of shelter beds provided by the city.
