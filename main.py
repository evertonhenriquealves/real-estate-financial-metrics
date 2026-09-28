import json
import os
import pandas as pd
from pydantic import BaseModel, Field

# Configuração de caminhos do projeto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
INPUT_FILE = os.path.join(DATA_DIR, "input_properties.json")
OUTPUT_CSV = os.path.join(DATA_DIR, "metrics_report.csv")


class PropertyInput(BaseModel):
    id: str
    nome_imovel: str
    valor_compra: float = Field(gt=0)
    custos_aquisicao: float = Field(ge=0)
    receita_aluguel_mensal: float = Field(ge=0)
    despesas_operacionais_mensais: float = Field(ge=0)
    entrada_financiamento: float = Field(ge=0)
    parcela_mensal_financiamento: float = Field(ge=0)


def calculate_real_estate_metrics(property_data: PropertyInput) -> dict:
    # 1. Investimento Total e Capital Próprio Incial
    custo_total_aquisicao = property_data.valor_compra + property_data.custos_aquisicao
    capital_proprio_investido = property_data.entrada_financiamento + property_data.custos_aquisicao

    # 2. Receita Operacional Líquida (NOI - Net Operating Income)
    noi_mensal = property_data.receita_aluguel_mensal - property_data.despesas_operacionais_mensais
    noi_anual = noi_mensal * 12

    # 3. Serviço da Dívida e Fluxo de Caixa Anual
    servico_divida_anual = property_data.parcela_mensal_financiamento * 12
    fluxo_caixa_anual = noi_anual - servico_divida_anual

    # 4. Indicadores de Rentabilidade e Retorno
    cap_rate_pct = (noi_anual / custo_total_aquisicao) * 100 if custo_total_aquisicao > 0 else 0.0
    
    cash_on_cash_pct = (
        (fluxo_caixa_anual / capital_proprio_investido) * 100
        if capital_proprio_investido > 0
        else 0.0
    )

    return {
        "id": property_data.id,
        "nome_imovel": property_data.nome_imovel,
        "custo_total_aquisicao": round(custo_total_aquisicao, 2),
        "capital_proprio_investido": round(capital_proprio_investido, 2),
        "noi_anual": round(noi_anual, 2),
        "fluxo_caixa_anual": round(fluxo_caixa_anual, 2),
        "cap_rate_pct": round(cap_rate_pct, 2),
        "cash_on_cash_pct": round(cash_on_cash_pct, 2),
    }


def main():
    if not os.path.exists(INPUT_FILE):
        print(f"Erro: O arquivo de entrada '{INPUT_FILE}' não foi encontrado.")
        return

    print("Iniciando o cálculo das métricas financeiras imobiliárias...\n")

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    processed_records = []

    for item in raw_data:
        try:
            validated_property = PropertyInput(**item)
            metrics = calculate_real_estate_metrics(validated_property)
            processed_records.append(metrics)
        except Exception as e:
            print(f"⚠️ Erro ao processar imóvel {item.get('id', 'Desconhecido')}: {e}")

    # Processamento com Pandas e ordenação por melhor Cap Rate
    df = pd.DataFrame(processed_records)
    df = df.sort_values(by="cap_rate_pct", ascending=False)

    # Salvando em CSV
    df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")

    print(f"✅ Relatório financeiro gerado com sucesso em: {OUTPUT_CSV}")
    print("\n--- RESUMO DAS MELHORES OPORTUNIDADES (TOP CAP RATE) ---")
    print(df[["id", "nome_imovel", "cap_rate_pct", "cash_on_cash_pct", "fluxo_caixa_anual"]].to_string(index=False))


if __name__ == "__main__":
    main()