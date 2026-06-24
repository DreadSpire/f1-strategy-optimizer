# F1 Strategy Optimizer

An end-to-end Python operational research tool that calculates the mathematically optimal pit stop strategy for a Formula 1 race. 

This project uses **Dynamic Programming** to navigate the massive decision tree of race strategies, ingests real-world telemetry via the **FastF1 API**, and accounts for the physical realities of thermal tire degradation using a quadratic "tire cliff" mathematical model.

## Features
* **Real-World Telemetry:** Ingests live timing and lap data from the FIA timing servers to calculate accurate base pace and linear degradation rates for different tire compounds.
* **Dynamic Programming Engine:** Evaluates lap-by-lap decisions to minimize total race time without brute-forcing exponential combinations.
* **Tire Cliff Physics:** Simulates realistic F1 tire behavior by applying an exponential time penalty as tire age increases, forcing realistic pit windows.
* **Command Line Interface (CLI):** Fully parameter-driven architecture allowing users to test infinite race scenarios without altering source code.
* **Visual Strategy Rendering:** Automatically generates a color-coded Matplotlib bar chart of the optimal race stint sequence.

## Project Architecture
* `main.py` - The CLI orchestrator that handles user inputs and connects the data, logic, and visual layers.
* `src/feeder.py` - The data pipeline that fetches FastF1 telemetry and uses linear regression to calculate tire profiles.
* `src/optimizer.py` - The mathematical core containing the recursive Dynamic Programming algorithm and quadratic degradation logic.
* `src/visualizer.py` - The rendering engine that translates the optimal path array into a visual strategy chart.

## Requirements
* Python 3.12+ (Standard Windows Distribution recommended)
* `fastf1`
* `matplotlib`

## Installation

1. **Clone the repository**
   ```bash
   git clone [https://github.com/yourusername/f1-strategy-optimizer.git](https://github.com/yourusername/f1-strategy-optimizer.git)
   cd f1-strategy-optimizer
 
 
 
 py -m venv venv
 .\venv\Scripts\activate



 pip install fastf1 matplotlib

## Run 

**to run the code**
```bash
 eg:- py main.py --gp Monaco --year 2024 --laps 78 --pit 20.0 --cliff 0.03
