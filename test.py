import json

from utils.getParams import CleanData
from utils.calculation import Calculator

### First we gather the data ...
toSplit = "assets\example_payload.json"
with open(toSplit) as t:
    toSplit = json.load(t)

load, fuels, plants = CleanData.separate_data(toSplit)

### ... and organize/clean them:
# take the conditions price and average wind strength into account
plants = CleanData.conditions(fuels, plants)
plants["per_unit"] = CleanData.formula_p(plants)
# recalculate the pmax for the wind turbines
plants = CleanData.variabel_pmax(plants)


### Next step: doing the calculations
### 1. add column "p" (price per unit generated)

plants = Calculator.algo(load, plants)

print(plants)