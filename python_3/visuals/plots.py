# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 11:38:29 2021
custom plots for data visualization
@author: Ashish
"""

def plot_bivariate(categorical_vars, data):
    from matplotlib import pyplot as plt
    import math
    import seaborn as sns
    
    '''A plot for bivariate analysis.'''
    
    fig, axes = plt.subplots(math.ceil(len(categorical_vars) / 3), 3, figsize=(20, 12))
    axes = axes.flatten()

    for ax, cat in zip(axes, categorical_vars):
        # customise the if else loop for variable to plot
        if cat == 'abc':
            sns.countplot(data[cat], palette='plasma', ax=ax)

        else:

            sns.countplot(x=cat,
                          data=data,
                          hue='abc',
                          palette='plasma',
                          ax=ax)
            ax.legend(title='abc?',
                      loc='upper right',
                      labels=['No', 'Yes'])

        plt.ylabel('Count', fontsize=15, weight='bold')

def plot_3chart(df, feature):
    import matplotlib.gridspec as gridspec
    from matplotlib.ticker import MaxNLocator
    from matplotlib import pyplot as plt
    import seaborn as sns
    from scipy import stats
    from scipy.stats import norm
    from scipy.stats import probplot
    import numpy as np
    
    # Creating a customized chart. and giving in figsize and everything.
    
    fig = plt.figure(constrained_layout=True, figsize=(12, 8))
    
    # Creating a grid of 3 cols and 3 rows.
    
    grid = gridspec.GridSpec(ncols=3, nrows=3, figure=fig)

    # Customizing the histogram grid.
    
    ax1 = fig.add_subplot(grid[0, :2])
    
    # Set the title.
    
    ax1.set_title('Histogram')
    
    # Plot the histogram.
    
    sns.distplot(df.loc[:, feature],
                 hist=True,
                 kde=True,
                 fit=norm,
                 ax=ax1,
                 color='#e74c3c')
    ax1.legend(labels=['Normal', 'Actual'])

    # Customizing the QQ_plot.
    
    ax2 = fig.add_subplot(grid[1, :2])
    
    # Set the title.
    
    ax2.set_title('Probability Plot')
    
    # Plotting the QQ_Plot.
    
    stats.probplot(df.loc[:, feature].fillna(np.mean(df.loc[:, feature])),
                   plot=ax2)
    ax2.get_lines()[0].set_markerfacecolor('#e74c3c')
    ax2.get_lines()[0].set_markersize(12.0)

    # Customizing the Box Plot.
    
    ax3 = fig.add_subplot(grid[:, 2])
    
    # Set title.
    
    ax3.set_title('Box Plot')
    
    # Plotting the box plot.
    
    sns.boxplot(df.loc[:, feature], orient='v', ax=ax3, color='#e74c3c')
    ax3.yaxis.set_major_locator(MaxNLocator(nbins=24))

    plt.suptitle(f'{feature}', fontsize=24)