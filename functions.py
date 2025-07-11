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

import pandas as pd
import matplotlib.pyplot as plt
    
def plot_unknown_minerals(nome,colonna,riga):

    ''' 
        Voglio fare una funzione che mi permetta di plottare i minerali da classificare,
        dando in input LISTE:
        nome file(s)    -- es: ["S1_bkg_mapA_11x11.csv", "S1_mapA_11x11.csv", "S2_bkg_mapA_11x11.csv", "S2_mapA_11x11.csv"] !!DEV'ESSERE UN LISTA!!
        colonne di interesse    -- es: [0] / [0,1,2,3,4,5,6,7,8,9,10]   (as above) 
        riga di interesse    -- es: [0,1,2,3,4,5,6,7,8,9,10]    (as above)
        
        !! righe e colonne sono indicizzate da 0 a 10 !!

        se non hai i file dentro la stessa cartella della funzione, non basta il nome del file,
        devi mettere tutto il percorso, es: "/home/luca/Uni/VI/Data science/Progetto/prog_DS/S1_bkg_mapA_11x11.csv"

    '''


    for k in range(len(nome)):
        for i in colonna:
            for j in riga:
                df = pd.read_csv(nome[k])
                filtro = df[(df['colonna'] == i) & (df['riga'] == j)]
                plt.figure(figsize=(10, 6))
                plt.plot(filtro['x'].values, filtro['y'].values, marker='.', linestyle=None, color='blue')
                plt.xlabel("lunghezza d'onda [cm^-1]")
                plt.ylabel('Emissione')
                plt.title(f"Colonna {i+1}, Riga {j+1} - {nome[k].removesuffix('.csv')}")
                plt.grid(True)
                plt.show()