enter_cells = '_________'
enter_cells = list(enter_cells)
cells = f'''---------
| {enter_cells[0]} {enter_cells[1]} {enter_cells[2]} |
| {enter_cells[3]} {enter_cells[4]} {enter_cells[5]} |
| {enter_cells[6]} {enter_cells[7]} {enter_cells[8]} |
---------'''
print(cells)
big_numbers = ['4', '5', '6', '7', '8', '9', '10']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
left_1 = '1 1'
left_2 = '1 2'
left_3 = '1 3'
middle_1 = '2 1'
middle_2 = '2 2'
middle_3 = '2 3'
right_1 = '3 1'
right_2 = '3 2'
right_3 = '3 3'

x = 'XXX'
o = 'OOO'
space = '_'
xo_counter = 0
while True:
    win_1 = enter_cells[0] + enter_cells[1] + enter_cells[2]
    win_2 = enter_cells[3] + enter_cells[4] + enter_cells[5]
    win_3 = enter_cells[6] + enter_cells[7] + enter_cells[8]
    win_4 = enter_cells[0] + enter_cells[3] + enter_cells[6]
    win_5 = enter_cells[1] + enter_cells[4] + enter_cells[7]
    win_6 = enter_cells[2] + enter_cells[5] + enter_cells[8]
    win_7 = enter_cells[0] + enter_cells[4] + enter_cells[8]
    win_8 = enter_cells[2] + enter_cells[4] + enter_cells[6]

    win_list = [win_1, win_2, win_3, win_4, win_5, win_6, win_7, win_8]

    if x in win_list:
        print('X wins')
        break
    elif o in win_list:
        print('O wins')
        break
    elif x and o not in win_list:
        if space in enter_cells:
            pass
        else:
            print('Draw')
            break
    xo_counter += 1
    enter_coordinates = input('Enter the coordinates: ')
    if enter_coordinates[0] not in numbers or enter_coordinates[2] not in numbers:
        xo_counter -= 1
        print("You should enter numbers!")
    elif enter_coordinates[0] in big_numbers or enter_coordinates[2] in big_numbers:
        xo_counter -= 1
        print('Coordinates should be from 1 to 3!')
    elif enter_coordinates == left_1:
        if enter_cells[6] != space:
            xo_counter -= 1
            print("This cell is occupied! Choose another one!")
        else:
            if xo_counter % 2 != 0:
                enter_cells[6] = 'X'
            else:
                enter_cells[6] = 'O'
            cells = f'''---------
| {enter_cells[0]} {enter_cells[1]} {enter_cells[2]} |
| {enter_cells[3]} {enter_cells[4]} {enter_cells[5]} |
| {enter_cells[6]} {enter_cells[7]} {enter_cells[8]} |
---------'''
            print(cells)
    elif enter_coordinates == left_2:
        if enter_cells[3] != space:
            xo_counter -= 1
            print("This cell is occupied! Choose another one!")
        else:
            if xo_counter % 2 != 0:
                enter_cells[3] = 'X'
            else:
                enter_cells[3] = 'O'
            cells = f'''---------
| {enter_cells[0]} {enter_cells[1]} {enter_cells[2]} |
| {enter_cells[3]} {enter_cells[4]} {enter_cells[5]} |
| {enter_cells[6]} {enter_cells[7]} {enter_cells[8]} |
---------'''
            print(cells)
    elif enter_coordinates == left_3:
        if enter_cells[0] != space:
            xo_counter -= 1
            print("This cell is occupied! Choose another one!")
        else:
            if xo_counter % 2 != 0:
                enter_cells[0] = 'X'
            else:
                enter_cells[0] = 'O'
            cells = f'''---------
| {enter_cells[0]} {enter_cells[1]} {enter_cells[2]} |
| {enter_cells[3]} {enter_cells[4]} {enter_cells[5]} |
| {enter_cells[6]} {enter_cells[7]} {enter_cells[8]} |
---------'''
            print(cells)
    elif enter_coordinates == middle_1:
        if enter_cells[7] != space:
            xo_counter -= 1
            print("This cell is occupied! Choose another one!")
        else:
            if xo_counter % 2 != 0:
                enter_cells[7] = 'X'
            else:
                enter_cells[7] = 'O'
            cells = f'''---------
| {enter_cells[0]} {enter_cells[1]} {enter_cells[2]} |
| {enter_cells[3]} {enter_cells[4]} {enter_cells[5]} |
| {enter_cells[6]} {enter_cells[7]} {enter_cells[8]} |
---------'''
            print(cells)
    elif enter_coordinates == middle_2:
        if enter_cells[4] != space:
            xo_counter -= 1
            print("This cell is occupied! Choose another one!")
        else:
            if xo_counter % 2 != 0:
                enter_cells[4] = 'X'
            else:
                enter_cells[4] = 'O'
            cells = f'''---------
| {enter_cells[0]} {enter_cells[1]} {enter_cells[2]} |
| {enter_cells[3]} {enter_cells[4]} {enter_cells[5]} |
| {enter_cells[6]} {enter_cells[7]} {enter_cells[8]} |
---------'''
            print(cells)
    elif enter_coordinates == middle_3:
        if enter_cells[1] != space:
            xo_counter -= 1
            print("This cell is occupied! Choose another one!")
        else:
            if xo_counter % 2 != 0:
                enter_cells[1] = 'X'
            else:
                enter_cells[1] = 'O'
            cells = f'''---------
| {enter_cells[0]} {enter_cells[1]} {enter_cells[2]} |
| {enter_cells[3]} {enter_cells[4]} {enter_cells[5]} |
| {enter_cells[6]} {enter_cells[7]} {enter_cells[8]} |
---------'''
            print(cells)
    elif enter_coordinates == right_1:
        if enter_cells[8] != space:
            xo_counter -= 1
            print("This cell is occupied! Choose another one!")
        else:
            if xo_counter % 2 != 0:
                enter_cells[8] = 'X'
            else:
                enter_cells[8] = 'O'
            cells = f'''---------
| {enter_cells[0]} {enter_cells[1]} {enter_cells[2]} |
| {enter_cells[3]} {enter_cells[4]} {enter_cells[5]} |
| {enter_cells[6]} {enter_cells[7]} {enter_cells[8]} |
---------'''
            print(cells)
    elif enter_coordinates == right_2:
        if enter_cells[5] != space:
            xo_counter -= 1
            print("This cell is occupied! Choose another one!")
        else:
            if xo_counter % 2 != 0:
                enter_cells[5] = 'X'
            else:
                enter_cells[5] = 'O'
            cells = f'''---------
| {enter_cells[0]} {enter_cells[1]} {enter_cells[2]} |
| {enter_cells[3]} {enter_cells[4]} {enter_cells[5]} |
| {enter_cells[6]} {enter_cells[7]} {enter_cells[8]} |
---------'''
            print(cells)
    elif enter_coordinates == right_3:
        if enter_cells[2] != space:
            xo_counter -= 1
            print("This cell is occupied! Choose another one!")
        else:
            if xo_counter % 2 != 0:
                enter_cells[2] = 'X'
            else:
                enter_cells[2] = 'O'
            cells = f'''--------
| {enter_cells[0]} {enter_cells[1]} {enter_cells[2]} |
| {enter_cells[3]} {enter_cells[4]} {enter_cells[5]} |
| {enter_cells[6]} {enter_cells[7]} {enter_cells[8]} |
---------'''
            print(cells)
