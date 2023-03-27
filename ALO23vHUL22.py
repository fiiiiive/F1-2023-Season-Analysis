import fastf1 as f1
import pandas as pd
from datetime import datetime as dt
from fastf1 import plotting
from matplotlib import pyplot as plt
plotting.setup_mpl()
f1.Cache.enable_cache('cache')
race = f1.get_session(2023, 'Saudi Arabia', 'R')
race.load()
race2 = f1.get_session(2022, 'Saudi Arabia', 'R')
race2.load()
d1 = race.laps.pick_driver('ALO')
d2 = race2.laps.pick_driver('HUL')
d1laps = d1.pick_quicklaps()
d2laps = d2.pick_quicklaps()
print(race)
print(race2)
plot_filename = "astonracetracejeddah"
fig, ax = plt.subplots()
ax.plot(d1laps['LapNumber'], d1laps['LapTime'], marker = ".", color = "green")
ax.plot(d2laps['LapNumber'], d2laps['LapTime'], marker = ".", color = "white")
ax.set_title("ALO 2023 (Green) vs HUL 2022 (White)")
ax.set_xlabel("Lap Number")
ax.set_ylabel("Lap Time")
ax.legend(loc="lower right")
plt.savefig(plot_filename, dpi=300)
plt.show()
