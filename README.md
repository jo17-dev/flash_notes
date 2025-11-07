# OUtils de prise de note / pense bête / organisation `Flash Note` __nf__

c'est un outils qui créer des dossier par jour et dans ces dossier créer des fichiers 





# 1. Fonctionnalités

- Ajouter une note `nf -a "Votre note ici"`
-  Edit note `nf -e id` :  Ouvre le fichier de de la note 
- Suprimmer les notes
- configurer le dossier principal du projet
    - Ajouter le dossier le dossier principal du projet: defini à l'installation dans un fichier _flashnoterc_
    - Modifier le dossier principal du projet

- Afficher les notes du dernier jour, de la derniere heure ou meme de la derniere minute


# Coeur du programme  & configuration par défaut

    ## Achitecture

- Un fichier `.flashnoterc` pour les configs de l'app 
    - chemin du dossier par defaut uniquement pour le moment
    - url de backup ?
    - le path de l'éditeur par defaut ( vim par default)
- Un dossier principal:
    - dossier 2025 _year2025_
        - dossier moi janvier 2025 _month01_
            - fichier jour1 _day01.flashnote.md_
                --- dans les fichiers, les notes sont séparés par Ajout avec les méta données à la premiere ligne: id=cedewdewd;timestamp=123343
            - fichier jour31 _day31.flashnote.md_
        - dossier moi fevrier 2025 _month02_
    - dossier 2026






# Processus d'affaires et cas d'utilisations

1. Ajout d'une note
    - Le user fait _nf -a "ddqdwqdwqdqwwqewqewqewq"_
        - Le programme insert dans yearX/monthX/dayX un ------\n id=qewqqwe; timestamp=1234343 \n la none. et créer les dossiers et fichiers s'l existent pas
    - Le user fait _nf -af_
        - Le programme ouvrre
        - Le programme créer le fichier s'il n'existe pas et l'ouvre avec l'éditeur de texte de son choix

2. Edition d'une note
     - Le user fait _nf -ef_
        - Le programme ouvrre
        - Le programme créer le fichier s'il n'existe pas et l'ouvre avec l'éditeur de texte de son choix

3. Afficher les notes d'un jour
    - Le user fait _nf -s_
        - Le pogramme fait un cat du fichier du jour ou le crée s'il n'est pas présent
    - Le user fait un _nf -sd yyyy/mm/dd _
        - Le programme fait un cat du fichie de la date pécifiée
