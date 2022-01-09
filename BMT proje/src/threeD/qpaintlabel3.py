from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtCore import *
import numpy as np
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class QPaintLabel3(QLabel):

    mpsignal = pyqtSignal(str)

    def __init__(self, parent):
        super(QLabel, self).__init__(parent)

        self.setMinimumSize(1, 1)
        self.setMouseTracking(False)
        self.image = None
        self.processedImage = None
        self.imgr, self.imgc = None, None
        self.imgpos_x, self.imgpos_y = None, None
        self.pos_x = 20
        self.pos_y = 20
        self.imgr, self.imgc = None, None
    
        self.pos_xy = []
       
        self.crosscenter = [0, 0]
        self.mouseclicked = None
        self.sliceclick = False
       
        self.type = 'general'
        self.slice_loc = [0, 0, 0]
        self.slice_loc_restore = [0, 0, 0]
        self.mousein = False

    def mouseMoveEvent(self, event: QMouseEvent):
        super().mouseMoveEvent(event)

        if not self.mousein:
            self.slice_loc_restore = self.slice_loc.copy()
            self.mousein = True

        self.imgpos_x = int(event.x() * self.imgc / self.width())
        self.imgpos_y = int(event.y() * self.imgr / self.height())

        if self.type == 'axial':
            self.slice_loc[0:2] = self.imgpos_x, self.imgpos_y
        elif self.type == 'sagittal':
            self.slice_loc[1:3] = self.imgpos_x, self.imgr - self.imgpos_y
        elif self.type == 'coronal':
            self.slice_loc[0] = self.imgpos_x
            self.slice_loc[2] = self.imgr - self.imgpos_y
        else:
            pass
        self.update()

    def leaveEvent(self, event):
        self.mousein = False
        self.slice_loc = self.slice_loc_restore
        self.update()

    def mousePressEvent(self, event: QMouseEvent):
        self.crosscenter[0] = event.x()
        self.crosscenter[1] = event.y()

        self.mpsignal.emit(self.type)

        self.slice_loc_restore = self.slice_loc.copy()
        self.update()

    def display_image(self, window=1):
        self.imgr, self.imgc = self.processedImage.shape[0:2]
        qformat = QImage.Format_Indexed8
        if len(self.processedImage.shape) == 3:  # rows[0], cols[1], channels[2]
            if (self.processedImage.shape[2]) == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(self.processedImage, self.processedImage.shape[1], self.processedImage.shape[0],
                     self.processedImage.strides[0], qformat)
        img = img.rgbSwapped()
        w, h = self.width(), self.height()
        if window == 1:
            self.setScaledContents(True)
            backlash = self.lineWidth() * 2
            self.setPixmap(QPixmap.fromImage(img).scaled(w - backlash, h - backlash, Qt.IgnoreAspectRatio))
            self.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        # 
        loc = QFont()
        loc.setPixelSize(10)
        loc.setBold(True)
        loc.setItalic(True)
        loc.setPointSize(15)
        if self.pixmap():
            painter = QPainter(self)
            pixmap = self.pixmap()
            painter.drawPixmap(self.rect(), pixmap)

            painter.setPen(QPen(Qt.magenta, 10))
            painter.setFont(loc)
            painter.drawText(5, self.height() - 5, 'x = %3d  ,  y = %3d  ,  z = %3d'
                             % (self.slice_loc[0], self.slice_loc[1], self.slice_loc[2]))

            if self.type == 'axial':
            
                painter.setPen(QPen(Qt.red, 3))
                painter.drawLine(self.crosscenter[0], 0, self.crosscenter[0], self.height())
                
                painter.setPen(QPen(Qt.cyan, 3))
                painter.drawLine(0, self.crosscenter[1], self.width(), self.crosscenter[1])
                #
                painter.setPen(QPen(Qt.yellow, 3))
                painter.drawPoint(self.crosscenter[0], self.crosscenter[1])

            elif self.type == 'sagittal':
                # 
                painter.setPen(QPen(Qt.cyan, 3))
                painter.drawLine(self.crosscenter[0], 0, self.crosscenter[0], self.height())
                # 
                painter.setPen(QPen(Qt.yellow, 3))
                painter.drawLine(0, self.crosscenter[1], self.width(), self.crosscenter[1])
                # 
                painter.setPen(QPen(Qt.red, 3))
                painter.drawPoint(self.crosscenter[0], self.crosscenter[1])

            elif self.type == 'coronal':
                # 
                painter.setPen(QPen(Qt.red, 3))
                painter.drawLine(self.crosscenter[0], 0, self.crosscenter[0], self.height())
                # 
                painter.setPen(QPen(Qt.yellow, 3))
                painter.drawLine(0, self.crosscenter[1], self.width(), self.crosscenter[1])
                # 
                painter.setPen(QPen(Qt.cyan, 3))
                painter.drawPoint(self.crosscenter[0], self.crosscenter[1])

            else:
                pass


def linear_convert(img):
    convert_scale = 255.0 / (np.max(img) - np.min(img))
    converted_img = convert_scale*img-(convert_scale*np.min(img))
    return converted_img
