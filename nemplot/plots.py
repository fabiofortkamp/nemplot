from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

from .config import nemplot_parameters

def refine_list(original_list, factor):
    """
    Return a new list, inserting more elements between the number in
    'original_list'.
    
    Assumes 'original_list' is evenly-spaced. The spacing between each
    element is divided by 'factor'
    
    >>>refine_list([1,2,3],factor=2)
    [1.0,1.5,2.0,2.5,3.0]
    """
    
    # calculate the original spacing between elements and refine it
    d = original_list[1] - original_list[0]
    d_refined = d / factor
        
    max_value = max(original_list)
    min_value = min(original_list)
    
    # the number of elements is the number of divisions between
    # the limit values, plus one aditional
    n_refined = ((max_value - min_value) / d_refined) + 1
        
    return np.linspace(min_value,max_value,int(n_refined))

def set_all_fontsizes_from_axis(ax):
    
    for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
        ax.get_xticklabels() +
        ax.get_yticklabels()):
            
        item.set_fontsize(nemplot_parameters["FONTSIZE"])

def refine_yticks(ax,factor):
    """
    Take an Axis object 'ax' and refine the y-ticks on it by 'factor'
    
    Parameters
    ----------
    ax : matplotlib.pyplot.Axex.Axis() object 
    factor: int

    Returns
    -------
    out : None 

    """

    ax.set_yticks(refine_list(ax.get_yticks(),factor),minor=True)
    

def create_plot(xlabel="",
                     ylabel="",
                     title=""):
    """
    Return (fig,axis) correspondent to a line plot,
    with 'xlabel','ylabel' and 'title'
    
    The size of the figure is controlled by FIGSIZE_INCHES"""

    figsize_inches = nemplot_parameters["FIGSIZE_INCHES"]
    
    fig = plt.figure(figsize=(figsize_inches,figsize_inches))
    axis = fig.add_subplot(111)
    
    axis.set_ylabel(ylabel)
    axis.set_xlabel(xlabel)
    axis.set_title(title)
    
    set_all_fontsizes_from_axis(axis)
    
    return fig, axis

def create_two_axes_plot(xlabel="", 
                              ylabel_left="", 
                              ylabel_right="",
                              title=""):
    """
    Return (fig, axis_left, axis_right) correspondent
    to a line plot with two y-axes.
    
    The size of the figure is controlled by FIGSIZE_INCHES
    """
    
    fig, axis_left = create_plot(xlabel, ylabel_left, title)
    
    axis_right = axis_left.twinx()
    axis_right.set_ylabel(ylabel_right)
    
    set_all_fontsizes_from_axis(axis_right)
    
    return (fig, axis_left, axis_right)
    
def save_figure(fig,name):
    """
    Save the 'fig' Figure object as 'name' (with extension PLOT_EXTENSION),
    inside FIG_FILE_PATH (a Path-like object)."""
    
    fig_path = nemplot_parameters["FIG_FILE_PATH"]
    file_basename = name + nemplot_parameters["PLOT_EXTENSION"]
    
    file_path = fig_path / file_basename
    fig.savefig(str(file_path),
                dpi=nemplot_parameters["DPI"],
                bbox_inches='tight')
