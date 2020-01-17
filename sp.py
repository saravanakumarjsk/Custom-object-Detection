# 'E:\\kaggle\\sigma data\\asgn\\dl\\no_modak'

import os

# # Function to rename multiple files
def main():
    i = 582

    for filename in os.listdir('E:\\kaggle\\sigma data\\asgn\\test\\no_modak'):
        dst ="img_" + str(i) + ".jpg"
        src ='E:\\kaggle\\sigma data\\asgn\\test\\no_modak\\'+ filename
        dst ='E:\\kaggle\\sigma data\\asgn\\test\\no_modak\\'+ dst

        # rename() function will
        # rename all the files
        os.rename(src, dst)
        i += 1

Driver Code
if __name__ == '__main__':

    # Calling main() function
    main()

import pandas as pd

df = pd.read_csv('final.csv')

train = df.iloc[:800, :]
test = df.iloc[800:, :]

train.to_csv('train.csv', index=False)
test.to_csv('test.csv', index = False)


