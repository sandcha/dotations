import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

from check import get_dgcl_values, get_table_data, strate_0_data, strate_1_data, strate_2_data, simulation, dsu_montant_eligible
from draw import generate_scatter_plots, generate_bars, generate_diff_graph, generate_table


communes_ids = simulation.persons.ids
communes_codes = get_dgcl_values('Informations générales - Code INSEE de la commune')
communes_names = get_dgcl_values('Informations générales - Nom de la commune')

dgcl_dsu = get_dgcl_values('Dotation de solidarité urbaine - Montant total réparti')


# COURBES par index croissant
courbes = generate_scatter_plots("communes", communes_ids, "dsu métropole", dgcl_dsu, dsu_montant_eligible, communes_names)
courbes.layout.title = "DSU par index de commune croissant"

# BARRES par strate démographique et population DGF croissante
communes_strate_0 = strate_0_data['Informations générales - Nom de la commune']
population_strate_0 = strate_0_data["Informations générales - Population DGF Année N'"]
dsu_strate_0 = strate_0_data['Dotation de solidarité urbaine - Montant total réparti']
dsu_strate_0_nb_non_nul = len(dsu_strate_0[dsu_strate_0 > 0])
barres_strate_0 = generate_bars(communes_strate_0, dsu_strate_0, None, communes_strate_0 + str(population_strate_0))  # strate_0_data.index
barres_strate_0.layout.title = "Strate moins de 5000 habitants"

communes_strate_1 = strate_1_data['Informations générales - Nom de la commune']
dsu_strate_1 = strate_1_data['Dotation de solidarité urbaine - Montant total réparti']
dsu_strate_1_nb_non_nul = len(dsu_strate_1[dsu_strate_1 > 0])
barres_strate_1 = generate_bars(communes_strate_1, dsu_strate_1, None, communes_strate_1)
barres_strate_1.layout.title = "Strate de 5000 à 9999 habitants"

communes_strate_2 = strate_2_data['Informations générales - Nom de la commune']
dsu_strate_2 = strate_2_data['Dotation de solidarité urbaine - Montant total réparti']
dsu_strate_2_nb_non_nul = len(dsu_strate_2[dsu_strate_2 > 0])
barres_strate_2 = generate_bars(communes_strate_2, dsu_strate_2, None, communes_strate_2)
barres_strate_2.layout.title = "Strate de 10000 habitants et plus"

# BARRES de différence calculé / dgcl
diff = generate_diff_graph(communes_names, dgcl_dsu, dsu_montant_eligible, communes_names)
diff.layout.title = "DSU, calculé - officiel"

# TABLE pour un montant minimal 
montant_dsu_min = 0  # strictement supérieur à 0
table_data = get_table_data(montant_dsu_min)
table = generate_table(table_data)


# APP 
app = dash.Dash(__name__)

@app.callback(
    Output('datatable-paging', 'data'),
    [Input('datatable-paging', "page_current"),
     Input('datatable-paging', "page_size")])
def update_table(page_current, page_size):
    return table_data.iloc[
        page_current*page_size:(page_current+ 1)*page_size  # ex: 0:2 pour 2 communes
    ].to_dict('records')


app.title = 'dotations'
server = app.server


# To serve offline, uncomment these lines and check for css dependency:
# app.css.config.serve_locally = True
# app.scripts.config.serve_locally = True
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

# <link rel="stylesheet" type="text/css" href="/css/main.css">
app.layout = html.Div(children=[
    html.H1(children=str(len(communes_ids)) + ' communes'),
    
    html.Div(children=[
        html.H2(children='DSU'),
        dcc.Graph(
            id='courbes',
            figure=courbes
        ),
        dcc.Graph(
            id='diff',
            figure=diff
        )
    ]),

    html.Div(children=[
        html.H3(children=str(len(strate_0_data)) + ' communes de moins de 5000 habitants *** ' + str(dsu_strate_0_nb_non_nul) + ' ont une DSU > 0'),
        dcc.Graph(
            id='barres_strate_0',
            figure=barres_strate_0
        )
    ]),

    html.Div(children=[
        html.H3(children=str(len(strate_1_data)) + ' communes de [5000, 10000[ habitants *** ' + str(dsu_strate_1_nb_non_nul) + ' ont une DSU > 0'),
        dcc.Graph(
            id='barres_strate_1',
            figure=barres_strate_1
        )
    ]),

    html.Div(children=[
        html.H3(children=str(len(strate_2_data)) + ' communes de [10000, +oo[ habitants *** ' + str(dsu_strate_2_nb_non_nul) + ' ont une DSU > 0'),
        dcc.Graph(
            id='barres_strate_2',
            figure=barres_strate_2
        )
    ]),

    html.Div(children=[
        html.H3(children=str(len(table_data)) + ' communes à DSU > 0'),
        table
    ])
])

if __name__ == '__main__':
    # http://127.0.0.1:8050/
    app.run_server(debug=True)
