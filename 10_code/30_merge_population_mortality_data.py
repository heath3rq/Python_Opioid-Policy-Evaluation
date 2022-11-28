### Merging Mortality and Population Data

## Import necessary dependencies
import pandas as pd
import numpy as np

## Read into tables
mortality = pd.read_csv(
    "https://github.com/MIDS-at-Duke/pds-2022-red-team/raw/main/20_intermediate_files/mortality_cleaned.csv",
    usecols=["County Code", "Year", "Deaths"],
)
pop = pd.read_csv(
    "https://github.com/MIDS-at-Duke/pds-2022-red-team/raw/main/20_intermediate_files/pop_merged.csv",
    usecols=["County", "Year", "Population", "State", "fips"],
)


## Merge population with mortality datasets
pop_mortality_03_15 = pop.merge(
    mortality,
    left_on=["fips", "Year"],
    right_on=["County Code", "Year"],
    how="outer",
    validate="m:m",
    indicator=True,
).drop(["County Code"], axis=1)
assert len(pop_mortality_03_15.fips.unique()) == 3114


## Subset data to treatment states and control states
states = [
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
pop_mortality_states = pop_mortality_03_15[
    pop_mortality_03_15.State.isin(states)
].copy()

## Confirm there is no row with missing FIPS code
assert pop_mortality_states.fips.notnull().all()

## Confirm that our final dataframe includes all 17 states
assert len(pop_mortality_states.State.unique()) == 17


## Change Population and Death data type from object to integer and float accordingly
pop_mortality_states["Population"] = pop_mortality_states["Population"].astype(int)
pop_mortality_states["Deaths"] = pop_mortality_states["Deaths"].astype(float)


pop_mortality_states._merge.value_counts()


pop_mortality_states[pop_mortality_states._merge == "left_only"]


## Calculate drug mortality rate
pop_death_03_15 = pop_mortality_states.copy()
pop_death_03_15["drug_mortality_per_capita"] = (
    pop_death_03_15["Deaths"] / pop_death_03_15["Population"]
)

## Due to the privacy censorship, we do not have data for smaller counties with less than 10 deaths.

## Imputation method 1: DO NOTHING as the 224 counties with no mortality data are really small
pop_death_03_15["drug_mortality_per_capita"] = pop_death_03_15[
    "drug_mortality_per_capita"
].fillna(0)

## Imputation method 2: To avoid potentially overinflation of death rate, we decided to assume a 0.01 death rate for small counties missing death data.
## This aligns with the domain knowlege that death is proportional to the population size.
# pop_death_03_15["drug_mortality_per_capita"] = pop_death_03_15.apply(
#     lambda row: 0.01
#     if np.isnan(row["drug_mortality_per_capita"])
#     else row["drug_mortality_per_capita"],
#     axis=1,
# )

# Comfirm there is no row with missing mortality per capita
assert pop_death_03_15.drug_mortality_per_capita.notnull().all()


pop_death_03_15.to_csv(
    ## Imputation Method 1
    "https://github.com/MIDS-at-Duke/pds-2022-red-team/raw/main/20_intermediate_files/pop_mortality_merged_no_imputation.csv",
    ## Imputation Method 2
    # "https://github.com/MIDS-at-Duke/pds-2022-red-team/raw/main/20_intermediate_files/pop_mortality_merged.csv",
    encoding="utf-8",
    index=False,
)
