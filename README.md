
# 📊 Cost Compass

**Cost Compass** is a lightweight Streamlit app that helps finance professionals analyze General Ledger (GL) data and benchmark spending against industry standards.

### Features
- Upload GL and benchmark files (CSV or Excel)
- Automatically classify and compare spend by category
- Flag vendors and categories with overspending
- Download detailed results as CSV

### How to Use
1. Upload your General Ledger file.
2. Upload your Benchmark Cost Table.
3. View flagged overspending and download the CSV report.

### Sample Format
**GL File**
```
Date,Vendor,Category,Amount
2025-01-01,ABC Waste,Waste,1200
...
```

**Benchmark File**
```
Category,Benchmark_Cost
Waste,1000
...
```

### Deploy Your Own
To deploy:
1. Push this repo to GitHub
2. Visit [Streamlit Cloud](https://streamlit.io/cloud)
3. Link your repo and set `cost_compass.py` as the main script

---

© 2025 Cost Compass by Levi Friedbauer. All rights reserved.
