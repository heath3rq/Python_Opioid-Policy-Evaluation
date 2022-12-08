import pandas as pd
import numpy as np

##import data
pop = pd.read_csv(
    "https://raw.githubusercontent.com/MIDS-at-Duke/pds-2022-red-team/main/20_intermediate_files/pop_merged.csv"
)
FL_pres = pd.read_csv(
    "https://raw.githubusercontent.com/MIDS-at-Duke/pds-2022-red-team/wa_and_comparisons/20_intermediate_files/Opioid_Prescriptions_FL_comparisons.csv"
)

##select FL and its control states
Florida_col = ["FL", "GA", "SC", "AL", "MS", "LA"]

# select only the states in Florida_col in population
FL_pop = pop[pop["State"].isin(Florida_col)]
FL_pop


##find all county names ending with 'County' or 'Parish'
FL_pop[
    (~FL_pop["County"].str.contains("County"))
    & (~FL_pop["County"].str.contains("Parish"))
]


##remove "County" and "Parish" from the county names in the FL population data
FL_pop["County"] = FL_pop["County"].str[:-7]
FL_pop


##drop the first column and rename the columns
FL_pres.drop(columns=["Unnamed: 0"], inplace=True)
FL_pres.rename(
    columns={
        "BUYER_STATE": "State",
        "BUYER_COUNTY": "County",
        "TRANSACTION_YEAR": "Year",
    },
    inplace=True,
)
FL_pres


##capitalize the first letter of each word in the County column
FL_pres["County"] = (FL_pres["County"].str.lower()).str.title()

##replace word in County column that contain Saint with St.
FL_pres["County"] = FL_pres["County"].replace(r"\w*Saint\w*", "St.", regex=True)

##replace county names in FL_pres that are not aligh with county nanes from FL_pop
FL_pres["County"] = FL_pres["County"].replace("De Kalb", "DeKalb")
FL_pres["County"] = FL_pres["County"].replace("Dekalb", "DeKalb")
FL_pres["County"] = FL_pres["County"].replace("Desoto", "DeSoto")
FL_pres["County"] = FL_pres["County"].replace("Mcintosh", "McIntosh")
FL_pres["County"] = FL_pres["County"].replace("Mccormick", "McCormick")
FL_pres["County"] = FL_pres["County"].replace("Mcduffie", "McDuffie")
FL_pres["County"] = FL_pres["County"].replace(
    "St John The Baptist", "St. John the Baptist"
)


##check there's not mismatch between FL_pop and FL_pres
set(FL_pres["County"].unique()) - set(FL_pop["County"].unique())

##drop the last column of FL_pop to enable merge
FL_pop.drop(columns=["_merge"], inplace=True)


##merge FL prescription data with FL population data
FL_pres_pop = pd.merge(
    FL_pres,
    FL_pop,
    on=["Year", "State", "County"],
    validate="m:1",
    indicator=True,
)

##append the shipment rate per capita to the FL_pres_pop
FL_pres_pop["Prescription Rate Per Capita"] = (
    FL_pres_pop["MME"] / FL_pres_pop["Population"]
)

FL_pres_pop.to_csv(
     "https://github.com/MIDS-at-Duke/pds-2022-red-team/raw/main/20_intermediate_files/FL_and_controls_pres_pop_merge.csv",
    #"/Users/jennyshen/Downloads/FL_and_controls_pres_pop_merge.csv",
)
