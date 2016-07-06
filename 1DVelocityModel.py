import matplotlib.pyplot as plt

def ler_modelos(arquivo):
    x = []
    y = []

    dataset = open(arquivo, 'r')

    for line in dataset:
        line = line.strip()
        X, Y = line.split(',')
        x.append(X)
        y.append(Y)

    dataset.close()


    return x, y

fig = plt.figure()
rect = fig.patch
rect.set_facecolor('w')
x, y = ler_modelos('iaspei.csv')
x2, y2 = ler_modelos('newbr.csv')
x3, y3 = ler_modelos('newbr_modificado.csv')


ax1 = fig.add_subplot(1, 1, 1, axisbg='w')
plt.subplots_adjust(bottom=0.20, right=0.65, top=0.80, left=0.35)
ax1.plot(x, y, 'c', linewidth=2.5, linestyle='-', label= 'IASPEI')
ax1.plot(x2, y2, 'r', linewidth=2.5, linestyle='-', label= 'NewBR')
ax1.plot(x3, y3, 'b', linewidth=2.5, linestyle='--', label= 'Pantanal')
ax1.legend(loc='lower left')

#ax1.set_title('Modelos de Velocidade IASPEI e NewBR')
ax1.set_xlabel('Velocidade Vp em Km/s')
ax1.set_ylabel('Profundidade h em Km')
ax1.set_ylim(ymin=0, ymax=60)
ax1.scale_x = 1e-9
ax1.scale_y = 1e3
#ax1 = plt.gca()
ax1.invert_yaxis()
ax1.set_xlim(xmin=5)
ax1.grid()
ax1.annotate('Descontinuidade', xy=(7, 30), xycoords='data', xytext=(0.6, 0.6), textcoords='axes fraction',
                arrowprops=dict(facecolor='black', shrink=0.05),
                horizontalalignment='left', verticalalignment='bottom', )
plt.show()
