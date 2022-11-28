# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plotnine import *
import os

# %%
# Read data
df = pd.read_csv(
    "https://raw.githubusercontent.com/MIDS-at-Duke/pds-2022-red-team/main/20_intermediate_files/pop_mortality_merged_no_imputation.csv"
)

# %%
# Take a peep:
df.head()

# %%
df.isnull().sum()

# %%
#### post_analysis
def post_analysis(df, main_state, year_implementation, counter_state):
    """
    This function takes in a dataframe, a state, and a year of policy implementation
    and returns a post-analysis graph:

    Parameters:
    df (dataframe): dataframe with all the data
    main_state (str): state of interest
    year_implementation (int): year of policy implementation

    Returns:
    A plotnine plot
    """
    # DataFrame
    df_post = df.copy()
    df_post = df_post[~df_post["State"].isin(counter_state)]
    df_post["Years from Policy Change"] = df_post["Year"] - year_implementation
    df_post["Policy Change"] = df_post["State"] == main_state
    df_post["Drug Mortality Rate per 100,000 People"] = (
        df_post["drug_mortality_per_capita"] * 100000
    )
    treated_success = df_post[df_post["Policy Change"]]

    # Plot
    g = (
        ggplot(
            treated_success,
            aes(
                x="Years from Policy Change", y="Drug Mortality Rate per 100,000 People"
            ),
        )
        + geom_smooth(
            method="lm",
            data=treated_success[treated_success["Years from Policy Change"] < 0],
            se=True,
        )
        + geom_smooth(
            method="lm",
            data=treated_success[treated_success["Years from Policy Change"] >= 0],
            se=True,
        )
        + geom_vline(xintercept=0, linetype="dashed")
        + geom_text(x=-0.7, y=6.1, label="Policy Change", color="black")
        + labs(title="Pre-Post Model Graph, Effective Policy Intervention")
    )

    # print the plot
    print(g)


# %%
##### Florida #####
##### Effective February, 2010
post_analysis(df, "FL", 2010, [])

# %%
##### Washington #####
##### Effective Jan 2, 2012
post_analysis(df, "WA", 2012, [])

# %%
##### Texas ####
##### Effective Jan 4, 2007
post_analysis(df, "TX", 2007, [])

# %%
#### DID ####
# WA: OR, CA, NV, ID, MT
# TX: NM, OK, LA, AZ, CO
# FL: GA, SC, AL, MS, LA


def did_graph(df, state_compare, year_implementaion, main_state):
    """
    This function takes in a dataframe, a list of states to compare to, and the year of implementation
    and returns a graph of the difference in difference model

    df: dataframe
    state_compare: list of states to compare to, including the main state
    year_implementaion: year of implementation

    returns: graph
    """
    # Dataframe
    df_test = df[df.State.isin(state_compare)]
    df_test["Years from Policy Change"] = df_test["Year"] - year_implementaion
    df_test["Policy Change"] = df_test["State"] == main_state
    df_test["Drug Mortality Rate per 100,000 People"] = (
        df_test["drug_mortality_per_capita"] * 100000
    )

    # Plot
    g = (
        ggplot(
            df_test,
            aes(
                x="Years from Policy Change",
                y="Drug Mortality Rate per 100,000 People",
                color="Policy Change",
            ),
        )
        + geom_smooth(
            method="lm", data=df_test[df_test["Years from Policy Change"] < 0]
        )
        + geom_smooth(
            method="lm", data=df_test[df_test["Years from Policy Change"] >= 0]
        )
        + geom_vline(xintercept=0, linetype="dashed")
        + geom_text(x=-0.7, y=7, label="Policy Change", color="black")
        + labs(
            title="Diff-in-Diff Model Graph, Effective Policy Intervention",
            color="Counties in State with Policy Change",
        )
        + theme(legend_position="bottom")
    )

    # Show plot
    print(g)


# %%
florida = ["FL", "GA", "SC", "AL", "MS", "LA"]
Washington = ["WA", "OR", "CA", "NV", "ID", "MT"]
Texas = ["TX", "NM", "OK", "LA", "AZ", "CO"]

# %%
##### Florida #####
did_graph(df, florida, 2010, "FL")

# %%
##### Texas ####
did_graph(df, Texas, 2007, "TX")

# %%
##### Washington #####
did_graph(df, Washington, 2012, "WA")
