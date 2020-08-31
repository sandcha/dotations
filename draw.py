import dash_table
import plotly.graph_objs as go


# GRAPH

def generate_scatter_plots(titre_abscisses, abscisses, titre_ordonnees, ordonnees_1, ordonnees_2, tooltips):
    trace1 = go.Scatter(
        name="Officiel",
        x=abscisses,
        y=ordonnees_1,
        text=tooltips,
        # fill='tonexty'
    )
    data = [trace1]

    if ordonnees_2 is not None:
        trace2 = go.Scatter(
            name="Calculé",
            x=abscisses,
            y=ordonnees_2,
            text=tooltips,
            # fill='tozeroy'
        )
        data += [trace2]

    layout = go.Layout(
        title="graphe",
        # margin=go.Margin(l=50, r=50, b=50, t=50),
        xaxis={'title': titre_abscisses},
        yaxis={'title': titre_ordonnees}
    )

    return go.Figure(data=data, layout=layout)

# https://plotly.com/python/bar-charts/
def generate_bars(abscisses, ordonnees_1, ordonnees_2, tooltips):
    trace1 = go.Bar(
        name="Officiel",
        x=abscisses,
        y=ordonnees_1,
        text=tooltips
    )
    data = [trace1]

    if ordonnees_2 is not None:
        trace2 = go.Bar(
            name="Calculé",
            x=abscisses,
            y=ordonnees_2,
            text=tooltips
        )
        data += [trace2]

    layout = go.Layout(
        barmode='group',  # 'stack',
        # KO : automargin=True,
        title='graphe'
    )

    return go.Figure(data=data, layout=layout)


def generate_diff_graph(abscisses, officiel, calcule, tooltips):
    trace1 = go.Bar(
        name="Différence",
        x=abscisses,
        y=calcule-officiel,
        text=tooltips
    )
    data = [trace1]

    layout = go.Layout(
        title='graphe',
        # xaxis_tickangle=-45
    )

    return go.Figure(data=data, layout=layout)


# https://dash.plotly.com/datatable/interactivity
def generate_table(data):
    return dash_table.DataTable(
        id='datatable-paging',
        columns=[{"name": i, "id": i} for i in data.columns],
        # data=data.to_dict('records')[:5],
        page_current=0,
        page_size=20,
        page_action='custom'
        )
