import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.style.use('ggplot')

df_survey = pd.read_csv('Topic_Survey_Assignment.csv')

df_survey.rename(columns={'Unnamed: 0': 'Topic'}, inplace=True)
df_survey.set_index('Topic', inplace=True)
df_survey.index.name = None

df_survey.sort_values('Very interested', axis=0, ascending=False, inplace=True)

df_survey_percentages = round(df_survey/(2223), 2)

ax = df_survey_percentages.plot(
    kind='bar',
    figsize=(20, 8),
    width=0.8,
    color=['#5cb85c', '#5bc0de', '#d9534f'],
    fontsize=14
)

ax.get_yaxis().set_visible(False)

ax.set_title('Percentage of Respondents\' Interest Data Science Areas', fontsize=16)
ax.set_facecolor('w')

for i in ax.patches:
    ax.text(i.get_x(), i.get_height() + 0.005 , str(round((i.get_height() * 100), 2)) + ' %', fontsize=14, color='dimgrey')

plt.show()