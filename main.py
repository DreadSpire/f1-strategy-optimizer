import argparse
from src.optimizer import optimize_strategy
from src.visualizer import plot_strategy
from src.feeder import load_race_profiles

def main():
    pr = argparse.ArgumentParser()
    pr.add_argument('--laps', type=int, default=52)
    pr.add_argument('--pit', type=float, default=22.0)
    pr.add_argument('--cliff', type=float, default=0.05)
    
    a = pr.parse_args()
    
    l = a.laps
    p = a.pit
    c = a.cliff
    
    print(f"Laps: {l} | Pit Loss: {p}s | Cliff: {c}")
    
    tp = load_race_profiles(2023, 'Silverstone', 'VER')
    
    tt, st, pt = optimize_strategy(l, p, tp, c)
    
    print(f"Time: {tt:.2f}s")
    print(f"Start: {st}")
    
    ps = [i for i, x in enumerate(pt) if x[0] == 'Make Pit Stop']
    if ps:
        for x in ps:
            print(f" -> Pit Lap {x + 1}")
    else:
        print(" -> 0 stops")
        
    plot_strategy(pt, tt)

if __name__ == "__main__":
    main()