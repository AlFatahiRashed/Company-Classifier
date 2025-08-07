# 🏷️ Insurance Company Classifier

This is a beginner-friendly Python project that classifies companies into a set of predefined insurance industry categories based on text matching logic.

---

## 🎯 Objective

- Accept a list of companies (description, tags, sector, etc.)
- Match each company to one or more insurance-related labels from a static taxonomy
- Output a labeled dataset with `insurance_label` assigned to each row

---

## 📁 Files

| File                        | Description                               |
|----------------------------|-------------------------------------------|
| `main.py`                  | Main script for data loading & classification |
| `ml_insurance_challenge.csv` | Company list input                        |
| `insurance_taxonomy.xlsx`  | Insurance taxonomy input                  |
| `classified_companies.csv` | Output: companies + their matched labels |

---

## ✅ Results

- **Match rate:** 96.7% (only ~300 companies unmatched out of 6700+)
- Uses a simple word overlap method to assign labels
- Lightweight, explainable, beginner-friendly

---

## 🧠 Why This Approach?

- No ML model used — keeps things transparent and easy to audit
- Works well with real-world company data
- Prioritized results over sophistication, given no labeled ground truth

---

## 🛠️ Requirements

```bash
pip install pandas openpyxl
