from scipy.stats import poisson
import matplotlib.pyplot as plt

backgroundcolor = '#100808'
textcolor = '#F0F0F0'

x = range(100)
axs = []
yticks = [i*0.05 for i in range(8)]

for i in range(1,51):
    fig = plt.figure()
    fig = plt.figure(figsize=(7.2, 7.2), dpi=100, facecolor=backgroundcolor, linewidth=0)
    ax = fig.add_subplot(111)
    ax.set_title('Scatter plot')
    ax.set_xlabel('poisson')
    # ax.set_ylabel('Y')
    ax.xaxis.label.set_color(textcolor)
    # ax.yaxis.label.set_color(textcolor)

    ax.spines['top'].set_color(backgroundcolor)
    ax.spines['bottom'].set_color(textcolor)
    ax.spines['left'].set_color(textcolor)
    ax.spines['right'].set_color(backgroundcolor)
    ax.tick_params(axis = 'x', colors = textcolor)
    ax.tick_params(axis = 'y', colors = textcolor)
    ax.set_facecolor((16/256,8/256,8/256,1))

    y = poisson.pmf(x, i)
    ax.bar(x,y,1,color='#F01010', linewidth=0)
    plt.ylim([0,0.4])

    axs.append(ax)
    dirname = './pics/poisson' + str(i).zfill(2) + '.png'
    fig.savefig(dirname, facecolor=fig.get_facecolor(), edgecolor=fig.get_edgecolor())

# plt.bar(x,y,1,color='#9F1E00', linewidth=0)
# fig = plt.rcParams['axes.facecolor'] = backgroundcolor
# plt.show()