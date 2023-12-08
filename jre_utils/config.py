asset_types = {
    "land": {
        "label": "Residential Land(Land Only)",
        "metric": "unit_price",
        "metric_pct_chg": "unit_price_pct_chg",
    },
    "building": {
        "label": "Residential Land(Land and Building)",
        "metric": "unit_price",
        "metric_pct_chg": "unit_price_pct_chg",
    },
}

statistics = {
    # should be weight average of unit price where weights are the areas
    "mean": {"unit_price": "mean", "count": "count"},
    "median": {"unit_price": "median", "count": "count"},
    "weighted_mean": {"unit_price": "mean", "count": "count"},
}

area_levels = {
    "area_code": {"columns": ["area", "area_code"]},
}

period_cols = {
    "yearly": "year",
    "quarterly": "date",
}
