import os
import numpy as np
import matplotlib.pyplot as plt

this_dir=os.path.dirname(os.path.abspath(__file__))
figures_path="/figures"
data_path=os.path.abspath('/dataset')
results_path=os.path.abspath('/results')

save_figures=False

def get_data_file_path(name):
  return os.path.join(data_path,name)

def get_results_file_path(name):
  return os.path.join(results_path,name)

def set_save_figures(val):
    global save_figures
    save_figures=val

def get_save_figures():
    global save_figures
    return save_figures

def save_figure(name):
    fig_name = os.path.join(figures_path,name+'.pdf')
    if(save_figures is True):
        plt.savefig(fig_name)
    else:
        print('Would have saved figure: ',fig_name)

def int16_samples_to_float32(y):
  """Convert int16 numpy array of audio samples to float32."""
  if y.dtype != np.int16:
    raise ValueError('input samples not int16')
  return y.astype(np.float32) / np.iinfo(np.int16).max

def print_signal(filename):
    orig_sig=np.fromfile(get_results_file_path(f'{filename}.dat'),dtype=np.single);
    plt.figure()
    plt.plot(orig_sig);
    plt.xlabel('Sample')
    plt.ylabel('Amplitude')
    save_figure(f'{filename}_time')

def print_signal_spectrum(filename,fs):
    orig_sig=np.fromfile(get_results_file_path(f'{filename}.dat'),dtype=np.single);
    plt.figure()
    plt.magnitude_spectrum(orig_sig,Fs=fs);
    save_figure(f'{filename}_spectrum');
    
def plot_tc_noise_spectrum(filename,m,r=1):
    tc_dat_file=f'{filename}_tc_m={m}_r={r}.dat';
    dat_vals=np.fromfile(get_results_file_path(tc_dat_file),dtype=np.single);
    plt.title(f'Spectrum of Time Compressed Signal (M={m}, R={r})');
    plt.magnitude_spectrum(dat_vals,Fs=fs*m/r);