# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/05_plotting.ipynb (unless otherwise specified).

__all__ = ['plt_style', 'plt_sz', 'plt_cat_pal', 'plt_tk_sz', 'plt_lbl_sz', 'plt_title_sz', 'plt_leg_sz', 'plot_preds']

# Cell
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional

# Cell
plt_style    = {'style':'whitegrid', 'rc':{'patch.edgecolor':'none'}}
plt_sz       = 8
plt_cat_pal  = 'tab10'
plt_tk_sz    = 16
plt_lbl_sz   = 24
plt_title_sz = 26
plt_leg_sz   = 16

# Cell
def plot_preds(df:pd.DataFrame, bin_edges:np.ndarray=np.linspace(0.,1.,11),
               pred_name:str='pred', wgt_name:Optional[str]=None) -> None:
    with sns.axes_style(**plt_style), sns.color_palette(plt_cat_pal) as palette:
        plt.figure(figsize=(plt_sz*16/9, plt_sz))
        for t,n in ((0,'Background'),(1,'Signal')):
            cut = (df['gen_target'] == t)
            hist_kws = {} if wgt_name is None else {'weights':wgt_scale*df.loc[cut, wgt_name]}
            sns.distplot(df.loc[cut, pred_name], bins=bin_edges, label=n, hist_kws=hist_kws, norm_hist=True, kde=False)
        plt.legend(fontsize=plt_leg_sz)
        plt.xlabel("Class prediction", fontsize=plt_lbl_sz)
        plt.ylabel(r"$\frac{1}{N}\ \frac{dN}{dp}$", fontsize=plt_lbl_sz)
        plt.xticks(fontsize=plt_tk_sz)
        plt.yticks(fontsize=plt_tk_sz)
        plt.show()