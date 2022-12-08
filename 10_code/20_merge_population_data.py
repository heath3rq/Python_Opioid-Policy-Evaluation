import pandas as pd


## Load FIPS Code data
fips = pd.read_csv(
    "https://github.com/MIDS-at-Duke/pds-2022-red-team/raw/"
    "main/00_source_data/state_and_county_fips_master.csv"
)
## Remove Alaska from the FIPS  Code data
fips_noAK = fips[fips["state"] != "AK"]
## Remove non-county-state level FIPS Code. For example, we have fips code for each state
# but for our research we are only interested in the ones at county-state level
fips_code = fips_noAK[~fips_noAK["state"].isna()].copy()
## Rename the county in FIPS code data to align with the naming convention in the population dataset
fips_code.loc[fips_code.name == "Do̱a Ana County", "name"] = "Doña Ana County"


## Read into the state abbreviation dataset
state_abbr = pd.read_csv(
    "https://github.com/MIDS-at-Duke/pds-2022-red-team/raw/"
    "main/00_source_data/state_name-abbr.csv"
)


## Read into the population data from 2000 - 2009 and keep only wanted columns
population_2k_09 = pd.read_csv(
    "https://github.com/MIDS-at-Duke/pds-2022-red-team/raw/"
    "main/00_source_data/US_population/2000_2009_US_population.csv",
    encoding="latin-1",
    usecols=[
        "STNAME",
        "CTYNAME",
        "CENSUS2000POP",
        "POPESTIMATE2001",
        "POPESTIMATE2002",
        "POPESTIMATE2003",
        "POPESTIMATE2004",
        "POPESTIMATE2005",
        "POPESTIMATE2006",
        "POPESTIMATE2007",
        "POPESTIMATE2008",
        "POPESTIMATE2009",
    ],
)

## Remove duplicate - District of Columbia appeared twice in the population dataset
pop_00_09 = population_2k_09.copy().drop_duplicates()

## Rename the population columns to the corresponding year
pop_00_09.rename(
    columns={
        "CENSUS2000POP": 2000,
        "POPESTIMATE2001": 2001,
        "POPESTIMATE2002": 2002,
        "POPESTIMATE2003": 2003,
        "POPESTIMATE2004": 2004,
        "POPESTIMATE2005": 2005,
        "POPESTIMATE2006": 2006,
        "POPESTIMATE2007": 2007,
        "POPESTIMATE2008": 2008,
        "POPESTIMATE2009": 2009,
    },
    inplace=True,
)

## Transform population dataset so that the each row is the population of a county at a given year
pop_00_09_melt = pop_00_09.melt(["STNAME", "CTYNAME"], var_name="Year")
pop_00_09_melt.rename(columns={"value": "Population"}, inplace=True)
assert len(pop_00_09_melt) == 3193 * 10

## Read into the population data from 2010 - 2020
population_10_20 = pd.read_csv(
    "https://github.com/MIDS-at-Duke/pds-2022-red-team/raw/"
    "main/00_source_data/US_population/2010_2020_US_population.csv",
    encoding="latin-1",
    usecols=[
        "STNAME",
        "CTYNAME",
        "CENSUS2010POP",
        "POPESTIMATE2011",
        "POPESTIMATE2012",
        "POPESTIMATE2013",
        "POPESTIMATE2014",
        "POPESTIMATE2015",
        "POPESTIMATE2016",
        "POPESTIMATE2017",
        "POPESTIMATE2018",
        "POPESTIMATE2019",
        "POPESTIMATE2020",
    ],
)


## Remove duplicate - District of Columbia appeared twice in the population dataset
pop_10_20 = population_10_20.copy().drop_duplicates()

## Rename the county name to align with the name in the 2000-2009 popualtion dataset
pop_10_20.loc[pop_10_20.CTYNAME == "LaSalle Parish", "CTYNAME"] = "La Salle Parish"

## Rename the population columns to the corresponding year
pop_10_20.rename(
    columns={
        "CENSUS2010POP": 2010,
        "POPESTIMATE2011": 2011,
        "POPESTIMATE2012": 2012,
        "POPESTIMATE2013": 2013,
        "POPESTIMATE2014": 2014,
        "POPESTIMATE2015": 2015,
        "POPESTIMATE2016": 2016,
        "POPESTIMATE2017": 2017,
        "POPESTIMATE2018": 2018,
        "POPESTIMATE2019": 2019,
        "POPESTIMATE2020": 2020,
    },
    inplace=True,
)

## Transform population dataset so that the each row is the population of a county at a given year
pop_10_20_melt = pop_10_20.melt(["STNAME", "CTYNAME"], var_name="Year")
pop_10_20_melt.rename(columns={"value": "Population"}, inplace=True)
assert len(pop_10_20_melt) == 3193 * 11


pop_00_20 = pd.concat([pop_00_09_melt, pop_10_20_melt], ignore_index=True)
assert len(pop_00_20) == 3193 * 21


## Remove Alaska from the dataset
pop_00_20_noAL = pop_00_20[pop_00_20["STNAME"] != "Alaska"].copy()
## Remove State-Level population data from the dataset
pop_00_20_noState = pop_00_20_noAL[
    ~(pop_00_20_noAL["STNAME"] == pop_00_20_noAL["CTYNAME"])
]

## Convert fully spelled out state name to state abbreviation for later merges
pop_00_20_cp = pop_00_20_noState.merge(
    state_abbr,
    left_on="STNAME",
    right_on="State",
    validate="m:1",
).drop(["State", "STNAME"], axis=1)
pop_00_20_cp.rename(
    columns={"Abbreviation": "State", "CTYNAME": "County"}, inplace=True
)


## merge the 2000-2020 population dataset with fips code
pop_00_20_fips = pop_00_20_cp.merge(
    fips_code,
    left_on=["County", "State"],
    right_on=["name", "state"],
    how="left",
    validate="m:1",
    indicator=True,
).drop(["name", "state"], axis=1)

## Oglala Lakota County, SD was found to be missing FIPS code because the county was known as Shannon County (FIPS 46113) until May 2015
## Therefore, we decided to assign the FIPS code for Shannon County (FIPS 46113) to Oglala Lakota County
pop_00_20_fips.loc[
    (
        (pop_00_20_fips["County"] == "Oglala Lakota County")
        & (pop_00_20_fips["State"] == "SD")
    ),
    "fips",
] = 46113.0

## Confirm all county-state combinations have fips code in the population dataset
assert len(pop_00_20_fips[pop_00_20_fips.fips.isnull()]) == 0


## Subset population data to years between 2003 and 2015
years = [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]
pop_03_15 = pop_00_20_fips[pop_00_20_fips["Year"].isin(years)]

pop_03_15.to_csv(
    "https://github.com/MIDS-at-Duke/pds-2022-red-team/raw/main/20_intermediate_files/pop_merged.csv",
    encoding="utf-8",
    index=False,
)
