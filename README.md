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
├── data/                     # CSV data files
│   └── portfolio_values.csv
├── images/                   # Generated plots
│   └── portfolio_plot.png
├── scripts/                  # Python scripts
│   └── main.py
├── README.md                 # Project documentation
└── requirements.txt          # Python dependencies

---

## Overview

This project analyzes portfolio performance by calculating returns and plotting portfolio value over time using historical data. It uses Python libraries such as pandas, numpy, and matplotlib.

---

## Setup

1. Clone the repository:

```bash
git clone https://github.com/vinhvu-rgb/Week2-Finance.git
cd Week2-Finance
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1   # PowerShell
# or
venv\Scripts\activate.bat     # Command Prompt
# or
source venv/Scripts/activate  # Git Bash
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

> `requirements.txt` should include:
> pandas  
> numpy  
> matplotlib

---

## How to Run

Run the main script:

```bash
python scripts/main.py
```

- The script will generate `images/portfolio_plot.png`  
- The portfolio plot visualizes value over time

---

## Results

### Portfolio Over Time
<p align="center">
  <img src="https://github.com/vinhvu-rgb/Week2-Finance/raw/main/images/portfolio_plot.png?ts=1" 
       alt="Portfolio Value Over Time" 
       width="600"/>
</p>

**Figure 1:** Portfolio value over time

> ⚠️ If the image does not display above, view it directly:  
> 👉 [portfolio_plot.png](https://github.com/vinhvu-rgb/Week2-Finance/raw/main/images/portfolio_plot.png)

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
