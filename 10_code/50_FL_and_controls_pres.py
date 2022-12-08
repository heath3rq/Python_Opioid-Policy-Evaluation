import pandas as pd
import numpy as np


# # Florida


# Read the data for FL
df_fl = pd.read_csv(
    "https://www.washingtonpost.com/wp-stat/dea-pain-pill-database/summary/arcos-fl-statewide-itemized.csv.gz",
    compression="gzip",
)
df_fl.head()


# check column names
df_fl.columns


# select columns of interest
selected_col = ["BUYER_STATE", "BUYER_COUNTY", "TRANSACTION_DATE", "MME"]
df_fl = df_fl[selected_col]
df_fl


# drop rows with missing values
df_fl = df_fl.drop(df_fl[df_fl["BUYER_COUNTY"].isnull()].index)


# assert no missing values in selected columns
# found missing values in BUYER_COUNTY

assert df_fl["BUYER_STATE"].notnull().all()
assert df_fl["BUYER_COUNTY"].notnull().all()
assert df_fl["TRANSACTION_DATE"].notnull().all()
assert df_fl["MME"].notnull().all()


df_fl["TRANSACTION_DATE"] = pd.to_datetime(df_fl["TRANSACTION_DATE"], format="%m%d%Y")
df_fl["TRANSACTION_YEAR"] = pd.DatetimeIndex(df_fl["TRANSACTION_DATE"]).year
# df_fl["MONTH"] = pd.DatetimeIndex(df_fl["TRANS_TIME"]).month
df_fl


# Group by County and year and calculate opioid quantity.
df_fl_county_yr = (
    df_fl.groupby(["BUYER_STATE", "BUYER_COUNTY", "TRANSACTION_YEAR"])
    .sum()
    .reset_index()
)
df_fl_county_yr


# # Georgia


# Read the data for GA
df_ga = pd.read_csv(
    "https://www.washingtonpost.com/wp-stat/dea-pain-pill-database/summary/arcos-ga-statewide-itemized.csv.gz",
    compression="gzip",
)
df_ga.head()


# filter columns of interest
df_ga = df_ga[selected_col]
df_ga


# drop rows with missing values
df_ga = df_ga.drop(df_ga[df_ga["BUYER_COUNTY"].isnull()].index)


# assert no missing values in selected columns
# found missing values in BUYER_COUNTY

assert df_ga["BUYER_STATE"].notnull().all()
assert df_ga["BUYER_COUNTY"].notnull().all()
assert df_ga["TRANSACTION_DATE"].notnull().all()
assert df_ga["MME"].notnull().all()


df_ga["TRANSACTION_DATE"] = pd.to_datetime(df_ga["TRANSACTION_DATE"], format="%m%d%Y")
df_ga["TRANSACTION_YEAR"] = pd.DatetimeIndex(df_ga["TRANSACTION_DATE"]).year
# df_ga["MONTH"] = pd.DatetimeIndex(df_or["TRANS_TIME"]).month
df_ga


# Group by County and year and calculate opioid quantity.
df_ga_county_yr = (
    df_ga.groupby(["BUYER_STATE", "BUYER_COUNTY", "TRANSACTION_YEAR"])
    .sum()
    .reset_index()
)
df_ga_county_yr


# # South Carolina


# Read the data for SC
df_sc = pd.read_csv(
    "https://www.washingtonpost.com/wp-stat/dea-pain-pill-database/summary/arcos-sc-statewide-itemized.csv.gz",
    compression="gzip",
)
df_sc.head()


# filter columns of interest
df_sc = df_sc[selected_col]
df_sc


# assert no missing values in selected columns
assert df_sc["BUYER_STATE"].notnull().all()
assert df_sc["BUYER_COUNTY"].notnull().all()
assert df_sc["TRANSACTION_DATE"].notnull().all()
assert df_sc["MME"].notnull().all()


df_sc["TRANSACTION_DATE"] = pd.to_datetime(df_sc["TRANSACTION_DATE"], format="%m%d%Y")
df_sc["TRANSACTION_YEAR"] = pd.DatetimeIndex(df_sc["TRANSACTION_DATE"]).year
# df_sc["MONTH"] = pd.DatetimeIndex(df_sc["TRANS_TIME"]).month
df_sc


# Group by County and year and calculate opioid quantity.
df_sc_county_yr = (
    df_sc.groupby(["BUYER_STATE", "BUYER_COUNTY", "TRANSACTION_YEAR"])
    .sum()
    .reset_index()
)
df_sc_county_yr


# # Alabama


