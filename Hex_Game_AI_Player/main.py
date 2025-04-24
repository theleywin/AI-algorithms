import os
from hex_board import HexBoard
from rave_player import RavePlayer

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    print("Bienvenido a HEX")
    try:
        size = int(input("Ingrese el tamaño del tablero (por ejemplo, 5): "))
    except ValueError:
        print("Tamaño inválido. Usando tamaño 5 por defecto.")
        size = 5

    board = HexBoard(size)

    # Game mode:
    # 1: Dos jugadores humanos
    # 2: Humano (jugador 1) vs. IA (jugador 2)
    # 3: IA vs IA
    mode = input("Seleccione modo de juego (1: Humano vs Humano, 2: Humano vs IA, 3: IA vs IA): ")

    if mode == "2":
        human_player = int(input("Elija su identificador (1 para 🔴, 2 para 🔵): "))
        ai_player = 2 if human_player == 1 else 1
        player_objects = {
            human_player: None,  # Human: will get input
           ai_player: RavePlayer(ai_player)
        }
    elif mode == "3":
        player_objects = {
            1: RavePlayer(1),  # IA
            2: RavePlayer(2)   # IA
        }
    else:
        player_objects = {
            1: None,  # Human
            2: None   # Human
        }

    current_player = 1
    while True:
        clear_console()
        print("\nTablero actual:")
        board.print_board()

        if board.check_connection(1):
            print("¡El jugador 1 (🔴) ha ganado!")
            break
        if board.check_connection(2):
            print("¡El jugador 2 (🔵) ha ganado!")
            break
        if not board.get_possible_moves():
            print("Empate. No hay más movimientos disponibles.")
            break

        print(f"Turno del jugador {current_player} ({'🔴' if current_player==1 else '🔵'}).")

        if player_objects.get(current_player) is None:
            # Human move
            try:
                move_input = input("Ingrese su movimiento como 'fila columna': ")
                row, col = map(int, move_input.split())
            except Exception as e:
                print("Entrada inválida. Inténtelo de nuevo.")
                continue
            if (row, col) not in board.get_possible_moves():
                print("Movimiento no válido o casilla ocupada. Inténtelo de nuevo.")
                continue
            board.place_piece(row, col, current_player)
        else:
            move = player_objects[current_player].play(board)
            print(f"La IA juega en la posición: {move}")
            board.place_piece(move[0], move[1], current_player)

        # Cambiar turno
        current_player = 2 if current_player == 1 else 1

if __name__ == "__main__":
    main()