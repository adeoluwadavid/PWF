# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 15:26:21 2020

@author: Adewole
"""

from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
from IPython.display import display
import ipywidgets as widgets
import pandas as pd
import matplotlib.pyplot as plt
from Keffi_Weather import weatherData
import widget as wd


plt.rcParams['figure.figsize'] = [12, 5]

from IPython.core.display import HTML
HTML("""
<style>
.output_png {
    display: table-cell;
    text-align: center;
    vertical-align: middle;
}
</style>
""")