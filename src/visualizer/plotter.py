import os
import simplekml
from definitions import ROOT_DIR
from src.extractor.read import ReadRawData


class Plotter:

    def __init__(self, date):

        if isinstance(date, str):
            self.reader = ReadRawData(date=date)
        else:
            raise TypeError('"date" must be of type string')

        self.visualization_kml_dir     = ROOT_DIR + '/plots/kml/'
        self.visualization_png_gt_dir  = ROOT_DIR + '/plots/png/gt/'
        self.visualization_png_gps_rtk_dir = ROOT_DIR + '/plots/png/gps_rtk/'
        self.visualization_png_gps_dir = ROOT_DIR + '/plots/png/gps/'
        self.visualization_png_wheel_odom_dir = ROOT_DIR + '/plots/png/wheel_odom/'
        self.visualization_png_all_dir = ROOT_DIR + '/plots/png/all/'

        # check directories
        if not os.path.exists(self.visualization_kml_dir):
            os.makedirs(self.visualization_kml_dir)

        if not os.path.exists(self.visualization_png_gt_dir):
            os.makedirs(self.visualization_png_gt_dir)

        if not os.path.exists(self.visualization_png_gps_rtk_dir):
            os.makedirs(self.visualization_png_gps_rtk_dir)

        if not os.path.exists(self.visualization_png_gps_dir):
            os.makedirs(self.visualization_png_gps_dir)

        if not os.path.exists(self.visualization_png_wheel_odom_dir):
            os.makedirs(self.visualization_png_wheel_odom_dir)

        if not os.path.exists(self.visualization_png_all_dir):
            os.makedirs(self.visualization_png_all_dir)

        self.kml = simplekml.Kml()
        self.green = simplekml.Color.lime
        self.red = simplekml.Color.red
        self.yellow = simplekml.Color.yellow
        self.magenta = simplekml.Color.magenta