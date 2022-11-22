import pandas as pd
import numpy as np


# # Washington

# Read the data for WA
df_wa = pd.read_csv(
    "https://www.washingtonpost.com/wp-stat/dea-pain-pill-database/summary/arcos-wa-statewide-itemized.csv.gz",
    # "/Users/jennyshen/Desktop/Opioid_Prescriptions_WA_comparisons/arcos-wa-statewide-itemized.csv.gz",
    compression="gzip",
)
df_wa.head()


# check column names
df_wa.columns


# select columns of interest
selected_col = ["BUYER_STATE", "BUYER_COUNTY", "TRANSACTION_DATE", "MME"]
df_wa = df_wa[selected_col]
df_wa


# assert no missing values in selected columns
assert df_wa["BUYER_STATE"].notnull().all()
assert df_wa["BUYER_COUNTY"].notnull().all()
assert df_wa["TRANSACTION_DATE"].notnull().all()
assert df_wa["MME"].notnull().all()


df_wa["TRANSACTION_DATE"] = pd.to_datetime(df_wa["TRANSACTION_DATE"], format="%m%d%Y")
df_wa["TRANSACTION_YEAR"] = pd.DatetimeIndex(df_wa["TRANSACTION_DATE"]).year
# df_wa["MONTH"] = pd.DatetimeIndex(df_wa["TRANS_TIME"]).month
df_wa


# Group by County and year and calculate opioid quantity.
df_wa_county_yr = (
    df_wa.groupby(["BUYER_STATE", "BUYER_COUNTY", "TRANSACTION_YEAR"])
    .sum()
    .reset_index()
)
df_wa_county_yr


# # Oregon


# Read the data for OR
df_or = pd.read_csv(
    "https://www.washingtonpost.com/wp-stat/dea-pain-pill-database/summary/arcos-or-statewide-itemized.csv.gz",
    compression="gzip",
)
df_or.head()


# filter columns of interest
df_or = df_or[selected_col]
df_or


# assert no missing values in selected columns
assert df_or["BUYER_STATE"].notnull().all()
assert df_or["BUYER_COUNTY"].notnull().all()
assert df_or["TRANSACTION_DATE"].notnull().all()
assert df_or["MME"].notnull().all()


df_or["TRANSACTION_DATE"] = pd.to_datetime(df_or["TRANSACTION_DATE"], format="%m%d%Y")
df_or["TRANSACTION_YEAR"] = pd.DatetimeIndex(df_or["TRANSACTION_DATE"]).year
# df_or["MONTH"] = pd.DatetimeIndex(df_or["TRANS_TIME"]).month
df_or


# Group by County and year and calculate opioid quantity.
df_or_county_yr = (
    df_or.groupby(["BUYER_STATE", "BUYER_COUNTY", "TRANSACTION_YEAR"])
    .sum()
    .reset_index()
)
df_or_county_yr


# # California


# Read the data for CA
df_ca = pd.read_csv(
    "https://www.washingtonpost.com/wp-stat/dea-pain-pill-database/summary/arcos-ca-statewide-itemized.csv.gz",
    compression="gzip",
)
df_ca.head()


# filter columns of interest
df_ca = df_ca[selected_col]
df_ca


# drop rows with missing values
df_ca = df_ca.drop(df_ca[df_ca["BUYER_COUNTY"].isnull()].index)


# assert no missing values in selected columns
# found missing values in BUYER_COUNTY

assert df_ca["BUYER_STATE"].notnull().all()
assert df_ca["BUYER_COUNTY"].notnull().all()
assert df_ca["TRANSACTION_DATE"].notnull().all()
assert df_ca["MME"].notnull().all()


df_ca["TRANSACTION_DATE"] = pd.to_datetime(df_ca["TRANSACTION_DATE"], format="%m%d%Y")
df_ca["TRANSACTION_YEAR"] = pd.DatetimeIndex(df_ca["TRANSACTION_DATE"]).year
# df_ca["MONTH"] = pd.DatetimeIndex(df_ca["TRANS_TIME"]).month
df_ca


# Group by County and year and calculate opioid quantity.
df_ca_county_yr = (
    df_ca.groupby(["BUYER_STATE", "BUYER_COUNTY", "TRANSACTION_YEAR"])
    .sum()
    .reset_index()
)
df_ca_county_yr


# # Nevada


# Read the data for NV
df_nv = pd.read_csv(
    "https://www.washingtonpost.com/wp-stat/dea-pain-pill-database/summary/arcos-nv-statewide-itemized.csv.gz",
    compression="gzip",
)
df_nv.head()


# filter columns of interest
df_nv = df_nv[selected_col]
df_nv


