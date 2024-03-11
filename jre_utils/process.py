def get_most_active_municipalities(df, count_column="count", n=500, keep=[]):
    most_active_areas = (
        df.groupby("area_code")
        .agg({count_column: "sum"})
        .sort_values(by=count_column, ascending=False)[:n]
        .reset_index()["area_code"]
    )

    return df[(df["area_code"].isin(most_active_areas)) | df["area_code"].isin(keep)]


def get_cumulative_growth(df, column):
    df["multiplier"] = df[column] + 1
    df = df.sort_values(by=["year", "area_code"], ascending=[True, True])
    return df.groupby("area_code")["multiplier"].cumprod()


def get_cumulative_growth_from_base(df, column):
    df = df.sort_values(by=["year", "area_code"], ascending=[True, True])
    df[f"{column}_yoy_growth"] = (
        df.groupby("area_code")[column].pct_change(periods=1).fillna(0)
    )
    return get_cumulative_growth(df, f"{column}_yoy_growth")


def get_highest_growth_municipalities(
    df, column, cumulative_column, end_year, n=10, keep=[]
):
    df["multiplier"] = df[column] + 1
    df = df.sort_values(by=["year", "area"], ascending=[True, True])
    df[cumulative_column] = df.groupby("area_code")["multiplier"].cumprod()

    highest_growth_municipalities = (
        df[df["year"] == end_year]
        .sort_values(by=cumulative_column, ascending=False)[:n]["area_code"]
        .unique()
    )

    lowest_growth_municipalities = (
        df[df["year"] == end_year]
        .sort_values(by=cumulative_column)[:n]["area_code"]
        .unique()
    )

    return df[
        (df["area_code"].isin(highest_growth_municipalities))
        | (df["area_code"].isin(lowest_growth_municipalities))
        | df["area_code"].isin(keep)
    ]


def get_window(df, area_code, year, window_length):
    return (
        df[(df["area_code"] == area_code) & (df["year"] <= year)]
        .sort_values(by="year")
        .tail(window_length)
    )
