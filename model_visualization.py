from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer
from model import *

def agent_portrayal(agent):
    portrayal = {
        'Shape': 'circle',
        'Layer': 0,
        'r': 0.8,
        'Color': 'blue'}

    # (Un)masked agents show up as (non-)filled circles
    if agent.masked == True:
        portrayal['Filled'] = 'true'

    if agent.infected == True:
        portrayal['Color'] = 'orange'

    if agent.immune == True:
        portrayal['Color'] = 'green'

    return portrayal

grid = CanvasGrid(agent_portrayal, 50, 50, 500, 500)

line_charts = ChartModule([
    {'Label': 'Susceptible', 'Color': 'blue'}, 
    {'Label': 'Infected', 'Color': 'orange'},
    {'Label': 'Recovered and Immune', 'Color': 'green'}])

server = ModularServer(CovidModel, [grid, line_charts], 'SIR Modelling of spread of COVID-19', model_params)
server.launch()