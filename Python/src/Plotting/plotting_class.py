"""
Author: Michael Scoleri
File: Plotting_class.py
Date: 10-19-2023
Functionality: Construct a plotting class for plotting capabilities.
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import os


class Plotting:
    def __init__(self):
        """
        Initizlize the plotting class.
        """
        pass

    def class_assistant(self):
        """
        Print out class details.
        """
        help(type(self))

    def make3dplot(self, x, y, z, xlabel, ylabel, zlabel, colorbar_label, title):
        """
        Create and return a return 3d plot.

        Args: x (ndarray): The x-axis data.
                y (ndarray): The y-axis data.
                z (ndarray): The z-axis data.
                xlabel (string): The x-axis label.
                ylabel (string): The y-axis label.
                zlabel (string): The z-axis label.
                colorbar_label (string): The colorbar label.
                title (string): The title of the graph.

        Returns:
            Figure of 3d plot.
        """
        # 3D plot of stream temperature
        fig = plt.figure()

        # Create a 3D axis
        ax = fig.add_subplot(111, projection="3d")

        # Create a surface plot
        # Make x, y axis take different length - https://stackoverflow.com/questions/46607106/python-3d-plot-with-different-array-sizes
        x_sized, y_sized = np.meshgrid(x, y)
        # ax.plot_surface() - https://matplotlib.org/stable/plot_types/3D/surface3d_simple.html#plot-surface-x-y-z

        surface = ax.plot_surface(
            x_sized, y_sized, z, cmap="jet", rstride=10, cstride=10
        )

        # Add a colorbar with label
        cbar = fig.colorbar(surface)
        cbar.set_label(colorbar_label, fontsize=11, fontweight="bold")

        ax.set_title(title, fontsize=12, fontweight="bold")
        ax.set_ylabel(ylabel, fontsize=11)
        ax.set_xlabel(xlabel, fontsize=11)
        ax.set_zlabel(zlabel, fontsize=11)
        ax.invert_xaxis()

        return fig

    def make_single_plot(
        self,
        x,
        y,
        xlabel,
        ylabel,
        title,
        linewidth=None,
        marker=None,
        legend=None,
        axis=None,
        ax=None,
    ):
        """
        Creates a basic line plot.

        Args:
            x (ndarray): The x-axis data.
            y (ndarray): The y-axis data.
            xlabel (str): The label for the x-axis.
            ylabel (str): The label for the y-axis.
            title (str): The title of the graph.
            xlimit (int): The limit for the x-axis.
            ylimit (int): The limit for the y-axis.
            linewidth (float): The width of the line.
            marker (str): The marker style.
            legend ([str]): List of strings for the legend.
            axis ([ndarray]): axis parameters for plots.

        Returns:
            Figure: Figure of the residual plot.
        """
        ax.plot(x, y, marker)
        ax.set_title(title, fontweight="bold")
        ax.set_ylabel(ylabel)
        ax.set_xlabel(xlabel)
        ax.axis(axis)
        plt.autoscale(enable=True)
        return ax

    def make_three_line_plot(
        self,
        low_x,
        low_y,
        base_x,
        base_y,
        high_x,
        high_y,
        title,
        xlabel,
        ylabel,
    ):
        """
        Creates a 3 line plot for low, base and high.

        Args:
            low_x (ndarray): X data for low.
            low_y (ndarray): Y data for low.
            base_x (ndarray): X data for base.
            base_y (ndarray): Y data for base.
            high_x (ndarray): X data for high.
            high_y (ndarray): Y data for high.
            xlimit ([ndarray]): limit for the X axis.
            ylimit ([ndarray]): limit for the Y axis.

        Return:
            Figure with plotted data.
        """
        fig = plt.figure()

        plt.plot(low_x, low_y, "--b", linewidth=2)
        plt.plot(base_x, base_y, "k", linewidth=2)
        plt.plot(high_x, high_y, "--r", linewidth=2)
        plt.title(title, fontweight="bold")
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.autoscale(enable=True)
        plt.legend(["Low", "Base", "High"])
        plt.tight_layout()
        return fig

    def make_residual_plot(self, data, xlabel, ylabel, title, colorbar_label, extent):
        """
        Creates a residual plot (heat map).

        Args:
            data (ndarray): The heatmap data.
            xlabel (str): The label for the x-axis.
            ylabel (str): The label for the y-axis.
            title (str): The title of the graph.
            colorbar_label (str): The label for the colorbar.
            extent (list[float]): List of floats to set the extent of the graph.

        Returns:
            Figure: Figure of line plot.
        """

        fig, ax = plt.subplots()
        plt.imshow(data, aspect="auto", cmap="jet", origin="lower", extent=None)
        plt.colorbar(label=colorbar_label)
        plt.axis("square")
        plt.title(title, fontsize=11, fontweight="bold")
        plt.xlabel(xlabel, fontsize=9)
        plt.ylabel(ylabel, fontsize=9)
        plt.autoscale(enable=True)
        plt.tight_layout()
        ax.invert_yaxis()
        return fig

    def heat_flux_comparison(
        self,
        x,
        y1,
        marker1,
        label1,
        y2,
        marker2,
        label2,
        y3,
        marker3,
        label3,
        y4,
        marker4,
        label4,
        y5,
        marker5,
        label5,
        y6,
        marker6,
        label6,
        title,
        xlabel,
        ylabel,
    ):
        fig = plt.figure()
        plt.plot(x, y1, marker1, label=label1)
        plt.plot(x, y2, marker2, label=label2)
        plt.plot(x, y3, marker3, label=label3)
        plt.plot(x, y4, marker4, label=label4)
        plt.plot(x, y5, marker5, label=label5)
        plt.plot(x, y6, marker6, label=label6)
        plt.title(title, fontweight="bold")
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.legend(loc="best")
        plt.tight_layout()
        return fig

    def save_plots(self, *args):
        """
        Takes a list of figures and saves them to a pdf.

        Args:
            *args ([figures]): list of figures to save.

        Return:
            None
        """
        pdf_path = os.path.join(os.getcwd(), "Results", "PDFs", "hflux.pdf")
        print(f"Saving PDF to {pdf_path}...")
        plots_pdf = PdfPages(pdf_path)
        for fig in args:
            plots_pdf.savefig(fig)
        plots_pdf.close()
        plt.close("all")
        print("Done!")
