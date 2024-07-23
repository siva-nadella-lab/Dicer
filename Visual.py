from Die import ADie
from DiceGroup import DiceGroup
import plotly.express as plex
import pandas as pan

rollingGroup = DiceGroup()

rollingGroup.addDie()
rollingGroup.addDie(10)

for num in range(1,1000):
    rollingGroup.rollAllDice()

frequencies = rollingGroup.getFrequencies()
possibleResults = list(range(rollingGroup.minRollResult, rollingGroup.maxRollResult+1))
resultsFrame = pan.DataFrame({'Frequency': frequencies,
                              'Result': possibleResults})

title ="Rolling Dice results"

# fig = plex.bar(x=possibleResults, y=frequencies,title=title)
fig = plex.bar(resultsFrame, x='Result', y='Frequency',title=title)

# fig = plex.line(x=possibleResults,y=frequencies)

# fig = plex.scatter(x=possibleResults,y=frequencies)

fig.update_layout(xaxis_dtick=1)

fig.show()




