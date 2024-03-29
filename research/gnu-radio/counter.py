"""
Embedded Python Blocks:

Each this file is saved, GRC will instantiate the first class it finds to get
ports and parameters of your block. The arguments to __init__  will be the
parameters. All of them are required to have default values!
"""
import numpy as np
from gnuradio import gr

class counter(gr.sync_block):
    def __init__(self):  # only default arguments here
        gr.sync_block.__init__(
            self,
            name='Sample Counter',
            in_sig=[np.byte],
            out_sig=[np.byte]
        )
        self.count = 0

    def get_count(self):
	return self.count

    def work(self, input_items, output_items):
        output_items[0][:] = input_items[0]
	items_processed = len(output_items[0])
	self.count = self.count + items_processed
        return items_processed
