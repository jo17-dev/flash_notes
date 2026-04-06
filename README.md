# Outils de prise de note / pense bête / organisation `Flash Note` __nf__

nf (flashnote) est un outils qui transforme vos idées spontanées en fichiers de notes par jour en markdown, avec un point d'honneur sur la vélocité.

Étant toujours dans le termnial en tant que dev, rien ne sert d'ouvrir une interface graphique pour noter une idée. ;)


# 1. Installation

## Sur linux
- clonez le projet `git clone https://github.com/jo17-dev/flash_notes.git && cd flash_notes`
- Je vous laisse compliler votre propre version avec `sudo make install` sur la branche main :)

> _NB 1_: il est fortement recommandé d'utiliser __make 4+__
> _NB 2_: Toute l'installation a été testé sur manjaro (arch based), mais pas sur les autres ditributions
	
## Sur windows: 
- le Makefile actuel ne prends pas encore en compte la plateforme windows.
- Aucune installation n'as été testée  pour la plateforme. Toutefois, la variable d'environement `$HOME` car le programme (en date de la 2.0.0-beta) se base dessus pour déterminer l'endroit ou stocker les fichiers.

# 2. Fonctionnalités

### Fonctionalités actuelle ( minimum viable )
- Ajouter une note `nf -a <Votre note ici>`
- Afficher le chemin vers le fichier de note de la journée: `nf`
- Afficher la version utilisée: `nf -v`

### 2.2 À venir....
-  Edit note `nf -e id` :  Ouvre le fichier de de la note 
- Supression des notes
- configurations externes ( ex le dossier principal de sauvegardes, etc... via un ficher de configuration )
- Afficher les notes du dernier jour, de la derniere heure ou meme de la derniere minute

# Coeur du programme  & configuration par défaut

## Achitecture
- Un dossier principal _.flashnote_ à la racine:
    - dossier 2025 _year2025_
        - dossier moi janvier 2025 _month01_
            - fichier jour1 _day01.flashnote.md_
                --- dans les fichiers, les notes sont séparés par Ajout avec les méta données à la premiere ligne: id=cedewdewd;timestamp=123343
            - fichier jour31 _day31.flashnote.md_
        - dossier moi fevrier 2025 _month02_
    - dossier 2026
