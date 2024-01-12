import pandas as pd

data = pd.read_csv("police.csv", sep=',')
maskM = (data['driver_gender'] == 'M')
maskF = (data['driver_gender'] == 'F')
maskF80 = (data['driver_gender'] == 'F') & (data['driver_age'] >= 80)
maskD20 = (data['driver_age'] == 20)

print(data.keys())
numberM = maskM.sum()
numberF = maskF.sum()
numberF80 = maskF80.sum()
numberD20 = maskD20.sum()

print(numberM, numberF, numberF80, numberD20)


