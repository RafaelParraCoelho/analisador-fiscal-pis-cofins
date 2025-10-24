import pandas as pd

# Caminho do arquivo de entrada
arquivo = "empresa.txt"

# Lê todas as linhas do arquivo
with open(arquivo, "r", encoding="utf-8") as f:
    linhas = [linha.strip() for linha in f if linha.strip()]

# Variáveis para manter o contexto hierárquico
reg_0000 = None
reg_C001 = None
reg_C100 = None

# Lista que guardará todas as linhas finais (com todos os níveis)
linhas_saida = []

# Cabeçalho solicitado
cabecalho = (
    "REG|DT_INI|DT_FIN|NOME|CNPJ|REG|IND_OPER|IND_EMIT|COD_MOD|COD_SIT|SER|NUM_DOC|CHV_NFE|"
    "DT_DOC|DT_E_S|VL_DOC|IND_PGTO|REG|NUM_ITEM|COD_ITEM|DESCR_COMPL|QTD|UNID|VL_ITEM|"
    "CST_PIS|VL_BC_PIS|ALIQ_PIS|VL_PIS|CST_COFINS|VL_BC_COFINS|ALIQ_COFINS|VL_COFINS"
)

for linha in linhas:
    campos = linha.strip("|").split("|")
    reg = campos[0]

    # Nível 0000
    if reg == "0000":
        reg_0000 = campos

    # Nível C001
    elif reg == "C001":
        reg_C001 = campos

    # Nível C100
    elif reg == "C100":
        reg_C100 = campos

    # Nível C170 (filho final)
    elif reg == "C170":
        if not reg_0000 or not reg_C100:
            continue  # ignora se não tiver pais válidos

        # Monta a linha hierárquica unificada
        linha_final = (
            f"{reg_0000[0]}|{reg_0000[1]}|{reg_0000[2]}|{reg_0000[3]}|{reg_0000[4]}|"
            f"{reg_C100[0]}|{reg_C100[1]}|{reg_C100[2]}|{reg_C100[3]}|{reg_C100[4]}|"
            f"{reg_C100[5]}|{reg_C100[6]}|{reg_C100[7]}|{reg_C100[8]}|{reg_C100[9]}|"
            f"{reg_C100[10]}|{reg_C100[11]}|"
            f"{reg}|{campos[1]}|{campos[2]}|{campos[3]}|{campos[4]}|{campos[5]}|{campos[6]}|"
            f"{campos[7]}|{campos[8]}|{campos[9]}|{campos[10]}|{campos[11]}|{campos[12]}|{campos[13]}|{campos[14]}"
        )
        linhas_saida.append(linha_final)

# Escreve o arquivo de saída
saida = "estrutura_hierarquica_completa.txt"
with open(saida, "w", encoding="utf-8") as f:
    f.write(cabecalho + "\n")
    for linha in linhas_saida:
        f.write(linha + "\n")

print(f"✅ Arquivo gerado com sucesso: {saida}")
print(f"Total de linhas: {len(linhas_saida)}")
