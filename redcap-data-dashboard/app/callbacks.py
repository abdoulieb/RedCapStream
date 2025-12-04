from dash import Input, Output, dash_table
from services.redcap_client import fetch_redcap_data
from main import app

@app.callback(
    [Output("data-status", "children"),
     Output("table-container", "children")],
    [Input("fetch-btn", "n_clicks")]
)
def update_data(n_clicks):
    if not n_clicks:
        return "", ""

    try:
        df = fetch_redcap_data()

        table = dash_table.DataTable(
            columns=[{"name": col, "id": col} for col in df.columns],
            data=df.to_dict("records"),
            page_size=20,
            style_table={"overflowX": "scroll"},
        )

        return "Data fetch successful.", table

    except Exception as e:
        return f"Error: {str(e)}", ""
