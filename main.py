import pandas as pd
from os import path
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import logging
import argparse

logging.basicConfig(filename='pydatacleaner.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def data_extract(caminho):
    if path.exists(caminho):
        try:
            df = pd.read_csv(caminho, low_memory=False)
            logging.info("Arquivo encontrado e carregado com sucesso: %s", caminho)
            return df
        except Exception as e:
            print("Erro ao ler o arquivo:", e)
            return None
    else:
        logging.error("Arquivo não encontrado: %s", caminho)
        return None
    
def clean_data(df):   
    df.drop_duplicates(inplace=True)
    logging.info("Duplicatas removidas com sucesso")
    #print(df.isnull().sum())
    return df

def explore_data(df):
    print("\nPrimeiras linhas do DataFrame:")
    print(df.head())
    
    print("Informações sobre o DataFrame:")
    print(df.info())
    
    print("\nEstatísticas Descritivas:")
    print(df.describe())

    print("\nHistogramas:")
    df.hist(bins=20, figsize=(10, 8))
    plt.show()
    
    logging.info("Exploração de dados concluída")

def excel_save(df, nome_arquivo):
    try:
        df.to_excel(nome_arquivo + '.xlsx', index=False)
        print("DataFrame salvo com sucesso em", nome_arquivo + '.xlsx')
    except Exception as e:
        print("Erro ao salvar o arquivo Excel:", e)
    
def integrate_with_database(df):
    engine = create_engine('sqlite:///NBADB.db')
    print(type(engine))
    df.to_sql('NBA', con=engine, index=True, index_label='id', if_exists='replace')
    connection = engine.connect()
    print(type(connection))

def data_save(df):
        op = input("Deseja salvar no banco de dados [N ou Y]: ").lower()
        if op == 'y':
            integrate_with_database(df)
        elif op == 'n':
            op = input("Deseja salvar em um arquivo Excel? [N ou Y]: ").lower()
            if op == 'y':
                nome_arquivo = input("Digite o nome do arquivo Excel para salvar: ")
                excel_save(df, nome_arquivo)

def parse_args():
    parser = argparse.ArgumentParser(description='PyDataCleaner - Ferramenta para extração, limpeza e exploração de dados')
    parser.add_argument('caminho_arquivo', help='Caminho para o arquivo de dados a ser processado')
    return parser.parse_args()

def main():
    args = parse_args()
    df = data_extract(args.caminho_arquivo)
    
    if df is not None:
        clean_data(df)
        explore_data(df)        
        data_save(df)
        
    logging.info("Execução do script PyDataCleaner finalizada")
        
if __name__ == "__main__":
    main()

