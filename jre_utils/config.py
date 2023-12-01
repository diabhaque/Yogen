asset_types = {
    "land": {
        "label": "Residential Land(Land Only)",
        "metric": "UnitPrice",
        "metric_pct_chg": "UnitPricePctChg",
    },
    "building": {
        "label": "Residential Land(Land and Building)",
        "metric": "TradePricePerArea",
        "metric_pct_chg": "TradePricePctChg",
    },
}

statistics = {
    "mean": {"TradePricePerArea": "mean", "UnitPrice": "mean", "Count": "count"},
    "median": {"TradePricePerArea": "median", "UnitPrice": "median", "Count": "count"},
}

area_levels = {
    "prefecture": {"columns": ["Prefecture"]},
    "municipality": {"columns": ["Prefecture", "Municipality"]},
}

period_cols = {
    "yearly": "Year",
    "quarterly": "Date",
}
