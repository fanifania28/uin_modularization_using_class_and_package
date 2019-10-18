import matplotlib.pyplot as plt

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'

data = [15, 30, 45, 10] #100%

fig1, ax1 = plt.subplots() #grafik
ax1.pie(data, labels=labels, shadow=True)
plt.show()