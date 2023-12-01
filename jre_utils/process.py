import math
import pandas as pd


def get_most_active_municipalities(df, n=500, keep=[]):
    df["Prefecture_Municipality"] = df["Prefecture"] + "_" + df["Municipality"]

    most_active_areas = (
        df.groupby("Prefecture_Municipality")
        .agg({"Count": "sum"})
        .sort_values(by="Count", ascending=False)[:n]
        .reset_index()["Prefecture_Municipality"]
    )

    return df[
        (df["Prefecture_Municipality"].isin(most_active_areas))
        | df["Prefecture_Municipality"].isin(keep)
    ]


def get_cumulative_growth(df, column):
    df["Prefecture_Municipality"] = df["Prefecture"] + "_" + df["Municipality"]
    df["multiplier"] = df[column] + 1
    return df.groupby("Prefecture_Municipality")["multiplier"].cumprod()


def get_highest_growth_municipalities(
    df, column, cumulative_column, end_year, n=10, keep=[]
):
    df["Prefecture_Municipality"] = df["Prefecture"] + "_" + df["Municipality"]

    df["multiplier"] = df[column] + 1
    df[cumulative_column] = df.groupby("Prefecture_Municipality")[
        "multiplier"
    ].cumprod()

    highest_growth_municipalities = (
        df[df["year"] == end_year]
        .sort_values(by=cumulative_column, ascending=False)[:n][
            "Prefecture_Municipality"
        ]
        .unique()
    )

    lowest_growth_municipalities = (
        df[df["year"] == end_year]
        .sort_values(by=cumulative_column)[:n]["Prefecture_Municipality"]
        .unique()
    )

    return df[
        (df["Prefecture_Municipality"].isin(highest_growth_municipalities))
        | (df["Prefecture_Municipality"].isin(lowest_growth_municipalities))
        | df["Prefecture_Municipality"].isin(keep)
    ]
