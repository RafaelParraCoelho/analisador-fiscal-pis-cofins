import pandas as pd  # mantido para consistência
from pathlib import Path

def ler_arquivo(caminho: str) -> list[str]:
    """Lê o arquivo texto e retorna uma lista de linhas não vazias."""
    with open(caminho, "r", encoding="utf-8") as f:
        return [linha.strip() for linha in f if linha.strip()]


def montar_linha(reg_0000: list[str], reg_C100: list[str], reg_C170: list[str]) -> str:
    """Monta uma linha hierárquica completa unindo 0000, C100 e C170."""
    return (
        f"{reg_0000[0]}|{reg_0000[1]}|{reg_0000[2]}|{reg_0000[3]}|{reg_0000[4]}|"
        f"{reg_C100[0]}|{reg_C100[1]}|{reg_C100[2]}|{reg_C100[3]}|{reg_C100[4]}|"
        f"{reg_C100[5]}|{reg_C100[6]}|{reg_C100[7]}|{reg_C100[8]}|{reg_C100[9]}|"
        f"{reg_C100[10]}|{reg_C100[11]}|"
        f"{reg_C170[0]}|{reg_C170[1]}|{reg_C170[2]}|{reg_C170[3]}|{reg_C170[4]}|"
        f"{reg_C170[5]}|{reg_C170[6]}|{reg_C170[7]}|{reg_C170[8]}|{reg_C170[9]}|"
        f"{reg_C170[10]}|{reg_C170[11]}|{reg_C170[12]}|{reg_C170[13]}|{reg_C170[14]}"
    )


def processar_arquivo(linhas: list[str]) -> list[str]:
    """Percorre as linhas e constrói as saídas hierárquicas."""
    reg_0000 = None
    reg_C001 = None
    reg_C100 = None
    linhas_saida = []

    for linha in linhas:
        campos = linha.strip("|").split("|")
        reg = campos[0]

        if reg == "0000":
            reg_0000 = campos
        elif reg == "C001":
            reg_C001 = campos
        elif reg == "C100":
            reg_C100 = campos
        elif reg == "C170":
            if not reg_0000 or not reg_C100:
                continue
            linha_final = montar_linha(reg_0000, reg_C100, campos)
            linhas_saida.append(linha_final)

    return linhas_saida


def salvar_saida(linhas_saida: list[str], caminho_saida: str, cabecalho: str) -> None:
    """Escreve o arquivo final no formato esperado."""
    with open(caminho_saida, "w", encoding="utf-8") as f:
        f.write(cabecalho + "\n")
        for linha in linhas_saida:
            f.write(linha + "\n")


def main():
    """Função principal que coordena a execução."""
    caminho_entrada = "empresa.txt"
    caminho_saida = "estrutura_hierarquica_completa.txt"

    cabecalho = (
        "REG|DT_INI|DT_FIN|NOME|CNPJ|"
        "REG|IND_OPER|IND_EMIT|COD_MOD|COD_SIT|SER|NUM_DOC|CHV_NFE|DT_DOC|DT_E_S|VL_DOC|IND_PGTO|"
        "REG|NUM_ITEM|COD_ITEM|DESCR_COMPL|QTD|UNID|VL_ITEM|CST_PIS|VL_BC_PIS|ALIQ_PIS|VL_PIS|"
        "CST_COFINS|VL_BC_COFINS|ALIQ_COFINS|VL_COFINS"
    )

    linhas = ler_arquivo(caminho_entrada)
    linhas_saida = processar_arquivo(linhas)
    salvar_saida(linhas_saida, caminho_saida, cabecalho)

    print(f"Arquivo gerado com sucesso: {caminho_saida}")
    print(f"Total de linhas: {len(linhas_saida)}")


if __name__ == "__main__":
    main()
