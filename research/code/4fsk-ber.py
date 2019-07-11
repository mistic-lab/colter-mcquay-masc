#!/usr/bin/env python

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

try:
    import scipy
    from scipy import stats
except ImportError:
    print("Error: Program requires scipy (www.scipy.org).")
    sys.exit(1)

try:
    from matplotlib import pyplot as plot
except ImportError:
    print("Error: Program requires Matplotlib (matplotlib.sourceforge.net).")
    sys.exit(1)

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from four_level_rrc_receiver import four_level_rrc_receiver  # grc-generated hier_block
from four_level_rrc_transmitter import four_level_rrc_transmitter  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fec
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import math
import sip



def main():
    print("Hello BER")


if __name__ == "__main__":
    main()