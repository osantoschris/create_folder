import os, locale
from datetime import datetime
import pandas as pd
from googletrans import Translator

class CreateFolder():

    def create_month_paths(self, year:str, source:str) -> bool:
        '''
        ### Create Month Directorys
        This function create all month paths for year you needs. Enter the base directory and year to define complete source.
        '''
        for month in range(1,13,1):
            month_number:str = pd.to_datetime(month, format='%m').strftime('%m')
            month_name:str = pd.to_datetime(month, format='%m').strftime('%b').capitalize()
            complete_month:str = f'{month_number} - {month_name}'

            complete_source:str = os.path.join(source, year, complete_month)
            if not os.path.exists(complete_source):
                os.makedirs(complete_source)

        return True
    
locale_br = 'pt_BR.UTF-8'
locale_us = 'en_US.UTF-8'
source_message = 'Entre com o diretório desejado: '
validate_message = 'Deseja criar os diretórios de acordo com o ano atual? (Y/n): '
success_message = 'Criação das pastas executada com sucesso!\nPrograma finalizado...'
error_message = 'Erro ao executar a criação das pastas'
final_message = 'Encerrando a execução...'
input_year = 'Digite o ano desejado no formato "AAAA": '

print('Selecione seu idioma')
print('Select your language')

while True:
    number_locale = int(input('Português BR (1)/Inglês US (2): '))

    if number_locale == 1:
        locale.setlocale(locale.LC_ALL, locale_br)
        break
    elif number_locale == 2:
        locale.setlocale(locale.LC_ALL, locale_us)
        source_message = Translator().translate(source_message, src='pt', dest='en').text
        validate_message = Translator().translate(validate_message, src='pt', dest='en').text
        success_message = Translator().translate(success_message, src='pt', dest='en').text
        error_message = Translator().translate(error_message, src='pt', dest='en').text
        final_message = Translator().translate(final_message, src='pt', dest='en').text
        input_year = Translator().translate(input_year, src='pt', dest='en').text
        break
    else:
        print('Verifique a localização escolhida...')
        print('Verify your location choice...')

while True:
    source = input(source_message)
    if source != '':
        break

while True:
    validate_year = input(validate_message)
    if validate_year != '':
        break

if (validate_year == 'Y') or (validate_year == 'y'):
    year = datetime.today().strftime('%Y')
    try:
        CreateFolder().create_month_paths(year=year, source=source)
        print(success_message)
    except NameError as error:
        print(error_message)
        print(error)
    finally:
        print(final_message)
else:
    while True:
        year = input(input_year)
        if len(year) == 4:
            break

    try:
        CreateFolder().create_month_paths(year=year, source=source)
        print(success_message)
    except NameError as error:
        print(error_message)
        print(error)
    finally:
        print(final_message)