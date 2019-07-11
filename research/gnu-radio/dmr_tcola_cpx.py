#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Dmr Tcola Cpx
# Generated: Thu Apr 25 15:26:00 2019
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

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sys
import time


class dmr_tcola_cpx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Dmr Tcola Cpx")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Dmr Tcola Cpx")
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

        self.settings = Qt.QSettings("GNU Radio", "dmr_tcola_cpx")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.tcola_r = tcola_r = 1
        self.tcola_m = tcola_m = 32
        self.standard_suffix = standard_suffix = "_tc_m="+str(tcola_m)+"_r="+str(tcola_r)
        self.samp_rate = samp_rate = 14000
        self.results_dir = results_dir = "/home/cjam/Documents/colter-thesis-results"
        self.file_name = file_name = "dmr_data1"
        self.usrp_tc_fs = usrp_tc_fs = samp_rate*tcola_m/tcola_r
        self.file_path = file_path = results_dir+"/"+file_name+standard_suffix+".dat"
        self.fc_ism = fc_ism = 915000000
        self.fc_dmr = fc_dmr = 446106250

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_sink_0_1 = uhd.usrp_sink(
        	",".join(("addr=192.168.10.2", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0_1.set_samp_rate(usrp_tc_fs)
        self.uhd_usrp_sink_0_1.set_center_freq(fc_ism, 0)
        self.uhd_usrp_sink_0_1.set_gain(0, 0)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, file_path, True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.uhd_usrp_sink_0_1, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "dmr_tcola_cpx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_tcola_r(self):
        return self.tcola_r

    def set_tcola_r(self, tcola_r):
        self.tcola_r = tcola_r
        self.set_standard_suffix("_tc_m="+str(self.tcola_m)+"_r="+str(self.tcola_r))
        self.set_usrp_tc_fs(self.samp_rate*self.tcola_m/self.tcola_r)

    def get_tcola_m(self):
        return self.tcola_m

    def set_tcola_m(self, tcola_m):
        self.tcola_m = tcola_m
        self.set_standard_suffix("_tc_m="+str(self.tcola_m)+"_r="+str(self.tcola_r))
        self.set_usrp_tc_fs(self.samp_rate*self.tcola_m/self.tcola_r)

    def get_standard_suffix(self):
        return self.standard_suffix

    def set_standard_suffix(self, standard_suffix):
        self.standard_suffix = standard_suffix
        self.set_file_path(self.results_dir+"/"+self.file_name+self.standard_suffix+".dat")

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_usrp_tc_fs(self.samp_rate*self.tcola_m/self.tcola_r)

    def get_results_dir(self):
        return self.results_dir

    def set_results_dir(self, results_dir):
        self.results_dir = results_dir
        self.set_file_path(self.results_dir+"/"+self.file_name+self.standard_suffix+".dat")

    def get_file_name(self):
        return self.file_name

    def set_file_name(self, file_name):
        self.file_name = file_name
        self.set_file_path(self.results_dir+"/"+self.file_name+self.standard_suffix+".dat")

    def get_usrp_tc_fs(self):
        return self.usrp_tc_fs

    def set_usrp_tc_fs(self, usrp_tc_fs):
        self.usrp_tc_fs = usrp_tc_fs
        self.uhd_usrp_sink_0_1.set_samp_rate(self.usrp_tc_fs)

    def get_file_path(self):
        return self.file_path

    def set_file_path(self, file_path):
        self.file_path = file_path
        self.blocks_file_source_0.open(self.file_path, True)

    def get_fc_ism(self):
        return self.fc_ism

    def set_fc_ism(self, fc_ism):
        self.fc_ism = fc_ism
        self.uhd_usrp_sink_0_1.set_center_freq(self.fc_ism, 0)

    def get_fc_dmr(self):
        return self.fc_dmr

    def set_fc_dmr(self, fc_dmr):
        self.fc_dmr = fc_dmr


def main(top_block_cls=dmr_tcola_cpx, options=None):

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
