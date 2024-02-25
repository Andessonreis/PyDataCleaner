# PyDataCleaner

PyDataCleaner é uma ferramenta Python para extração, limpeza e exploração de dados de conjuntos de dados usando bibliotecas como Pandas e SQLAlchemy.

## Funcionalidades

- **Extração de Dados Inicial**: Carrega um conjunto de dados inicial, verificando se o arquivo existe e pode ser acessado.
- **Limpeza de Dados**: Identifica e remove duplicatas dos dados, permitindo ao usuário escolher estratégias adicionais de limpeza, como tratamento de valores ausentes e normalização de dados.
- **Exploração de Dados**: Fornece uma visualização preliminar dos dados após a limpeza, incluindo estatísticas descritivas básicas e histogramas.
- **Armazenamento de Dados Limpos**: Oferece opções para salvar os dados limpos em diferentes formatos, como CSV, Excel ou banco de dados SQLite.
- **Integração com Banco de Dados**: Permite ao usuário integrar os dados limpos diretamente a um banco de dados SQLite.
- **Personalização de Processamento**: Flexibilidade para adicionar funcionalidades adicionais de limpeza e exploração de dados conforme necessário.
- **Log de Atividades**: Registra informações sobre a execução do script em um arquivo de log.

## Como Usar

1. Certifique-se de ter o Python instalado.
2. Clone este repositório em sua máquina local usando o seguinte comando:

```git
git clone https://github.com/Andessonreis/PyDataCleaner.git
```
3. Navegue até o diretório do projeto.
4. Execute o script `main.py` com o caminho para o arquivo de dados como argumento.

Exemplo de uso:
```
python3 main.py /caminho/para/seu/arquivo.csv
```

## Dependências

- Python 3.x
- pandas
- sqlalchemy
- matplotlib (opcional, para visualização de dados)

Você pode instalar as dependências executando o seguinte comando:
```
pip install -r requirements.txt
```