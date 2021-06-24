# Tournoi_P4

[![Generic badge](https://img.shields.io/badge/MADE_WITH-PYTHON-blueviolet.svg)](https://shields.io/)   
[![Generic badge](https://img.shields.io/badge/APPROVED_BY-AURELIE_BERNICHE-blueviolet.svg)](https://shields.io/)

Ce programme a été réalisé à la demande d'un club d'échec. Les organisateurs voulaient un logiciel autonome fonctionnant hors ligne. 

## Pour commencer

Ce code est dévéloppé en langage Python. Il permet de gérer les événements des tournois d'echec et de produire des rapports en l'absence de connexion internet.

### Pré-requis

- Python 3  [Download Python](https://www.python.org/ftp/python/3.9.1/python-3.9.1-amd64.exe)  
- Visual Studio Code  [Download VS Code](https://code.visualstudio.com/)  
- Dépôt GitHub  [Create a new repository](https://github.com/new)

### Installation

Dans un premier temps, vous devez créer un dossier pour ce programme afin de télécharger l'application:  
1) ```mkdir projet4```: Créer un dossier projet2 
2) ```cd projet4```: Se placer dans ce dossier
3) ```git clone https://github.com/BernicheAurelie/Tournoi_P4.git```: Cloner le repository contenant l'application  
4) ```cd Tournoi_P4```: Se placer dans le dépôt cloné
5) ```Python -m venv env```  : Créer l'environnement virtuel
6) Cet environnement nécessite d'être activé via:  
sous Windows: ```source env/scripts/activate```  
sous Mac/Linux: ```source env/bin/activate```  
7)```pip install -r requirements.txt```: Récupérer les modules nécessaires à l'application du code, contenus dans le fichier **requirements.txt**.  

## Démarrage

Vous pouvez maintenant lancer l'application avec la commande suivante:  
```python main_menu.py```  
Celle-ci va alors vous permettre d'accéder au menu principal.
Vous pourrez alors choisir entre plusieurs actions:
1) Commencer un nouveau tournoi
2) Recharger un tournoi déjà commencé
3) Accéder aux joueurs et aux rapports
4) Quitter le programme

Lors de la création d'un nouveau tournoi, un fichier **players.json** va être créé avec tous les joueurs participants aux tournois.
Un autre fichier **tournaments.json** contiendra tous les tournois. Les tournois seront sauvegardés dès que les premières informations seront saisies et pourront être interrompus à la fin d'un tour et repris plus tard. 

Vous serez guidé ensuite dans ce programme par plusieurs menus successifs.
Ils vous permettront de choisir les actions que vous souhaitez effectuer à partir de la base de données au format *"json"*.

Pour vérifier que les directives de la PEP8 sont bien respectées, je vous invite à utiliser flake8 de la manière suivante:
1) installer **flake8-html** avec la commande ```pip install flake8-html```
2) Créer un ficher de configuration ```touch .flake8```
3) A partir du fichier **flake8.config** vous pouvez modifier les otptions pour générer le rapport HTML.
4) Dans le terminal, au sein de Tournoi_P4, lancer la commande ```flake8```
5) Ouvrir le dossier **flake8-report-p4**
6) Double-cliquez ensuite sur le document HTML **index**. Aucune erreur ne doit être signalée.


## Fabriqué avec

- [Python 3](https://www.python.org/ftp/python/3.9.1/python-3.9.1-amd64.exe) - langage de programmation
- [Visual Studio Code](https://code.visualstudio.com/) - Editeur de textes

## Contributing

**Ranga Gonnage** _[Mentor OpenClassrooms](https://openclassrooms.com/fr/)_

## Versions

**Dernière version :** 1.0

## Auteurs

**Aurélie Berniche** _[lien GitHub](https://github.com/BernicheAurelie)_
