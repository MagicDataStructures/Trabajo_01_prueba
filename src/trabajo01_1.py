
class Pawn:
    def __init__(self, color):
        self.color = color;

    def __str__(self):
        if self.color == 0:
            return '??';
        else:
            return '?';

class Rook:
    def __init__(self, color):
        self.color = color;

    def __str__(self):
        if self.color == 0:
            return '?';
        else:
            return '?';

class Knight:
    def __init__(self, color):
        self.color = color;

    def __str__(self):
        if self.color == 0:
            return '?';
        else:
            return '?';

class Bishop:
    def __init__(self, color):
        self.color = color;

    def __str__(self):
        if self.color == 0:
            return '?';
        else:
            return '?';

class Queen:
    def __init__(self, color):
        self.color = color;

    def __str__(self):
        if self.color == 0:
            return '?';
        else:
            return '?';

class King:
    def __init__(self, color):
        self.color = color;

    def __str__(self):
        if self.color == 0:
            return '?';
        else:
            return '?';

class ChessGame:

    def __init__(self, white_player, black_player):
        self.white_player = white_player;
        self.black_player = black_player;
        self.white_captured_pieces = [];
        self.black_captured_pieces = [];
        # init board
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      ]
        #init white pieces
        # zero represents color white
        for i in range(8):
            self.board[6][i] = Pawn(0);
        self.board[7][0] = Rook(0);
        self.board[7][1] = Knight(0);
        self.board[7][2] = Bishop(0);
        self.board[7][3] = Queen(0);
        self.board[7][4] = King(0);
        self.board[7][5] = Bishop(0);
        self.board[7][6] = Knight(0);
        self.board[7][7] = Rook(0);
        #init black pieces
        # One represents the color black, of course. lol
        for i in range(8):
            self.board[1][i] = Pawn(1);
        self.board[0][0] = Rook(1);
        self.board[0][1] = Knight(1);
        self.board[0][2] = Bishop(1);
        self.board[0][3] = Queen(1);
        self.board[0][4] = King(1);
        self.board[0][5] = Bishop(1);
        self.board[0][6] = Knight(1);
        self.board[0][7] = Rook(1);

    def move(self, from_1, from_2, to_1, to_2):
        #if the space is empty, we just move the piece
        if self.board[from_1][from_2] != 0:
            piece = self.board[from_1][from_2];
            if self.board[to_1][to_2] != 0:
                captured_piece = self.board[to_1][to_2];
                self.white_captured_pieces.append(captured_piece);
            self.board[to_1][to_2] = piece;
            self.board[from_1][from_2] = 0;

    def display_moves(self): #mostrar movimientos
        for i in self.board:
            print([str(item) for item in i]);

    def display_captured_pieces(self): #mostrar piezas capturadas
        pass;

    def undo(self): #Deshacer último movimiento
        pass;

    def add(self, mov_index): #agregar movimiento en cualquier lugar
        pass;

    def delete(self, mov_index): #Eliminar movimiento
        pass;

awesome = ChessGame('me', 'Magnus Carlsen');
switch = True;
notation = ['a', 'b', 'c', 'd','e','f','g','h'];
while switch:
    print('inserte la coordenada de la pieza que desea mover');
    coordenada_1 = str(input());
    first = int(notation.index(coordenada_1[0]));
    second = int(coordenada_1[1]);
    print('Genial. Ahora inserte la coordenada a la que deseas mover tu pieza');
    coordenada_2 = str(input());
    primero = int(notation.index(coordenada_2[0]));
    segundo = int(coordenada_2[1]);
    awesome.move((8-second), first, (8-segundo), primero);
    awesome.display_moves();
    print('quieres salir?');
    hey = str(input());
    if hey == 'si':
        break;

awesome.display_moves();
