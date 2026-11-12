🇬🇧 [English version](README.md)

# EsCATe Game

Un jeu de plateau à deux joueurs qui se joue dans le terminal. Il est écrit en Python et c'est le projet du premier semestre du Bachelor Cybersécurité de l'EPITA (2025-2026).

Deux gardiens retiennent 14 chats dans une pension. Un joueur déplace les chats et essaie d'en faire sortir le plus possible, l'autre déplace les gardiens et essaie de les attraper avant. La partie se joue en deux manches avec inversion des rôles, et chaque chat évadé rapporte un point à son joueur.

## Règles (telles que codées)

- **Plateau :** 11 × 11 cases, colonnes `A` à `K` et lignes `1` à `11`.
- **Sorties (`S`) :** en `F1`, `A5` et `K5`. Un chat qui atteint une sortie s'évade et quitte le plateau.
- **Bassin (`O`) :** 6 cases au centre, infranchissables pour tout le monde.
- **Chats (`C`, 14) :** ils partent du bas du plateau et avancent d'une case dans n'importe quelle direction, diagonales comprises.
- **Gardiens (`W`, 2) :** ils partent de `C2` et `I2` et avancent d'une case dans n'importe quelle direction. Un gardien capture un chat en allant sur sa case, et il peut sauter par-dessus un robot vers la case d'en face.
- **Robots aspirateurs (`R`, 9) :** placés au hasard. Chacun a une chance sur 3 de bouger d'une case, seulement à l'horizontale ou à la verticale.
- **Téléporteurs (`T`, une paire) :** placés au hasard. Un seul acteur (chat ou gardien) peut s'en servir par tour, et seulement si le portail d'arrivée est libre.
- **Filets (`F`, 2 par manche) :** les gardiens peuvent poser un filet sur une case vide pour la bloquer, ou sur un chat pour l'immobiliser un tour.

**Un tour se déroule en trois phases :**
1. Le joueur des chats déplace jusqu'à 7 chats.
2. Le joueur des gardiens déplace ses 2 gardiens et peut poser des filets.
3. Les robots se déplacent au hasard.

Une manche se termine quand il n'y a plus de chat sur le plateau, qu'ils se soient évadés ou fait capturer. Ces règles sont aussi affichées dans le menu du jeu.

## Prérequis

- Python 3.10 ou plus récent. Le jeu n'utilise que la bibliothèque standard.
- Un terminal qui gère les couleurs ANSI (Windows Terminal, PowerShell, ou n'importe quel terminal Linux/macOS).
- `pygame` n'est nécessaire que pour le prototype graphique expérimental (voir plus bas).

## Utilisation

```bash
git clone https://github.com/MrChr0ma/Projet-Epita-S1---EsCATe-Game.git
cd Projet-Epita-S1---EsCATe-Game
python "EsCATe Game.py"
```

Entre le nom des deux joueurs, puis choisis `1` pour lancer la partie ou `2` pour lire les règles. Une case se saisit sous la forme lettre + chiffre (`A6`, `D11`) ou chiffre + lettre (`6A`).

## Fichiers

| Fichier | Contenu |
|---|---|
| `EsCATe Game.py` | Le jeu complet en terminal |
| `EsCATe Game_pygame.py` | Un premier prototype graphique avec pygame (affichage du plateau et sélection des pièces) |

## État d'avancement

Le jeu en terminal se joue du début à la fin (deux manches), et le gagnant est le joueur dont les chats se sont le plus évadés. Problème connu :

- **Le prototype pygame n'est pas terminé.** Il charge ses images depuis des chemins écrits en dur (`Desktop\Projet EPITA semestre 1\...`) qui ne sont pas dans ce dépôt, donc il ne se lance pas tel quel.

### TODO
- [ ] Ajouter les images du prototype pygame au dépôt et les charger avec des chemins relatifs, ou abandonner le prototype.
- [ ] Ajouter une des fonctionnalités supplémentaires proposées dans le sujet, par exemple la sauvegarde et le chargement d'une partie.

## Auteurs

Projet de groupe réalisé par Hector, Florentin, Enzo et Gaël dans le cadre du Bachelor Cybersécurité de l'EPITA, 2025-2026.

C'est un travail académique, qui n'est pas destiné à un usage commercial.
