import plotly.express as px
import matplotlib.pyplot as plt
from sklearn.metrics import PredictionErrorDisplay


def plot_time_series(
    df,
    column,
    group_by_columns,
    granularity_columns,
    title,
    visible=None,
    width=1600,
    height=800,
    showlegend=True,
    highlight=False,
    highlight_range=("2020", "2022"),
    highlight_color="LightSalmon",
    color_discrete_map={},
):
    plot_df = df.set_index(group_by_columns)
    plot_df = plot_df[column].unstack(list(range(len(granularity_columns))))
    plot_df.columns = [f"{a}" for a in plot_df.columns]

    fig = px.line(plot_df, y=plot_df.columns, title=title)

    for trace in fig.data:
        if color_discrete_map.get(trace.name) is not None:
            trace.line.color = color_discrete_map[trace.name]

    fig.update_traces(mode="lines+markers", visible=visible)
    fig.update_layout(
        autosize=False,
        width=width,
        height=height,
        hovermode="closest",
        showlegend=showlegend,
    )
    if highlight:
        fig.add_vrect(
            x0=highlight_range[0],
            x1=highlight_range[1],
            fillcolor=highlight_color,
            opacity=0.5,
            layer="below",
            line_width=0,
        )

    fig.show()


def plot_prediction_error_display(y, y_pred):
    _, ax = plt.subplots(figsize=(5, 5))
    display = PredictionErrorDisplay.from_predictions(
        y,
        y_pred,
        kind="actual_vs_predicted",
        ax=ax,
        scatter_kwargs={"alpha": 0.5},
    )
    ax.set_title("Actual vs Predicted")
    plt.tight_layout()
