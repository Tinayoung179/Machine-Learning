import pandas as pd
from keras.models import load_model
import numpy as np

inputDF = pd.read_csv('./benign_CICMalDroid.csv')

modifiedDF = pd.read_csv('./malware_CICMalDroid.csv')

result = pd.concat([inputDF, modifiedDF], ignore_index=True, axis=0).fillna(0)

result.to_csv("CICMalDroid_dataset.csv", index = False)
