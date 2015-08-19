#! /usr/bin/env python
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import statsmodels.api as sm

def linear(x,a,b):
    return a*x+b

def quadratic(x,a,b,c):
    return a*x**2+b*x+c

def power_law(x,a,b,c):
    return a*x**b+c
    
def movingaverage (values, window):
    weights = np.repeat(1.0, window)/window
    sma = np.convolve(values, weights, 'valid')
    return sma

def scatterplot_fit(X,Y,**kwargs):
    """
    Takes the X and Y lists and plots them as a 2D scatter plot
    through matplotlib. Additionally, the least squares fit is
    plotted throughout the datapoints.
    
    Keyword arguments:
    X -- List of the X-coordinates
    Y -- List of the Y-coordinates
    function -- Function to be used for curve fitting (default 'linear')
         Alternatives: 'quadratic','lowess' and 'power_law'
    xlabel -- Label for the X-axis (default "")
    ylabel -- Label for the Y-axis (default "")
    title -- Title for the plot (default "")
    """
    function, xlabel, ylabel, title = kwargs.get('function','linear'), kwargs.get('xlabel',""), kwargs.get('ylabel',""), kwargs.get('title',"")
    fig = plt.figure()
    fig.patch.set_facecolor('white')
    ax = fig.add_subplot(111)
    s = ax.scatter(X,Y)
    newX = np.linspace(min(X), max(X), 1000)
    if function == 'linear':
        popt, pcov = curve_fit(linear, X, Y)
        newY = linear(newX,*popt)
        a,b = popt
        label = "{:.2f}".format(a)+"*x+"+"{:.2f}".format(b)
    elif function == 'quadratic':
        popt, pcov = curve_fit(quadratic, X, Y)
        newY = quadratic(newX,*popt)
        a,b,c = popt
        label = "{:.2f}".format(a)+"*x**2+"+"{:.2f}".format(b)+"b*x+"+"{:.2f}".format(c)
    elif function == 'lowess':
        lowess = sm.nonparametric.lowess(Y, X)
        newX,newY = lowess[:, 0], lowess[:, 1]
        label='Lowess Fit'
    elif function == 'power_law':
        popt, pcov = curve_fit(power_law, X, Y)
        newY = power_law(newX,*popt)
        a,b,c = popt
        label = "{:.2f}".format(a)+"*x**"+"{:.2f}".format(b)+"+"+"{:.2f}".format(c)
    else:
        print "Incorrect function specified, please use linear, quadratic, lowess or power_law"
        return None
    plt.plot(newX,newY,label=label)
    ax.grid(True)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
    plt.show()
    plt.close()
    
def heatmap_scatterplot(X,Y,Z,**kwargs):
    """
    Takes the X and Y lists and plots them as a scatterplot
    through matplotlib.with color coding of the points based 
    on the Z list.

    Keyword arguments:
    X -- List of the X-coordinates
    Y -- List of the Y-coordinates
    Z -- List of the Z-coordinates
    vmin -- Minimum value to be displayed in the colorbar (default min(Z))
    vmax -- Maximum value to be displayed in the colorbar (default max(Z))
    edges -- The edges of each individual datapoint (default 'black')
    cm -- The colormap used for the colorbar (default 'jet')
    xlabel -- Label for the X-axis (default "")
    ylabel -- Label for the Y-axis (default "")
    zlabel -- Label for the Z-axis (default "")
    title -- Title for the plot (default "")
    """
    vmin, vmax, edges, cm, xlabel, ylabel, zlabel, title = kwargs.get('vmin',min(Z)), kwargs.get('vmax',max(Z)), kwargs.get('edges','black'), kwargs.get('cm','jet'), kwargs.get('xlabel',""), kwargs.get('ylabel',""), kwargs.get('zlabel',""), kwargs.get('title',"")
    fig = plt.figure()
    fig.patch.set_facecolor('white')
    ax = fig.add_subplot(111)
    s = ax.scatter(X,Y,c=Z,edgecolor=edges)
    ax.grid(True)
    norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)
    ax1 = fig.add_axes([0.95, 0.1, 0.01, 0.8])
    cb = mpl.colorbar.ColorbarBase(ax1,norm=norm,cmap=cm,orientation='vertical')
    cb.set_clim(vmin=min(Z), vmax=max(Z))
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    cb.set_label(zlabel)
    ax.set_title(title)
    plt.show()
    plt.close()
    
def three_dimension_scatterplot(X,Y,Z,**kwargs):
    """
    Takes the X, Y and Z lists and plots them as a 3D scatter plot
    through matplotlib.
    
    Keyword arguments:
    X -- List of the X-coordinates
    Y -- List of the Y-coordinates
    Z -- List of the Z-coordinates
    xlabel -- Label for the X-axis (default "")
    ylabel -- Label for the Y-axis (default "")
    zlabel -- Label for the Z-axis (default "")
    title -- Title for the plot (default "")
    """
    xlabel, ylabel, zlabel, title = kwargs.get('xlabel',""), kwargs.get('ylabel',""), kwargs.get('zlabel',""), kwargs.get('title',"")
    fig = plt.figure()
    fig.patch.set_facecolor('white')
    ax = fig.add_subplot(111, projection='3d')
    s = ax.scatter(X,Y,Z)
    ax.grid(True)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(title)
    plt.show()
    plt.close()
    
def wireframe(X,Y,Z,**kwargs):
    """
    Takes the X, Y and Z lists and plots them as a 3D wireframe
    through matplotlib.
    
    Keyword arguments:
    X -- List of the X-coordinates
    Y -- List of the Y-coordinates
    Z -- List of the Z-coordinates
    xlabel -- Label for the X-axis (default "")
    ylabel -- Label for the Y-axis (default "")
    zlabel -- Label for the Z-axis (default "")
    title -- Title for the plot (default "")
    """
    xlabel, ylabel, zlabel, title = kwargs.get('xlabel',""), kwargs.get('ylabel',""), kwargs.get('zlabel',""), kwargs.get('title',"")
    fig = plt.figure()
    fig.patch.set_facecolor('white')
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_wireframe(X,Y,Z)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(title)
    plt.show()
    plt.close()
    
def surface(X,Y,Z,**kwargs):
    """ 
    Takes the X, Y and Z lists and plots them as a 3D surface plot
    through matplotlib.
    
    Keyword arguments:
    X -- List of the X-coordinates
    Y -- List of the Y-coordinates
    Z -- List of the Z-coordinates
    xlabel -- Label for the X-axis (default "")
    ylabel -- Label for the Y-axis (default "")
    zlabel -- Label for the Z-axis (default "")
    title -- Title for the plot (default "")
    """
    xlabel, ylabel, zlabel, title = kwargs.get('xlabel',""), kwargs.get('ylabel',""), kwargs.get('zlabel',""), kwargs.get('title',"")
    fig = plt.figure()
    fig.patch.set_facecolor('white')
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X,Y,Z)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(title)
    plt.show()
    plt.close()
