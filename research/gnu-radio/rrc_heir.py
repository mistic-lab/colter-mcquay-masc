#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: BER 4FSK 
# Author: Colter McQuay
# Generated: Fri May 17 17:44:04 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
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
import tcola


class rrc_heir(gr.top_block, Qt.QWidget):

    def __init__(self, parameter_0=0):
        gr.top_block.__init__(self, "BER 4FSK ")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("BER 4FSK ")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "rrc_heir")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Parameters
        ##################################################
        self.parameter_0 = parameter_0

        ##################################################
        # Variables
        ##################################################
        self.samp_per_sym = samp_per_sym = 120
        self.symb_rate = symb_rate = 1200
        self.rrc_taps = rrc_taps = samp_per_sym*6+1
        self.tcola_r = tcola_r = 1
        self.tcola_m = tcola_m = 32
        self.symbol_delay = symbol_delay = rrc_taps/samp_per_sym
        self.samp_rate = samp_rate = symb_rate*samp_per_sym
        self.noise = noise = 0
        self.fsk_deviation_hz = fsk_deviation_hz = 648
        self.fc = fc = 900e6
        self.bits_per_sym = bits_per_sym = 2

        ##################################################
        # Blocks
        ##################################################
        self._noise_range = Range(0, 5, 0.01, 0, 200)
        self._noise_win = RangeWidget(self._noise_range, self.set_noise, "Noise", "counter_slider", float)
        self.top_layout.addWidget(self._noise_win)
        self.tcola_time_compression_0 = tcola.time_compression_c(tcola_m, tcola_r, ())
        self.tcola_overlap_add_0 = tcola.overlap_add_c(tcola_m, tcola_r, ())
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	100, #size
        	samp_rate, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(0, 3)
        
        self.qtgui_time_sink_x_0_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()
        
        labels = ["Symbols", "Received Symbols", "RRC RX", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 2, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	4096, #size
        	samp_rate, #samp_rate
        	"", #name
        	3 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ["Post RRC Tx", "Post RRC Rx", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(3):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_number_sink_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0.set_title("")
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        units = ["", "", "", "", "",
                 "", "", "", "", ""]
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_0.set_min(i, 0.0)
            self.qtgui_number_sink_0_0.set_max(i, 1)
            self.qtgui_number_sink_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_0_win)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("")
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        units = ["", "", "", "", "",
                 "", "", "", "", ""]
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, -7)
            self.qtgui_number_sink_0.set_max(i, 0)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_win)
        self.four_level_rrc_transmitter_0 = four_level_rrc_transmitter(
            alpha=0.350,
            bits_per_symbol=2,
            rrc_taps=rrc_taps,
            samp_per_sym=samp_per_sym,
            sym_rate=symb_rate,
        )
        self.four_level_rrc_receiver_0_0 = four_level_rrc_receiver(
            alpha=0.350,
            bits_per_sym=2,
            rrc_taps=rrc_taps,
            samp_per_sym=samp_per_sym,
            sym_rate=symb_rate,
        )
        self.four_level_rrc_receiver_0 = four_level_rrc_receiver(
            alpha=0.350,
            bits_per_sym=2,
            rrc_taps=rrc_taps,
            samp_per_sym=samp_per_sym,
            sym_rate=symb_rate,
        )
        self.fec_ber_bf_0 = fec.ber_bf(False, 100, -7.0)
        self.digital_glfsr_source_x_0 = digital.glfsr_source_b(8, True, 0, 1)
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=noise,
        	frequency_offset=0.0,
        	epsilon=1.0,
        	taps=(1, ),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_vco_c_0 = blocks.vco_c(samp_rate, fsk_deviation_hz*2*math.pi, 1)
        self.blocks_pack_k_bits_bb_0_0 = blocks.pack_k_bits_bb(8)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_char*1)
        self.blocks_delay_2 = blocks.delay(gr.sizeof_char*1, (symbol_delay+symb_rate)*bits_per_sym-2)
        self.blocks_delay_0_0_0 = blocks.delay(gr.sizeof_gr_complex*1, samp_rate)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_gr_complex*1, samp_rate-tcola_m)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, symbol_delay*samp_per_sym/2+samp_rate)
        self.blocks_char_to_float_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.blks2_error_rate_0 = grc_blks2.error_rate(
        	type='BER',
        	win_size=1000,
        	bits_per_symbol=1,
        )
        self.analog_quadrature_demod_cf_0_0 = analog.quadrature_demod_cf(samp_rate/(2*math.pi*fsk_deviation_hz))
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(samp_rate/(2*math.pi*fsk_deviation_hz))

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.four_level_rrc_receiver_0, 0))    
        self.connect((self.analog_quadrature_demod_cf_0_0, 0), (self.four_level_rrc_receiver_0_0, 0))    
        self.connect((self.blks2_error_rate_0, 0), (self.qtgui_number_sink_0_0, 0))    
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_0_0, 1))    
        self.connect((self.blocks_char_to_float_0_0, 0), (self.qtgui_time_sink_x_0_0, 0))    
        self.connect((self.blocks_delay_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.blocks_delay_0_0, 0), (self.analog_quadrature_demod_cf_0, 0))    
        self.connect((self.blocks_delay_0_0_0, 0), (self.analog_quadrature_demod_cf_0_0, 0))    
        self.connect((self.blocks_delay_2, 0), (self.blks2_error_rate_0, 0))    
        self.connect((self.blocks_delay_2, 0), (self.blocks_char_to_float_0_0, 0))    
        self.connect((self.blocks_delay_2, 0), (self.blocks_pack_k_bits_bb_0, 0))    
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.fec_ber_bf_0, 0))    
        self.connect((self.blocks_pack_k_bits_bb_0_0, 0), (self.fec_ber_bf_0, 1))    
        self.connect((self.blocks_vco_c_0, 0), (self.blocks_delay_0_0_0, 0))    
        self.connect((self.blocks_vco_c_0, 0), (self.tcola_time_compression_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.tcola_overlap_add_0, 0))    
        self.connect((self.digital_glfsr_source_x_0, 0), (self.blocks_delay_2, 0))    
        self.connect((self.digital_glfsr_source_x_0, 0), (self.four_level_rrc_transmitter_0, 0))    
        self.connect((self.fec_ber_bf_0, 0), (self.qtgui_number_sink_0, 0))    
        self.connect((self.four_level_rrc_receiver_0, 2), (self.blks2_error_rate_0, 1))    
        self.connect((self.four_level_rrc_receiver_0, 2), (self.blocks_char_to_float_0, 0))    
        self.connect((self.four_level_rrc_receiver_0, 2), (self.blocks_pack_k_bits_bb_0_0, 0))    
        self.connect((self.four_level_rrc_receiver_0, 0), (self.qtgui_time_sink_x_0, 1))    
        self.connect((self.four_level_rrc_receiver_0_0, 2), (self.blocks_null_sink_0, 0))    
        self.connect((self.four_level_rrc_receiver_0_0, 0), (self.qtgui_time_sink_x_0, 2))    
        self.connect((self.four_level_rrc_transmitter_0, 1), (self.blocks_delay_0, 0))    
        self.connect((self.four_level_rrc_transmitter_0, 1), (self.blocks_vco_c_0, 0))    
        self.connect((self.tcola_overlap_add_0, 0), (self.blocks_delay_0_0, 0))    
        self.connect((self.tcola_time_compression_0, 0), (self.channels_channel_model_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "rrc_heir")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_parameter_0(self):
        return self.parameter_0

    def set_parameter_0(self, parameter_0):
        self.parameter_0 = parameter_0

    def get_samp_per_sym(self):
        return self.samp_per_sym

    def set_samp_per_sym(self, samp_per_sym):
        self.samp_per_sym = samp_per_sym
        self.set_rrc_taps(self.samp_per_sym*6+1)
        self.set_samp_rate(self.symb_rate*self.samp_per_sym)
        self.set_symbol_delay(self.rrc_taps/self.samp_per_sym)
        self.four_level_rrc_receiver_0.set_samp_per_sym(self.samp_per_sym)
        self.four_level_rrc_receiver_0_0.set_samp_per_sym(self.samp_per_sym)
        self.four_level_rrc_transmitter_0.set_samp_per_sym(self.samp_per_sym)
        self.blocks_delay_0.set_dly(self.symbol_delay*self.samp_per_sym/2+self.samp_rate)

    def get_symb_rate(self):
        return self.symb_rate

    def set_symb_rate(self, symb_rate):
        self.symb_rate = symb_rate
        self.set_samp_rate(self.symb_rate*self.samp_per_sym)
        self.four_level_rrc_receiver_0.set_sym_rate(self.symb_rate)
        self.four_level_rrc_receiver_0_0.set_sym_rate(self.symb_rate)
        self.four_level_rrc_transmitter_0.set_sym_rate(self.symb_rate)
        self.blocks_delay_2.set_dly((self.symbol_delay+self.symb_rate)*self.bits_per_sym-2)

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.set_symbol_delay(self.rrc_taps/self.samp_per_sym)
        self.four_level_rrc_receiver_0.set_rrc_taps(self.rrc_taps)
        self.four_level_rrc_receiver_0_0.set_rrc_taps(self.rrc_taps)
        self.four_level_rrc_transmitter_0.set_rrc_taps(self.rrc_taps)

    def get_tcola_r(self):
        return self.tcola_r

    def set_tcola_r(self, tcola_r):
        self.tcola_r = tcola_r

    def get_tcola_m(self):
        return self.tcola_m

    def set_tcola_m(self, tcola_m):
        self.tcola_m = tcola_m
        self.blocks_delay_0_0.set_dly(self.samp_rate-self.tcola_m)

    def get_symbol_delay(self):
        return self.symbol_delay

    def set_symbol_delay(self, symbol_delay):
        self.symbol_delay = symbol_delay
        self.blocks_delay_0.set_dly(self.symbol_delay*self.samp_per_sym/2+self.samp_rate)
        self.blocks_delay_2.set_dly((self.symbol_delay+self.symb_rate)*self.bits_per_sym-2)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_quadrature_demod_cf_0.set_gain(self.samp_rate/(2*math.pi*self.fsk_deviation_hz))
        self.analog_quadrature_demod_cf_0_0.set_gain(self.samp_rate/(2*math.pi*self.fsk_deviation_hz))
        self.blocks_delay_0_0_0.set_dly(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.blocks_delay_0.set_dly(self.symbol_delay*self.samp_per_sym/2+self.samp_rate)
        self.blocks_delay_0_0.set_dly(self.samp_rate-self.tcola_m)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        self.channels_channel_model_0.set_noise_voltage(self.noise)

    def get_fsk_deviation_hz(self):
        return self.fsk_deviation_hz

    def set_fsk_deviation_hz(self, fsk_deviation_hz):
        self.fsk_deviation_hz = fsk_deviation_hz
        self.analog_quadrature_demod_cf_0.set_gain(self.samp_rate/(2*math.pi*self.fsk_deviation_hz))
        self.analog_quadrature_demod_cf_0_0.set_gain(self.samp_rate/(2*math.pi*self.fsk_deviation_hz))

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc

    def get_bits_per_sym(self):
        return self.bits_per_sym

    def set_bits_per_sym(self, bits_per_sym):
        self.bits_per_sym = bits_per_sym
        self.blocks_delay_2.set_dly((self.symbol_delay+self.symb_rate)*self.bits_per_sym-2)


def argument_parser():
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option(
        "-n", "--parameter-0", dest="parameter_0", type="eng_float", default=eng_notation.num_to_str(0),
        help="Set Noise [default=%default]")
    return parser


def main(top_block_cls=rrc_heir, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(parameter_0=options.parameter_0)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
