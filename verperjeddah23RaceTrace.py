import fastf1
import pandas as pd
from datetime import datetime
from fastf1 import plotting
from matplotlib import pyplot as plt

def main():
    plotting.setup_mpl()
    fastf1.Cache.enable_cache('cache')
    cutoff = pd.Timedelta('00:01:48')
    race = fastf1.get_session(2023, 'Bahrain', 'R')
    race.load()

    d1 = race.laps.pick_driver('PER')
    d2 = race.laps.pick_driver('VER')

    d1laps = d1.pick_quicklaps();
    d2laps = d2.pick_quicklaps();
    
    print(race)
    print(cutoff)
    
    plot_filename = "2023jeddahverperRACE"
    fig, ax = plt.subplots()
    ax.plot(d1laps['LapNumber'], d1laps['LapTime'], marker = ".", color='blue')
    ax.plot(d2laps['LapNumber'], d2laps['LapTime'], marker = ".", color='red')
    
    ax.set_title("PER (Blue) v VER (Red)")
    ax.set_xlabel("Lap Number")
    ax.set_ylabel("Lap Time")
    ax.legend(loc="lower right")
    plt.savefig(plot_filename, dpi=300)
    plt.show()
    
    
if __name__ == "__main__":
    main()
