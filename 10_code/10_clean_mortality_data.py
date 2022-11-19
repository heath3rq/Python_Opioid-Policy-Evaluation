## CleanUp Mortality Dataset
## Import necessary dependencies
import pandas as pd
import numpy as np

## Load mortality dataset
mortality = pd.read_csv(
    "https://github.com/MIDS-at-Duke/pds-2022-red-team/"
    "raw/main/20_intermediate_files/mortality_data.csv"
)

## Drop a column and remove Alaska from the data
mortality_df = mortality[mortality["County"].str.contains(", AK") == False].copy()

## Rename the county coulmn to avoid confusion
mortality_df.rename(
    columns={
        "County": "County_State",
    },
    inplace=True,
)

## Replace missing values with NaN
mortality_df = mortality_df.replace("Missing", np.NaN)

## Change deaths data type from object to float
mortality_df["Deaths"] = mortality_df["Deaths"].astype(float)

# Collapsing the dataset to get total number of deaths per county per year
mortality_cp = mortality_df.groupby(
    ["Year", "County Code", "County_State"], as_index=False
)["Deaths"].apply(lambda x: x.sum())

## Confirm data assumptions
assert len(mortality_cp["County_State"].unique()) == 3102
assert len(mortality_cp["Year"].unique()) == 13

## Upon investigation of discrenpencies between the FIPS code dataset and mortality dataset, we found that:
###The following counties exists in the mortality dataset but not in FIPS code dataset
#### Clifton Forge city, VA	: The independent city of Clifton Forge (FIPS 51560) merges into Alleghany county (FIPS 51005) in 2001.
##### We  will drop the only observation for Clifton Forge city in 2015 where the death count is missing because by then it is already merged into Allegphany county
mortality_cp.drop(
    [mortality_cp[mortality_cp["County Code"].isin([51560])].index[0]], inplace=True
)
#### Bedford city, VA: The independent city of Bedford (FIPS 51515) merges into Bedford County (FIPS 51019) in 2013.
##### No Adjustment is needed because the change happened close to 2015 and we have almost complete data for Bedford city from 2003 to 2015. Therefore, we will continue to treat it as an independent city

mortality_cp.to_csv(
    "/Users/qiujiahui/Desktop/Fall 2022/IDS 720 Practical Data Science/Group Project/"
    "pds-2022-red-team/20_intermediate_files/mortality_cleaned.csv",
    encoding="utf-8",
    index=False,
)
