class Minerale:
    def __init__(self, nome, x_vals, y_vals):
        self.nome = nome
        self.x = x_vals
        self.y = y_vals

class Minerali_da_riconoscere:
    def __init__(self, nome, x_vals, y_vals,num_riga, num_colonna):
        self.nome = nome
        self.riga = num_riga
        self.colonna = num_colonna
        self.x = x_vals
        self.y = y_vals