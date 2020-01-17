import os

c = 0

# 'E:\\kaggle\\sigma data\\asgn\\dl\\no_modak'
for i in os.listdir('E:\\kaggle\\sigma data\\asgn\\test\\no_modak'):
    c += 1

print(c)


d = 0

# 'E:\\kaggle\\sigma data\\asgn\\dl\\no_modak'
for i in os.listdir('E:\\kaggle\\sigma data\\asgn\\test\\modak'):
    d += 1

print(d)



import pandas as pd
import shutil
from sklearn.utils import shuffle as s
import numpy as np


df = pd.DataFrame(columns = ['name', 'id'])

for i in os.listdir('E:\\kaggle\\sigma data\\asgn\\test\\modak\\'):
    df = df.append({'name': str(i), 'id': 1}, ignore_index = True)

for i in os.listdir('E:\\kaggle\\sigma data\\asgn\\test\\no_modak\\'):
    df = df.append({'name': str(i), 'id': 0}, ignore_index = True)

df.to_csv('E:\\kaggle\\sigma data\\asgn\\test\\data.csv', index = False)

