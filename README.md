🇫🇷 [Version française](README.fr.md)

# EsCATe Game

A two-player board game played in the terminal, written in Python as the first-semester project of the EPITA Cybersecurity Bachelor (2025-2026).

A group of 14 cats is held in a boarding house by two wardens. One player moves the cats and tries to get as many of them as possible to an exit, while the other player moves the wardens and tries to catch them first. The game is played in two rounds with the roles swapped, and each cat that escapes earns its player one point.

## Rules (as implemented)

- **Board:** 11 × 11 squares, columns `A`–`K` and rows `1`–`11`.
- **Exits (`S`):** at `F1`, `A5` and `K5`. A cat that reaches an exit escapes and leaves the board.
- **Pond (`O`):** 6 squares in the centre that nobody can cross.
- **Cats (`C`, 14):** start at the bottom of the board and move one square in any direction, diagonals included.
- **Wardens (`W`, 2):** start at `C2` and `I2` and move one square in any direction. A warden catches a cat by moving onto its square, and can jump over a robot to the square behind it.
- **Vacuum robots (`R`, 9):** placed at random. Each one has a 1-in-3 chance to move one square, horizontally or vertically only.
- **Teleporters (`T`, a pair):** placed at random. Only one actor (a cat or a warden) can use them per turn, and only if the exit portal is free.
- **Nets (`F`, 2 per round):** the wardens can drop a net on an empty square to block it, or on a cat to freeze it for one turn.

**A turn has three phases:**
1. The cats' player moves up to 7 cats.
2. The wardens' player moves both wardens and can drop nets.
3. The robots move at random.

A round ends when no cats are left on the board, whether they escaped or were caught. The in-game menu also shows these rules.

## Requirements

- Python 3.10 or later. The game uses only the standard library.
- A terminal that supports ANSI colours (Windows Terminal, PowerShell, or any Linux/macOS terminal).
- `pygame` is needed only for the experimental graphical prototype (see below).

## Usage

```bash
git clone https://github.com/MrChr0ma/Projet-Epita-S1---EsCATe-Game.git
cd Projet-Epita-S1---EsCATe-Game
python "EsCATe Game.py"
```

Enter both players' names, then choose `1` to start or `2` to read the rules. Squares are typed as letter + number (`A6`, `D11`) or number + letter (`6A`).

## Files

| File | Content |
|---|---|
| `EsCATe Game.py` | The full terminal game |
| `EsCATe Game_pygame.py` | An early graphical prototype with pygame (board drawing and piece selection) |

## Status

The terminal game can be played from start to finish (two rounds), and the winner is the player whose cats escaped the most. Known issue:

- **The pygame prototype is unfinished.** It loads its images from hard-coded paths (`Desktop\Projet EPITA semestre 1\...`) that are not in this repository, so it does not run as is.

### TODO
- [ ] Add the pygame images to the repository and load them with relative paths, or drop the prototype.
- [ ] Add one of the extra features suggested in the brief, such as saving and loading a game.

## Authors

A group project by Hector, Florentin, Enzo and Gaël for the EPITA Cybersecurity Bachelor, 2025-2026.

This is an academic project and is not intended for commercial use.
