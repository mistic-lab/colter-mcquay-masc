#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: BER BPSK
# Author: Colter McQuay
# Generated: Wed May 29 11:43:00 2019
##################################################

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from four_level_symbol_mapper import four_level_symbol_mapper  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fec
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
from sample_counter import sample_counter  # grc-generated hier_block
import math


class bpsk_ber_measure(gr.top_block):

    def __init__(self, ebno_db=10, min_errors=100, samp_per_sym=1):
        gr.top_block.__init__(self, "BER BPSK")

        ##################################################
        # Parameters
        ##################################################
        self.ebno_db = ebno_db
        self.min_errors = min_errors
        self.samp_per_sym = samp_per_sym

        ##################################################
        # Variables
        ##################################################
        self.symb_rate = symb_rate = 4800
        self.bits_per_sym = bits_per_sym = 1
        self.bit_rate = bit_rate = symb_rate*bits_per_sym
        self.average_power = average_power = 1.0
        self.ebno = ebno = 10**(ebno_db/10.0)
        self.eb = eb = average_power/bit_rate
        self.samp_rate = samp_rate = symb_rate*samp_per_sym
        self.no = no = eb/ebno
        self.noise_variance = noise_variance = no*samp_rate/2.0
        self.A = A = math.sqrt(average_power)

        ##################################################
        # Blocks
        ##################################################
        self.sample_counter = sample_counter()
        self.probe_avg_power = analog.probe_avg_mag_sqrd_f(0, 1)
        self.pack_rx_bits = blocks.pack_k_bits_bb(8)
        self.pack_msg_bits = blocks.pack_k_bits_bb(8)
        self.glfsr = digital.glfsr_source_b(8, True, 0, 1)
        self.four_level_symbol_mapper_0 = four_level_symbol_mapper(
            symbol_map=[-1,1],
        )
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bf(([-A,A]), 1)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_float*1, samp_per_sym)
        self.blocks_keep_one_in_n_0 = blocks.keep_one_in_n(gr.sizeof_float*1, samp_per_sym)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.ber_sink = blocks.vector_sink_f(1)
        self.ber_measure = fec.ber_bf(True, min_errors, -7.0)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, math.sqrt(noise_variance), 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.ber_measure, 0), (self.ber_sink, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_keep_one_in_n_0, 0))    
        self.connect((self.blocks_keep_one_in_n_0, 0), (self.four_level_symbol_mapper_0, 0))    
        self.connect((self.blocks_repeat_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_repeat_0, 0), (self.probe_avg_power, 0))    
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.blocks_repeat_0, 0))    
        self.connect((self.four_level_symbol_mapper_0, 0), (self.sample_counter, 0))    
        self.connect((self.glfsr, 0), (self.digital_chunks_to_symbols_xx_0, 0))    
        self.connect((self.glfsr, 0), (self.pack_msg_bits, 0))    
        self.connect((self.pack_msg_bits, 0), (self.ber_measure, 0))    
        self.connect((self.pack_rx_bits, 0), (self.ber_measure, 1))    
        self.connect((self.sample_counter, 0), (self.pack_rx_bits, 0))    

    def get_ebno_db(self):
        return self.ebno_db

    def set_ebno_db(self, ebno_db):
        self.ebno_db = ebno_db
        self.set_ebno(10**(self.ebno_db/10.0))

    def get_min_errors(self):
        return self.min_errors

    def set_min_errors(self, min_errors):
        self.min_errors = min_errors

    def get_samp_per_sym(self):
        return self.samp_per_sym

    def set_samp_per_sym(self, samp_per_sym):
        self.samp_per_sym = samp_per_sym
        self.set_samp_rate(self.symb_rate*self.samp_per_sym)
        self.blocks_keep_one_in_n_0.set_n(self.samp_per_sym)

    def get_symb_rate(self):
        return self.symb_rate

    def set_symb_rate(self, symb_rate):
        self.symb_rate = symb_rate
        self.set_bit_rate(self.symb_rate*self.bits_per_sym)
        self.set_samp_rate(self.symb_rate*self.samp_per_sym)

    def get_bits_per_sym(self):
        return self.bits_per_sym

    def set_bits_per_sym(self, bits_per_sym):
        self.bits_per_sym = bits_per_sym
        self.set_bit_rate(self.symb_rate*self.bits_per_sym)

    def get_bit_rate(self):
        return self.bit_rate

    def set_bit_rate(self, bit_rate):
        self.bit_rate = bit_rate
        self.set_eb(self.average_power/self.bit_rate)

    def get_average_power(self):
        return self.average_power

    def set_average_power(self, average_power):
        self.average_power = average_power
        self.set_A(math.sqrt(self.average_power))
        self.set_eb(self.average_power/self.bit_rate)

    def get_ebno(self):
        return self.ebno

    def set_ebno(self, ebno):
        self.ebno = ebno
        self.set_no(self.eb/self.ebno)

    def get_eb(self):
        return self.eb

    def set_eb(self, eb):
        self.eb = eb
        self.set_no(self.eb/self.ebno)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_noise_variance(self.no*self.samp_rate/2.0)

    def get_no(self):
        return self.no

    def set_no(self, no):
        self.no = no
        self.set_noise_variance(self.no*self.samp_rate/2.0)

    def get_noise_variance(self):
        return self.noise_variance

    def set_noise_variance(self, noise_variance):
        self.noise_variance = noise_variance
        self.analog_noise_source_x_0.set_amplitude(math.sqrt(self.noise_variance))

    def get_A(self):
        return self.A

    def set_A(self, A):
        self.A = A
        self.digital_chunks_to_symbols_xx_0.set_symbol_table(([-self.A,self.A]))


def argument_parser():
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option(
        "-n", "--ebno-db", dest="ebno_db", type="eng_float", default=eng_notation.num_to_str(10),
        help="Set Eb/N0 (dB) [default=%default]")
    parser.add_option(
        "-e", "--min-errors", dest="min_errors", type="intx", default=100,
        help="Set BER Min Errors [default=%default]")
    parser.add_option(
        "-s", "--samp-per-sym", dest="samp_per_sym", type="intx", default=1,
        help="Set Samples per Symbol [default=%default]")
    return parser


def main(top_block_cls=bpsk_ber_measure, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(ebno_db=options.ebno_db, min_errors=options.min_errors, samp_per_sym=options.samp_per_sym)
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
