from django.core.management.base import BaseCommand
from seattlizationAPI.models import CommunitySurvey
from requests.auth import HTTPDigestAuth
import requests
import json
import environ
import logging

env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env()

YEARS = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]

BASE_URL = "https://api.census.gov/data/"

URL_2010_to_2014 = "/acs/acs1?get=B01003_001E,B19083_001E,B19013_001E,B19001_002E,B19001_003E,B19001_004E,B19001_005E,B19001_006E,B19001_007E,B19001_008E,B19001_009E,B19001_010E,B19001_011E,B19001_012E,B19001_013E,B19001_014E,B19001_015E,B19001_016E,B19001_017E,NAME&for=county:033&in=state:53&key="

URL_POST_2014 = "/acs/acs1?get=B01003_001E,B19083_001E,B19013_001E,B19001_002E,B19001_003E,B19001_004E,B19001_005E,B19001_006E,B19001_007E,B19001_008E,B19001_009E,B19001_010E,B19001_011E,B19001_012E,B19001_013E,B19001_014E,B19001_015E,B19001_016E,B19001_017E,B25031_002E,B25031_003E,B25031_004E,B25031_005E,B25031_006E,B25031_007E,NAME&for=county:033&in=state:53&key="

class Command(BaseCommand):
    help = 'Seeds CommunitySurvey model'

    def _seed_model(self):
        for year in YEARS:

            if year <= 2014:
                myResponse = requests.get(f'{BASE_URL}{year}{URL_2010_to_2014}' + env('US_CENSUS_BUREAU_KEY'))
                    #print (myResponse.status_code)
                    #For successful API call, response code will be 200 (OK)
                if(myResponse.ok):
                    jData = json.loads(myResponse.content)
                    print("The response contains {0} properties".format(len(jData)))

                    create_survey_pre2014(year = year, data = jData[1])
                else:
                    myResponse.raise_for_status()
            else:
                myResponse = requests.get(f'{BASE_URL}{year}{URL_POST_2014}' + env('US_CENSUS_BUREAU_KEY'))

                if(myResponse.ok):
                    jData = json.loads(myResponse.content)
                    print("The response contains {0} properties".format(len(jData)))

                    data = {"year": year, "data":jData[1]}
                    create_survey_post2014(year = year, data = jData[1])
                else:
                    myResponse.raise_for_status()

    def handle(self, *args, **options):
        self.stdout.write('seeding CommunitySurvey data...')
        self._seed_model()

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
