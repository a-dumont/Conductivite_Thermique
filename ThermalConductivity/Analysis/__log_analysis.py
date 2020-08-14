import sys
import os
import datetime

import numpy as np
import numpy.polynomial.polynomial as npp

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

import ThermalConductivity.Analysis.Functions.__functions as F
import ThermalConductivity.Utilities.__utilities as U
import ThermalConductivity.Utilities.Database.__database as D
import ThermalConductivity.Visualization.__plots as V
from ThermalConductivity.Thermometry.__Thermometry import seebeck_thermometry
from ThermalConductivity.Analysis.__base_class import Measurement

################################################################################
#                          ____ _        _    ____ ____                        #
#                         / ___| |      / \  / ___/ ___|                       #
#                        | |   | |     / _ \ \___ \___ \                       #
#                        | |___| |___ / ___ \ ___) |__) |                      #
#                         \____|_____/_/   \_\____/____/                       #
################################################################################


class Log(Measurement):
    """
    This class is meant to read data from a log file for debugging
    """

    def __init__(self, filename=None):
        super().__init__()

        # Importing dictionaries
        self["dict_measures"] = D.log_data_dict
        self["dict_parameters"] = D.parameters_dict

        if filename is not None:
            # Read the file
            filename = os.path.abspath(filename)
            header = U.read_header(filename)

            # Find the parameters
            self.Store_as_parameter(U.find_H(filename), "H")
            self.Store_as_parameter(U.find_date(filename), "date")
            self.Store_as_parameter(U.find_mount(filename), "mount")
            self.Store_as_parameter(U.find_probe(filename, header), "probe")
            self.Store_as_parameter(U.find_sample(filename, header), "sample")

            # Find the measurements
            log_data = U.read_file_log(filename)

            for key, value in log_data.items():
                self.Store_as_measure(value, key)

        return

    def Get_stabilized(self):
        """
        Returns a Log instance containing only points where the measure is
        stable
        """
        index = np.where(self["Stabilized"] == 1)
        new_log = self[index]
        return new_log

    def Plot(self, key, *args, **kwargs):
        """
        Used as a layer between the object and Visualization.Plot

        Parameters:
        ------------------------------------------------------------------------
        key:        string
                    The measurement to plot

        Kwargs:
        ------------------------------------------------------------------------
        show:       Bool
                    Determines if the figure is shown ore closed defaults to True

        parameters: list
                    list of parameters to be used for legends

        axis_fs:    Int
                    The axis labels fontsize

        fig:        matplotlib.figure
                    Used to draw on an existing figure, requires ax

        ax:         matplotlib.ax
                    Used to draw on an existing figure, requires fig

        x_axis:     string
                    The measurement to use as x-axis defaults to T_av
        """

        # Deal with kwargs
        if "fig" in kwargs:
            return_fig = False
        else:
            return_fig = True

        if "x_axis" in kwargs:
            x_axis = kwargs["x_axis"]
            kwargs.pop("x_axis")
            if x_axis in self.measures:
                pass
            else:
                raise Exception("x_axis must be in self.measures")
        else:
            x_axis = "Time"

        if "figtext" not in kwargs:
            kwargs["figtext"] = self["sample"]
        else:
            pass

        if "parameters" in kwargs:
            parameters = dict()
            parameters_list = kwargs["parameters"]
            kwargs.pop("parameters")
            for p in parameters_list:
                if p in self.parameters:
                    parameters[p] = self[p]
                else:
                    raise Exception("parameters must be in self.parameters")
        else:
            parameters = dict()

        kwargs["parameters"] = parameters

        # Plot the data
        xdata, xkey = self[x_axis], x_axis
        ydata, ykey = self[key], key

        fig, ax = V.Plot(xdata, ydata, xkey, ykey, *args, **kwargs)

        if return_fig is False:
            return
        else:
            return fig, ax
