# 🏷️ Insurance Company Classifier

This is a beginner-friendly Python project that classifies companies into a set of predefined insurance industry categories based on text matching logic.

---
## 🤔 The Thought Process

At first, I knew I had to match each company to a label, but there was no correct answer to compare with. So I realized the only thing I could rely on was the text: descriptions, tags, sector, etc.
I decided to put all of that into one big text per company and then check if any of the insurance labels were mentioned, or at least most of the words from a label.
Instead of using complicated tools, I kept it simple: lowercase everything, split the label into words, and match based on word presence. If most of the label words were in the company’s text, I assigned that label.
It’s not perfect, but it worked really well! I got matches for 96% of the companies. And for a beginner, that was the main goal: make it work, keep it clean, and get results I can explain.

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
