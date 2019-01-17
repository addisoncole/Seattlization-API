from django.core.management.base import BaseCommand
from seattlizationAPI.models import *
from requests.auth import HTTPDigestAuth
import os
import sys
import pandas
import requests
import json
import environ
import csv
import logging

env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env()

#US CENSUS BUREAU CONSTANTS
CENSUS_BUREAU_YEARS = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
CENSUS_BUREAU_BASE_URL = "https://api.census.gov/data/"
URL_2010_to_2014 = "/acs/acs1?get=B01003_001E,B19083_001E,B19013_001E,B19001_002E,B19001_003E,B19001_004E,B19001_005E,B19001_006E,B19001_007E,B19001_008E,B19001_009E,B19001_010E,B19001_011E,B19001_012E,B19001_013E,B19001_014E,B19001_015E,B19001_016E,B19001_017E,NAME&for=county:033&in=state:53&key="
URL_POST_2014 = "/acs/acs1?get=B01003_001E,B19083_001E,B19013_001E,B19001_002E,B19001_003E,B19001_004E,B19001_005E,B19001_006E,B19001_007E,B19001_008E,B19001_009E,B19001_010E,B19001_011E,B19001_012E,B19001_013E,B19001_014E,B19001_015E,B19001_016E,B19001_017E,B25031_002E,B25031_003E,B25031_004E,B25031_005E,B25031_006E,B25031_007E,NAME&for=county:033&in=state:53&key="

#data.seattle.gov Constants
SEATTLE_DATA_BASE_URL = "https://data.seattle.gov/resource/"
#data.seattle.gov/SOCRATA SODA tables for models
LOW_INCOME_HOUSING_IDENTIFIER="dwr3-dvgb.json?"
BUILDING_PERMIT_IDENTIFIER="k44w-2dcq.json?"
MFTE_PROJECT_IDENTIFIER="g958-yakb.json?"

class Command(BaseCommand):
    help = 'Seeds data for model'

    def _seed_model(self):
        # community_surveys_wrapper()
        # low_income_housing_wrapper()
        # building_permit_wrapper()
        mfte_project_wrapper()

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        self._seed_model()


def community_surveys_wrapper():
    for year in CENSUS_BUREAU_YEARS:

        if year <= 2014:
            myResponse = requests.get(f'{CENSUS_BUREAU_BASE_URL}{year}{URL_2010_to_2014}' + env('US_CENSUS_BUREAU_KEY'))
                #print (myResponse.status_code)
                #For successful API call, response code will be 200 (OK)
            if(myResponse.ok):
                jData = json.loads(myResponse.content)
                print("The response contains {0} properties".format(len(jData)))

                create_survey_pre2014(year = year, data = jData[1])
            else:
                myResponse.raise_for_status()
        else:
            myResponse = requests.get(f'{CENSUS_BUREAU_BASE_URL}{year}{URL_POST_2014}' + env('US_CENSUS_BUREAU_KEY'))

            if(myResponse.ok):
                jData = json.loads(myResponse.content)
                print("The response contains {0} properties".format(len(jData)))

                data = {"year": year, "data":jData[1]}
                create_survey_post2014(year = year, data = jData[1])
            else:
                myResponse.raise_for_status()

def create_survey_post2014(**kwargs):
    print (kwargs["year"])
    new_survey = CommunitySurvey(
        year = kwargs["year"],
        total_population = kwargs["data"][0],
        gini_index = kwargs["data"][1],
        median_income = kwargs["data"][2],
        income_under_10000 = kwargs["data"][3],
        income_10000_14999 = kwargs["data"][4],
        income_15000_19999 = kwargs["data"][5],
        income_20000_24999 = kwargs["data"][6],
        income_25000_29999 = kwargs["data"][7],
        income_30000_34999 = kwargs["data"][8],
        income_35000_39999 = kwargs["data"][9],
        income_40000_44999 = kwargs["data"][10],
        income_45000_49999 = kwargs["data"][11],
        income_50000_59999 = kwargs["data"][12],
        income_60000_74999 = kwargs["data"][13],
        income_75000_99999 = kwargs["data"][14],
        income_100000_124999 = kwargs["data"][15],
        income_125000_149999 = kwargs["data"][16],
        income_150000_199999 = kwargs["data"][17],
        income_over_200000 = kwargs["data"][18],
        median_rent_studio = kwargs["data"][19],
        median_rent_1br = kwargs["data"][20],
        median_rent_2br = kwargs["data"][21],
        median_rent_3br = kwargs["data"][22],
        median_rent_4br = kwargs["data"][23],
        median_rent_5br = kwargs["data"][24],
    )
    print(new_survey)
    new_survey.save()
    logging.info("{} created.".format(new_survey))
    return new_survey

def create_survey_pre2014(**kwargs):
    print (kwargs["year"])
    new_survey = CommunitySurvey(
        year = kwargs["year"],
        total_population = kwargs["data"][0],
        gini_index = kwargs["data"][1],
        median_income = kwargs["data"][2],
        income_under_10000 = kwargs["data"][3],
        income_10000_14999 = kwargs["data"][4],
        income_15000_19999 = kwargs["data"][5],
        income_20000_24999 = kwargs["data"][6],
        income_25000_29999 = kwargs["data"][7],
        income_30000_34999 = kwargs["data"][8],
        income_35000_39999 = kwargs["data"][9],
        income_40000_44999 = kwargs["data"][10],
        income_45000_49999 = kwargs["data"][11],
        income_50000_59999 = kwargs["data"][12],
        income_60000_74999 = kwargs["data"][13],
        income_75000_99999 = kwargs["data"][14],
        income_100000_124999 = kwargs["data"][15],
        income_125000_149999 = kwargs["data"][16],
        income_150000_199999 = kwargs["data"][17],
        income_over_200000 = kwargs["data"][18],
    )
    print(new_survey)
    new_survey.save()
    logging.info("{} created.".format(new_survey))
    return new_survey

