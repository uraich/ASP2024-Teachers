# ASP2024-Teachers
Documentation de l'atelier IoT (**I**nternet **o**f **T**hings, Internet des Objets) à ASP2024 (African School of Physics, l'École de Physique Fondamentale) Marrakech

Ces pages sont dédié au cours pour les professeurs d'école.

## Introduction
Pendant ASP2022 un atelier sur des petites expériences de physique et IoT a été intégré pour la première fois dans le programme de l'école. Il s'agit d'un atelier ou le étudiants créent des petite expérience de physique. Puisque le temps alloué pour cet atelier est très restreint dans le cadre du programme pour le professeur d'école, seulement des capteurs et actionneurs simulé sont utilisé.
L'équipement de l'atelier est très peu chère (~ 20 Euros par kit) et consiste en
* une carte CPU ESP32 avec un interpréteur MicroPython installé dans la mémoire flash et un LED programmable connecté à une ligne GPIO (**G**enerale **P**urpose **IO** line, ligne d'entrée / sortie digitale)
* un câble USB-C (ou micro USB) pour communiquer entre PC et ESP32. Cette connexion est utilisé pour programmer la mémoire flash, pour télécharger les programmes Python de l'utilisateur et pour visualiser du texte imprimé par les programmes
* un fond de panier avec 3 places reliant la carte CPU avec des cartes capteurs ou actionneurs
* un interrupteur bouton connecté a une ligne GPIO via le fond de panier
* un potentiomètre 10 k&Omega connecté au Convertisseur Analogique Digital (ADC, **A**anlog to **D**igital **C**onverter)
* un anneau avec 7 LED couleur (neopixel)

Pour plus d'information regardez les page Wiki de ce dépôt github s.v.p.
