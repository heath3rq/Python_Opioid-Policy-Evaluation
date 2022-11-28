# %%
import pandas as pd
import numpy as np

# %%
root = [
    "https://raw.githubusercontent.com/MIDS-at-Duke/pds-2022-red-team/main/00_source_data/US_VitalStatistics/Underlying%20Cause%20of%20Death%2C%202003.txt?token=GHSAT0AAAAAABZL3TDWMAAEZGADCVDLZRK2Y3MJVHA",
    "https://raw.githubusercontent.com/MIDS-at-Duke/pds-2022-red-team/main/00_source_data/US_VitalStatistics/Underlying%20Cause%20of%20Death%2C%202004.txt?token=GHSAT0AAAAAABZL3TDXSZUJGNLIHOU6TQXIY3MJX4Q",
    "https://raw.githubusercontent.com/MIDS-at-Duke/pds-2022-red-team/main/00_source_data/US_VitalStatistics/Underlying%20Cause%20of%20Death%2C%202005.txt?token=GHSAT0AAAAAABZL3TDWQAZPZYYDNC2M6G46Y3MJYKQ",
    "https://raw.githubusercontent.com/MIDS-at-Duke/pds-2022-red-team/main/00_source_data/US_VitalStatistics/Underlying%20Cause%20of%20Death%2C%202006.txt?token=GHSAT0AAAAAABZL3TDWBGSDCNH7EVXPARA4Y3MJYVA",
    "https://raw.githubusercontent.com/MIDS-at-Duke/pds-2022-red-team/main/00_source_data/US_VitalStatistics/Underlying%20Cause%20of%20Death%2C%202007.txt?token=GHSAT0AAAAAABZL3TDXMW7NMOF43UOZKA54Y3MJ4FA",
    "https://raw.githubusercontent.com/MIDS-at-Duke/pds-2022-red-team/main/00_source_data/US_VitalStatistics/Underlying%20Cause%20of%20Death%2C%202008.txt?token=GHSAT0AAAAAABZL3TDXGNJNYHURXROTD5AEY3MJ45A",
    "https://raw.githubusercontent.com/MIDS-at-Duke/pds-2022-red-team/main/00_source_data/US_VitalStatistics/Underlying%20Cause%20of%20Death%2C%202009.txt?token=GHSAT0AAAAAABZL3TDWBZFLPU7ARU5UF45CY3MJ5EQ",
    "https://raw.githubusercontent.com/MIDS-at-Duke/pds-2022-red-team/main/00_source_data/US_VitalStatistics/Underlying%20Cause%20of%20Death%2C%202010.txt?token=GHSAT0AAAAAABZL3TDW5WABXLBLMP5MPTMUY3MJ5PA",
    "https://raw.githubusercontent.com/MIDS-at-Duke/pds-2022-red-team/main/00_source_data/US_VitalStatistics/Underlying%20Cause%20of%20Death%2C%202011.txt?token=GHSAT0AAAAAABZL3TDWQLT7RUM5AXTLGK3AY3MJ5WQ",
    "https://raw.githubusercontent.com/MIDS-at-Duke/pds-2022-red-team/main/00_source_data/US_VitalStatistics/Underlying%20Cause%20of%20Death%2C%202012.txt?token=GHSAT0AAAAAABZL3TDWGAUY3PLSG5OP6UWCY3MJ62Q",
    "https://raw.githubusercontent.com/MIDS-at-Duke/pds-2022-red-team/main/00_source_data/US_VitalStatistics/Underlying%20Cause%20of%20Death%2C%202013.txt?token=GHSAT0AAAAAABZL3TDX6IVI4T4E22FXAPWOY3MJ7GA",
    "https://raw.githubusercontent.com/MIDS-at-Duke/pds-2022-red-team/main/00_source_data/US_VitalStatistics/Underlying%20Cause%20of%20Death%2C%202014.txt?token=GHSAT0AAAAAABZL3TDXG7NJVFUWBDKV6A4UY3MJ7NA",
    "https://raw.githubusercontent.com/MIDS-at-Duke/pds-2022-red-team/main/00_source_data/US_VitalStatistics/Underlying%20Cause%20of%20Death%2C%202015.txt?token=GHSAT0AAAAAABZL3TDW5XDR6LTD7GUVFVZSY3MJ7UA",
]


# %%
data = pd.DataFrame()
for i in root:
    df = pd.read_csv(i, delimiter="\t")
    df = df[df["Notes"].isna()]
    data = pd.concat([data, df], axis=0, ignore_index=True)

# %%
data.drop(columns="Notes")

# %%
data.to_csv("final_data.csv")
