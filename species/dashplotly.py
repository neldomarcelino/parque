from django.db.models import Count
from species.models import Specie

import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
from django_plotly_dash import DjangoDash

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def format_data():
    data_specie = Specie.objects.values('year').annotate(total=Count('year')).order_by('year')

    total = []
    year = []

    for specie in data_specie:
        total.append(specie.get('total'))
        year.append(specie.get('year'))

    dict_specie_data = {
        "year": year,
        "total": total,
    }
    return dict_specie_data


def add_to_layout(specie_line_graph, specie_pie_graph):
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = DjangoDash('SpecieDash', external_stylesheets=external_stylesheets)
    app.layout = html.Div(children=[
        html.H3(children='Analise Especies'),

        dcc.Graph(
            id='specie-graph',
            figure=specie_line_graph
        ),
        dcc.Graph(
            id='specie-pie',
            figure=specie_pie_graph
        )
    ])



dict_specie_data = format_data()
df = pd.DataFrame(dict_specie_data)

specie_line_graph = px.line(df, x="year", y="total", title='Linha de registo de especies')
specie_pie_graph = px.pie(df, values='total', names='year', title='Percentagem de especies por ano')

add_to_layout(specie_line_graph, specie_pie_graph)





