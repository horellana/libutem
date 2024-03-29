#!/usr/bin/env python3

import sys
import json
import argparse

import utem.miutem as miutem
import utem.dirdoc as dirdoc


def main(args):
    if not (args.rut and args.contraseña):
        if args.rut:
            args.contraseña = args.rut
        else:
            print('Necesito un rut y una contraseña', file=sys.stderr)
            return -1

    if args.dirdoc:
        cliente = dirdoc.Cliente()
    else:
        cliente = miutem.Cliente()

    cliente.login(args.rut, args.contraseña)

    if args.notas:
        notas = json.dumps(list(cliente.notas()),
                           indent=4,
                           ensure_ascii=False)
        print(notas)

    return 0


def leer_argumentos():
    parser = argparse.ArgumentParser(
        description='Obtiene informacion relacionada a un estudiante'
    )
    parser.add_argument('rut')
    parser.add_argument('-c', '--contraseña',
                        help='Por defecto es la misma que el rut')
    parser.add_argument('--notas',
                        action='store_true')
    parser.add_argument('--miutem',
                        action='store_true',
                        help='sacar informacion desde miutem')
    parser.add_argument('--dirdoc',
                        action='store_true',
                        help='sacar informacion desde dirdoc')

    return parser.parse_args()


if __name__ == '__main__':
    sys.exit(main(leer_argumentos()))
