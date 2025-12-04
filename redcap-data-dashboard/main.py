from dash import Dash
from app.layout import layout
from app import callbacks  # noqa: F401 (ensures callbacks load)

app = Dash(__name__, suppress_callback_exceptions=True)
app.layout = layout

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8050)
