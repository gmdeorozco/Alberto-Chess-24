from bitarray import bitarray

column_a = bitarray(64)
column_b = bitarray(64)
column_c = bitarray(64)
column_d = bitarray(64)
column_e = bitarray(64)
column_f = bitarray(64)
column_g = bitarray(64)
column_h = bitarray(64)

columns = {'A': column_a,
           'B': column_b, 
           'C':column_c, 
           'D':column_d, 
           'E':column_e, 
           'F': column_f,
           'G':column_g,
           'H':column_h,}

factor=0
for key in columns:
    for num in range(0,57,8):
        columns[key][factor + num] = True
    factor += 1

row_1 = bitarray(64)
row_2 = bitarray(64)
row_3 = bitarray(64)
row_4 = bitarray(64)
row_5 = bitarray(64)
row_6 = bitarray(64)
row_7 = bitarray(64)
row_8 = bitarray(64)

rows = {
    1 : row_1,
    2 : row_2,
    3 : row_3,
    4 : row_4,
    5 : row_5,
    6 : row_6,
    7 : row_7,
    8 : row_8,

}
factor=0
for key in rows:
    for num in range(8):
        rows[key][factor + num] = True
    factor += 8


cells = dict()
for k_row in rows:
    for k_col in columns:
        cells[k_col+str(k_row)] = columns[k_col] & rows[k_row]

def get_row(bits:bitarray) -> bitarray:
    for index, row in rows.items():
        if bits & row == bits:
            return index, row

def get_col(bits:bitarray) -> bitarray:
    for index, col in columns.items():
        if bits & col == bits:
            return index, col


def add_9_to_diagonal(origin:bitarray, lst:list ):
    plus = origin >> 9
    if plus & column_a == plus:
        return
    if plus.any():
        lst.append(plus)
        add_9_to_diagonal(plus, lst)

def add_7_to_diagonal(origin:bitarray, lst:list ):
    plus = origin >> 7
    if plus & column_h == plus:
        return
    if plus.any():
        lst.append(plus)
        add_7_to_diagonal(plus, lst)

def sub_9_to_diagonal(origin:bitarray, lst:list ):
    minus = origin << 9
    if minus & column_h == minus:
        return
    if minus.any():
        lst.append(minus)
        sub_9_to_diagonal(minus, lst)
  
def sub_7_to_diagonal(origin:bitarray, lst:list ):
    minus = origin << 7
    if minus & column_a == minus:
        return
    if minus.any():
        lst.append(minus)
        sub_7_to_diagonal(minus, lst)
        
def calculate_diag() -> bitarray:
    result = dict()
    for a in range(64):
        
        origin = bitarray(64)
        origin[a] = True
        
        diag_1 = list()
        diag_2 = list()
        
        add_9_to_diagonal(origin=origin,lst=diag_1)
        sub_9_to_diagonal(origin=origin,lst=diag_1)
        
        add_7_to_diagonal(origin=origin,lst=diag_2)
        sub_7_to_diagonal(origin=origin,lst=diag_2)
        
        diagonal_1 = bitarray(64)
        for bit in diag_1:
            diagonal_1 |= bit
            
        diagonal_2 = bitarray(64)
        for bit in diag_2:
            diagonal_2 |= bit
        
        result[a] = ( diagonal_1, diagonal_2 )

    return result


diagonals = calculate_diag()

def get_diag(bits:bitarray):
    index = bits.index(True)
    #print(diagonals)
    return diagonals[index]

center_1 = ( cells['D4'] | cells['D5'] | cells['E4'] | cells['E5']  | cells['C4'] | cells['F4']
    | cells['C5'] | cells['F5'])
border_1 = column_a | column_h | row_1 | row_8

border_2 = (column_b | column_g | row_2 | row_7 ) &~ center_1  &~ border_1 

full = bitarray(64)
full.setall(True)

center_2 = (
    cells['C3'] | cells['D3'] | cells['E3'] | cells['F3']
    
    | cells['C6'] | cells['D6'] | cells['E6'] | cells['F6']
            )