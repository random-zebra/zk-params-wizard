#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2020 The PIVX developers
# Distributed under the MIT software license, see the accompanying
# file LICENSE.txt or http://www.opensource.org/licenses/mit-license.php.

APP_VERSION = "0.0.1"     # !TODO: move to version file

import sys
import os

def set_src_dir():
    if getattr(sys, 'frozen', False):
        print("Running in a bundle")
        # running in a bundle
        sys.path.append(os.path.join(sys._MEIPASS, 'src'))
        # if linux export qt plugins path
        if sys.platform == 'linux':
            os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(sys._MEIPASS, 'PyQt5', 'Qt', 'plugins')
    else:
        # running live
        print("Running live")
        sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

if __name__ == '__main__':
    set_src_dir()

    # Create App and main window
    from PyQt5.QtWidgets import QApplication
    from mainwindow import MainWindow
    app = QApplication(sys.argv)
    ex = MainWindow(app, APP_VERSION)

    # Execute App
    app.exec_()
    try:
        app.deleteLater()
    except Exception as e:
        print(e)

    sys.exit()
