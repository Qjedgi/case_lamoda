import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Тестовое задание_мл аналитик.xlsx")

mean_scans_per_employee = df['Общий итог сканирований по сотруднику'].sum() / len(df)
mean_packages_per_employee = df['Общее кол-во паков обработанных на всем складе'].sum() / len(df)
mean_hours_per_employee = df['Кол-во отработанных часов по сотруднику'].sum() / len(df)
mean_shifts_per_employee = df['Кол-во отработанных смен по сотруднику'].sum() / len(df)
mean_scans_per_warehouse = df.groupby('Транзитный склад')['Общий итог сканирований по сотруднику'].sum().mean()
mean_packages_per_warehouse = df.groupby('Транзитный склад')['Общее кол-во паков обработанных на всем складе'].sum().mean()
mean_hours_per_warehouse = df.groupby('Транзитный склад')['Кол-во отработанных часов по сотруднику'].sum().mean()
mean_shifts_per_warehouse = df.groupby('Транзитный склад')['Кол-во отработанных смен по сотруднику'].sum().mean()

large_warehouses = df[df['Кол-во отработанных часов по сотруднику'] > mean_hours_per_employee].groupby('Транзитный склад').size()
small_warehouses = df[df['Кол-во отработанных часов по сотруднику'] <= mean_hours_per_employee].groupby('Транзитный склад').size()


plt.figure(figsize=(8, 6))
plt.hist(df['Общий итог сканирований по сотруднику'], bins=50)
plt.title('Гистограмма количества сканирований')
plt.xlabel('Сканирование')
plt.ylabel('Частота')


plt.figure(figsize=(8, 6))
plt.hist(df['Общее кол-во паков обработанных на всем складе'], bins=50)
plt.title('Гистограмма количества посылок')
plt.xlabel('Паки')
plt.ylabel('Частота')


plt.figure(figsize=(8, 6))
plt.hist(df['Кол-во отработанных часов по сотруднику'], bins=50)
plt.title('Гистограмма количества часов')
plt.xlabel('Отработанные часы')
plt.ylabel('Частота')


plt.figure(figsize=(8, 6))
plt.hist(df['Кол-во отработанных смен по сотруднику'], bins=50)
plt.title('гистограмма отработанных смен')
plt.xlabel('Отработанная смена')
plt.ylabel('Частота')


plt.figure(figsize=(8, 6))
plt.bar(['Large', 'Small'], [len(large_warehouses), len(small_warehouses)])
plt.title('Склад')
plt.xlabel('Размер склада')
plt.ylabel('Количество')

plt.show()