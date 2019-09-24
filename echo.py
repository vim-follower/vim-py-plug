import vim

def sayHello():
    print("Hello Vim!")
    w = vim.current.window
    row, col = w.cursor
    print("row: {}, col: {}".format(row, col))