# drop rows with missing values
df_nv = df_nv.drop(df_nv[df_nv["BUYER_COUNTY"].isnull()].index)


# assert no missing values in selected columns
# found missing values in BUYER_COUNTY

assert df_nv["BUYER_STATE"].notnull().all()
assert df_nv["BUYER_COUNTY"].notnull().all()
assert df_nv["TRANSACTION_DATE"].notnull().all()
assert df_nv["MME"].notnull().all()


df_nv["TRANSACTION_DATE"] = pd.to_datetime(df_nv["TRANSACTION_DATE"], format="%m%d%Y")
df_nv["TRANSACTION_YEAR"] = pd.DatetimeIndex(df_nv["TRANSACTION_DATE"]).year
# df_nv["MONTH"] = pd.DatetimeIndex(df_nv["TRANS_TIME"]).month
df_nv


# Group by County and year and calculate opioid quantity.
df_nv_county_yr = (
    df_nv.groupby(["BUYER_STATE", "BUYER_COUNTY", "TRANSACTION_YEAR"])
    .sum()
    .reset_index()
)
df_nv_county_yr


# # Idaho


# Read the data for ID
df_id = pd.read_csv(
    "https://www.washingtonpost.com/wp-stat/dea-pain-pill-database/summary/arcos-id-statewide-itemized.csv.gz",
    compression="gzip",
)
df_id.head()


# filter columns of interest
df_id = df_id[selected_col]
df_id


# assert no missing values in selected columns
assert df_id["BUYER_STATE"].notnull().all()
assert df_id["BUYER_COUNTY"].notnull().all()
assert df_id["TRANSACTION_DATE"].notnull().all()
assert df_id["MME"].notnull().all()


df_id["TRANSACTION_DATE"] = pd.to_datetime(df_id["TRANSACTION_DATE"], format="%m%d%Y")
df_id["TRANSACTION_YEAR"] = pd.DatetimeIndex(df_id["TRANSACTION_DATE"]).year
# df_id["MONTH"] = pd.DatetimeIndex(df_id["TRANS_TIME"]).month
df_id


# Group by County and year and calculate opioid quantity.
df_id_county_yr = (
    df_id.groupby(["BUYER_STATE", "BUYER_COUNTY", "TRANSACTION_YEAR"])
    .sum()
    .reset_index()
)
df_id_county_yr


# # Montana


# Read the data for MT
df_mt = pd.read_csv(
    "https://www.washingtonpost.com/wp-stat/dea-pain-pill-database/summary/arcos-mt-statewide-itemized.csv.gz",
    compression="gzip",
)
df_mt.head()


# filter columns of interest
df_mt = df_mt[selected_col]
df_mt


# assert no missing values in selected columns
assert df_mt["BUYER_STATE"].notnull().all()
assert df_mt["BUYER_COUNTY"].notnull().all()
assert df_mt["TRANSACTION_DATE"].notnull().all()
assert df_mt["MME"].notnull().all()


df_mt["TRANSACTION_DATE"] = pd.to_datetime(df_mt["TRANSACTION_DATE"], format="%m%d%Y")
df_mt["TRANSACTION_YEAR"] = pd.DatetimeIndex(df_mt["TRANSACTION_DATE"]).year
# df_mt["MONTH"] = pd.DatetimeIndex(df_mt["TRANS_TIME"]).month
df_mt


# Group by County and year and calculate opioid quantity.
df_mt_county_yr = (
    df_mt.groupby(["BUYER_STATE", "BUYER_COUNTY", "TRANSACTION_YEAR"])
    .sum()
    .reset_index()
)
df_mt_county_yr


# # Concatenate all the dataframes


Opioid_Prescriptions_WA_comparisons = pd.concat(
    (
        df_wa_county_yr,
        df_or_county_yr,
        df_ca_county_yr,
        df_nv_county_yr,
        df_id_county_yr,
        df_mt_county_yr,
    ),
    axis=0,
)
Opioid_Prescriptions_WA_comparisons


# assert no missing values in selected columns
assert Opioid_Prescriptions_WA_comparisons["BUYER_STATE"].notnull().all()
assert Opioid_Prescriptions_WA_comparisons["BUYER_COUNTY"].notnull().all()
assert Opioid_Prescriptions_WA_comparisons["TRANSACTION_YEAR"].notnull().all()
assert Opioid_Prescriptions_WA_comparisons["MME"].notnull().all()


# output to csv
Opioid_Prescriptions_WA_comparisons.to_csv(
    "https://github.com/MIDS-at-Duke/pds-2022-red-team/raw/main/20_intermediate_files/Opioid_Prescriptions_WA_comparisons.csv"
)
