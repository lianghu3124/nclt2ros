import numpy as np
from raw_data import RawData


class ReadRawData(RawData):
    """Class to read the raw data

    USAGE:
            ReadRawData('2013-01-10')

    """
    def __init__(self, date):
        RawData.__init__(self, date=date)

    def read_gt_csv(self, all_in_one=None):
        """reads the data in the ground_truth csv file

        :param   all_in_one: Boolean
        :return: ndarray: containing all data, if all_in_one is True
                 else
                 each column seperated as utimes, x, y, z, roll_rad, pitch_rad, yaw_rad
        """

        gt = np.loadtxt(self.ground_truth_dir + '/groundtruth_%s.csv' % self.date, delimiter=",")

        if all_in_one is True:

            return gt

        else:
            utimes    = gt[:, 0]
            x         = gt[:, 1]
            y         = gt[:, 2]
            z         = gt[:, 3]
            roll_rad  = gt[:, 4]
            pitch_rad = gt[:, 5]
            yaw_rad   = gt[:, 6]

            return utimes, x, y, z, roll_rad, pitch_rad, yaw_rad

    def read_gt_cov_csv(self, all_in_one=None):
        """reads the data in the ground_truth_covariance csv file

        :param   all_in_one: Boolean
        :return: ndarray: containing all data, if all_in_one is True
                 else
                 each column seperated as utimes and covariance matrice ...
        """
        gt_cov = np.loadtxt(self.ground_truth_covariance_dir + '/cov_%s.csv' % self.date, delimiter=",")

        if all_in_one is True:

            return gt_cov

        else:
            utimes = gt_cov[:, 0]
            xx = gt_cov[:, 1];  xy = gt_cov[:, 2];  xz = gt_cov[:, 3];  xr = gt_cov[:, 4];  xp = gt_cov[:, 5]; xh = gt_cov[:, 6]
            yy = gt_cov[:, 7];  yz = gt_cov[:, 8];  yr = gt_cov[:, 9];  yp = gt_cov[:, 10]; yh = gt_cov[:, 11]
            zz = gt_cov[:, 12]; zr = gt_cov[:, 13]; zp = gt_cov[:, 14]; zh = gt_cov[:, 15]
            rr = gt_cov[:, 16]; rp = gt_cov[:, 17]; rh = gt_cov[:, 18]
            pp = gt_cov[:, 19]; ph = gt_cov[:, 20]
            hh = gt_cov[:, 21]

            return utimes, xx, xy, xz, xr, xp, xh, yy, yz, yr, yp, yh, zz, zr, zp, zh, rr, rp, rh, pp, ph, hh

    # data in sensor_data directory
    def read_gps_csv(self, all_in_one=None):
        """reads the data in the gps csv file

        :param   all_in_one: Boolean
        :return: ndarray: containing all data, if all_in_one is True
                 else
                 each column seperated as utimes, modes, num_satss, lat, long, alts, tracks, speeds
        """
        gps = np.loadtxt(self.sensor_data_dir + '/%s/gps.csv' % self.date, delimiter=",")

        if all_in_one is True:

            return gps

        else:

            utimes    = gps[:, 0]
            modes     = gps[:, 1]
            num_satss = gps[:, 2]
            lat       = gps[:, 3]
            long      = gps[:, 4]
            alts      = gps[:, 5]
            tracks    = gps[:, 6]
            speeds    = gps[:, 7]

            return utimes, modes, num_satss, lat, long, alts, tracks, speeds

    def read_gps_rtk_csv(self, all_in_one=None):
        """reads the data in the gps_rtk csv file

        :param   all_in_one: Boolean
        :return: ndarray: containing all data, if all_in_one is True
                 else
                 each column seperated as utimes, modes, num_satss, lat, long, alts, tracks, speeds
        """

        gps_rtk = np.loadtxt(self.sensor_data_dir + '/%s/gps_rtk.csv' % self.date, delimiter=",")

        if all_in_one is True:

            return gps_rtk

        else:

            utimes    = gps_rtk[:, 0]
            modes     = gps_rtk[:, 1]
            num_satss = gps_rtk[:, 2]
            lat       = gps_rtk[:, 3]
            long      = gps_rtk[:, 4]
            alts      = gps_rtk[:, 5]
            tracks    = gps_rtk[:, 6]
            speeds    = gps_rtk[:, 7]

            return utimes, modes, num_satss, lat, long, alts, tracks, speeds

    def read_gps_rtk_err_csv(self, all_in_one=None):
        """reads the data in the gps_rtk_err csv file

        :param all_in_one: Boolean
        :return: ndarray: containing all data, if all_in_one is True
                 else
                 each column seperated as utimes, error in meters
        """

        gps_rtk_err = np.loadtxt(self.sensor_data_dir + '/%s/gps_rtk_err.csv' % self.date, delimiter=",")

        if all_in_one is True:

            return gps_rtk_err

        else:

            utimes    = gps_rtk_err[:, 0]
            error     = gps_rtk_err[:, 1]

            return utimes, error

    def read_kvh_csv(self, all_in_one=None):
        """reads the data in the kvh csv file

        :param   all_in_one: Boolean
        :return: ndarray: containing all data, if all_in_one is True
                 else
                 each column seperated as utimes, heading in rad
        """

        kvh = np.loadtxt(self.sensor_data_dir + '/%s/kvh.csv' % self.date, delimiter=",")

        if all_in_one is True:

            return kvh

        else:

            utimes    = kvh[:, 0]
            heading   = kvh[:, 1]

            return utimes, heading

    def read_ms25_csv(self, all_in_one=None):
        """reads the data in the ms25 csv file

        :param   all_in_one: Boolean
        :return: ndarray: containing all data, if all_in_one is True
                 else
                 each column seperated as utimes, mag_xs, mag_ys, mag_zs, accel_xs, accel_ys, accel_zs, rot_rs, rot_ps, rot_hs
        """
        ms25 = np.loadtxt(self.sensor_data_dir + '/%s/ms25.csv' % self.date, delimiter=",")

        if all_in_one is True:

            return ms25

        else:

            utimes =   ms25[:, 0]

            mag_xs =   ms25[:, 1]
            mag_ys =   ms25[:, 2]
            mag_zs =   ms25[:, 3]

            accel_xs = ms25[:, 4]
            accel_ys = ms25[:, 5]
            accel_zs = ms25[:, 6]

            rot_rs =   ms25[:, 7]
            rot_ps =   ms25[:, 8]
            rot_hs =   ms25[:, 9]

            return utimes, mag_xs, mag_ys, mag_zs, accel_xs, accel_ys, accel_zs, rot_rs, rot_ps, rot_hs

    def read_ms25_euler_csv(self, all_in_one=None):
        """reads the data in the ms25_euler csv file

        :param   all_in_one: Boolean
        :return: ndarray: containing all data, if all_in_one is True
                 else
                 each column seperated as utimes, roll, pitch, heading
        """
        ms25_euler = np.loadtxt(self.sensor_data_dir + '/%s/ms25.csv' % self.date, delimiter=",")

        if all_in_one is True:

            return ms25_euler

        else:

            utimes  = ms25_euler[:, 0]
            roll    = ms25_euler[:, 1]
            pitch   = ms25_euler[:, 2]
            heading = ms25_euler[:, 3]

            return utimes, roll, pitch, heading

    def read_odometry_cov_csv(self):
        # TODO odometry_cov.csv
        pass

    def read_odometry_cov_100hz_csv(self, all_in_one=None):
        """reads the data in the odometry_mu_100hz csv file

        :param all_in_one: Boolean
        :return: ndarray: containing all data, if all_in_one is True
                 else
                 each column seperated as utimes and the upper diagonal of the covariance matrix (row major)
        """

        odom_cov = np.loadtxt(self.sensor_data_dir + '/%s/odometry_cov_100hz.csv' % self.date, delimiter=",")

        if all_in_one is True:

            return odom_cov

        else:

            utimes = odom_cov[:, 0]

            xx = odom_cov[:, 1]; xy = odom_cov[:, 2]; xz = odom_cov[:, 3]; xr = odom_cov[:, 4]; xp = odom_cov[:, 5]; xh = odom_cov[:, 6]
            yy = odom_cov[:, 7]; yz = odom_cov[:, 8]; yr = odom_cov[:, 9]; yp = odom_cov[:, 10]; yh = odom_cov[:, 11]
            zz = odom_cov[:, 12]; zr = odom_cov[:, 13]; zp = odom_cov[:, 14]; zh = odom_cov[:, 15]
            rr = odom_cov[:, 16]; rp = odom_cov[:, 17]; rh = odom_cov[:, 18]
            pp = odom_cov[:, 19]; ph = odom_cov[:, 20]
            hh = odom_cov[:, 21]

            return utimes, xx, xy, xz, xr, xp, xh, yy, yz, yr, yp, yh, zz, zr, zp, zh, rr, rp, rh, pp, ph, hh

    def read_odometry_mu_csv(self):
        # TODO odometry_mu.csv
        pass

    def read_odometry_mu_100hz_csv(self, all_in_one=None):
        """reads the data in the odometry_mu_100hz csv file

        :param all_in_one: Boolean
        :return: ndarray: containing all data, if all_in_one is True
                 else
                 each column seperated as utimes, x, y, z, roll, pitch, heading
        """

        odom = np.loadtxt(self.sensor_data_dir + '/%s/odometry_mu_100hz.csv' % self.date, delimiter=",")

        if all_in_one is True:

            return odom

        else:

            utimes  = odom[:, 0]
            x       = odom[:, 1]
            y       = odom[:, 2]
            z       = odom[:, 3]
            roll    = odom[:, 4]
            pitch   = odom[:, 5]
            heading = odom[:, 6]

            return utimes, x, y, z, roll, pitch, heading

    def read_wheels_csv(self, all_in_one=None):
        """reads the data in the wheels csv file

        :param all_in_one: Boolean
        :return: ndarray: containing all data, if all_in_one is True
                 else
                 each column seperated as utimes, vl, vr
        """

        wheels = np.loadtxt(self.sensor_data_dir + '/%s/wheels.csv' % self.date, delimiter=",")

        if all_in_one is True:

            return wheels

        else:

            utimes = wheels[:, 0]
            vl     = wheels[:, 1]
            vr     = wheels[:, 2]

            return utimes, vl, vr


if __name__ == '__main__':
    rw = ReadRawData('2013-01-10')
    utimes = rw.read_gt_cov_csv(all_in_one=True)
    print(utimes[:, 2])