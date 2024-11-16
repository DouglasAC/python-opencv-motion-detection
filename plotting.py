from app import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import SingleIntervalTicker

p = figure(x_axis_type='datetime', height=200, width=500, title="Gráfico de Movimiento", sizing_mode="stretch_width")
p.yaxis.ticker = SingleIntervalTicker(interval=1)


q = p.quad(left=df["Inicio"], right=df["Fin"], bottom=0, top=1, color="green")


output_file("Graph.html")

show(p)