import fastf1 as f1
from fastf1 import plotting
from fastf1 import utils

from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

import numpy as np
import pandas as pd

plotting.setup_mpl()
f1.Cache.enable_cache('cache')

year, gp, session = 2023, 'Saudi Arabia', 'Q'

race = f1.get_session(year, gp, session)
race.load()

race2 = f1.get_session(2022, 'Saudi Arabia', 'Q')
race2.load()

d1, d2 = 'PER', 'PER'

laps_d1 = race.laps.pick_driver(d1)
laps_d2 = race2.laps.pick_driver(d2)

fastest_d1 = laps_d1.pick_fastest()
fastest_d2 = laps_d2.pick_fastest()


telemetry_d1 = fastest_d1.get_telemetry().add_distance()
telemetry_d2 = fastest_d2.get_telemetry().add_distance()

team_d1 = fastest_d1['Team']
team_d2 = fastest_d2['Team']

delta_time, ref_tel, compare_tel = utils.delta_time(fastest_d1, fastest_d2)

print(race.event)

plot_size = [15,15]
plot_title = "Red Bull Qualifying Differences 2022 (White) v 2023 (Blue)"
plot_ratios = [4, 2, 1]
plot_filename = "redbullJEDDAHQuali22-23.png"

plt.rcParams['figure.figsize'] = plot_size
fig, ax = plt.subplots(3, gridspec_kw = {'height_ratios': plot_ratios})

ax[0].title.set_text(plot_title)

ax[0].plot(telemetry_d1['Distance'], telemetry_d1['Speed'], label = d1, color='blue')
ax[0].plot(telemetry_d2['Distance'], telemetry_d2['Speed'], label = d2, color='white')
ax[0].set(ylabel = 'Speed')
ax[0].legend(loc="lower right")

ax[1].plot(telemetry_d1['Distance'], telemetry_d1['Throttle'], label = d1, color='blue')
ax[1].plot(telemetry_d2['Distance'], telemetry_d2['Throttle'], label = d2, color='white')
ax[1].set(ylabel = 'Throttle')

ax[2].plot(ref_tel['Distance'], delta_time, label = "delta")
ax[2].set(ylabel=f"<--2022 Ahead | 2023 Ahead -->")
ax[2].hlines(y = 0, xmin = -100, xmax = 4500, linestyle = 'dashed', linewidth = .5, color = 'cyan', label = "0.0")
ax[2].set(xlabel='Lap distance (m)')
ax[2].legend(loc="upper right")

for a in ax.flat:
    a.label_outer()



plt.savefig(plot_filename, dpi=300)
plt.show()
