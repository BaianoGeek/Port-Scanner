#!/usr/bin/python

import socket, informacoes
from datetime import datetime

print ("\nLearning Python")


def port_scan():
        inicio =  datetime.now()
        
        ip = input("\nInsira o IP do alvo: ")
        lista_portas = informacoes.escolher_portas()
        print ("\nIniciando os Scans no IP: ", ip)
        print ("A lista de portas escolhidas possui as seguintes portas: ", lista_portas,"\n")

        for porta in lista_portas:
                meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(0.5)
                if meusocket.connect_ex((ip, porta)) == 0:
                        print ("\n[+] Porta TCP Aberta:", porta)
                        meusocket.close()
        final = datetime.now()
        tempoTotal = (final - inicio)
        print("\n O tempo de duração do scan foi de: ", tempoTotal)
port_scan()
