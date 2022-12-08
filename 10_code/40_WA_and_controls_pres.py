import pandas as pd
import numpy as np
from datetime import datetime

# # Washington

# select columns of interest
selected_col = ["BUYER_STATE", "BUYER_COUNTY", "TRANSACTION_DATE", "MME"]

# Read the data for WA
custom_date_parser = lambda x: datetime.strptime(x, "%m%d%Y")
df_wa = pd.read_csv(
    "https://www.washingtonpost.com/wp-stat/dea-pain-pill-database/summary/arcos-wa-statewide-itemized.csv.gz",
    compression="gzip",
    usecols=selected_col,
    parse_dates=["TRANSACTION_DATE"],
    date_parser=custom_date_parser,
)
df_wa["TRANSACTION_YEAR"] = pd.DatetimeIndex(df_wa["TRANSACTION_DATE"]).year
# df_wa["MONTH"] = pd.DatetimeIndex(df_wa["TRANS_TIME"]).month


# assert no missing values in selected columns
assert df_wa["BUYER_STATE"].notnull().all()
assert df_wa["BUYER_COUNTY"].notnull().all()
assert df_wa["TRANSACTION_DATE"].notnull().all()
assert df_wa["MME"].notnull().all()


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
    usecols=selected_col,
    parse_dates=["TRANSACTION_DATE"],
    date_parser=custom_date_parser,
)
df_or["TRANSACTION_YEAR"] = pd.DatetimeIndex(df_or["TRANSACTION_DATE"]).year
# df_or["MONTH"] = pd.DatetimeIndex(df_or["TRANS_TIME"]).month

# assert no missing values in selected columns
assert df_or["BUYER_STATE"].notnull().all()
assert df_or["BUYER_COUNTY"].notnull().all()
assert df_or["TRANSACTION_DATE"].notnull().all()
assert df_or["MME"].notnull().all()


# Group by County and year and calculate opioid quantity.
df_or_county_yr = (
    df_or.groupby(["BUYER_STATE", "BUYER_COUNTY", "TRANSACTION_YEAR"])
    .sum()
    .reset_index()
)


# # California

# Read the data for CA
df_ca = pd.read_csv(
    "https://www.washingtonpost.com/wp-stat/dea-pain-pill-database/summary/arcos-ca-statewide-itemized.csv.gz",
    compression="gzip",
    usecols=selected_col,
    parse_dates=["TRANSACTION_DATE"],
    date_parser=custom_date_parser,
)
df_ca["TRANSACTION_YEAR"] = pd.DatetimeIndex(df_ca["TRANSACTION_DATE"]).year
# df_ca["MONTH"] = pd.DatetimeIndex(df_ca["TRANS_TIME"]).month


# drop rows with missing values
df_ca = df_ca.drop(df_ca[df_ca["BUYER_COUNTY"].isnull()].index)


# assert no missing values in selected columns
# found missing values in BUYER_COUNTY

assert df_ca["BUYER_STATE"].notnull().all()
assert df_ca["BUYER_COUNTY"].notnull().all()
assert df_ca["TRANSACTION_DATE"].notnull().all()
assert df_ca["MME"].notnull().all()


# Group by County and year and calculate opioid quantity.
df_ca_county_yr = (
    df_ca.groupby(["BUYER_STATE", "BUYER_COUNTY", "TRANSACTION_YEAR"])
    .sum()
    .reset_index()
)


# # Nevada


# Read the data for NV
df_nv = pd.read_csv(
    "https://www.washingtonpost.com/wp-stat/dea-pain-pill-database/summary/arcos-nv-statewide-itemized.csv.gz",
    compression="gzip",
    usecols=selected_col,
    parse_dates=["TRANSACTION_DATE"],
    date_parser=custom_date_parser,
)
df_nv["TRANSACTION_YEAR"] = pd.DatetimeIndex(df_nv["TRANSACTION_DATE"]).year
# df_nv["MONTH"] = pd.DatetimeIndex(df_nv["TRANS_TIME"]).month


# drop rows with missing values
df_nv = df_nv.drop(df_nv[df_nv["BUYER_COUNTY"].isnull()].index)


# assert no missing values in selected columns
# found missing values in BUYER_COUNTY

assert df_nv["BUYER_STATE"].notnull().all()
assert df_nv["BUYER_COUNTY"].notnull().all()
assert df_nv["TRANSACTION_DATE"].notnull().all()
assert df_nv["MME"].notnull().all()


# Group by County and year and calculate opioid quantity.
df_nv_county_yr = (
    df_nv.groupby(["BUYER_STATE", "BUYER_COUNTY", "TRANSACTION_YEAR"])
    .sum()
    .reset_index()
)


# # Idaho


# Read the data for ID
df_id = pd.read_csv(
    "https://www.washingtonpost.com/wp-stat/dea-pain-pill-database/summary/arcos-id-statewide-itemized.csv.gz",
    compression="gzip",
    usecols=selected_col,
    parse_dates=["TRANSACTION_DATE"],
    date_parser=custom_date_parser,
)
df_id["TRANSACTION_YEAR"] = pd.DatetimeIndex(df_id["TRANSACTION_DATE"]).year
# df_id["MONTH"] = pd.DatetimeIndex(df_id["TRANS_TIME"]).month


# assert no missing values in selected columns
assert df_id["BUYER_STATE"].notnull().all()
assert df_id["BUYER_COUNTY"].notnull().all()
assert df_id["TRANSACTION_DATE"].notnull().all()
assert df_id["MME"].notnull().all()


# Group by County and year and calculate opioid quantity.
df_id_county_yr = (
    df_id.groupby(["BUYER_STATE", "BUYER_COUNTY", "TRANSACTION_YEAR"])
    .sum()
    .reset_index()
)


# # Montana


# Read the data for MT
df_mt = pd.read_csv(
    "https://www.washingtonpost.com/wp-stat/dea-pain-pill-database/summary/arcos-mt-statewide-itemized.csv.gz",
    compression="gzip",
    usecols=selected_col,
    parse_dates=["TRANSACTION_DATE"],
    date_parser=custom_date_parser,
)
df_mt["TRANSACTION_YEAR"] = pd.DatetimeIndex(df_mt["TRANSACTION_DATE"]).year


# assert no missing values in selected columns
assert df_mt["BUYER_STATE"].notnull().all()
assert df_mt["BUYER_COUNTY"].notnull().all()
assert df_mt["TRANSACTION_DATE"].notnull().all()
assert df_mt["MME"].notnull().all()


# Group by County and year and calculate opioid quantity.
df_mt_county_yr = (
    df_mt.groupby(["BUYER_STATE", "BUYER_COUNTY", "TRANSACTION_YEAR"])
    .sum()
    .reset_index()
)


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
