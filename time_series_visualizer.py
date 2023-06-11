import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col=0, parse_dates=True)

# Clean data
df_clean = df[df['value'].between(df['value'].quantile(0.025), df['value'].quantile(0.975), inclusive='both')].copy()

months_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def draw_line_plot():
    # Draw line plot
    x_axis = df_clean.index
    y_axis = df_clean.value
    fig, ax = plt.subplots(figsize=(25,8))
    plt.plot(x_axis, y_axis, 'r', lw=2)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_clean['month'] = df_clean.index.strftime('%B')
    df_clean['year'] = df_clean.index.strftime('%Y')
    df_clean
  
    df_bar = pd.pivot_table(df_clean, index=['year', 'month'], values='value')
    df_bar = df_bar.reindex(months_order, level='month')
    df_bar.reset_index(inplace=True)
    df_bar

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(20,20))
    bar_chart = sns.barplot(data=df_bar, x='year', y='value', hue='month', hue_order=months_order, palette='bright', saturation=0.5)
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(loc='upper left')
    sns.set(style='whitegrid', font_scale=3)
    plt.xticks(rotation=90)
  

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_clean['month'] = df_clean['month'].str.slice(stop=3)
    months_order_sliced = []
    for month in months_order:
        months_order_sliced.append(month[0:3])
    
    # Draw box plots (using Seaborn)

    fig = plt.figure(figsize=(35,15))
    plt.subplot(1, 2, 1)
    plt.title('Year-wise Box Plot (Trend)')
    sns.boxplot(data=df_clean, x='year', y='value' )
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    
    plt.subplot(1, 2, 2)
    plt.title('Month-wise Box Plot (Seasonality)')
    sns.boxplot(data=df_clean, x='month', y='value', order=months_order_sliced)
    plt.xlabel('Month')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
