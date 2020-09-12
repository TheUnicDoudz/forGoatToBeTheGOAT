from toolbox import Game
import numpy as np

def h(board, solution):
    result = board != solution
    result = result.astype(int).sum()
    return result

if __name__ == '__main__':
    solution = np.array([[0, 1, 2],
                [3, 4, 5],
                [6, 7, 8]])

    board = np.array([[8, 1, 5],
                    [0, 6, 2],
                    [7, 4, 3]])

    game = Game(board)

    ouvert = []  # Liste de tous les sommets en attente
    ferme = []  # Liste de tous les sommets traités

    ouvert.append((game.get_board().copy(), 0, None))
    complete = False
    n = 0
    while len(ouvert) > 0 or not complete:
        n = n + 1
        ouvert = sorted(ouvert, key=lambda c:c[1])
        current = ouvert.pop(0)
        ferme.append(current)

        if np.array_equal(current[0], solution):
            complete = True
            break


        next = Game(current[0])
        next.move_to_up()
        f = h(next.get_board(), solution) + n
        ouvert.append((next.get_board().copy(), f, len(ferme)-1))

        next = Game(current[0])
        next.move_to_down()
        f = h(next.get_board(), solution) + n
        ouvert.append((next.get_board().copy(), f, len(ferme)-1))

        next = Game(current[0])
        next.move_to_left()
        f = h(next.get_board(), solution) + n
        ouvert.append((next.get_board().copy(), f, len(ferme)-1))

        next = Game(current[0])
        next.move_to_right()
        f = h(next.get_board(), solution) + n
        ouvert.append((next.get_board().copy(), f, len(ferme)-1))

    if len(ouvert) == 0:
        print("Pas de solution")

    step = ferme[-1]
    print(f"{step[0]}")
    print("="*20)
    while step[2] is not None:
        step = ferme[step[2]]
        print(f"{step[0]}")
        print("=" * 20)