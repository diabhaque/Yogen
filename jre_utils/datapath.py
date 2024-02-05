DATA_DIRECTORY_PATH = "../../data"
WEIGHTS_DIRECTORY_PATH = "../../weights"

PRETRAINING_DATA_PATH = f"{DATA_DIRECTORY_PATH}/pretraining"

DERIVED_DATA_PATH = f"{DATA_DIRECTORY_PATH}/derived/transactions"
DERIVED_DATA_PATH_LPA = f"{DATA_DIRECTORY_PATH}/derived/lpa"
DERIVED_DATA_PATH_PLPS = f"{DATA_DIRECTORY_PATH}/derived/plps"
DERIVED_DATA_PATH_LEGACY = f"{DATA_DIRECTORY_PATH}/derived/legacy"


factor_data_paths = {
    "unprocessed": {
        "population": {
            "prefecture": "",
            "municipality": f"{DATA_DIRECTORY_PATH}/municipality/unprocessed/population/population_2020.csv",
        },
        "birth_death": {
            "prefecture": "",
            "municipality": "",
        },
        "migration": {
            "prefecture": "",
            "municipality": f"{DATA_DIRECTORY_PATH}/municipality/unprocessed/migration/migration_1996_2022.csv",
        },
        "taxable_income": {
            "prefecture": "",
            "municipality": f"{DATA_DIRECTORY_PATH}/municipality/unprocessed/taxable_income/taxable_income_1985_2021.csv",
        },
        "taxpayer": {
            "prefecture": "",
            "municipality": f"{DATA_DIRECTORY_PATH}/municipality/unprocessed/taxpayer/taxpayer_1985_2021.csv",
        },
        "new_dwellings": {
            "prefecture": "",
            "municipality": f"{DATA_DIRECTORY_PATH}/municipality/unprocessed/dwelling/new_dwellings_2000_2021.csv",
        },
        "existing_dwellings": {
            "prefecture": "",
            "municipality": f"{DATA_DIRECTORY_PATH}/municipality/unprocessed/dwelling/existing_dwellings_2003_2018.csv",
        },
        "lfs_revenue_breakdown": {
            "prefecture": "",
            "municipality": f"{DATA_DIRECTORY_PATH}/municipality/unprocessed/lfs_revenue_breakdown/combined_1989_2022.csv",
        },
    },
    "processed": {
        "population": {
            "prefecture": "",
            "municipality": f"{DATA_DIRECTORY_PATH}/municipality/processed/population/population_est_2022.csv",
            "submunicipality": f"{DATA_DIRECTORY_PATH}/submunicipality/processed/population/population_est_2022.csv",
        },
        "birth_death": {
            "prefecture": "",
            "municipality": "",
            "submunicipality": "",
        },
        "migration": {
            "prefecture": "",
            "municipality": f"{DATA_DIRECTORY_PATH}/municipality/processed/migration/migration_1996_2022.csv",
            "submunicipality": f"{DATA_DIRECTORY_PATH}/submunicipality/processed/migration/migration_1996_2022.csv",
        },
        "taxable_income": {
            "prefecture": "",
            "municipality": f"{DATA_DIRECTORY_PATH}/municipality/processed/taxable_income/taxable_income_1985_2021.csv",
            "submunicipality": f"{DATA_DIRECTORY_PATH}/submunicipality/processed/taxable_income/taxable_income_1985_2021.csv",
        },
        "taxpayer": {
            "prefecture": "",
            "municipality": f"{DATA_DIRECTORY_PATH}/municipality/processed/taxpayer/taxpayer_1985_2021.csv",
            "submunicipality": f"{DATA_DIRECTORY_PATH}/submunicipality/processed/taxpayer/taxpayer_1985_2021.csv",
        },
        "new_dwellings": {
            "prefecture": "",
            "municipality": f"{DATA_DIRECTORY_PATH}/municipality/processed/dwelling/new_dwellings_2000_2021.csv",
            "submunicipality": f"{DATA_DIRECTORY_PATH}/submunicipality/processed/dwelling/new_dwellings_2000_2021.csv",
        },
        "existing_dwellings": {
            "prefecture": "",
            "municipality": f"{DATA_DIRECTORY_PATH}/municipality/processed/dwelling/existing_dwellings_2003_2018.csv",
            "submunicipality": f"{DATA_DIRECTORY_PATH}/submunicipality/processed/dwelling/existing_dwellings_2003_2018.csv",
        },
        "lfs_revenue_breakdown": {
            "prefecture": "",
            "municipality": f"{DATA_DIRECTORY_PATH}/municipality/processed/lfs_revenue_breakdown/combined_1989_2022.csv",
            "submunicipality": f"{DATA_DIRECTORY_PATH}/municipality/processed/lfs_revenue_breakdown/combined_1989_2022.csv",
        },
    },
}

dataset_types = ["transactions"]
asset_types = ["land", "building", "condo", "all"]
metrics = ["median_smoothed", "weighted_median_smoothed"]
years_ahead = [1, 2]
eval_years = [2020, 2021]

model_built_data_paths = {
    key: f"{DATA_DIRECTORY_PATH}/model_built/{key}.csv"
    for key in [
        f"sequence_{dataset_type}_{asset_type}_{metric}_{year_ahead}"
        for dataset_type in dataset_types
        for asset_type in asset_types
        for metric in metrics
        for year_ahead in years_ahead
    ]
}

model_ready_data_paths = {
    key: f"{DATA_DIRECTORY_PATH}/model_ready/{key}.csv"
    for key in [
        f"sequence_{dataset_type}_{asset_type}_{metric}_{year_ahead}"
        for dataset_type in dataset_types
        for asset_type in asset_types
        for metric in metrics
        for year_ahead in years_ahead
    ]
}

model_output_data_paths = {
    key: f"{DATA_DIRECTORY_PATH}/model_output/{key}.csv"
    for key in [
        f"sequence_{dataset_type}_{asset_type}_{metric}_{year_ahead}_{eval_year}"
        for dataset_type in dataset_types
        for asset_type in asset_types
        for metric in metrics
        for year_ahead in years_ahead
        for eval_year in eval_years
    ]
}


def get_derived_csv_path_legacy(asset_type):
    filename = f"{asset_type}.csv"
    return f"{DERIVED_DATA_PATH_LEGACY}/{filename}"


def get_derived_csv_path(asset_type):
    filename = f"{asset_type}.csv"
    return f"{DERIVED_DATA_PATH}/{filename}"


def get_derived_plps_path():
    filename = f"combined.csv"
    return f"{DERIVED_DATA_PATH_PLPS}/{filename}"


def get_derived_lpa_path():
    filename = f"combined.csv"
    return f"{DERIVED_DATA_PATH_LPA}/{filename}"
