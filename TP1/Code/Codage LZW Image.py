# -*- coding: utf-8 -*-
"""Copy of Codage LZW.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U-TiICzIV-Il8akavDEyyAeOM_IIWgYy

INF8770 Technologies multimédias

Polytechnique Montréal

Exemple de codage LZW
"""

import numpy as np
import time
t1 = time.perf_counter() * 1000

import cv2

img_color = cv2.imread('image_1.png',1)
img_list = list(img_color.tobytes())
print(img_list)

"""Message à coder"""

Message = img_list

"""Construction du dictionnaire à partir des symboles contenus dans le message. """

dictsymb =[Message[0]]
dictbin = ["{:b}".format(0)]
nbsymboles = 1
for i in range(1,len(Message)):
    if Message[i] not in dictsymb:
        dictsymb += [Message[i]]
        dictbin += ["{:b}".format(nbsymboles)] 
        nbsymboles +=1
        
longueurOriginale = np.ceil(np.log2(nbsymboles))*len(Message)

"""Ajustement des codes binaires selon le nombre total de symboles en ajoutant des zéros. Tri des symboles. Affichage du dictionnaire initial."""

for i in range(nbsymboles):
    dictbin[i] = "{:b}".format(i).zfill(int(np.ceil(np.log2(nbsymboles))))
        
dictsymb.sort()
dictionnaire = np.transpose([dictsymb,dictbin])
print(dictionnaire)

"""Codage du message"""

i=0;
MessageCode = []
longueur = 0
while i < len(Message):
    precsouschaine = Message[i] #sous-chaine qui sera codé
    souschaine = Message[i] #sous-chaine qui sera codé + 1 caractère (pour le dictionnaire)
    
    #Cherche la plus grande sous-chaine. On ajoute un caractère au fur et à mesure.
    while souschaine in dictsymb and i < len(Message):
        i += 1
        precsouschaine = souschaine
        if i < len(Message):  #Si on a pas atteint la fin du message
            souschaine += Message[i]  

    #Codage de la plus grande sous-chaine à l'aide du dictionnaire  
    codebinaire = [dictbin[dictsymb.index(precsouschaine)]]
    MessageCode += codebinaire
    longueur += len(codebinaire[0]) 
    #Ajout de la sous-chaine codé + symbole suivant dans le dictionnaire.
    if i < len(Message):
        dictsymb += [souschaine]
        dictbin += ["{:b}".format(nbsymboles)] 
        nbsymboles +=1
    
    #Ajout de 1 bit si requis
    if np.ceil(np.log2(nbsymboles)) > len(MessageCode[-1]):
        for j in range(nbsymboles):
            dictbin[j] = "{:b}".format(j).zfill(int(np.ceil(np.log2(nbsymboles))))
    
t2 = time.perf_counter() * 1000
print("Temps moyen d'exécution: {0} ms".format(round(t2-t1), 3))

"""Affichage du message codé"""

print(MessageCode)

"""Affichage du dictionnaire final"""

dictionnaire = np.transpose([dictsymb,dictbin])
print(dictionnaire)

"""Longueur en bits du message codé et celle de l'original"""

print("Longueur = {0}".format(longueur))
print("Longueur originale = {0}".format(longueurOriginale))

tauxCompression = 1 - (longueur/longueurOriginale)
print("Taux de compression : {0}".format(round(tauxCompression,3)))