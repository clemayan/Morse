# Décodage en morse 🔢 :

## Description 📌
Ce projet a été réalisé en janvier 2022 dans le cadre de la matière NSI au Centre Internationnal de Valbonne (CIV).
Il s'agit d'une mini base de données permettant la gestion d'un hôpital grâce à diverses fonctionnalités accessibles en ligne de commande.

## Fonctionnalités 🎯
### Au démarrage 
Installer les bibliothèque nécessaires :
>> pip install networkx

Lors de l'exécution du programme un arbre binaire représentant le langage Morse s'affiche pour voir les caractères possibles d'utilisation.
Le programme met plusieurs secondes à exécuter l'encodage des gros fichiers.
La moyenne de l'encodage d'un fichier est effectuée sur 3 fichiers texte de différentes tailles.
La moyenne du décodage d'un fichier n'a pas pu être terminé un problème suivant avec la structure dictionnaire.

L'encodage d'un message peut mélanger majuscules et minuscules.
L'utilisateur à le choix entre utiliser une structure d'arbre ou une structure de dictionnaire.
Tous les caractères ayant une alternative en morse peuvent être encodés.

### Limites 
Certains caractères ne sont pas disponibles :
ô, ê, œ, â, î, û, ù, ó, ò, ì, ï, ë, ü, °, %

De plus, les guillemets sont ceux du clavier traditionnel '""' et non "«»".
Le fichier à encoder ne doit pas contenir de retour à la ligne.

Tout message rentré par l'utilisateur doit terminer par un *
Par exemple :
°°°*---*°°°*
Et non :
°°°*---*°°°

De même qu'un message retourné en morse se terminera toujours par * (sauf pour une seule lettre)
L'utilisateur à la possibilité de faire un retour ou de stopper le programme en rentrant "retour" ou "stop".

Un message s'affiche lorsqu'un autre caractère (autres que 1, 2, retour, stop) est entré par l'utilisateur.

## Technologies utilisées 🛠
Python 3

## Auteure 👥
Mazuet Maya

## 📜 Licence  
Ce projet est protégé par des droits d’auteur. Toute utilisation, modification, reproduction ou distribution sans autorisation est interdite.  

🔗 Consultez le fichier [LICENCE.txt](LICENCE.txt) pour plus de détails.  
