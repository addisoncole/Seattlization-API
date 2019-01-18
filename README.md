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
Returns a list of yearly homeless counts for the yearly Count Us In/One Night Count for King County (some data localized for Seattle). Contains shelter and unsheltered counts and demographics of individuals counted when data available. Years 1998 - 2018.

```
GET /homelesscounts/:year
```
Returns the results of the point in time count for that year.

### Low Income Housing Stock
```
GET /lowincomehousing/
```
Returns a list all rent & income restricted housing in Seattle, the number of units at the address, when they were added to the list of stock and details about who manages the contracts for the housing. Data comes from data.seattle.gov. Years 1942 - Present.

<!-- ```
GET /lowincomehousing/:year
```
Returns a list of all rent & income restricted housing in Seattle added during the provided year. -->

### Building Permitting in Seattle
```
GET /buildingpermits/
```
Returns a list of collected building permits in Seattle, details about the project, whether it is residential or commercial, and any housing units permitted to be added or removed. Covers mostly years mid 2000s to present, though some data extends as far back as 1986.

### Encampment Removals
```
GET /encampmentremovals/
```
Returns a list of each removal of an 'illegal' encampment. Returns removal dates, agencies responsible for removal, as well as reasons used for removal. Data currently only available for first half of 2018.

### Multi-Family Tax Exempted(MFTE) Projects
```
GET /mfteprojects/
```
Returns a list of each project approved under Seattle's MFTE Program, which provides tax exemptions in exchange for setting aside 20-25% of the homes as income or rent-restricted. Years 1999 to present.

### U.S. Census Bureau Yearly American Community Surveys
```
GET /communitysurveys/
```
Returns a list of statistics for King County collected by the yearly US Census Bureau's American Community Survey. Returns total population, median income, Gini index coefficient, breakdown of population by earnings, and the median rental cost of different rental listings. Years Available: 2010 - 2017.
```
GET /communitysurveys/:year
```
Returns the above data for the provided year.

### City Budget Data
```
GET /citybudgets/
```
Returns a list of the yearly budget expenditures by Seattle City Council. Years 2010 - 2016.

### Seattle Housing Market Data
```
GET /housingmarkets/
```
Returns a list data collected from Redfin broken down by year and the month of the reported median sale price of homes, the percentage of homes sold above list price, number of homes sold, housing sale inventory, and the average time a house spends on the market. Years 2012 - 2018.


## IN DEVELOPMENT

Advanced filtering of existing endpoints

Additional future Endpoints: number of death per year of individuals living on the street,  yearly data on stock of shelter beds provided by the city
