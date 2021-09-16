import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np
import pvlib
import pathlib

irrdata = pd.read_csv('Irradiance_2015_UPOT.csv', sep=';', index_col='timestamp', parse_dates=True)

ghi = irrdata.GHI
ghi = ghi.dropna()
time = irrdata.index

plt.figure()
plt.plot(ghi)
plt.show()

solpos = pvlib.solarposition.ephemeris(irrdata.index, 52.0845, 5.1751, temperature=irrdata.temp_air)

ghi_disc = pvlib.irradiance.disc(ghi, solpos.zenith, irrdata.index)
ghi_dirint = pvlib.irradiance.dirint(ghi, solpos.zenith, irrdata.index)
solpos_clearsky = solpos[['apparent_zenith', 'zenith', 'apparent_elevation']]
clearsky = pvlib.location.Location.get_clearsky(time, model='ineichen', solar_position=solpos_clearsky)
ghi_dirindex = pvlib.irradiance.dirindex(ghi, clearsky, solpos.zenith, irrdata.index)
ghi_erbs = pvlib.irradiance.erbs(ghi, solpos.zenith, irrdata.index)

result = pd.concat([ghi, ghi_disc, ghi_dirint, ghi_dirindex, ghi_erbs], axis=1)
test
test 2
test 3
test 4
#gefsldg nskdljg



