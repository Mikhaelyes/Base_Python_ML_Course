import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Electric_Car.csv')
df.groupby('Brand')

brands = df['Brand'].unique()
new_row = {'Brand': [], 'Values': []}
for i in brands:
        new_row['Brand'].append(i)
        new_row['Values'].append((df[df['Brand'] == i].shape)[0])


count_model = pd.DataFrame.from_dict(new_row).sort_values(by='Values', ascending=False)
count_model_t2 = pd.DataFrame.from_dict(new_row).sort_values(by='Values', ascending=False)
V_show = count_model[count_model['Values'] >= 6]

V_rest_prc = (count_model['Values'].sum() - V_show['Values'].sum())
new_row = {'Brand': ['Rest'], 'Values': V_rest_prc}
count_model1 = pd.DataFrame.from_dict(new_row)#.sort_values(by='Values', ascending=False)
V_show = pd.concat([V_show, count_model1], ignore_index=True)

#pie_chart = plt.pie(V_show['Values'], labels=V_show['Brand'],
#        autopct='%.1f%%', radius=2)
#plt.savefig('auto_pie.png')
#plt.show()


barh_chart = plt.barh(count_model_t2['Brand'], count_model_t2['Values'])
plt.grid()
plt.title('Количество моделей определенного бренда')
plt.savefig('saved_figure_barh.png')
plt.show()