#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: E310 Top Block
# Generated: Sat Jan 16 07:18:33 2016
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
from dmr_signal_source import dmr_signal_source  # grc-generated hier_block
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import tcola
import time


class e310_top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "E310 Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("E310 Top Block")
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

        self.settings = Qt.QSettings("GNU Radio", "e310_top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.tcola_r = tcola_r = 1
        self.tcola_m = tcola_m = 32
        self.samp_rate = samp_rate = 30000
        self.usrp_fs = usrp_fs = samp_rate*tcola_m/tcola_r
        self.fc = fc = 915000000

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("serial=F644E0", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(usrp_fs)
        self.uhd_usrp_sink_0.set_center_freq(fc, 0)
        self.uhd_usrp_sink_0.set_normalized_gain(.8, 0)
        self.tcola_time_compression_0 = tcola.time_compression_c(tcola_m, tcola_r, ())
        self.dmr_signal_source_0 = dmr_signal_source(
            root_directory="/media/ramdisk/",
            signal_index=0,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.dmr_signal_source_0, 0), (self.tcola_time_compression_0, 0))    
        self.connect((self.tcola_time_compression_0, 0), (self.uhd_usrp_sink_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "e310_top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_tcola_r(self):
        return self.tcola_r

    def set_tcola_r(self, tcola_r):
        self.tcola_r = tcola_r
        self.set_usrp_fs(self.samp_rate*self.tcola_m/self.tcola_r)

    def get_tcola_m(self):
        return self.tcola_m

    def set_tcola_m(self, tcola_m):
        self.tcola_m = tcola_m
        self.set_usrp_fs(self.samp_rate*self.tcola_m/self.tcola_r)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_usrp_fs(self.samp_rate*self.tcola_m/self.tcola_r)

    def get_usrp_fs(self):
        return self.usrp_fs

    def set_usrp_fs(self, usrp_fs):
        self.usrp_fs = usrp_fs
        self.uhd_usrp_sink_0.set_samp_rate(self.usrp_fs)

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self.uhd_usrp_sink_0.set_center_freq(self.fc, 0)


def main(top_block_cls=e310_top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
