# 🏢 Real Estate Financial Metrics Calculator

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=flat-square&logo=pandas)
![Pydantic](https://img.shields.io/badge/Pydantic-Data%20Validation-E92063?style=flat-square&logo=pydantic)

A Data Engineering & Financial Analysis pipeline built in Python to evaluate investment properties. It validates property financial payloads, computes key metrics (**NOI**, **Cap Rate**, **Cash-on-Cash Return**, and **Annual Cash Flow**), and ranks investments for portfolio decision-making.

---

## 🏗️ Architecture & Data Flow

```text
[ JSON Input Payload ] ──► [ Pydantic Data Validation ] ──► [ Financial Metrics Engine ]
                                                                      │
                                                                      ▼
                                                          [ Pandas Data Sorting ]
                                                                      │
                                                                      ▼
                                                           data/metrics_report.csv

```

---

## 🧮 Applied Financial Formulas

* **Total Acquisition Cost:** $\text{Purchase Price} + \text{Closing / Renovation Costs}$
* **Net Operating Income (NOI):** $(\text{Monthly Rent} - \text{Monthly OpEx}) \times 12$
* **Annual Cash Flow:** $\text{NOI} - (\text{Monthly Mortgage Payment} \times 12)$
* **Cap Rate (%):** $\left( \frac{\text{NOI}}{\text{Total Acquisition Cost}} \right) \times 100$
* **Cash-on-Cash Return (%):** $\left( \frac{\text{Annual Cash Flow}}{\text{Initial Cash Outlay}} \right) \times 100$

---

### 📊 Key Financial Metrics

* **NOI (Net Operating Income / Receita Operacional Líquida)**
  * 🇬🇧 Annual property revenue minus operating expenses, before debt service and taxes.
  * 🇧🇷 Receita anual do imóvel menos despesas operacionais, antes de dívidas e impostos.

* **Cap Rate (Capitalization Rate / Taxa de Capitalização)**
  * 🇬🇧 Unleveraged annual return rate based on property purchase price ($\text{NOI} / \text{Total Cost}$).
  * 🇧🇷 Taxa de retorno anual sem alavancagem sobre o custo total do imóvel ($\text{NOI} / \text{Custo Total}$).

* **Cash-on-Cash Return (CoC / Retorno sobre Capital Próprio)**
  * 🇬🇧 Net annual cash flow percentage relative to actual cash invested ($\text{Cash Flow} / \text{Cash Invested}$).
  * 🇧🇷 Percentual do fluxo de caixa anual em relação ao capital próprio investido ($\text{Fluxo de Caixa} / \text{Capital Investido}$).
  ---


## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Data Processing:** Pandas
* **Data Validation & Typing:** Pydantic
* **Version Control:** Git / GitHub

---

## 📁 Repository Structure

```text
.
├── data/
│   ├── input_properties.json      # Raw investment properties dataset (10 records)
│   └── metrics_report.csv         # Calculated metrics report sorted by Cap Rate
├── main.py                        # Pipeline execution and calculation engine
├── requirements.txt               # Project Python dependencies
├── .gitignore               # Version control rules
└── README.md                      # Technical documentation

```



---
## ⚙️ Setup & Execution

1. **Clone the repository:**
```bash
git clone [https://github.com/evertonhenriquealves/real-estate-financial-metrics.git](https://github.com/evertonhenriquealves/real-estate-financial-metrics.git)
cd real-estate-financial-metrics

```


2. **Install Python dependencies:**
```bash
pip install -r requirements.txt

```


3. **Run the calculation pipeline:**
```bash
python main.py

```
