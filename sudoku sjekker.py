def sudoku_grid_correct(sudoku: list):

    main_sjekk = True
    grid_list = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3),(6,6)]

    for i in range(9):
        a = row_correct(sudoku,i)
        b = column_correct(sudoku,i)
        #print(a,"a")
        #print(b,"b")
        if a == False or b == False:
            main_sjekk = False
    
    for i in grid_list:
        row_no = i[0]
        column_no = i[1]
        c = block_correct(sudoku,row_no,column_no)
        #print(c,"c")

        if c == False:
            main_sjekk = False
    
    return main_sjekk

def block_correct(sudoku: list, row_no: int, column_no: int):     

    if row_no > 6 or column_no > 6:
      return False
    sjekk = True
    square = []

    for x in range(3):
        for i in range(3):
            
            a = sudoku[row_no+x][column_no+i]       
            square.append(a)

    sjekk = skekk(square)

    return sjekk

def skekk(ist:list):

  for i in range(1,10):
      a = ist.count(i)
      if a > 1:
        return False
  return True

def column_correct(sudoku: list, column_no: int):

    sjekk = True
    colum = []

    for i in sudoku:
        colum.append(i[column_no])
    
    sjekk = skekk(colum)
    return sjekk

def row_correct(sudoku: list, row_no: int):

    row = sudoku[row_no]
    
    sjekk = skekk(row)
    
    return sjekk

