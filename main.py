from dash import Dash, dcc, html
import plotly.express as px

app = Dash(__name__)

# Create a simple bar chart for performance scores
fig = px.bar(employee_data, x='department', y='performance_score', title='Performance Scores by Department')

app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
