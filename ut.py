from sklearn.utils import shuffle as s
import pandas as pd

df = pd.read_csv('data.csv')
print(df.head())

## shuffle the dataframe

df = df.sample(frac = 1).reset_index(drop = True)

df.to_csv('final.csv', index = False)

import os
import shutil

source = 'E:\\kaggle\\sigma data\\asgn\\test\\all\\'
des = 'E:\\kaggle\\sigma data\\asgn\\test\\test\\'

import pandas as pd

test = pd.read_csv('test.csv')

files = []

for f in test['name']:
    files.append(f)

for i in files:
    shutil.move(source+i, des)

source = 'E:\\kaggle\\sigma data\\asgn\\test\\all\\'
des = 'E:\\kaggle\\sigma data\\asgn\\test\\train\\'

import pandas as pd

train = pd.read_csv('train.csv')

files = []

for f in train['name']:
    files.append(f)

for i in files:
    shutil.move(source+i, des)
