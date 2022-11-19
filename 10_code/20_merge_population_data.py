### Merge Population Datasets

## Import necessary dependencies
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
## Rename the county in FIPS code data to align with the naming convention in the mortality dataset
fips_code.loc[fips_code.name == "Do̱a Ana County", "name"] = "Doña Ana County"


## Read into the state abbreviation dataset
state_abbr = pd.read_csv(
    "https://github.com/MIDS-at-Duke/pds-2022-red-team/raw/"
    "main/00_source_data/state_name-abbr.csv"
)


## Read into the population data from 2000 - 2009
population_2k_09 = pd.read_csv(
    "https://github.com/MIDS-at-Duke/pds-2022-red-team/raw/"
    "main/00_source_data/US_population/2000_2009_US_population.csv",
    encoding="latin-1",
)
## Subset to unique population dataset per county-state
pop_00_09 = population_2k_09[
    [
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
    ]
].drop_duplicates()

## Remove Alaska from the dataset
pop_00_09_noAK = pop_00_09[pop_00_09["STNAME"] != "Alaska"]
pop_00_09_cp = pop_00_09_noAK.copy()

## Rename the population columns to the corresponding year
pop_00_09_cp.rename(
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


## Convert fully spelled out state name to state abbreviation for later merges
pop_00_09_abbr = pop_00_09_cp.merge(
    state_abbr,
    left_on="STNAME",
    right_on="State",
    validate="m:1",
).drop(["State", "STNAME"], axis=1)
pop_00_09_abbr.rename(
    columns={"Abbreviation": "State", "CTYNAME": "County"}, inplace=True
)


## merge the 2000-2009 population dataset with fips code
pop_00_09_fips = pop_00_09_abbr.merge(
    fips_code,
    left_on=["County", "State"],
    right_on=["name", "state"],
    how="left",
    validate="1:1",
).drop(["name", "state"], axis=1)


## Confirm the number of states and counties remain the same after the merges
assert (len(pop_00_09_cp.CTYNAME.unique() == 1897)) & (
    len(pop_00_09_cp.STNAME.unique() == 50)
)
assert (len(pop_00_09_abbr.County.unique() == 1897)) & (
    len(pop_00_09_abbr.State.unique() == 50)
)
assert (len(pop_00_09_fips.County.unique() == 1897)) & (
    len(pop_00_09_fips.State.unique() == 50)
)
assert len(pop_00_09_fips.fips.unique()) == 3115


## Repeat the process above with population dataset from 2010-2020
population_10_20 = pd.read_csv(
    "https://github.com/MIDS-at-Duke/pds-2022-red-team/raw/"
    "main/00_source_data/US_population/2010_2020_US_population.csv",
    encoding="latin-1",
)
## Subset to unique population dataset per county-state
pop_10_20 = population_10_20[
    [
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
    ]
].drop_duplicates()

## Remove Alaska from the dataset
pop_10_20_noAK = pop_10_20[pop_10_20["STNAME"] != "Alaska"]
pop_10_20_cp = pop_10_20_noAK.copy()

## Rename the county name to align with the name in the 2000-2009 popualtion dataset
pop_10_20_cp.loc[
    pop_10_20_cp.CTYNAME == "LaSalle Parish", "CTYNAME"
] = "La Salle Parish"

## Rename the population columns to the corresponding year
pop_10_20_cp.rename(
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


## Convert fully spelled out state name to state abbreviation for later merges
pop_10_20_abbr = pop_10_20_cp.merge(
    state_abbr, left_on="STNAME", right_on="State", validate="m:1"
).drop(["State", "STNAME"], axis=1)
pop_10_20_abbr.rename(
    columns={"Abbreviation": "State", "CTYNAME": "County"}, inplace=True
)


## merge the 2000-2009 population dataset with fips code
pop_10_20_fips = pop_10_20_abbr.merge(
    fips_code,
    left_on=["County", "State"],
    right_on=["name", "state"],
    how="left",
    validate="1:1",
).drop(["name", "state"], axis=1)


## Confirm state and county counts after merges
assert (len(pop_10_20_cp.CTYNAME.unique() == 1897)) & (
    len(pop_10_20_cp.STNAME.unique() == 50)
)
assert (len(pop_10_20_abbr.County.unique() == 1897)) & (
    len(pop_10_20_abbr.State.unique() == 50)
)
assert (len(pop_10_20_fips.County.unique() == 1897)) & (
    len(pop_10_20_fips.State.unique() == 50)
)
assert len(pop_10_20_fips.fips.unique()) == 3113


## Transform population dataset so that the each row is the population of a county at a given year
pop_00_09_fips_cp = pop_00_09_fips.copy()
pop_00_09_melt = pop_00_09_fips_cp.melt(["County", "State", "fips"], var_name="Year")
pop_00_09_melt.rename(columns={"value": "Population", "fips": "FIPS"}, inplace=True)

pop_10_20_fips_cp = pop_10_20_fips.copy()
pop_10_20_melt = pop_10_20_fips_cp.melt(["County", "State", "fips"], var_name="Year")
pop_10_20_melt.rename(columns={"value": "Population", "fips": "FIPS"}, inplace=True)

pop_00_20 = pd.concat([pop_00_09_melt, pop_10_20_melt], ignore_index=True)


## Confirm county and state counts after reshaping the dataframe
assert (len(pop_00_20.County.unique() == 1897)) & (len(pop_00_20.State.unique() == 50))
assert len(pop_00_20.FIPS.unique()) == 3115

pop_00_20.to_csv(
    "/Users/qiujiahui/Desktop/Fall 2022/IDS 720 Practical Data Science/Group Project/pds-2022-red-team/20_intermediate_files/pop_merged.csv",
    encoding="utf-8",
    index=False,
)
