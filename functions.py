import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
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

def plot_minerale(minerale, ax=None):
    ''' 
        Voglio fare una funzione che mi permetta di plottare i minerali tabulati,
        dando in input:
        numero minerale(i) [LISTA]   -- es: ["Nontronite"] / ["Nontronite","Albite",...] !!DEV'ESSERE UN LISTA!!
                                            o anche una stringa di int
        ax: oggetto matplotlib.axes.Axes su cui plottare (opzionale)
    '''
    file = "/home/luca/Uni/VI/Data science/Progetto/prog_DS/data_norm_csv/minerali_norm.csv"
    df = pd.read_csv(file)

    # Se i minerali non sono stringhe, interpreta come indici
    if not isinstance(minerale[0], str):
        nomi = np.unique(df['nome'].values)
        nomi = [nomi[j] for j in minerale]
    else:
        nomi = minerale

    # Se non è passato un ax, creane uno nuovo
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))
        show_plot = True
    else:
        show_plot = False  # evita plt.show() se lo gestisci fuori

    for nome in nomi:
        filtro = df[df['nome'] == nome]
        ax.plot(filtro['x'].values, filtro['y'].values, marker='.', linestyle='-', label=nome)

    ax.set_xlabel("lunghezza d'onda [cm^-1]")
    ax.set_ylabel("Emissione")
    ax.grid(True)
    ax.legend()
    ax.set_title("Spettri minerali selezionati")

    if show_plot:
        plt.show()

def plot_unknown_minerals(nome, colonna, riga, ax=None):
    
    ''' 
        Voglio fare una funzione che mi permetta di plottare i minerali da classificare,
        dando in input LISTE:
        nome file(s)    -- es: ["S1_bkg_mapA_11x11.csv", "S1_mapA_11x11.csv", "S2_bkg_mapA_11x11.csv", "S2_mapA_11x11.csv"] !!DEV'ESSERE UN LISTA!!
        colonne di interesse    -- es: [0] / [0,1,2,3,4,5,6,7,8,9,10]   (as above) 
        riga di interesse    -- es: [0,1,2,3,4,5,6,7,8,9,10]    (as above)
        
        !! righe e colonne sono indicizzate da 0 a 10 !!

        se non hai i file dentro la stessa cartella della funzione, non basta il nome del file,
        devi mettere tutto il percorso, es: "/home/luca/Uni/VI/Data science/Progetto/prog_DS/S1_bkg_mapA_11x11.csv"
        - ax: oggetto matplotlib.axes.Axes su cui plottare (opzionale)
    '''
    for k in range(len(nome)):
        df = pd.read_csv(nome[k])  # leggi file una sola volta per efficienza

        for i in colonna:
            for j in riga:
                filtro = df[(df['colonna'] == i) & (df['riga'] == j)]

                # Se non è passato un ax, crea nuova figura
                if ax is None:
                    fig, ax_local = plt.subplots(figsize=(10, 6))
                    show_plot = True
                else:
                    ax_local = ax
                    show_plot = False

                ax_local.plot(filtro['x'].values, filtro['y'].values, marker='.', linestyle='-', label=f"C{i+1}-R{j+1} [{os.path.basename(nome[k]).removesuffix('.csv')}]")
                ax_local.set_xlabel("lunghezza d'onda [cm^-1]")
                ax_local.set_ylabel("Emissione")
                ax_local.set_title(f"Colonna {i+1}, Riga {j+1} - {os.path.basename(nome[k]).removesuffix('.csv')}")
                ax_local.grid(True)
                ax_local.legend()
                if show_plot:
                    plt.show()