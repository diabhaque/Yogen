import pandas as pd

from torchvision import transforms
from torch.utils.data import DataLoader

from jre_utils.data import JapanRETimeSeriesDataset, PadAndMask, ToNumpy, ToTensor


# def predict_periodic_return(
#     model, df, area_code, year, asset_type, metric, feature_columns, device="cpu"
# ):
#     area_row = df[
#         (df["year"] == year)
#         & (df["area_code"] == area_code)
#         & (df["asset_type"] == asset_type)
#     ]  # len == 1

#     area_dataset = JapanRETimeSeriesDataset(
#         df,
#         area_row,
#         feature_columns=feature_columns,
#         metrics=[metric],
#         transform=transforms.Compose([ToNumpy(), PadAndMask(), ToTensor()]),
#     )

#     area_dataloader = DataLoader(
#         area_dataset, batch_size=1, shuffle=False, num_workers=0
#     )

#     batch = next(iter(area_dataloader))

#     model.eval()

#     output = model(batch["window"].to(device), batch["mask"].to(device))
#     return output.item()


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


def predict_returns_unknown():
    pass
