from dash import html, dcc

layout = html.Div([
    html.H2("REDCap Data Dashboard"),
    html.Button("Fetch Data", id="fetch-btn"),
    html.Div(id="data-status"),

    dcc.Loading(
        id="loading",
        children=[
            html.Div(id="table-container")
        ],
        type="circle"
    )
])