# Read the data for AL
df_al = pd.read_csv(
    "https://www.washingtonpost.com/wp-stat/dea-pain-pill-database/summary/arcos-al-statewide-itemized.csv.gz",
    compression="gzip",
)
df_al.head()


# filter columns of interest
df_al = df_al[selected_col]
df_al


# assert no missing values in selected columns
assert df_al["BUYER_STATE"].notnull().all()
assert df_al["BUYER_COUNTY"].notnull().all()
assert df_al["TRANSACTION_DATE"].notnull().all()
assert df_al["MME"].notnull().all()


df_al["TRANSACTION_DATE"] = pd.to_datetime(df_al["TRANSACTION_DATE"], format="%m%d%Y")
df_al["TRANSACTION_YEAR"] = pd.DatetimeIndex(df_al["TRANSACTION_DATE"]).year
# df_al["MONTH"] = pd.DatetimeIndex(df_al["TRANS_TIME"]).month
df_al


# Group by County and year and calculate opioid quantity.
df_al_county_yr = (
    df_al.groupby(["BUYER_STATE", "BUYER_COUNTY", "TRANSACTION_YEAR"])
    .sum()
    .reset_index()
)
df_al_county_yr


# # Mississippi


# Read the data for MS
df_ms = pd.read_csv(
    "https://www.washingtonpost.com/wp-stat/dea-pain-pill-database/summary/arcos-ms-statewide-itemized.csv.gz",
    compression="gzip",
)
df_ms.head()


# filter columns of interest
df_ms = df_ms[selected_col]
df_ms


# assert no missing values in selected columns
assert df_ms["BUYER_STATE"].notnull().all()
assert df_ms["BUYER_COUNTY"].notnull().all()
assert df_ms["TRANSACTION_DATE"].notnull().all()
assert df_ms["MME"].notnull().all()


df_ms["TRANSACTION_DATE"] = pd.to_datetime(df_ms["TRANSACTION_DATE"], format="%m%d%Y")
df_ms["TRANSACTION_YEAR"] = pd.DatetimeIndex(df_ms["TRANSACTION_DATE"]).year
# df_ms["MONTH"] = pd.DatetimeIndex(df_ms["TRANS_TIME"]).month
df_ms


# Group by County and year and calculate opioid quantity.
df_ms_county_yr = (
    df_ms.groupby(["BUYER_STATE", "BUYER_COUNTY", "TRANSACTION_YEAR"])
    .sum()
    .reset_index()
)
df_ms_county_yr


# # Louisiana


# Read the data for LA
df_la = pd.read_csv(
    "https://www.washingtonpost.com/wp-stat/dea-pain-pill-database/summary/arcos-la-statewide-itemized.csv.gz",
    compression="gzip",
)
df_la.head()


# filter columns of interest
df_la = df_la[selected_col]
df_la


# assert no missing values in selected columns
assert df_la["BUYER_STATE"].notnull().all()
assert df_la["BUYER_COUNTY"].notnull().all()
assert df_la["TRANSACTION_DATE"].notnull().all()
assert df_la["MME"].notnull().all()


df_la["TRANSACTION_DATE"] = pd.to_datetime(df_la["TRANSACTION_DATE"], format="%m%d%Y")
df_la["TRANSACTION_YEAR"] = pd.DatetimeIndex(df_la["TRANSACTION_DATE"]).year
# df_la["MONTH"] = pd.DatetimeIndex(df_la["TRANS_TIME"]).month
df_la


# Group by County and year and calculate opioid quantity.
df_la_county_yr = (
    df_la.groupby(["BUYER_STATE", "BUYER_COUNTY", "TRANSACTION_YEAR"])
    .sum()
    .reset_index()
)
df_la_county_yr


# # Concatenate all the dataframes


Opioid_Prescriptions_FL_comparisons = pd.concat(
    (
        df_fl_county_yr,
        df_ga_county_yr,
        df_sc_county_yr,
        df_al_county_yr,
        df_ms_county_yr,
        df_la_county_yr,
    ),
    axis=0,
)
Opioid_Prescriptions_FL_comparisons


# assert no missing values in selected columns
assert Opioid_Prescriptions_FL_comparisons["BUYER_STATE"].notnull().all()
assert Opioid_Prescriptions_FL_comparisons["BUYER_COUNTY"].notnull().all()
assert Opioid_Prescriptions_FL_comparisons["TRANSACTION_YEAR"].notnull().all()
assert Opioid_Prescriptions_FL_comparisons["MME"].notnull().all()


# output to csv
Opioid_Prescriptions_FL_comparisons.to_csv(
    "https://github.com/MIDS-at-Duke/pds-2022-red-team/raw/main/20_intermediate_files/Opioid_Prescriptions_FL_comparisons.csv"
)
