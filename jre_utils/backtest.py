import pandas as pd
import numpy as np

from torchvision import transforms
from torch.utils.data import DataLoader

from jre_utils.data import JapanRETimeSeriesDataset, PadAndMask, ToNumpy, ToTensor


class Portfolio:
    def __init__(self, assets={}, liabilities={}, cash=1000):
        self.assets = assets
        self.liabilities = liabilities
        self.cash = cash

    def nav(self):
        return sum(self.assets.values()) - sum(self.liabilities.values()) + self.cash


class Timeline:
    def __init__(self, initial_year: int, initial_portfolio: Portfolio):
        self.curve = {initial_year: initial_portfolio}
        self.current_year = initial_year
        self.rebalancing_years = []

    def get_portfolio(self, year):
        return self.curve[year]

    def get_current_portfolio(self):
        return self.get_portfolio(self.current_year)

    def add_portfolio(self, year, portfolio):
        self.curve[year] = portfolio
        self.current_year = year

    def remark(self, year, current_year_df):
        portfolio = self.get_current_portfolio()
        assets, liabilities, cash = (
            portfolio.assets,
            portfolio.liabilities,
            portfolio.cash,
        )

        remarked_assets = {
            area_code: value
            * (1 + current_year_df.loc[area_code, "yearly_price_growth"])
            for area_code, value in assets.items()
        }

        remarked_liabiities = {
            area_code: value
            * (1 + current_year_df.loc[area_code, "yearly_price_growth"])
            for area_code, value in liabilities.items()
        }

        remarked_portfolio = Portfolio(remarked_assets, remarked_liabiities, cash)

        self.add_portfolio(year, remarked_portfolio)

    def rebalance(self, top_areas, bottom_areas):
        # Close all positions
        cash = self.get_current_portfolio().nav()

        # Invest
        assets = {area_code: cash * (1 / len(top_areas)) for area_code in top_areas}

        # Short
        liabilities = {
            area_code: cash * (1 / len(bottom_areas)) for area_code in bottom_areas
        }

        # Pay
        cash -= sum(assets.values())
        cash += sum(liabilities.values())

        rebalanced_portfolio = Portfolio(assets, liabilities, cash)
        self.add_portfolio(self.current_year, rebalanced_portfolio)
        self.rebalancing_years.append(self.current_year)

    def calculate_annualized_return(self):
        timeline = sorted(self.curve.items(), key=lambda x: x[0])
        initial_nav = timeline[0][1].nav()
        ending_nav = timeline[-1][1].nav()
        return (ending_nav / initial_nav) ** (1 / len(timeline)) - 1

    def calculate_sharpe_ratio(self, risk_free_rate=0.0):
        """
        Risk Free rate is zero in Japan
        """
        timeline = sorted(self.curve.items(), key=lambda x: x[0])
        navs = [portfolio.nav() for year, portfolio in timeline]
        returns = np.diff(navs) / navs[:-1]
        return (np.mean(returns) - risk_free_rate) / np.std(returns)

    def calculate_asset_rebalancing_ratio(self):
        rebalancing_ratios = []
        for y1, y2 in zip(self.rebalancing_years, self.rebalancing_years[1:]):
            y1_assets = self.curve[y1].assets.keys()
            y2_assets = self.curve[y2].assets.keys()

            maintained_assets = [
                y1_asset for y1_asset in y1_assets if y1_asset in y2_assets
            ]
            rebalancing_ratio = 1 - len(maintained_assets) / len(y1_assets)
            rebalancing_ratios.append((y2, rebalancing_ratio))
            print(f"{y2} Rebalancing ratio: {rebalancing_ratio:.2f}")

        return rebalancing_ratios

    def calculate_liabilities_rebalancing_ratio(self):
        rebalancing_ratios = []
        for y1, y2 in zip(self.rebalancing_years, self.rebalancing_years[1:]):
            y1_liabilities = self.curve[y1].liabilities.keys()
            y2_liabilities = self.curve[y2].liabilities.keys()

            maintained_assets = [
                y1_liability
                for y1_liability in y1_liabilities
                if y1_liability in y2_liabilities
            ]
            rebalancing_ratio = 1 - len(maintained_assets) / len(y1_liabilities)
            rebalancing_ratios.append((y2, rebalancing_ratio))
            print(f"{y2} Rebalancing ratio: {rebalancing_ratio:.2f}")

        return rebalancing_ratios


def predict_periodic_return(
    model, df, area_code, year, asset_type, feature_columns, device="cpu"
):
    sample = {
        "window": df[
            (df["area_code"] == area_code)
            & (df["asset_type"] == asset_type)
            & (df["year"] <= year - 2)
        ]
        .sort_values(by="year")
        .tail(5)[feature_columns],
        "target": pd.DataFrame(),
        "weight": pd.DataFrame(),
    }

    transform = transforms.Compose([ToNumpy(), PadAndMask(), ToTensor()])
    sample = transform(sample)
    window = sample["window"].unsqueeze(0).to(device)
    mask = sample["mask"].unsqueeze(0).to(device)

    model.eval()
    output = model(window, mask)
    return output.item()


def predict_returns(model, complete_df, prediction_df, feature_columns, device="cpu"):
    return prediction_df.apply(
        lambda row: predict_periodic_return(
            model,
            complete_df,
            row["area_code"],
            row["year"],
            row["asset_type"],
            feature_columns,
            device,
        ),
        axis=1,
    )
