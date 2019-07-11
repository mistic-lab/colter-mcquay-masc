#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: BER 4FSK TCOLA
# Author: Colter McQuay
# Generated: Thu May 23 13:33:49 2019
##################################################

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
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
from sample_counter import sample_counter  # grc-generated hier_block
import math
import tcola


class ber_measure_4fsk_tcola(gr.top_block):

    def __init__(self, min_errors=100, noise=0, samp_per_sym=50, tcola_m=32, tcola_r=1):
        gr.top_block.__init__(self, "BER 4FSK TCOLA")

        ##################################################
        # Parameters
        ##################################################
        self.min_errors = min_errors
        self.noise = noise
        self.samp_per_sym = samp_per_sym
        self.tcola_m = tcola_m
        self.tcola_r = tcola_r

        ##################################################
        # Variables
        ##################################################
        self.symb_rate = symb_rate = 4800
        self.rrc_taps = rrc_taps = samp_per_sym*6+1
        self.symbol_delay = symbol_delay = rrc_taps/samp_per_sym-1
        self.samp_rate = samp_rate = symb_rate*samp_per_sym
        self.fsk_deviation_hz = fsk_deviation_hz = 648
        self.bits_skip = bits_skip = 10000
        self.bits_per_sym = bits_per_sym = 2

        ##################################################
        # Blocks
        ##################################################
        self.delay = blocks.delay(gr.sizeof_char*1, (symbol_delay+symb_rate)*bits_per_sym)
        self.vco = blocks.vco_c(samp_rate, fsk_deviation_hz*2*math.pi, 1)
        self.tcola_time_compression_0 = tcola.time_compression_c(tcola_m, tcola_r, ())
        self.tcola_overlap_add_0 = tcola.overlap_add_c(tcola_m, tcola_r, ())
        self.sample_counter = sample_counter()
        self.quadrature_demod = analog.quadrature_demod_cf(samp_rate/(2*math.pi*fsk_deviation_hz))
        self.probe_avg_power = analog.probe_avg_mag_sqrd_c(0, 1)
        self.pack_rx_bits = blocks.pack_k_bits_bb(8)
        self.pack_msg_bits = blocks.pack_k_bits_bb(8)
        self.glfsr = digital.glfsr_source_b(8, True, 0, 1)
        self.four_level_rrc_transmitter = four_level_rrc_transmitter(
            alpha=0.350,
            bits_per_symbol=2,
            rrc_taps=rrc_taps,
            samp_per_sym=samp_per_sym,
            sym_rate=symb_rate,
        )
        self.four_level_rrc_receiver = four_level_rrc_receiver(
            alpha=0.350,
            bits_per_sym=2,
            rrc_taps=rrc_taps,
            samp_per_sym=samp_per_sym,
            sym_rate=symb_rate,
        )
        self.channel_model = channels.channel_model(
        	noise_voltage=noise,
        	frequency_offset=0.0,
        	epsilon=1.0,
        	taps=(1, ),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_skiphead_0_0 = blocks.skiphead(gr.sizeof_char*1, bits_skip)
        self.blocks_skiphead_0 = blocks.skiphead(gr.sizeof_char*1, bits_skip)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_gr_complex*1, samp_rate-tcola_m)
        self.ber_sink = blocks.vector_sink_f(1)
        self.ber_measure = fec.ber_bf(True, min_errors, -7.0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.ber_measure, 0), (self.ber_sink, 0))    
        self.connect((self.blocks_delay_0_0, 0), (self.quadrature_demod, 0))    
        self.connect((self.blocks_skiphead_0, 0), (self.sample_counter, 0))    
        self.connect((self.blocks_skiphead_0_0, 0), (self.pack_rx_bits, 0))    
        self.connect((self.channel_model, 0), (self.tcola_overlap_add_0, 0))    
        self.connect((self.delay, 0), (self.blocks_skiphead_0, 0))    
        self.connect((self.four_level_rrc_receiver, 2), (self.blocks_skiphead_0_0, 0))    
        self.connect((self.four_level_rrc_transmitter, 1), (self.vco, 0))    
        self.connect((self.glfsr, 0), (self.delay, 0))    
        self.connect((self.glfsr, 0), (self.four_level_rrc_transmitter, 0))    
        self.connect((self.pack_msg_bits, 0), (self.ber_measure, 0))    
        self.connect((self.pack_rx_bits, 0), (self.ber_measure, 1))    
        self.connect((self.quadrature_demod, 0), (self.four_level_rrc_receiver, 0))    
        self.connect((self.sample_counter, 0), (self.pack_msg_bits, 0))    
        self.connect((self.tcola_overlap_add_0, 0), (self.blocks_delay_0_0, 0))    
        self.connect((self.tcola_time_compression_0, 0), (self.channel_model, 0))    
        self.connect((self.tcola_time_compression_0, 0), (self.probe_avg_power, 0))    
        self.connect((self.vco, 0), (self.tcola_time_compression_0, 0))    

    def get_min_errors(self):
        return self.min_errors

    def set_min_errors(self, min_errors):
        self.min_errors = min_errors

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        self.channel_model.set_noise_voltage(self.noise)

    def get_samp_per_sym(self):
        return self.samp_per_sym

    def set_samp_per_sym(self, samp_per_sym):
        self.samp_per_sym = samp_per_sym
        self.set_rrc_taps(self.samp_per_sym*6+1)
        self.set_samp_rate(self.symb_rate*self.samp_per_sym)
        self.set_symbol_delay(self.rrc_taps/self.samp_per_sym-1)
        self.four_level_rrc_receiver.set_samp_per_sym(self.samp_per_sym)
        self.four_level_rrc_transmitter.set_samp_per_sym(self.samp_per_sym)

    def get_tcola_m(self):
        return self.tcola_m

    def set_tcola_m(self, tcola_m):
        self.tcola_m = tcola_m
        self.blocks_delay_0_0.set_dly(self.samp_rate-self.tcola_m)

    def get_tcola_r(self):
        return self.tcola_r

    def set_tcola_r(self, tcola_r):
        self.tcola_r = tcola_r

    def get_symb_rate(self):
        return self.symb_rate

    def set_symb_rate(self, symb_rate):
        self.symb_rate = symb_rate
        self.set_samp_rate(self.symb_rate*self.samp_per_sym)
        self.four_level_rrc_receiver.set_sym_rate(self.symb_rate)
        self.four_level_rrc_transmitter.set_sym_rate(self.symb_rate)
        self.delay.set_dly((self.symbol_delay+self.symb_rate)*self.bits_per_sym)

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.set_symbol_delay(self.rrc_taps/self.samp_per_sym-1)
        self.four_level_rrc_receiver.set_rrc_taps(self.rrc_taps)
        self.four_level_rrc_transmitter.set_rrc_taps(self.rrc_taps)

    def get_symbol_delay(self):
        return self.symbol_delay

    def set_symbol_delay(self, symbol_delay):
        self.symbol_delay = symbol_delay
        self.delay.set_dly((self.symbol_delay+self.symb_rate)*self.bits_per_sym)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_delay_0_0.set_dly(self.samp_rate-self.tcola_m)
        self.quadrature_demod.set_gain(self.samp_rate/(2*math.pi*self.fsk_deviation_hz))

    def get_fsk_deviation_hz(self):
        return self.fsk_deviation_hz

    def set_fsk_deviation_hz(self, fsk_deviation_hz):
        self.fsk_deviation_hz = fsk_deviation_hz
        self.quadrature_demod.set_gain(self.samp_rate/(2*math.pi*self.fsk_deviation_hz))

    def get_bits_skip(self):
        return self.bits_skip

    def set_bits_skip(self, bits_skip):
        self.bits_skip = bits_skip

    def get_bits_per_sym(self):
        return self.bits_per_sym

    def set_bits_per_sym(self, bits_per_sym):
        self.bits_per_sym = bits_per_sym
        self.delay.set_dly((self.symbol_delay+self.symb_rate)*self.bits_per_sym)


def argument_parser():
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option(
        "-e", "--min-errors", dest="min_errors", type="intx", default=100,
        help="Set BER Min Errors [default=%default]")
    parser.add_option(
        "-n", "--noise", dest="noise", type="eng_float", default=eng_notation.num_to_str(0),
        help="Set Noise [default=%default]")
    parser.add_option(
        "-s", "--samp-per-sym", dest="samp_per_sym", type="intx", default=50,
        help="Set Samples per Symbol [default=%default]")
    parser.add_option(
        "-m", "--tcola-m", dest="tcola_m", type="intx", default=32,
        help="Set TCOLA Window Size [default=%default]")
    parser.add_option(
        "-r", "--tcola-r", dest="tcola_r", type="intx", default=1,
        help="Set TCOLA Hop Size [default=%default]")
    return parser


def main(top_block_cls=ber_measure_4fsk_tcola, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(min_errors=options.min_errors, noise=options.noise, samp_per_sym=options.samp_per_sym, tcola_m=options.tcola_m, tcola_r=options.tcola_r)
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
