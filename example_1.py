"""Illustrate how to use DAPPER to run a 'twin experiment'."""

# Load DAPPER
from dapper import *

# Load experiment setup: the hidden Markov Model (HMM)
from dapper.mods.Lorenz63.sak12 import HMM
HMM.t.T = 30 # shorten experiment

# Simulate synthetic truth (xx) and noisy obs (yy)
xx,yy = simulate(HMM)

# Specify a DA method configuration
config = EnKF('Sqrt', N=10, infl=1.02, rot=True)
# config = Var3D()
# config = PartFilt(N=100,reg=2.4,NER=0.3)

# Turn on liveplotting
config.liveplots = True

# Assimilate yy, knowing the HMM; xx is used for assessment.
config.assimilate(HMM,xx,yy)

# Average stats time series
config.average_stats()

# Print averages
config.print_avrgs(['rmse_a','rmv_a'])

# Replay liveplotters -- can adjust speed, time-window, etc.
config.replay()

# Further diagnostic plots:
# plot_rank_histogram(config.stats)
# plot_err_components(config.stats)
# plot_hovmoller(xx)

# Explore objects:
# print(HMM)
# print(config)
# print(config.stats)
# print(config.avrgs)

# Excercise: Try using
# - Optimal interpolation
# - The (extended) Kalman filter
# - The iterative EnKS
# Hint: suggested DA configs are listed in the HMM file.

# Excercise: Run an experiment for each of the models:
# - LotkaVolterra
# - Lorenz95
# - LA
# - QG


