import pandas as pd
import re


def remove_public_expenses(text):
    if pd.isna(text):
        return 'Не заполнено'
    print(text.split('\n'))



def extend_table(data_file:str, end_folder:str):
    """
    Функция для обработки выгрузки из 1с по наименованию
    :param data_file:
    :param end_folder:
    :return:
    """
    df = pd.read_excel(data_file,skiprows=10,header=None)
    df.drop(columns=[6,9,10,11],inplace=True)
    df.columns = ['Период','Документ','Аналитика Дт','Аналитика Кт','Дебет счет','Дебет значение','Кредит счет','Кредит значение']



    df['Аналитика Дт без хвоста'] = df['Аналитика Дт'].apply(remove_public_expenses)
    df.to_excel('data/dff.xlsx',index=False)


















if __name__ == '__main__':
    main_file = 'data/6.xlsx'
    main_end_folder = 'data/Результат'

    extend_table(main_file,main_end_folder)

    print('Lindy Booth')