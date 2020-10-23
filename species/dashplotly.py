import datetime

from django.db.models import Count
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import plotly.express as px

from django_plotly_dash import DjangoDash

from species.models import Specie

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('SpecieDash', external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
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
df = pd.DataFrame(dict_specie_data)

specie_line_graph = px.line(df, x="year", y="total", title='Linha de registo de especies')
specie_pie_graph = px.pie(df, values='total', names='year')

app.layout = html.Div(children=[
    html.H3(children='Analise Especies'),

    html.Div(children='''
        Registo de Especies por Ano.
    '''),

    dcc.Graph(
        id='specie-graph',
        figure=specie_line_graph
    ),
    dcc.Graph(
        id='specie-pie',
        figure=specie_pie_graph
    )
])

