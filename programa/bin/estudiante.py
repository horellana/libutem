import argparse
from sys import stderr, exit

import miutem


def main(args):
    if not (args.rut and args.contraseña):
        stderr.write('Necesito un rut y una contraseña\n')
        return -1

    cliente = miutem.Cliente()
    cliente.login(args.rut, args.contraseña)

    if args.notas:
        notas = list(cliente.notas())
        print(notas)

    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Obtiene informacion relacionada a un estudiante'
    )
    parser.add_argument('rut')
    parser.add_argument('contraseña')
    parser.add_argument('--notas',
                        action='store_true')

    args = parser.parse_args()

    exit(main(args))
