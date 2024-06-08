import matplotlib.pyplot as plt

import matplotlib

hn = 10
vn = 10
hstep = 1.0/float(hn)
vstep = 1.0/float(vn)

fig_dpi = 72
fig_width = 200
fig_height = 200
font_size = float(fig_height)/float(vn)

fig = plt.figure()
#fig.subplots_adjust(bottom=0.0,left=0.0,top=1.0,right=1.0,wspace=0.0,hspace=0.0)
fig.set_facecolor('black')
fig.set_figwidth(float(fig_width)/float(fig_dpi))
fig.set_figheight(float(fig_height)/float(fig_dpi))

i = 0
for y in range(vn):
    for x in range(hn):
        fig.text(
            x*hstep+hstep/2.0,1.0-(y)*vstep-vstep/2.0, chr(i+33), 
            color='white', 
            fontsize=font_size, 
            family='sans-serif', 
            fontweight='normal', 
            horizontalalignment='center', 
            verticalalignment='center')
        i+=1


plt.savefig('demiurge_font.png', format='png', dpi=fig_dpi, transparent=True)
plt.show()
