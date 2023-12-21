DATA_DIRECTORY_PATH = "../../data"

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
    },
}

model_ready_data_paths = {
    "xgb_transactions": f"{DATA_DIRECTORY_PATH}/model_ready/xgb_transactions.csv",
    "sequence_transactions": f"{DATA_DIRECTORY_PATH}/model_ready/sequence_transactions.csv",
    "xgb_plps": f"{DATA_DIRECTORY_PATH}/model_ready/xgb_plps.csv",
    "sequence_plps": f"{DATA_DIRECTORY_PATH}/model_ready/sequence_plps.csv",
    "xgb_lpa": f"{DATA_DIRECTORY_PATH}/model_ready/xgb_lpa.csv",
    "sequence_lpa": f"{DATA_DIRECTORY_PATH}/model_ready/sequence_lpa.csv",
}

pretraining_data_paths = {
    "jena_climate": f"{PRETRAINING_DATA_PATH}/jena_climate/jena_climate_2009_2016.csv",
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
