# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/06_inference.ipynb (unless otherwise specified).

__all__ = ['bin_preds']

# Cell
import pandas as pd
import numpy as np

# Cell
def bin_preds(df:pd.DataFrame, bins:np.ndarray=np.linspace(0.,1.,11), pred_name='pred')