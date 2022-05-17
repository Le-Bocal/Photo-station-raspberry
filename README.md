# Photo-station-raspberry


## Objectif

Ici, nous avons un raspberry pi avec la distribution raspbian et la solution dodoc installée.
L'objectif est de construire une station qui capture une photo d'un projet, et stock la photo sur un projet dodoc en pressant simplement un bouton

## la solution

Nous utilisons les GPIO du raspberry pi pour brancher un bouton dessus et aussi une LED indiquant la prise de photo.

![branchement du raspberry] (branchement_rasp.jpg)

Puis on utilise un script python (taking-picture.py) pour commander la prise et de photo et ranger celles-ci au bon endroit, il y a un dossier "Station de captation photo" de créé sur le dodoc dans lequel les photos sont stockées.

## la configuration

* [Installer une distribution raspbian sur un raspberry pi](https://www.raspberrypi-france.fr/guide/installer-raspbian-raspberry-pi/)
* connecter le raspberry pi sur votre réseau local
* [Installer dodoc sur le raspberry](https://latelier-des-chercheurs.fr/docs/manuel-dodoc)
* dans le dossier "/hompe/pi/" mettre les script "launcher.sh" et "taking-picture.py"
*  [modifier le crontab pour lancer le script au démarage du raspberry pi](https://www.instructables.com/Raspberry-Pi-Launch-Python-script-on-startup/) , utiliser le script sh de ce dépot !
* explication sur le script python (choix du projet)

