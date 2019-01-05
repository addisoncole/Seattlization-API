# Seattlization-API
_Back-end API for Seattlization project [Built with Django/Python]_

### About
This is a project built with Python 3.7.2, Django 2.1.4 and Postgres and serves as the backend API of the [Seattlization Project](https://github.com/addisoncole/Seattlization "Seattlization"). 

The data one can access at the endpoints of this API is made up of publicly accessed data on income, housing, homelessness and inequality in Seattle, WA.
This data was attained through data scraping public data, public records requests and the use of governmental and city APIs.

## ENDPOINTS

### Yearly Homeless Counts
```
GET /homelesscounts
```
Returns yearly homeless count for King County and demographics of individuals counted.

