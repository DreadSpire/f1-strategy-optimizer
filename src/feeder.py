import os
import fastf1

def fit(x, y):
    n = len(x)
    sx = sum(x)
    sy = sum(y)
    sxy = sum(i * j for i, j in zip(x, y))
    sx2 = sum(i ** 2 for i in x)
    den = (n * sx2 - sx ** 2)
    m = (n * sxy - sx * sy) / den if den != 0 else 0.0
    b = (sy - m * sx) / n if n != 0 else 0.0
    return m, b

def load_race_profiles(yr, gp, drv):
    os.makedirs('fastf1_cache', exist_ok=True)
    fastf1.Cache.enable_cache('fastf1_cache')
    
    s = fastf1.get_session(yr, gp, 'R')
    s.load(laps=True, telemetry=False, weather=False, messages=False)
    
    laps = s.laps.pick_driver(drv).pick_quicklaps()
    
    map_comp = {'SOFT': 'Soft', 'MEDIUM': 'Medium', 'HARD': 'Hard'}
    prof = {}
    
    for f_name, p_name in map_comp.items():
        c_laps = laps[laps['Compound'] == f_name]
        if c_laps.empty:
            continue
            
        stints = c_laps['Stint'].unique()
        x_data = []
        y_data = []
        
        for st in stints:
            s_laps = c_laps[c_laps['Stint'] == st]
            if len(s_laps) < 3:
                continue
                
            times = s_laps['LapTime'].dt.total_seconds().tolist()
            ages = list(range(1, len(times) + 1))
            
            x_data.extend(ages)
            y_data.extend(times)
            
        if len(x_data) > 2:
            m, b = fit(x_data, y_data)
            prof[p_name] = {'base': round(b, 2), 'deg': round(max(0.0, m), 3)}
            
    return prof