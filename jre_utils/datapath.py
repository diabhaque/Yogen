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

model_ready_data_paths = {
    "sequence_transactions_weighted_mean_smoothed_1": f"{DATA_DIRECTORY_PATH}/model_ready/sequence_transactions_weighted_mean_smoothed_1.csv",
    "sequence_transactions_weighted_median_smoothed_1": f"{DATA_DIRECTORY_PATH}/model_ready/sequence_transactions_weighted_median_smoothed_1.csv",
    "sequence_transactions_mean_smoothed_1": f"{DATA_DIRECTORY_PATH}/model_ready/sequence_transactions_mean_smoothed_1.csv",
    "sequence_transactions_median_smoothed_1": f"{DATA_DIRECTORY_PATH}/model_ready/sequence_transactions_median_smoothed_1.csv",
    "sequence_plps_weighted_mean_smoothed_1": f"{DATA_DIRECTORY_PATH}/model_ready/sequence_plps_weighted_mean_smoothed_1.csv",
    "sequence_plps_weighted_median_smoothed_1": f"{DATA_DIRECTORY_PATH}/model_ready/sequence_plps_weighted_median_smoothed_1.csv",
    "sequence_plps_mean_smoothed_1": f"{DATA_DIRECTORY_PATH}/model_ready/sequence_plps_mean_smoothed_1.csv",
    "sequence_plps_median_smoothed_1": f"{DATA_DIRECTORY_PATH}/model_ready/sequence_plps_median_smoothed_1.csv",
    "sequence_lpa_weighted_mean_smoothed_1": f"{DATA_DIRECTORY_PATH}/model_ready/sequence_lpa_weighted_mean_smoothed_1.csv",
    "sequence_lpa_weighted_median_smoothed_1": f"{DATA_DIRECTORY_PATH}/model_ready/sequence_lpa_weighted_median_smoothed_1.csv",
    "sequence_lpa_mean_smoothed_1": f"{DATA_DIRECTORY_PATH}/model_ready/sequence_lpa_mean_smoothed_1.csv",
    "sequence_lpa_median_smoothed_1": f"{DATA_DIRECTORY_PATH}/model_ready/sequence_lpa_median_smoothed_1.csv",
    "sequence_transactions_weighted_mean_smoothed_2": f"{DATA_DIRECTORY_PATH}/model_ready/sequence_transactions_weighted_mean_smoothed_2.csv",
    "sequence_transactions_weighted_median_smoothed_2": f"{DATA_DIRECTORY_PATH}/model_ready/sequence_transactions_weighted_median_smoothed_2.csv",
    "sequence_transactions_mean_smoothed_2": f"{DATA_DIRECTORY_PATH}/model_ready/sequence_transactions_mean_smoothed_2.csv",
    "sequence_transactions_median_smoothed_2": f"{DATA_DIRECTORY_PATH}/model_ready/sequence_transactions_median_smoothed_2.csv",
    "sequence_plps_weighted_mean_smoothed_2": f"{DATA_DIRECTORY_PATH}/model_ready/sequence_plps_weighted_mean_smoothed_2.csv",
    "sequence_plps_weighted_median_smoothed_2": f"{DATA_DIRECTORY_PATH}/model_ready/sequence_plps_weighted_median_smoothed_2.csv",
    "sequence_plps_mean_smoothed_2": f"{DATA_DIRECTORY_PATH}/model_ready/sequence_plps_mean_smoothed_2.csv",
    "sequence_plps_median_smoothed_2": f"{DATA_DIRECTORY_PATH}/model_ready/sequence_plps_median_smoothed_2.csv",
    "sequence_lpa_weighted_mean_smoothed_2": f"{DATA_DIRECTORY_PATH}/model_ready/sequence_lpa_weighted_mean_smoothed_2.csv",
    "sequence_lpa_weighted_median_smoothed_2": f"{DATA_DIRECTORY_PATH}/model_ready/sequence_lpa_weighted_median_smoothed_2.csv",
    "sequence_lpa_mean_smoothed_2": f"{DATA_DIRECTORY_PATH}/model_ready/sequence_lpa_mean_smoothed_2.csv",
    "sequence_lpa_median_smoothed_2": f"{DATA_DIRECTORY_PATH}/model_ready/sequence_lpa_median_smoothed_2.csv",
}

