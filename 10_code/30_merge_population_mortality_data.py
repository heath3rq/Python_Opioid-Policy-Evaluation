### Merging Mortality, FIPS, and Population Data

## Import necessary dependencies
import pandas as pd
import numpy as np

## Read into tables
mortality = pd.read_csv(
    "https://github.com/MIDS-at-Duke/pds-2022-red-team/raw/main/20_intermediate_files/mortality_cleaned.csv"
)
pop_00_20 = pd.read_csv(
    "https://github.com/MIDS-at-Duke/pds-2022-red-team/raw/main/20_intermediate_files/pop_merged.csv"
)

## Merge population with mortality datasets
pop_mortality_00_20 = pop_00_20.merge(
    mortality,
    left_on=["FIPS", "Year"],
    right_on=["County Code", "Year"],
    how="left",
    validate="m:m",
    indicator=True,
)
## Subset the dataframe to years between 2003 and 2015
pop_mortality_03_15 = pop_mortality_00_20[
    pop_mortality_00_20["Year"].isin(
        [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]
    )
]


## Confirm county and state counts after merging
assert (len(pop_mortality_03_15.County.unique() == 1897)) & (
    len(pop_mortality_03_15.State.unique() == 50)
)
assert len(pop_mortality_03_15.FIPS.unique()) == 3115


## Keep only county level mortality data by removing state population data where no mortality data is available
pop_mortality_03_15_df = pop_mortality_03_15[
    ~(
        (pop_mortality_03_15["County"].str.contains("County") == False)
        & (pop_mortality_03_15["FIPS"].notnull() == False)
    )
]
pop_mortality_03_15_cp = pop_mortality_03_15_df.copy()

## Change Population and Death data type from object to integer and float accordingly
pop_mortality_03_15_cp["Population"] = pop_mortality_03_15_cp["Population"].astype(int)
pop_mortality_03_15_cp["Deaths"] = pop_mortality_03_15_cp["Deaths"].astype(float)


## Confirm the county and state counts are to be expected
assert (len(pop_mortality_03_15_cp.County.unique() == 1897)) & (
    len(pop_mortality_03_15_cp.State.unique() == 50)
)
assert len(pop_mortality_03_15_cp.FIPS.unique()) == 3115


pop_mortality_03_15_cp[np.isnan(pop_mortality_03_15_cp["FIPS"])]

## Calculate drug mortality rate
pop_death_03_15 = pop_mortality_03_15_cp.copy()
pop_death_03_15["drug_mortality_per_capita"] = (
    pop_death_03_15["Deaths"] / pop_death_03_15["Population"]
)

## Oglala Lakota County was found to be missing FIPS code because the county was known as Shannon County (FIPS 46113) until May 2015
## Therefore, we decided to assign the FIPS code for Shannon County (FIPS 46113) to Oglala Lakota County
pop_death_03_15["FIPS"] = pop_death_03_15.apply(
    lambda row: 46113 if np.isnan(row["FIPS"]) else row["FIPS"], axis=1
)

## Due to the privacy censorship, we do not have data for smaller counties with less than 10 deaths.
## To avoid overinflation of death rate, we decided to assume a 0.01 death rate for small counties missing death data.
## This aligns with the domain knowlege that death is proportional to the population size.
pop_death_03_15["drug_mortality_per_capita"] = pop_death_03_15.apply(
    lambda row: 0.01
    if np.isnan(row["drug_mortality_per_capita"])
    else row["drug_mortality_per_capita"],
    axis=1,
)

# Drop unneeded columns
pop_death_03_15.drop(["County_State", "County Code", "_merge"], axis=1, inplace=True)


# Confirm there is no row with missing FIPS code
assert len(pop_death_03_15[pop_death_03_15.FIPS.isnull()]) == 0
# Comfirm there is no row with missing mortality per capita
assert len(pop_death_03_15[pop_death_03_15["drug_mortality_per_capita"].isnull()]) == 0


# Subset data to treatment states and control states
pop_mortality_states = pop_death_03_15[
    pop_death_03_15.State.isin(
        [
            "WA",
            "OR",
            "CA",
            "NV",
            "ID",
            "MT",
            "TX",
            "NM",
            "OK",
            "LA",
            "AZ",
            "CO",
            "FL",
            "GA",
            "SC",
            "AL",
            "MS",
        ]
    )
]


## Confirm that our final dataframe includes all 17 treatment and control states
assert len(pop_mortality_states.State.unique()) == 17

pop_mortality_states.to_csv(
    "https://github.com/MIDS-at-Duke/pds-2022-red-team/raw/main/20_intermediate_files/pop_mortality_merged.csv",
    encoding="utf-8",
    index=False,
)
