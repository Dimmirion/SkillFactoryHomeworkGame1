def print_board(board):
    '''Выводит игровое поле в консоль.'''
    for i in range(3):
        print(f" {board[i][0]} | {board[i][1]} | {board[i][2]} ")
        if i < 2:
            print("-----------")


def check_winner(board):
    '''Проверяет наличие победителя или ничьей. Возвращает 'X' или 'O' при победе, 'Draw' при ничье, None если игра продолжается.'''
    # Проводится проверка строк и столбцов
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    # Проверка на ничью
    if all(cell != ' ' for row in board for cell in row):
        return 'Draw'

    return None


def get_valid_move(board, player):
    '''Получает и проверяет корректность хода от игрока.'''
    while True:
        try:
            row = int(input(f"Игрок {player}, введите номер строки (1-3): ")) - 1
            col = int(input(f"Игрок {player}, введите номер столбца (1-3): ")) - 1

            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == ' ':
                    return (row, col)
                else:
                    print('Эта клетка уже занята! Попробуйте снова.')
            else:
                print('Числа должны быть от 1 до 3! Попробуйте снова.')
        except ValueError:
            print('Пожалуйста, вводите только числа! Попробуйте снова.')


def main():
    '''Основная функция игры, управляющая игровым процессом.'''
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    print('Добро пожаловать в игру "Крестики-нолики!"')
    print('Для совершения хода вводите номера строки и столбца от 1 до 3.')

    while True:
        print_board(board)
        print()

        # Получаем ход от текущего игрока
        row, col = get_valid_move(board, current_player)
        board[row][col] = current_player

        # Проверяем состояние игры
        result = check_winner(board)
        if result:
            print_board(board)
            if result == 'Draw':
                print("\nИгра окончена! Ничья!")
            else:
                print(f"\nИгрок {result} победил! Поздравляем!")
            break

        # Смена игрока
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    main()