from django.db.models import Count
from django.db.models.functions import TruncYear
import dash
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
data_specie_1 = Specie.objects.values(year='date_created').annotate(total=Count('date_created__year'))
print(data_specie_1)
for s in data_specie_1:
    print(s)

data_specie = Specie.objects.all()
species = []
habitat = []
year = []
for specie in data_specie:
    species.append(specie.specie)
    habitat.append(specie.habitat)
    year.append(specie.date_created.year)
dict_specie_data = {
        "species": species,
        "habitat": habitat,
        "year": year,
    }
df = pd.DataFrame(dict_specie_data)

fig = px.line(df, x="year", y="habitat", color="species")


app.layout = html.Div(children=[
    html.H3(children='Analise Especies'),

    html.Div(children='''
        Registo de Especies por Ano.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

