import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plotnine import *
import os


# Read data
FL_control = pd.read_csv(
    "https://raw.githubusercontent.com/MIDS-at-Duke/pds-2022-red-team/main/20_intermediate_files/FL_and_controls_pres_pop_merge.csv"
)
# FL_control.head()


# Read data
WA_control = pd.read_csv(
    "https://raw.githubusercontent.com/MIDS-at-Duke/pds-2022-red-team/main/20_intermediate_files/WA_and_controls_pres_pop_merge.csv"
)
# WA_control.head()


### pre-post analysis
def pre_post_graph(df, treatment_state, year_implementation):
    """
    This function takes in a dataframe, a treatment state, and the year of policy implementation
    and returns a pre-post analysis graph:

    Parameters:
    df (dataframe): dataframe with all the data
    treatment_state (str): state of interest
    year_implementation (int): year of policy implementation

    Returns:
    A plotnine plot
    """
    # DataFrame
    df_pre_post = df.copy()
    df_pre_post["Policy Change"] = df_pre_post["State"] == treatment_state
    df_pre_post["Years from Policy Change"] = df_pre_post["Year"] - year_implementation
    treated_success = df_pre_post[df_pre_post["Policy Change"]]

    # Plot
    pre_post = (
        ggplot(
            treated_success,
            aes(x="Year", y="Prescription Rate Per Capita"),
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
        + geom_vline(xintercept=year_implementation, linetype="dashed")
        + geom_text(x=-0.7, y=6.1, label="Policy Change", color="black")
        + xlab("Year")
        + ylab("Morphine Milligram Equivalents per Capita")
    )

    return pre_post


##### Florida #####
##### Effective February, 2010
pre_post_FL = pre_post_graph(FL_control, "FL", 2010) + labs(
    title="Pre-post Analysis of Opioid Shipments (in MME per Capita) for Florida"
)
ggsave(plot=pre_post_FL, filename="Pre_Post_FL_Opiod_Shipment.png")
# print(pre_post_FL)


##### Washington #####
##### Effective Jan 2, 2012
pre_post_WA = pre_post_graph(WA_control, "WA", 2012) + labs(
    title="Pre-post Analysis of Opioid Shipments (in MME per Capita) for Washington"
)
ggsave(plot=pre_post_WA, filename="Pre_Post_WA_Opiod_Shipment.png")
# print(pre_post_WA)


#### DID ####


##no need to define control state in this function due to the filtered dataset with only treatment state and its control states
def did_graph(df, treatment_state, year_implementaion):
    """
    This function takes in a dataframe, a list of states to compare to, and the year of implementation
    and returns a graph of the difference in difference model

    df: dataframe
    treatment_state (str): state of interest
    year_implementaion: year of implementation

    returns: graph
    """
    # Dataframe
    df_did = df.copy()
    df_did["Policy Change"] = df_did["State"] == treatment_state
    df_did["Years from Policy Change"] = df_did["Year"] - year_implementaion

    # Plot
    did = (
        ggplot(
            df_did,
            aes(
                x="Year",
                y="Prescription Rate Per Capita",
                color="Policy Change",
            ),
        )
        + geom_smooth(method="lm", data=df_did[df_did["Years from Policy Change"] < 0])
        + geom_smooth(method="lm", data=df_did[df_did["Years from Policy Change"] >= 0])
        + geom_vline(xintercept=year_implementaion, linetype="dashed")
        + geom_text(x=-0.7, y=7, label="Policy Change", color="black")
        + xlab("Year")
        + ylab("Morphine Milligram Equivalents per Capita")
    )

    return did


##### Florida #####
# FL_control_states = ["GA", "SC", "AL", "MS", "LA"]
did_FL = did_graph(FL_control, "FL", 2010) + labs(
    title="Diff-in-Diff Analysis of Opioid Shipments (in MME per Capita) \n for Florida vs Control State"
)

ggsave(plot=did_FL, filename="DID_FL_controls_Opiod_Shipment.png")
# print(did_FL)


##### Washington #####
# WA_control_states = ["OR", "CA", "NV", "ID", "MT"]

did_WA = did_graph(WA_control, "WA", 2012) + labs(
    title="Diff-in-Diff Analysis of Opioid Shipments (in MME per Capita) \n for Washington vs Control State"
)
ggsave(plot=did_WA, filename="DID_WA_controls_Opiod_Shipment.png")
# print(did_WA)
