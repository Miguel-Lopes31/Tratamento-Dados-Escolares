
# 📊 Projeto: Padronização e Tradução de Dados Escolares

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python) ![Pandas](https://img.shields.io/badge/Pandas-data-green) 
## 📝 Descrição

Este projeto **trata e padroniza datasets de estudantes** do ensino médio, para Matemática e Português, garantindo que os dados fiquem **prontos para análise, dashboards e machine learning**.

Ele realiza:

* 📌 Tradução e padronização de nomes de colunas (curtas e claras)
* 📌 Conversão de colunas binárias (`yes/no`) em **0/1**
* 📌 Tradução de valores categóricos: **profissão dos pais, motivo da escola, responsável**
* 📌 Verificação de colunas faltantes e logs detalhados de tratamento

---

## 🎯 Benefícios

* ✅ Dados **prontos para análise** sem inconsistências
* ✅ **Colunas claras e curtas** para fácil leitura
* ✅ **Valores binários já em 0/1** para estatísticas e modelos
* ✅ **Logs detalhados** para rastrear transformações

---

## ⚙️ Requisitos

* Python 3.x
* Bibliotecas: `pandas`
* Ambiente virtual recomendado

Estrutura de pastas:

```
projeto_tratamento_dados/
│
├─ dados_brutos/           # CSVs originais
│   ├─ student-mat.csv
│   └─ student-por.csv
│
├─ dados_tratados/         # CSVs tratados
│
├─ tratamento.py           # Script principal
│
└─ README.md               # Documentação
```

Instalação rápida:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install pandas
```

---

## 🚀 Como usar

1. Coloque os datasets originais em `dados_brutos/`.
2. Crie a pasta `dados_tratados/` se não existir.
3. Execute o script:

```bash
python tratamento.py
```

4. Acompanhe os logs no terminal:

   * Linhas carregadas
   * Valores yes/no convertidos
   * Traduções aplicadas
   * Mensagem de sucesso

5. Os arquivos tratados estarão em `dados_tratados/` prontos para análise.

---

## 🛠️ Funcionalidades do Script

* ✅ Carregamento seguro dos datasets
* ✅ Verificação de colunas faltantes
* ✅ Tradução de colunas para português
* ✅ Conversão de valores binários para 0/1
* ✅ Tradução de categorias importantes
* ✅ Logs detalhados de todas as etapas

---

## 📊 Exemplo de dataset tratado

| escola | sexo | idade | endereco | tam\_familia | apoio\_escola | trab\_mae | trab\_pai | motivo\_escola | responsavel | aula\_paga | nota\_final |
| ------ | ---- | ----- | -------- | ------------ | ------------- | --------- | --------- | -------------- | ----------- | ---------- | ----------- |
| GP     | F    | 17    | U        | GT3          | 1             | saude     | servicos  | curso          | mae         | 1          | 15          |
| MS     | M    | 16    | R        | LE3          | 0             | prof      | casa      | reputacao      | pai         | 0          | 13          |

> 💡 Valores binários já em 0/1; colunas traduzidas; categorias padronizadas.

---

## 📸 Visualização do Fluxo

```
dados_brutos/*.csv  -->  tratamento.py  -->  dados_tratados/*.csv
```

**Exemplo de log no terminal:**

```
[INFO] Arquivo 'student-mat.csv' carregado com 382 linhas.
[INFO] Colunas renomeadas com sucesso.
[INFO] Conversão yes/no → 1/0 aplicada em 12 valores.
[INFO] Tradução de profissões aplicada: 5 (mãe), 6 (pai).
[SUCESSO] Arquivo tratado e salvo em: dados_tratados/student-mat_traduzido.csv
```

---

## 📌 Conclusão

Este projeto torna **os dados escolares consistentes, claros e prontos para análise**. Ele reduz erros, economiza tempo de preparação e facilita qualquer análise exploratória ou dashboard interativo.

---

## 🔗 Contato e LinkedIn

* Miguel Lopes
* LinkedIn: [https://www.linkedin.com/in/miguel-lopes](https://www.linkedin.com/in/miguel-lopes)


