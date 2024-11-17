from app import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import SingleIntervalTicker
from bokeh.models import HoverTool, ColumnDataSource

# Se formatean las fechas
df["Inicio_s"] = df["Inicio"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["Fin_s"] = df["Fin"].dt.strftime("%Y-%m-%d %H:%M:%S")

# Se crea el origen de datos
cds = ColumnDataSource(df)

# Se crea el gráfico
p = figure(x_axis_type='datetime', height=200, width=500, title="Gráfico de Movimiento", sizing_mode="stretch_width")
p.yaxis.ticker = SingleIntervalTicker(interval=1)

# Se añade la herramienta de hover
hover = HoverTool(tooltips=[("Inicio", "@Inicio_s"), ("Fin", "@Fin_s")])
p.add_tools(hover)

# Se dibujan los cuadros
q = p.quad(left="Inicio", right="Fin", bottom=0, top=1, color="green", source=cds)

# Se guarda el gráfico
output_file("Graph.html")

# Se muestra el gráfico
show(p)