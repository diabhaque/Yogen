import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


def plot_time_series(
    df, column, group_by_columns, granularity_columns, title, visible=None
):
    plot_df = df.set_index(group_by_columns)
    plot_df = plot_df[column].unstack(list(range(len(granularity_columns))))
    plot_df.columns = [f"{a}" for a in plot_df.columns]

    fig = px.line(plot_df, y=plot_df.columns, title=title)

    fig.update_traces(mode="lines+markers", visible=visible)
    fig.update_layout(autosize=False, width=1600, height=800, hovermode="closest")
    fig.show()
