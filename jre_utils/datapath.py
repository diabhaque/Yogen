DATA_DIRECTORY_PATH = "../../data"
DERIVED_DATA_PATH = f"{DATA_DIRECTORY_PATH}/derived"

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


def get_derived_csv_path(period, area_level, asset_type, statistic):
    filename = f"{period}_{area_level}_{asset_type}_{statistic}.csv"
    return f"{DERIVED_DATA_PATH}/{filename}"
