# Week 2 Finance Project – Portfolio Analysis Simulation

This project simulates a portfolio over time and visualizes its performance using Python.

---

## Table of Contents
- [Folder Structure](#folder-structure)
- [Overview](#overview)
- [Setup](#setup)
- [How to Run](#how-to-run)
- [Results](#results)
- [License](#license)

---

## Folder Structure

Week2-Finance/
├── data/               # Input data files (e.g., CSV)
├── images/             # Generated plots
├── scripts/            # Python scripts
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies

---

## Overview

This project analyzes portfolio performance by calculating returns and plotting portfolio value over time using historical data. It leverages Python libraries such as pandas, numpy, and matplotlib for analysis and visualization.

---

## Setup

1. Clone the repository:

```
git clone https://github.com/vinhvu-rgb/Week2-Finance.git
cd Week2-Finance
```

2. Create a virtual environment (optional but recommended):

```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```
pip install -r requirements.txt
```

> `requirements.txt` should include:
> pandas
> numpy
> matplotlib

---

## How to Run

Run the main script:

```
python scripts/main.py
```

- The script will generate `images/portfolio_plot.png`  
- The portfolio plot visualizes value over time

---

## Results

### Portfolio Over Time
<p align="center">
  <img src="https://github.com/vinhvu-rgb/Week2-Finance/raw/main/images/portfolio_plot.png" 
       alt="Portfolio Value Over Time" 
       width="600"/>
</p>

**Figure 1:** Portfolio value over time


---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
