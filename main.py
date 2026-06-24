import argparse
from src.optimizer import optimize_strategy
from src.visualizer import plot_strategy
from src.feeder import load_race_profiles

def main():
    pr = argparse.ArgumentParser(description="F1 Race Strategy Optimizer")
    pr.add_argument('--laps', type=int, default=52, help="Total race laps")
    pr.add_argument('--pit', type=float, default=22.0, help="Time lost in pit lane (s)")
    pr.add_argument('--cliff', type=float, default=0.05, help="Tire cliff penalty multiplier")
    pr.add_argument('--gp', type=str, default='Silverstone', help="Grand Prix name")
    pr.add_argument('--year', type=int, default=2023, help="Season year")
    
    a = pr.parse_args()
    
    print(f"--- Strategy for {a.gp} {a.year} ---")
    print(f"Laps: {a.laps} | Pit Loss: {a.pit}s | Cliff: {a.cliff}")
    
    # Ingest telemetry based on CLI arguments
    tp = load_race_profiles(a.year, a.gp, 'VER')
    
    # Run optimizer with the new cliff value
    tt, st, pt = optimize_strategy(a.laps, a.pit, tp, a.cliff)
    
    print(f"Optimal Total Time: {tt:.2f}s")
    print(f"Start Compound: {st}")
    
    plot_strategy(pt, tt)

if __name__ == "__main__":
    main()