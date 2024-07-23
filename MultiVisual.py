from plotly.subplots import make_subplots
import plotly.graph_objects as graphO
import pandas as pan
from DiceGroup import DiceGroup

fig = make_subplots(rows=3, cols=1)

rollingGroup = DiceGroup()

rollingGroup.addDie()
rollingGroup.addDie(10)

for num in range(1,1000):
    rollingGroup.rollAllDice()

frequencies = rollingGroup.getFrequencies()
possibleResults = list(range(rollingGroup.minRollResult, rollingGroup.maxRollResult+1))
resultsFrame = pan.DataFrame({'Frequency': frequencies,
                              'Result': possibleResults})
fig.append_trace(graphO.Bar(x=possibleResults,y=frequencies), row=1, col=1)

# fig.append_trace(graphO.Line(x=possibleResults,y=frequencies,title=title), row=2, col=1)

fig.append_trace(graphO.Scatter(x=possibleResults,y=frequencies), row=3, col=1)

fig.update_layout(xaxis_dtick=1)

fig.show()