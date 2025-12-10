import os
import datetime
import subprocess

# classe de gestion de la persistance
class FileManager:
    def __init__(self):
        # Déterminer le chemin du fichier de configuration
        config_path = os.path.expanduser('~/.flashnoterc')
        
        # Initialisation par défaut
        self.parent_folder = "~/.flashnote/"
        
        # Si le fichier de configuration existe
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                for line in f:
                    line = line.strip()
                    # Ignorer les lignes vides et les commentaires
                    if not line or line.startswith('#'):
                        continue
                    
                    # Chercher la variable parent_folder
                    if line.startswith('parent_folder:'):
                        # Séparer la clé de la valeur
                        key, value = line.split(':', 1)
                        self.parent_folder = value.strip()
                        break

        # Expansion du chemin (gestion du ~)
        self.parent_folder = os.path.expanduser(self.parent_folder)

    # ajouter une note 
    # is_editor_mode -> defini si on ouvre le fichier avec un text editor ou pas
    def add_note(self, note:str="# __Votre note ici!__ ", is_editor_mode:bool=False):

        full_path = self.prepare_files()
        
        # Générer un ID unique et timestamp pour les métadonnées
        timestamp = int(datetime.datetime.now().timestamp())
        displayable_date_time = datetime.datetime.fromtimestamp(timestamp).strftime("%A, %b %-d %Y - %H:%M")
        note_id = f"id_{timestamp}"

        # Créer le fichier s'il n'existe pas déjà
        if not os.path.exists(full_path):
            # Écrire l'en-tête avec les métadonnées
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(f"id={note_id};timestamp={displayable_date_time}\n\n")
                f.write(note)
                f.write("\n---\n")
                f.close()
        else:
            # Écrire l'en-tête avec les métadonnées
            with open(full_path, 'a', encoding='utf-8') as f:
                f.write(f"id={note_id};timestamp={displayable_date_time}\n\n")
                f.write(note)
                f.write("\n---\n")
                f.close()
        
        # Gestion du mode éditeur
        if is_editor_mode:
            try:
                subprocess.run(['vim', full_path])
            except FileNotFoundError:
                print(f"Le fichier est disponible à: {full_path}")
        
        return full_path
    
    def prepare_files(self):
        """Crée la structure de dossiers et fichiers organisés par date"""
        # Obtenir la date actuelle
        now = datetime.datetime.now()
        
        # Construire les chemins
        year_folder = f"year{now.year}"
        month_folder = f"month{now.month:02d}"
        day_file = f"day{now.day:02d}.flashnote.md"
        
        # Chemin complet
        full_path = os.path.join(
            self.parent_folder,
            year_folder,
            month_folder,
            day_file
        )
        
        # Créer les dossiers parents si ils n'existent pas
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        return full_path
    
    def get_today_notes_full_path(self):
        full_path = self.prepare_files()
        if os.path.exists(full_path):
            return full_path
        else:
            try:
                with open(full_path, 'a', encoding='utf-8') as f:
                    f.close()
            except:
                print("something happened.. please prevent the devellopper...")