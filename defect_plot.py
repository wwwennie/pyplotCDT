import matplotlib.pyplot as plt
import numpy as np


def defect_plot(list_lambdas,title="",axes_labels=("",""),xaxis=(0,10),yaxis=(-10,-10),
             show_legend=False,show_min=True,symm_surf=True,labels=[]):
    """
    Function for plotting defect formation energies of a defect

    list_lambdas: list of lambda functions [lambda1, lambda2,...] 
    title: (string), title of plot
    axes_labels: list containing [x_axis_label,y_axis_label]
    xaxis, yaxis: containing min and max of axes
    label: tuple containing (xaxis_label, yaxis_label)
    show_legend: boolean for displaying legend
    show_min: boolean, display minimum formation energies of charge states
    labels: list of strings to label curves
    symm_surf: boolean; symmetric surfaces have one defect per surface, so factor of 2

    """
    # numerically evaluate the lambdas in list_lambdas
    x = np.arange(xaxis[0],xaxis[1],0.05)
    
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    if show_min:
       # collect y's and return the minimum
       y = []
       for func in list_lambdas:
         if symm_surf:
           y.append(np.multiply(func(x),0.5))
         else:
           y.append(func(x))
       y = np.min(y,axis=0)
   
       ax.plot(x,y) 
    else:
       for func in list_lambdas:
          if symm_surf:
            ax.plot(x,np.multiply(func(x),0.5))
          else:
            ax.plot(x,func(x))

    #prettify the plot
    ax.set_xlabel(axes_labels[0],fontsize=22)
    ax.set_ylabel(axes_labels[1],fontsize=22)
    ax.tick_params(axis='both', labelsize=16)

    if show_legend:
        ax.legend(loc='best')

    plt.tight_layout()
    #plt.gca().set_aspect('equal',adjustable='box')
    return ax
