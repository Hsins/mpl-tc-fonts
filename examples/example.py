"""Plot examples of SciencePlot styles."""

import numpy as np
import matplotlib.pyplot as plt
import mpl_tc_fonts

mpl_tc_fonts.load_font('cwtex', 'link')


def model(x, p):
    return x ** (2 * p + 1) / (1 + x ** (2 * p))


pparam = dict(xlabel='電壓 (mV)', ylabel='電流 ($\mu$A)')

x = np.linspace(0.75, 1.25, 201)

# Noto Sans CJK TC
mpl_tc_fonts.set_font('Noto Sans CJK TC')

fig, ax = plt.subplots()
fig.suptitle('Noto Sans CJK TC', fontsize=12, fontweight=700)
for p in [10, 15, 20, 30, 50, 100]:
    ax.plot(x, model(x, p), label=p)
ax.legend(title='Order')
ax.autoscale(tight=True)
ax.set(**pparam)
fig.savefig('figures/fig1.pdf')
fig.savefig('figures/fig1.jpg', dpi=300)

# Noto Serif CJK TC
mpl_tc_fonts.set_font('Noto Serif CJK TC')

fig, ax = plt.subplots()
fig.suptitle('Noto Serif CJK TC', fontsize=12, fontweight=700)
for p in [10, 15, 20, 30, 50, 100]:
    ax.plot(x, model(x, p), label=p)
ax.legend(title='Order')
ax.autoscale(tight=True)
ax.set(**pparam)
fig.savefig('figures/fig2.pdf')
fig.savefig('figures/fig2.jpg', dpi=300)

# cwTeX Q Ming
mpl_tc_fonts.set_font('cwTeX Q Ming')

fig, ax = plt.subplots()
fig.suptitle('cwTeX Q Ming', fontsize=12, fontweight=700)
for p in [10, 15, 20, 30, 50, 100]:
    ax.plot(x, model(x, p), label=p)
ax.legend(title='Order')
ax.autoscale(tight=True)
ax.set(**pparam)
fig.savefig('figures/fig3.pdf')
fig.savefig('figures/fig3.jpg', dpi=300)

# cwTeX Q Kai
mpl_tc_fonts.set_font('cwTeX Q Kai')

fig, ax = plt.subplots()
fig.suptitle('cwTeX Q Kai', fontsize=12, fontweight=700)
for p in [10, 15, 20, 30, 50, 100]:
    ax.plot(x, model(x, p), label=p)
ax.legend(title='Order')
ax.autoscale(tight=True)
ax.set(**pparam)
fig.savefig('figures/fig4.pdf')
fig.savefig('figures/fig4.jpg', dpi=300)

# cwTeX Q Yuan
mpl_tc_fonts.set_font('cwTeX Q Yuan')

fig, ax = plt.subplots()
fig.suptitle('cwTeX Q Yuan', fontsize=12, fontweight=700)
for p in [10, 15, 20, 30, 50, 100]:
    ax.plot(x, model(x, p), label=p)
ax.legend(title='Order')
ax.autoscale(tight=True)
ax.set(**pparam)
fig.savefig('figures/fig5.pdf')
fig.savefig('figures/fig5.jpg', dpi=300)

# cwTeX Q Fangsong
mpl_tc_fonts.set_font('cwTeX Q Fangsong')

fig, ax = plt.subplots()
fig.suptitle('cwTeX Q Fangsong', fontsize=12, fontweight=700)
for p in [10, 15, 20, 30, 50, 100]:
    ax.plot(x, model(x, p), label=p)
ax.legend(title='Order')
ax.autoscale(tight=True)
ax.set(**pparam)
fig.savefig('figures/fig6.pdf')
fig.savefig('figures/fig6.jpg', dpi=300)

# cwTeX Q Hei
mpl_tc_fonts.set_font('cwTeX Q Hei')

fig, ax = plt.subplots()
fig.suptitle('cwTeX Q Hei', fontsize=12, fontweight=700)
for p in [10, 15, 20, 30, 50, 100]:
    ax.plot(x, model(x, p), label=p)
ax.legend(title='Order')
ax.autoscale(tight=True)
ax.set(**pparam)
fig.savefig('figures/fig7.pdf')
fig.savefig('figures/fig7.jpg', dpi=300)