def low_income_housing_wrapper():
    myResponse = requests.get(f'{SEATTLE_DATA_BASE_URL}{LOW_INCOME_HOUSING_IDENTIFIER}$limit=5000&$$app_token=' + env('SOCRATA_KEY'))
    ## print (myResponse.status_code)
    ## For successful API call, response code will be 200 (OK)
    if(myResponse.ok):
        jData = json.loads(myResponse.content)
        print("The response contains {0} properties".format(len(jData)))
        for item in jData:
            create_low_income_housing(data = item)
    else:
        myResponse.raise_for_status()

def create_low_income_housing(**kwargs):
    data = kwargs["data"]
    new_housing = LowIncomeHousing(
        number_of_units = data["units_with_income_rent_limits"],
        year_placed_in_service = data["year_placed_in_service"],
        name = data["name"],
        address = data["address"],
        zip_code = data["zip_code"],
        council_district = data["council_district"],
    )
    if ("hud" in data):
        new_housing.hud = populate_boolean_field_convert_x(data["hud"])

    if ("sha" in data):
        new_housing.sha = populate_boolean_field_convert_x(data["sha"])

    if ("state_or_county" in data):
        new_housing.state_or_county = populate_boolean_field_convert_x(data["state_of_wa_or_county"])

    if ("wshfc" in data):
        new_housing.wshfc = populate_boolean_field_convert_x(data["wshfc"])

    if ("city_of_seattle" in data):
        new_housing.city_of_seattle = populate_boolean_field_convert_x(data["city_of_seattle"])

    new_housing.save()
    logging.info("{} created.".format(new_housing))
    return new_housing

def populate_boolean_field_convert_x(field):
    if (field == "X"):
        return True
    else:
        return False

def building_permit_wrapper():

    with open(os.path.join(sys.path[0], '.Building_Permits.csv'), "r") as building_permit_csv_file:
        csv_data = pandas.read_csv(building_permit_csv_file)
        row_count = 0
        for index, row in csv_data.iterrows():
            create_building_permit(data = row)
            print(row_count)
            row_count += 1
        print(f'# of Permits Loaded: {row_count}')

def create_building_permit(**kwargs):
    data = kwargs["data"]
    new_permit = BuildingPermit(
        permit_number = data[0],
        permit_class = data[1],
        permit_class_mapped = data[2],
        permit_type = data[4],
        permit_type_mapped = data[3],
        description = data[5],
        permit_application_date = data[10],
        permit_approval_date = data[11],
        permit_completion_date = data[13],
        location = data[23],
        link = data[20],
    )

    if not(pandas.isnull(data[6])):
        new_permit.number_of_units = data[6]

    if not(pandas.isnull(data[7])):
        new_permit.housing_units_removed = data[7]

    if not(pandas.isnull(data[8])):
        new_permit.housing_units_added = data[8]

    new_permit.save()
    logging.info("{} created.".format(new_permit))
    return new_permit

def mfte_project_wrapper():
    myResponse = requests.get(f'{SEATTLE_DATA_BASE_URL}{MFTE_PROJECT_IDENTIFIER}$limit=5000&$$app_token=' + env('SOCRATA_KEY'))
    ## print (myResponse.status_code)
    ## For successful API call, response code will be 200 (OK)
    if(myResponse.ok):
        jData = json.loads(myResponse.content)
        print("The response contains {0} properties".format(len(jData)))
        count = 1
        for item in jData:
            print(f'Load item #{count}')
            print(item)
            create_mfte_project(data = item)
            count += 1
    else:
        myResponse.raise_for_status()

def create_mfte_project(**kwargs):
    data = kwargs["data"]
    new_project= MFTEProject(
        project_name = data["project_name"],
        # tax_exemption_start = data["tax_exemption_effective_year"],
        # tax_exemption_end = data["tax_exemption_expires_12_31"],
        year_of_approval = data["year_of_approval"],
        address = data["address_address"],
        council_district = data["city_council_district"],
        targeted_area = data["residential_targeted_area_urban_center_urban_village"],
        total_units = data["all_total"],
        total_affordable_units = data["all_afford"],
        SEDU_total = data["sedu_total"],
        SEDU_affordable = data["sedu_afford"],
        studio_units_total = data["studio_total"],
        studio_units_affordable = data["studio_afford"],
        one_br_total = data["_1br_total"],
        one_br_affordable = data["_1br_afford"],
        two_br_total = data["_2br_total"],
        two_br_affordable = data["_2br_afford"],
        three_br_total = data["_3br_total"],
        three_br_affordable = data["_3br_afford"],
        four_br_total = data["_4br_total"],
        four_br_affordable = data["_4br_afford"],
    )
    new_project.subsidized = populate_boolean_field_convert_yes(data['subsidized'])

    new_project.microhousing = populate_boolean_field_convert_yes(data['micro'])

    if "tax_exemption_effective_year" in data:
        new_project.tax_exemption_start = data["tax_exemption_effective_year"]

    if "tax_exemption_expires_12_31" in data:
        new_project.tax_exemption_end = data["tax_exemption_expires_12_31"]

    logging.info("{} created.".format(new_project))
    new_project.save()
    return new_project

def populate_boolean_field_convert_yes(field):
    if (field == "Yes"):
        return True
    else:
        return False
