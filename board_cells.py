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

def get_diag(bits:bitarray) -> bitarray:
    ind_row, row = get_row(bits)
    ind_col, col = get_col(bits)

    diagonal_1 = bitarray(64)
    diagonal_2 = bitarray(64)

    for i in range(8):
        
        if ord(ind_col)+i > 72 or ind_row+i > 8:
            break
        temp_col = columns[chr(ord(ind_col)+i)]
        temp_row =rows[ind_row+i]
        diagonal_1 |= (temp_col & temp_row)
    
    for i in range(8):
        if ord(ind_col)-i < 65 or ind_row-i < 1:
            break
        temp_col = columns[chr(ord(ind_col)-i)]
        temp_row = rows[ind_row-i]
        diagonal_1 |= (temp_col & temp_row)
    
    for i in range(8):
        
        if ord(ind_col)+i > 72 or ind_row-i < 1:
            break
        temp_col = columns[chr(ord(ind_col)+i)]
        temp_row =rows[ind_row-i]
        diagonal_2 |= (temp_col & temp_row)
    
    for i in range(8):
        if ord(ind_col)-i < 65 or ind_row+i > 8:
            break
        temp_col = columns[chr(ord(ind_col)-i)]
        temp_row = rows[ind_row+i]
        diagonal_2 |= (temp_col & temp_row)

    return diagonal_1, diagonal_2


diagonals = dict()
for key,cell in cells.items():
    diagonals[key] = get_diag( cell )