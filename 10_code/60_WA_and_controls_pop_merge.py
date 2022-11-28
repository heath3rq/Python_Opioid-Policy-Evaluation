import pandas as pd
import numpy as np


##import data
pop = pd.read_csv(
    "https://raw.githubusercontent.com/MIDS-at-Duke/pds-2022-red-team/main/20_intermediate_files/pop_merged.csv"
)
WA_pres = pd.read_csv(
    "https://raw.githubusercontent.com/MIDS-at-Duke/pds-2022-red-team/wa_and_comparisons/20_intermediate_files/Opioid_Prescriptions_WA_comparisons.csv"
)


WA_col = ["WA", "OR", "CA", "NV", "ID", "MT"]

# select only the states in Florida_col in population
WA_pop = pop[pop["State"].isin(WA_col)]


##find all county names ending with 'County' or 'Parish' except for Carson City
WA_pop[
    (~WA_pop["County"].str.contains("County"))
    & (~WA_pop["County"].str.contains("Parish"))
]


##define condition when fips is 32510
condition = WA_pop["fips"] == 32510

##add string to values in column equal to 'A'
WA_pop.loc[condition, "County"] = WA_pop["County"].astype(str) + " County"


##remove "County" and "Parish" from the county names in the FL population data
WA_pop["County"] = WA_pop["County"].str[:-7]


##drop the first column and rename the columns
WA_pres.drop(columns=["Unnamed: 0"], inplace=True)
WA_pres.rename(
    columns={
        "BUYER_STATE": "State",
        "BUYER_COUNTY": "County",
        "TRANSACTION_YEAR": "Year",
    },
    inplace=True,
)


##capitalize the first letter of each word in the County column
WA_pres["County"] = (WA_pres["County"].str.lower()).str.title()

##replace county names in WA_pres that are not aligh with county nanes from WA_pop
WA_pres["County"] = WA_pres["County"].replace("Lewis And Clark", "Lewis and Clark")


##check there's not mismatch between WA_pop and WA_pres
set(WA_pres["County"].unique()) - set(WA_pop["County"].unique())


WA_pop.drop(columns=["_merge"], inplace=True)


# Great, now can merge on state-county-year
WA_pres_pop = pd.merge(
    WA_pres,
    WA_pop,
    on=["Year", "State", "County"],
    validate="m:1",
    indicator=True,
)

WA_pres_pop["Shipment Rate Per Capita"] = WA_pres_pop["MME"] / WA_pres_pop["Population"]


WA_pres_pop.to_csv(
    # "https://github.com/MIDS-at-Duke/pds-2022-red-team/raw/main/20_intermediate_files/FL_and_controls_pres_pop_merge.csv",
    "/Users/jennyshen/Downloads/WA_and_controls_pop_merge.csv",
)
