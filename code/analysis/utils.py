import os
import numpy as np
import matplotlib.pyplot as plt

this_dir=os.path.dirname(os.path.abspath(__file__))
figures_path=os.path.abspath(os.path.join(this_dir,'../../figures'))

save_figures=False

def set_save_figures(val):
    global save_figures
    save_figures=val

def save_figure(name):
    fig_name = os.path.join(figures_path,name+'.svg')
    if(save_figures is True):
        plt.savfig(fig_name)
    else:
        print('Would have saved figure: ',fig_name)

def int16_samples_to_float32(y):
  """Convert int16 numpy array of audio samples to float32."""
  if y.dtype != np.int16:
    raise ValueError('input samples not int16')
  return y.astype(np.float32) / np.iinfo(np.int16).max