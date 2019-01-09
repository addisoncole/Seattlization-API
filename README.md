# Seattlization-API
_Back-end API for Seattlization project [Built with Django/Python]_

### About
This is a project built with Python 3.7.2, Django 2.0.9 and Postgres and serves as the backend API of the [Seattlization Project](https://github.com/addisoncole/Seattlization "Seattlization"). 

The data one can access at the endpoints of this API is made up of publicly accessed data on income, housing, homelessness and inequality in Seattle, WA.
This data was attained through data scraping public data from nonprofits, U.S. Census Bureau data, public records requests and the use of local governmental data and APIs.

## DOCUMENTATION

### Yearly Homeless Counts
```
GET /homelesscounts/
```
Returns a list of yearly homeless counts for King County and demographics of individuals counted.

```
GET /homelesscounts/:year
```
Returns the homeless count for that year.

### Low Income Housing Stock
```
GET /lowincomehousing/
```
Returns a list all rent & income restricted housing in Seattle, the number of units at the address, when they were added to the list of stock and details about who manages the contracts for the housing.

```
GET /lowincomehousing/:year
```
Returns a list of all rent & income restricted housing in Seattle added during the provided year.

### Building Permitting in Seattle
```
GET /buildingpermits/
```
Returns a list of collected building permits in Seattle, details about the project, whether it is residential or commercial, and any housing units permitted to be added or removed. 

### Encampment Removals
```
GET /encampmentremovals/
```
Returns a list of each removal of an 'illegal' encampment. Returns removal dates, agencies responsible for removal, as well as reasons used for removal. 

### Multi-Family Tax Exempted(MFTE) Projects
```
GET /mfteprojects/
```
Returns a list of each project approved under Seattle's MFTE Program, which provides tax emptions in exchange for setting aside 20-25% of the homes as income or rent-restricted.

### U.S. Census Bureau Yearly American Community Surveys
```
GET /communitysurveys/
```
Returns a list of statistics for King County collected by the yearly US Census Bureau's American Commuity Survey. Returns total population, median income, Gini index coefficient, breakdown of population by earnings, and the median rental cost of different rental listings. 
```
GET /communitysurveys/:year
```
Returns the above data for the provided year.

## IN DEVELOPMENT

Additonal Endpoints desired: yearly city budgets, number of death per year of individuals living on the street,  yearly data on stock of shelter beds provided by the city
