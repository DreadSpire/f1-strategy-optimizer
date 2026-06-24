import fastf1
import fastf1.plotting

def load_race_profiles(year, gp, driver):
    # Enable cache to speed up subsequent runs
    fastf1.Cache.enable_cache('fastf1_cache') 
    
    # Fetch specific session
    session = fastf1.get_session(year, gp, 'R')
    session.load()
    
    # Filter for the specific driver
    d = session.laps.pick_driver(driver)
    
    # Basic logic to derive base pace and degradation
    # For a robust model, you'd perform a linear regression here
    profiles = {}
    for compound in d['Compound'].unique():
        stint = d[d['Compound'] == compound]
        if len(stint) > 5:
            # Simple heuristic: base is the average of the first 3 laps
            base = stint['LapTime'].dt.total_seconds().head(3).mean()
            # Simple heuristic: deg is the average increase per lap
            deg = (stint['LapTime'].dt.total_seconds().iloc[-1] - base) / len(stint)
            profiles[compound] = {'base': base, 'deg': max(0.01, deg)}
            
    return profiles