model_output_data_paths = {
    "sequence_transactions_weighted_median_smoothed_2_2020": f"{DATA_DIRECTORY_PATH}/model_output/sequence_transactions_weighted_median_smoothed_2_2020.csv",
}

pretraining_data_paths = {
    "jena_climate": f"{PRETRAINING_DATA_PATH}/jena_climate/jena_climate_2009_2016.csv",
    "etth1": f"{PRETRAINING_DATA_PATH}/ett_small/etth1.csv",
    "etth2": f"{PRETRAINING_DATA_PATH}/ett_small/etth2.csv",
    "ettm1": f"{PRETRAINING_DATA_PATH}/ett_small/ettm1.csv",
    "ettm2": f"{PRETRAINING_DATA_PATH}/ett_small/ettm2.csv",
    "illness": f"{PRETRAINING_DATA_PATH}/illness/national_illness.csv",
    "psm": f"{PRETRAINING_DATA_PATH}/psm",  # incomplete
    "swat": f"{PRETRAINING_DATA_PATH}/swat/swat2.csv",
    "exchange_rate": f"{PRETRAINING_DATA_PATH}/exchange_rate/exchange_rate.csv",
}

processed_pretraining_data_paths = {
    "jena_climate": {  # Done
        "train": f"{PRETRAINING_DATA_PATH}/jena_climate/train.csv",
        "eval": f"{PRETRAINING_DATA_PATH}/jena_climate/eval.csv",
    },
    "etth1": {  # Done
        "train": f"{PRETRAINING_DATA_PATH}/ett_small/etth1_train.csv",
        "eval": f"{PRETRAINING_DATA_PATH}/ett_small/etth1_eval.csv",
    },
    "etth2": {  # Done
        "train": f"{PRETRAINING_DATA_PATH}/ett_small/etth2_train.csv",
        "eval": f"{PRETRAINING_DATA_PATH}/ett_small/etth2_eval.csv",
    },
    "ettm1": {
        "train": f"{PRETRAINING_DATA_PATH}/ett_small/ettm1_train.csv",
        "eval": f"{PRETRAINING_DATA_PATH}/ett_small/ettm1_eval.csv",
    },
    "ettm2": {
        "train": f"{PRETRAINING_DATA_PATH}/ett_small/ettm2_train.csv",
        "eval": f"{PRETRAINING_DATA_PATH}/ett_small/ettm2_eval.csv",
    },
    "illness": {
        "train": f"{PRETRAINING_DATA_PATH}/illness/train.csv",
        "eval": f"{PRETRAINING_DATA_PATH}/illness/eval.csv",
    },
    "psm": {
        "train": f"{PRETRAINING_DATA_PATH}/psm/train.csv",
        "eval": f"{PRETRAINING_DATA_PATH}/psm/eval.csv",
    },
    "swat": {
        "train": f"{PRETRAINING_DATA_PATH}/swat/train.csv",
        "eval": f"{PRETRAINING_DATA_PATH}/swat/eval.csv",
    },
    "exchange_rate": {  # Done
        "train": f"{PRETRAINING_DATA_PATH}/exchange_rate/train.csv",
        "eval": f"{PRETRAINING_DATA_PATH}/exchange_rate/eval.csv",
    },
    "electricity": f"{PRETRAINING_DATA_PATH}/electricity/electricity.csv",
}

pretrained_weights_paths = {
    "jena_climate": f"{WEIGHTS_DIRECTORY_PATH}/jena_climate.pt",
    "etth1": f"{WEIGHTS_DIRECTORY_PATH}/etth1.pt",
    "etth2": f"{WEIGHTS_DIRECTORY_PATH}/etth2.pt",
    "national_illness": f"{WEIGHTS_DIRECTORY_PATH}/national_illness.pt",
    "all": f"{WEIGHTS_DIRECTORY_PATH}/all.pt",
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
