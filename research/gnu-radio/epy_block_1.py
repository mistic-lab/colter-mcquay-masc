"""
Embedded Python Blocks:

Each this file is saved, GRC will instantiate the first class it finds to get
ports and parameters of your block. The arguments to __init__  will be the
parameters. All of them are required to have default values!
"""
import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self, base=10.0):  # only default arguments here
        gr.sync_block.__init__(
            self,
            name='power',
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.base = base

    def work(self, input_items, output_items):
        output_items[0][:] = np.power(self.base,input_items[0])
        return len(output_items[0])
