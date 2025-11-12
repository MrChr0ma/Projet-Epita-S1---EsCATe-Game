# 🐱 Projet S1 - Jeu « EsCATe Game »

## 📝 Description

Ce projet consiste à développer un jeu de plateau à deux joueurs nommé **EsCATe Game**.  
Dans ce jeu, un groupe de chats est retenu dans une pension par deux gardiens. L’objectif pour le premier joueur est de faire s’échapper un maximum de chats, tandis que le second joueur tente de les capturer avant leur fuite.

---

## 🎯 Objectif

Coder un jeu de plateau à deux joueurs où :
- Un joueur contrôle **14 chats** qui tentent de s’évader.
- L’autre joueur contrôle **2 gardiens** qui tentent de capturer les chats.

---

## 🧩 Principe du jeu

### Plateau
- Plateau carré de **11x11 cases**.
- Contient :
  - Une **zone de départ** pour les chats (14 cases au centre en bas).
  - Un **bassin d’eau** infranchissable (6 cases au centre).
  - **Trois sorties** en (1, F), (5, A) et (5, K).

### Acteurs
- **14 chats** : débutent dans la zone réservée.
- **2 gardiens** : débutent en (2, C) et (2, I).
- **9 robots aspirateurs** : placés aléatoirement en début de partie.

### Déplacements
- Tous les acteurs se déplacent d’**au plus une case par tour** (horizontale, verticale ou diagonale – sauf les robots qui ne se déplacent qu’horizontalement ou verticalement).
- Les gardiens peuvent **sauter par-dessus les robots**.
- Le bassin est **infranchissable** pour tous.

### Phases d’un tour
1. **Phase Chats** : Déplacement de 7 chats (au choix).
2. **Phase Gardiens** : Déplacement des 2 gardiens.
3. **Phase Robots** : Chaque robot a 1 chance sur 3 de se déplacer aléatoirement.

### Fin de manche et victoire
- Une manche se termine quand **tous les chats ont quitté le plateau** (évadés ou capturés).
- Chaque chat évadé rapporte **1 point**.
- Les rôles sont **inversés** à la manche suivante.
- La partie se joue en **2 manches**.
- Le gagnant est le joueur avec le **plus de points**.

### Plateau
- Plateau carré de **11x11 cases**.
- Contient :
  - Une **zone de départ** pour les chats (14 cases au centre en bas).
  - Un **bassin d'eau** infranchissable (6 cases au centre).
  - **Trois sorties** en (1, F), (5, A) et (5, K).

#### Figure 1 : Exemple d'un plateau initial

```
    A B C D E F G H I J K
1   R         S          
2       W       R   W    
3           O O O        
4         R O O O        
5   S     R             S
6                     R  
7       R       R   R    
8             C        
9           C C C         
10  R     C C C C C        
11        C C C C C        
          
```

**Légendes :**
- `C` : les chats
- `W` : les deux gardiens (Wardens)
- `R` : les robots aspirateur
- `O` : le bassin d'eau
- `S` : les sorties
---

## ⚙️ Contraintes imposées

### Fonctionnalités de base
- Jeu à 2 joueurs respectant les règles décrites.
- Affichage du plateau dans le terminal.

### Fonctionnalités additionnelles
Deux fonctionnalités supplémentaires doivent être implémentées, par exemple :
- Sauvegarder / charger une partie.
- Ajouter un chat avec un rôle spécial.
- ... ou toute autre idée enrichissant le jeu.

---

## 👥 Auteurs

Projet réalisé dans le cadre du Bachelor Cybersécurité à EPITA – Année 2025-26.

---

## 📄 Licence

Ce projet est un travail académique et n’est pas destiné à une utilisation commerciale.
