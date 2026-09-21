import tensorflow as tf
from tensorflow import keras

import os
import gc
import tempfile
from pickle import dump, load

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import shap

from sklearn.preprocessing import MinMaxScaler

from datetime import datetime
from pandas.tseries.offsets import DateOffset