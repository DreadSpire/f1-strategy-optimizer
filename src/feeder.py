import fastf1
import fastf1.plotting

def load_race_profiles(year, gp, driver):

    fastf1.Cache.enable_cache('fastf1_cache') 

    session = fastf1.get_session(year, gp, 'R')
    session.load()
    
    d = session.laps.pick_driver(driver)
    
    profiles = {}
    for compound in d['Compound'].unique():
        stint = d[d['Compound'] == compound]
        if len(stint) > 5:
            base = stint['LapTime'].dt.total_seconds().head(3).mean()
            deg = (stint['LapTime'].dt.total_seconds().iloc[-1] - base) / len(stint)
            profiles[compound] = {'base': base, 'deg': max(0.01, deg)}
            
    return profiles
