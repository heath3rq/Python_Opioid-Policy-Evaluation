## Cleanup & Filter Mortality Dataset
## Import necessary dependencies
import pandas as pd
import numpy as np

## Load mortality dataset
mortality = pd.read_csv(
    "https://github.com/MIDS-at-Duke/pds-2022-red-team/"
    "raw/main/20_intermediate_files/mortality_data.csv",
    usecols=[
        "County",
        "County Code",
        "Year",
        "Drug/Alcohol Induced Cause",
        "Drug/Alcohol Induced Cause Code",
        "Deaths",
    ],
)


## Drop  Alaska from the data
mortality_df = mortality[mortality["County"].str.contains(", AK") == False].copy()

## Rename the county coulmn to avoid confusion
mortality_df.rename(
    columns={
        "County": "County_State",
    },
    inplace=True,
)


## Subset to all Drug-Related Causes
### Though Drug poisonings (overdose) Homicide (X85) - D3 also counts drug-related deaths,
### among the five observations we have, all data are missing from this category.
### Therefore, we will exclude D3 from our analysis
Drug_Induced_Cause_Code = ["D1", "D9", "D2", "D4"]

death = mortality_df[
    mortality_df["Drug/Alcohol Induced Cause Code"].isin(Drug_Induced_Cause_Code)
]

## Replace missing values with NaN
death = death.replace("Missing", np.NaN)

## Change deaths data type from object to float
death["Deaths"] = death["Deaths"].astype(float)


# Collapsing the dataset to get total number of deaths per county per year
death_cp = death.groupby(["Year", "County Code", "County_State"], as_index=False)[
    "Deaths"
].apply(lambda x: x.sum())


## Confirm data assumptions
assert death_cp["County Code"].notnull().all()
assert len(death_cp["Year"].unique()) == 13


death_cp.to_csv(
    "https://github.com/MIDS-at-Duke/pds-2022-red-team/raw/main/20_intermediate_files/mortality_cleaned.csv",
    encoding="utf-8",
    index=False,
)
