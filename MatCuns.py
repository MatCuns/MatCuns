import pandas as pd
import numpy as np 
from matplotlib import pyplot as plt
from pathlib import Path

"""Series of functions written by myself for easy of use in the future projects, to not rewrite all the functions"""

def import_all_csv(path_files):
    """ Reads all the csv in a folder and returns the pandas dataframe with the name of each csv WITH DATE TIME INDEX AND -99 AS NA """
    
    path = Path(path_files)
    
    for file in path.glob("*.csv"):
        name = file.stem
        
        globals()[name] = pd.read_csv(
            file,
            header=0,
            index_col=0,
            parse_dates=True,
            na_values=-99.99
        )
        
        print(name, "--- Loaded")

def sharpe_ratio(mean_return,risk_free,ann_vol)
    sharpe_Ratio=(mean_return - risk_free)/ann_vol

    return sharpe_Ratio

def sortino_ratio()
    semideviation_annual
    return (annualized_returns - risk_free_rate)/semideviation_annual

def summary_stats(Price_Or_Returns, Returns=True, Sortino_Sharpe=False):
    """ 
    Given DAILY (PD dataframe) Prices or Returns (SPECIFY WITH T or F) 
    Gives Key stats such as ann.volatility, ann. returns, mean return, 
    sharpe ratio, sortino ratio,Max drawdown,
    min and max returns, skewness, kurtosis, historical Var 95%,
    Gaussian VaR 95%, Cornish-Fisher VaR 95%, calmar ratio 
    """
    
    if Returns=False:
        returns=Price_Or_Returns.pct_change()
        returns=returns.dropna()
    else:
        returns=Price_Or_Returns
        
    if Sortino_Sharpe=True:
        sharpe_ratio=sharpe_ratio(mean_return,risk_free,ann_vol)
        sortino_ratio=sortino_Ratio()

    ann_vol=returns.std()*np.sqrt(252)
    ann_returns=returns*np.sqrt(252)
    min_returns=returns.min()
    max_returns=returns.max()
    skewnewss=returns.skewnewss()
    kurtosis=returns.kurtosis()
    mean_return=returns.mean()
    historic_var = -np.percentile(returns, 5)

    




    print("The Annualized Volatility is --> ",ann_vol)
    print("The Annualized Return is --> ", ann_returns)
    print("The Max Return was --> ",max_returns)
    print("The Min Return was --> ", min_returns)
    print("The Mean Return was --> ", mean_return)

    if Sortino_Sharpe=True:
        print("The Sharpe Ratio is --> ", sharpe_ratio)
        print("The Sortino Ratio is --> ", sortino_ratio)
        
        
    
    


def prova_print(c):

    if c>1:
        print("c è maggiore di 1!!!!")
    else:
        print("c è minore di 1!!")