import pandas as pd
import numpy as np
from scipy.stats import norm

import torch
import torch.nn.functional as F
from torch.utils.data import Dataset


class JapanRESpatialTimeSeriesDataset(Dataset):
    def __init__(
        self,
        complete_df,
        df,
        metrics,
        neighbours_dictionary,
        asset_type="building",  # building or land or condo
        weight_column=None,
        feature_columns=None,
        neighbour_feature_columns=None,
        shift=1,
        window_length=5,
        transform=None,
        type="regression",  # "regression" or "classification"
    ):
        self.feature_columns = (
            feature_columns if feature_columns is not None else df.columns
        )
        self.neighbour_feature_columns = (
            neighbour_feature_columns if neighbour_feature_columns is not None else []
        )
        self.complete_df = complete_df
        self.df = df
        self.neighbours_dictionary = neighbours_dictionary
        self.transform = transform
        self.metrics = metrics
        self.asset_type = asset_type
        self.weight_column = weight_column
        self.shift = shift
        self.window_length = window_length
        self.type = type

    def __len__(self):
        return len(self.df)

    def get_class(self, target):
        n_boundary = norm.ppf(1 / 3)
        p_boundary = norm.ppf(2 / 3)

        if target < n_boundary:
            return 0
        elif target > p_boundary:
            return 1
        else:
            return 2

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        row = self.df.iloc[idx]
        target = row[self.metrics]
        area_code, year = row["area_code"], row["year"]
        area_df = (
            self.complete_df[
                (self.complete_df["area_code"] == area_code)
                & (self.complete_df["year"] <= year - self.shift)
            ]
            .sort_values(by="year")
            .tail(self.window_length)
        )

        area_df["building"] = self.asset_type == "building"
        area_df["land"] = self.asset_type == "land"
        area_df["condo"] = self.asset_type == "condo"

        area_df = area_df[self.feature_columns + ["year"]].astype(float)

        # add all features from 5 nearest neighbours
        neighbours = self.neighbours_dictionary[area_code]
        for i, (neighbour, distance) in enumerate(neighbours.items()):
            neighbour_df = (
                self.complete_df[
                    (self.complete_df["area_code"] == neighbour)
                    & (self.complete_df["year"] <= year - self.shift)
                ]
                .sort_values(by="year")
                .tail(self.window_length)
            )
            neighbour_df = neighbour_df[self.neighbour_feature_columns + ["year"]]
            neighbour_df = neighbour_df.astype(float)
            neighbour_df[f"distance_n{i}"] = distance

            area_df = area_df.merge(
                neighbour_df,
                on=["year"],
                how="left",
                suffixes=("", f"_n{i}"),
            )

            # left merge causes nan values, fill them with 0
            area_df = area_df.fillna(0)

        sample = {
            "window": area_df.drop(columns=["year"]),
            "target": (
                target.astype(float)
                if self.type == "regression"
                else target.apply(self.get_class)
            ),
            "weight": (
                row[[self.weight_column]].astype(float)
                if self.weight_column is not None
                else pd.Series({self.weight_column: 1.0})
            ),
        }

        if self.transform:
            sample = self.transform(sample)

        return sample


class JapanRETimeSeriesDataset(Dataset):
    def __init__(
        self,
        complete_df,
        df,
        metrics,
        weight_column=None,
        asset_type="building",  # building or land or condo
        feature_columns=None,
        shift=1,
        window_length=5,
        transform=None,
        type="regression",  # "regression" or "classification"
    ):
        self.feature_columns = (
            feature_columns if feature_columns is not None else df.columns
        )
        self.complete_df = complete_df
        self.df = df
        self.transform = transform
        self.metrics = metrics
        self.weight_column = weight_column
        self.asset_type = asset_type
        self.shift = shift
        self.window_length = window_length
        self.type = type

    def __len__(self):
        return len(self.df)

    def get_class(self, target):
        n_boundary = norm.ppf(1 / 3)
        p_boundary = norm.ppf(2 / 3)

        if target < n_boundary:
            return 0
        elif target > p_boundary:
            return 1
        else:
            return 2

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        row = self.df.iloc[idx]
        target = row[self.metrics]
        area_code, year = row["area_code"], row["year"]
        area_df = (
            self.complete_df[
                (self.complete_df["area_code"] == area_code)
                & (self.complete_df["year"] <= year - self.shift)
            ]
            .sort_values(by="year")
            .tail(self.window_length)
        )

        area_df["building"] = self.asset_type == "building"
        area_df["land"] = self.asset_type == "land"
        area_df["condo"] = self.asset_type == "condo"

        sample = {
            "window": area_df[self.feature_columns].astype(float),
            "target": (
                target.astype(float)
                if self.type == "regression"
                else target.apply(self.get_class)
            ),
            "weight": (
                row[[self.weight_column]].astype(float)
                if self.weight_column is not None
                else pd.Series({self.weight_column: 1.0})
            ),
        }

        if self.transform:
            sample = self.transform(sample)

        return sample


class TimeSeriesDataset(Dataset):
    def __init__(
        self,
        df,
        metrics=["target"],
        weight_column=None,
        feature_columns=None,
        shift=1,
        window_length=6,
        transform=None,
    ):
        self.feature_columns = (
            feature_columns if feature_columns is not None else df.columns
        )
        self.df = df
        self.transform = transform
        self.metrics = metrics
        self.weight_column = weight_column
        self.shift = shift
        self.window_length = window_length

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        row = self.df.iloc[idx]
        target = row[self.metrics]

        window_end = idx - self.shift + 1
        window_start = max(window_end - self.window_length, 0)
        window_end = max(window_end, 0)
        window = self.df.iloc[window_start:window_end]

        sample = {
            "window": window[self.feature_columns],
            "target": target,
            "weight": (
                row[[self.weight_column]]
                if self.weight_column is not None
                else pd.Series({self.weight_column: 1.0})
            ),
        }

        if self.transform:
            sample = self.transform(sample)

        return sample


class ToNumpy(object):
    """Convert pandas dataframes in sample to ndarrays."""

    def __call__(self, sample):
        window, target, weight = sample["window"], sample["target"], sample["weight"]
        return {
            "window": window.values,
            "target": target.values,
            "weight": weight.values,
        }


class PadAndMask(object):
    """Pad all inputs to be of the same length and create a mask"""

    def __init__(self, pad_length=5):
        self.pad_length = pad_length

    def __call__(self, sample):
        window, target, weight = sample["window"], sample["target"], sample["weight"]

        # the first n elements of the mask are 1, the rest are 0
        mask = np.zeros(self.pad_length)
        mask[: window.shape[0]] = 1

        padded_window = np.pad(
            window, ((0, self.pad_length - window.shape[0]), (0, 0)), "constant"
        )
        return {
            "window": padded_window,
            "mask": mask,
            "target": target,
            "weight": weight,
        }


class ToTensor(object):
    """Convert ndarrays in sample to Tensors."""

    def __call__(self, sample):
        window, target, mask, weight = (
            sample["window"],
            sample["target"],
            sample["mask"],
            sample["weight"],
        )
        return {
            "window": torch.from_numpy(window).to(torch.float32),
            "mask": torch.from_numpy(mask).to(torch.float32),
            "target": torch.from_numpy(target).to(torch.float32),
            "weight": torch.from_numpy(weight).to(torch.float32),
        }
