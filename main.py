#!/bin/python3
from pygal import Bar

# Create a chart
chart = Bar(title='Equipos con mas goles de Argentina')
# Add data to the chart
ri = ['River', 2000]
id = ['Indepediente', 1413]
rc = ['Racing', 1304]
bo = ['Boca', 780]
sl = ['San Lorenzo', 671]
dy = ['Defensa y Justicia', 524]
chart.add(ri[0], ri[1])
chart.add(id[0], id[1])
chart.add(rc[0], rc[1])
chart.add(bo[0], bo[1])
chart.add(sl[0], sl[1])
chart.add(dy[0], dy[1])
# Display the chart
chart.render()
