### 🧾 Analisador Fiscal PIS/COFINS 

### 📘 Descrição

Este projeto tem como objetivo **automatizar a leitura e a análise de arquivos fiscais**, especialmente **registros do SPED PIS/COFINS**, organizando as informações de forma hierárquica e estruturada.  
O programa percorre o arquivo texto original, identifica os registros principais e seus filhos, e gera uma **estrutura completa de dados** para posterior tratamento ou exportação.

---

### ⚙️ Funcionalidades

- Leitura de arquivos `.txt` contendo registros fiscais (ex: `0000`, `C001`, `C100`, `C170` etc);
- Montagem hierárquica dos dados, preservando a estrutura dos blocos;
- Exportação do resultado para arquivo `.txt` organizado (ex: `estrutura_hierarquica_completa.txt`);
- Manutenção de delimitador `|` entre os campos;
- Cabeçalho automático com todos os campos esperados;
- Compatível com Python 3.10+.

---

### 🧠 Exemplo de uso

```bash
python teste.py
```

**Entrada (`empresa.txt`):**
```
0000|01012024|31012024|Empresa X|12345678000199
C001|0
C100|55|00|1|1234|...|...
C170|1|001|Produto teste|10|UN|100.00|...
```

**Saída (`estrutura_hierarquica_completa.txt`):**
```
REG|DT_INI|DT_FIN|NOME|CNPJ|REG|IND_OPER|IND_EMIT|COD_MOD|COD_SIT|SER|NUM_DOC|...
0000|01012024|31012024|Empresa X|12345678000199|C001|0|C100|55|00|1|1234|...|C170|1|001|Produto teste|...
```

---

###  📦 Estrutura do Projeto

```
├── empresa.txt
├── estrutura_hierarquica_completa.txt
├── teste.py
├── requirements.txt
└── README.md
```

---

### 🧰 Tecnologias Utilizadas

- **Python 3.10+**
- **VS Code**
- **Git / GitHub**
- (Opcional) `pandas` para manipulação de dados tabulares

---

### 🚀 Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/RafaelParraCoelho/analisador-fiscal-pis-cofins.git
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd analisador-fiscal-pis-cofins
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute o script:
   ```bash
   python teste.py
   ```

---

### ✨ Autor

**Rafael Parra Coelho**  
💼 Assistente de Dados • Python | Automação Fiscal  
🌐 [GitHub](https://github.com/RafaelParraCoelho)
