#! /usr/bin/env python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def heatmap_scatterplot(X,Y,Z,**kwargs):
    """ WRITE DOCUMENTATION.
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
    """ WRITE DOCUMENTATION.
    """
    xlabel, ylabel, zlabel, title = kwargs.get('xlabel',""), kwargs.get('ylabel',""), kwargs.get('zlabel',""), kwargs.get('title',"")
    fig = plt.figure()#! /usr/bin/env python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def heatmap_scatterplot(X,Y,Z,**kwargs):
    """ WRITE DOCUMENTATION.
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
    """ WRITE DOCUMENTATION.
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
    """ WRITE DOCUMENTATION
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
    """ WRITE DOCUMENTATION
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
