import pandas as pd

# === Dicionário de colunas traduzidas ===
colunas_traduzidas = {
    "school": "escola",
    "sex": "sexo",
    "age": "idade",
    "address": "endereco",
    "famsize": "tam_familia",
    "Pstatus": "status_pais",
    "Medu": "esc_mae",
    "Fedu": "esc_pai",
    "Mjob": "trab_mae",
    "Fjob": "trab_pai",
    "reason": "motivo_escola",
    "guardian": "responsavel",
    "traveltime": "tempo_viagem",
    "studytime": "tempo_estudo",
    "failures": "reprovacoes",
    "schoolsup": "apoio_escola",
    "famsup": "apoio_familia",
    "paid": "aula_paga",
    "activities": "atividades",
    "nursery": "creche",
    "higher": "sup_desejado",
    "internet": "internet",
    "romantic": "namoro",
    "famrel": "rel_familia",
    "freetime": "tempo_livre",
    "goout": "sair_amigos",
    "Dalc": "alcool_semana",
    "Walc": "alcool_fds",
    "health": "saude",
    "absences": "faltas",
    "G1": "nota1",
    "G2": "nota2",
    "G3": "nota_final"
}

# === Conversão yes/no para 1/0 ===
yes_no_map = {"yes": 1, "no": 0}

job_map = {
    "teacher": "professora",
    "health": "saude",
    "services": "servicos",
    "at_home": "casa",
    "other": "outro"
}

reason_map = {
    "home": "casa",
    "reputation": "reputacao",
    "course": "curso",
    "other": "outro"
}

guardian_map = {
    "mother": "mae",
    "father": "pai",
    "other": "outro"
}

# === Função para tratar um dataset com logs detalhados e booleanos ===
def tratar_dados(input_path, output_path):
    try:
        # Carregar dataset
        df = pd.read_csv(input_path, sep=";")
        print(f"[INFO] Arquivo '{input_path}' carregado com {len(df)} linhas.")

        # Verificar colunas esperadas
        colunas_esperadas = list(colunas_traduzidas.keys())
        colunas_faltando = [col for col in colunas_esperadas if col not in df.columns]
        if colunas_faltando:
            raise ValueError(f"Colunas faltando: {colunas_faltando}")

        # Renomear colunas
        df = df.rename(columns=colunas_traduzidas)
        print(f"[INFO] Colunas renomeadas com sucesso.")

        # Converter yes/no diretamente em 1/0
        count_yes_no = 0
        for col in df.columns:
            if df[col].dtype == "object" and df[col].isin(["yes","no"]).any():
                qtd = df[col].isin(["yes","no"]).sum()
                count_yes_no += qtd
                df[col] = df[col].map(yes_no_map).fillna(df[col])
        print(f"[INFO] Conversão yes/no → 1/0 aplicada em {count_yes_no} valores.")

        # Traduzir profissões
        qtd_trab_mae = df["trab_mae"].isin(job_map.keys()).sum()
        qtd_trab_pai = df["trab_pai"].isin(job_map.keys()).sum()
        df["trab_mae"] = df["trab_mae"].map(job_map).fillna(df["trab_mae"])
        df["trab_pai"] = df["trab_pai"].map(job_map).fillna(df["trab_pai"])
        print(f"[INFO] Tradução de profissões aplicada: {qtd_trab_mae} (mãe), {qtd_trab_pai} (pai).")

        # Traduzir razão da escola
        qtd_motivo = df["motivo_escola"].isin(reason_map.keys()).sum()
        df["motivo_escola"] = df["motivo_escola"].map(reason_map).fillna(df["motivo_escola"])
        print(f"[INFO] Tradução de motivo da escola aplicada em {qtd_motivo} valores.")

        # Traduzir responsável
        qtd_resp = df["responsavel"].isin(guardian_map.keys()).sum()
        df["responsavel"] = df["responsavel"].map(guardian_map).fillna(df["responsavel"])
        print(f"[INFO] Tradução de responsável aplicada em {qtd_resp} valores.")

        # Salvar dataset tratado
        df.to_csv(output_path, sep=";", index=False, encoding="utf-8")
        print(f"[SUCESSO] Arquivo tratado e salvo em: {output_path}")

    except Exception as e:
        print(f"[ERRO] Falha ao tratar o arquivo '{input_path}': {e}")

# === Executar para os dois datasets ===
if __name__ == "__main__":
    tratar_dados("dados_brutos/student-mat.csv", "dados_tratados/student-mat_tratados.csv")
    tratar_dados("dados_brutos/student-por.csv", "dados_tratados/student-por_tratados.csv")
