import numpy as np
import pandas as pds

from openfisca_core.simulation_builder import SimulationBuilder
from openfisca_france_dotations_locales import CountryTaxBenefitSystem

from dotations.load_dgcl_data import load_dgcl_file, adapt_dgcl_data
from dotations.simulation import simulation_from_dgcl_csv


def list_columns(dataframe, regex):
    l = dataframe.filter(regex=regex,axis=1).head()
    return l.columns


def sort_by_column(data, column_name):
    return data.sort_values(by=[column_name])


def get_dgcl_values(column_name):
    return data[column_name]


def get_minimum_data(data):
    df = pds.DataFrame(index = data.index)
    df['Informations générales - Nom de la commune'] = data['Informations générales - Nom de la commune'].values 
    df["Informations générales - Population DGF Année N'"] = data["Informations générales - Population DGF Année N'"].values
    df['Dotation de solidarité urbaine - Montant total réparti'] = data['Dotation de solidarité urbaine - Montant total réparti'].values
    return df


def new_simulation(period, data):
    sb = SimulationBuilder()
    ofdl = CountryTaxBenefitSystem()
    return simulation_from_dgcl_csv(period, data, ofdl)


def get_table_data(montant_dsu_min):
    table_data = data_adapted_min
    table_data['DSU calculée'] = dsu_montant_eligible
    table_data = table_data.loc[
        (table_data['Dotation de solidarité urbaine - Montant total réparti'] > montant_dsu_min) 
        | (table_data['DSU calculée'] > montant_dsu_min)
        ]
    table_data = sort_by_column(table_data, "Informations générales - Population DGF Année N'")
    return table_data


def get_strate_0(data):
    return sort_by_column(
        data.loc[data["Informations générales - Population DGF Année N'"] < 5_000],
        "Informations générales - Population DGF Année N'"
        )


def get_strate_1(data):
    return sort_by_column(
        data.loc[
            (data["Informations générales - Population DGF Année N'"] >= 5_000)
            & (data["Informations générales - Population DGF Année N'"] < 10_000)
            ],
        "Informations générales - Population DGF Année N'"
        )


def get_strate_2(data):
    return sort_by_column(
        data.loc[data["Informations générales - Population DGF Année N'"] >= 10_000],
        "Informations générales - Population DGF Année N'"
        )


# strates par nombre d'habitants
# strates_leximpact = [500, 1000, 2000, 3500, 5000, 7500, 10_000, 15_000, 20_000, 35_000, 50_000, 75_000, 100_000]
# strates_dsu = [5000, 10_000]  # 5000+, 10_000+

data = load_dgcl_file()
data_adapted = adapt_dgcl_data(data)
data_adapted_min = get_minimum_data(data)

period = 2021
simulation = new_simulation(period, data_adapted)
dsu_montant_eligible = simulation.calculate('dsu_montant_eligible', period)

strate_0_data = get_strate_0(data_adapted_min)
strate_1_data = get_strate_1(data_adapted_min)
strate_2_data = get_strate_2(data_adapted_min)

