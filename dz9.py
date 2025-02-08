import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загружаем данные из файла
with open('events.json', 'r') as file:
    data = pd.read_json(file)

# Извлекаем данные из вложенной структуры все, что в events
df = pd.json_normalize(data['events'])

print(df.head(),"\n")

# Распределение событий по полю signature
event_distribution = df['signature'].value_counts()
print(event_distribution)

# Создание графика
plt.figure(figsize=(10, 6))
sns.countplot(y='signature', data=df, order=df['signature'].value_counts().index, palette="viridis")

plt.title('Распределение типов событий информационной безопасности', fontsize=16)
plt.xlabel('Количество событий', fontsize=12)
plt.ylabel('Тип события (signature)', fontsize=12)

plt.show()