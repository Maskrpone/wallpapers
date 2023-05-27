import os
import glob

def rename():
    dossier = "/home/maskrpone/Pictures/wallpapers/"
    i = 1
    #Utilisation de glob pour obtenir tous les fichiers d'image dans le dossier
    fichiers_images = glob.glob(os.path.join(dossier, "*"))

    for fichier in fichiers_images:
        if os.path.isfile(fichier) and os.path.splitext(fichier)[1].lower() in [".png", ".jpg", ".jpeg"]:
            ancien_nom = fichier
            extension = os.path.splitext(fichier)[1]  # Récupération de l'extension du fichier
            nouveau_nom = os.path.join(dossier, str(i) + extension)
            os.rename(ancien_nom, nouveau_nom)
            i += 1

    print("Le renommage des images est terminé.")

rename()
