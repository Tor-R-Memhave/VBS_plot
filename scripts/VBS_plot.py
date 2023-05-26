import warnings
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def VBS_plot(g1,g2,n1,n2,text_axis, text_title, labels):
    ## g1 = variable 1 --> n x none
    ## g2 = variable 2 --> n x none
    ## n1 = length of g1
    ## n2 = length of g2 
    ## text_axis printed on y-axis
    ## text_title printed at top
    ## labels given as list of strings
    
    warnings.filterwarnings("ignore", category=FutureWarning) 

    met = pd.DataFrame(data=np.vstack((np.hstack((g1[:,np.newaxis],np.tile(0,(n1,1)))),
                                 np.hstack((g2[:,np.newaxis],np.tile(1,(n2,1)))))),
                                 columns=['param','group'])

    #sns.set_style('white')
    #iris = sns.load_dataset('iris')

    palette = 'pastel'
    palette = np.flip(sns.color_palette("deep", 10)[4:8:3])
    palette = np.zeros((2,3))
    palette[1,:] = np.array((0,0.6,0.27))
    
    ax = sns.violinplot(x='group',y='param',data=met, dodge=False,
                        palette=palette, width =1.2,
                        scale="width", inner=None,alpha=0.5)
    count = 0

    ### Removing the violin plot side toward the "center" of the plot
    for violin in ax.collections:
        if count == 0:
            bbox = violin.get_paths()[0].get_extents()
            x0, y0, width, height = bbox.bounds
            violin.set_clip_path(plt.Rectangle((x0, y0), width / 2, height, transform=ax.transData))
            violin.set_alpha(0.5)
        else:
            bbox = violin.get_paths()[0].get_extents()
            x0, y0, width, height = bbox.bounds
            violin.set_clip_path(plt.Rectangle((x0 + width/2, y0), width / 2, height, transform=ax.transData))
            violin.set_alpha(0.5)
        count += 1


    old_len_collections = len(ax.collections)
    
    sns.stripplot(x="group", y="param", data=met, palette=palette, dodge=False, ax=ax, jitter = 0.1, zorder=0)
    count = 0

    ## Offset of points toward the center of the plot
    for dots in ax.collections[old_len_collections:]:
        if count == 0:
            dots.set_offsets(dots.get_offsets() + np.array([0.125, 0]))
            dots.set_alpha(0.25)
        else:
            dots.set_offsets(dots.get_offsets() - np.array([0.125, 0]))
            dots.set_alpha(0.25)
        count += 1

    sns.boxplot(x="group", y="param", data=met, saturation=1, showfliers=False, color=[0,0,0],
                width=0.5, boxprops={'zorder': int(1e6), 'facecolor': 'none'}, ax=ax, linewidth=1.5)        

    ## Default limits
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    ymin = ylim[0]-0.25*(ylim[1]-ylim[0])
    ymax = ylim[1]+0.25*(ylim[1]-ylim[0])
    yround = int(np.log10(1/(ymax-ymin)))+1
    
    
    ax.set_xticks([0,1])
    ax.set_title(text_title,fontsize=20)
    ax.set_xticklabels(labels,fontsize=20)
    ax.set_xlim([-0.75,1.75])
    ax.set_yticks(np.linspace(np.floor(ymin *(10**yround))/10**yround,np.ceil(ymax*(10**yround))/10**yround,5))
    ax.set_xlabel('')
    ax.set_ylabel(text_axis,fontsize=16)
    return print(ymin,ymax,yround)