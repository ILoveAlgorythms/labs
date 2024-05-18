# этот ноутбук относится к лабе 3.3.3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from ipywidgets import interact
# from pyperclip import copy

data = pd.read_csv('laba333.csv').sort_values('n', ignore_index=True)
data_print = data.copy()
data_print['kV'] = (data_print['kV'] * 1000).astype('int')

rho = 898 # Си
h = 10**-3 # м
eta = 1.83 * 10**-5 #Си
l = 0.725*10**-2 # Си
g = 9.81
e_podgon = -1.6022 * 10**-19

koef = 9 * np.pi *\
  np.sqrt(\
    (2 * eta**3 * h**3) / (g * rho)
  ) * l
print(koef)

def q(t_0, t, V):
  V = 10**3 * V
  if 1==0:
    print("--> ", t_0)
  ans = koef * ((t_0 + t) / (V * (t_0**1.5) * t))
  return ans


for i in range(len(data)):
  data['q'] = q(data['t0'], data['t'], data['kV'])*10**19

# Данные data не указаны, добавлю их в качестве заглушки

step = 2
mn = data['q'].min() - 0.001
mx = data['q'].max() + 0.001
y = []
x = []

def plot(megastep, milistep):
  plt.clf()
  step = megastep + milistep
  for i in np.arange(mn, mx, step):
    x.append(i)
    y.append(data[(data['q'] >= i) & (data['q'] < i + step)]['q'].count())
  plt.xticks(
      ticks = np.arange(round(mn), round(mx), step=1),
      minor = True
  )
  plt.bar(x=x, height=y)

@interact(megastep = (0.1, 10, 0.01), milistep = (0.001, 0.5, 0.001))
def interactive_plot(megastep, milistep):
  plot(megastep, milistep)
  plt.show()

interactive_plot(1, 1)
