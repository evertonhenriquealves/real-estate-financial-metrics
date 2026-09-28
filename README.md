# 🏢 Real Estate Financial Metrics Calculator

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=flat-square&logo=pandas)
![Pydantic](https://img.shields.io/badge/Pydantic-Data%20Validation-E92063?style=flat-square&logo=pydantic)

🇬🇧 A Data Engineering & Financial Analysis pipeline built in Python to evaluate investment properties. It validates property financial payloads, computes key metrics (NOI, Cap Rate, Cash-on-Cash Return, and Annual Cash Flow), and ranks investments for portfolio decision-making.

🇧🇷 Um pipeline de Engenharia de Dados e Análise Financeira desenvolvido em Python para avaliação de investimentos imobiliários. O sistema valida os dados de entrada, calcula métricas essenciais (NOI, Cap Rate, Cash-on-Cash Return e Fluxo de Caixa Anual) e ranqueia as melhores oportunidades para tomada de decisão

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



## 📊 Key Financial Metrics & Formulas / Métricas e Fórmulas Financeiras

* **NOI (Net Operating Income / Receita Operacional Líquida)**
  * 🇬🇧 Annual revenue minus operating expenses (pre-debt/tax).
  * 🇧🇷 Receita anual menos despesas operacionais (antes de dívidas e impostos).
  * 🧮 **Formula:** $(\text{Monthly Rent / Aluguel Mensal} - \text{Monthly OpEx / Despesas Mensais}) \times 12$

* **Total Acquisition Cost / Custo Total de Aquisição**
  * 🇬🇧 Total capital required to acquire and prepare the property.
  * 🇧🇷 Capital total necessário para adquirir e preparar o imóvel.
  * 🧮 **Formula:** $\text{Purchase Price / Preço de Compra} + \text{Closing Costs / Custos de Aquisição}$

* **Annual Cash Flow / Fluxo de Caixa Anual**
  * 🇬🇧 Net cash remaining after paying all operating expenses and debt service.
  * 🇧🇷 Saldo líquido restante após pagar despesas operacionais e financiamento.
  * 🧮 **Formula:** $\text{NOI} - (\text{Monthly Mortgage / Parcela Mensal} \times 12)$

* **Cap Rate (Capitalization Rate / Taxa de Capitalização)**
  * 🇬🇧 Unleveraged annual return over total property cost.
  * 🇧🇷 Retorno anual sem alavancagem sobre o custo total do imóvel.
  * 🧮 **Formula:** $\left( \frac{\text{NOI}}{\text{Total Acquisition Cost / Custo Total}} \right) \times 100$

* **Cash-on-Cash Return (CoC / Retorno sobre Capital Próprio)**
  * 🇬🇧 Annual cash flow percentage relative to actual equity invested.
  * 🇧🇷 Percentual do fluxo de caixa anual sobre o capital próprio investido.
  * 🧮 **Formula:** $\left( \frac{\text{Annual Cash Flow / Fluxo de Caixa}}{\text{Initial Cash Outlay / Capital Próprio}} \right) \times 100$

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
├── .gitignore                     # Version control rules
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
