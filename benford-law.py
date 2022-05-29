from pynubank import Nubank
import pandas as pd
import datetime
import dateutil.relativedelta
from getpass import getpass
import matplotlib.pyplot as plt


def get_first_digit(row):
    amount = row.amount
    return str(amount)[0]

if __name__ == "__main__":
    nu = Nubank()
    uuid, qr_code = nu.get_qr_code()
    # Nesse momento será printado o QRCode no console
    # Você precisa escanear pelo o seu app do celular
    # Esse menu fica em NU > Perfil > Acesso pelo site
    qr_code.print_ascii(invert=True)
    input('Após escanear o QRCode pressione enter para continuar')
    # Somente após escanear o QRCode você pode chamar a linha abaixo
    cpf = input('CPF: ')
    cpf = cpf.replace('.','').replace('-','')
    password = getpass()
    nu.authenticate_with_qr_code(cpf, password, uuid)
    card_statements = nu.get_card_statements()
    df = pd.DataFrame(card_statements)
    df['firt-digit'] = df.apply(get_first_digit, axis=1)
    print(type(df['firt-digit'].value_counts()))
    s = df['firt-digit'].value_counts(normalize=True)
    print(s)
    s.plot.bar()
    plt.show()