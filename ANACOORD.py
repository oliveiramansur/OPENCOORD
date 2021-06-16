# -*- coding: utf-8 -*-
#
#  PYCOORD.py
#  
#  Copyright 2020 Mansur <Mansur@DESKTOP-C68E9EI>

def IEC_NI(tape, inst, TDS):
    Iarray = np.linspace((tape+0.0001), inst, 1000)
    #Tarray = (0.14 * TDS) / (((Iarray / tape) ^ 0.02) - 1)
    t1 = ((Iarray / tape)) 
    t2 = np.power(t1, 0.02)
    t3 = t2 - 1
    t4 = (0.14*TDS)/t3
    return (Iarray, t4)

def IEC_MI(tape, inst, TDS):
    Iarray = np.linspace((tape+0.0001), inst, 1000)
    #Tarray = (13.5 * TDS) / (((Iarray / tape) ^ 1) - 1)
    t1 = ((Iarray / tape)) 
    t2 = np.power(t1, 1)
    t3 = t2 - 1
    t4 = (13.5*TDS)/t3
    return (Iarray, t4)

def IEC_EI(tape, inst, TDS):
    Iarray = np.linspace((tape+0.0001), inst, 1000)
    #Tarray = (80 * TDS) / (((Iarray / tape) ^2) - 1)
    t1 = ((Iarray / tape)) 
    t2 = np.power(t1, 2)
    t3 = t2 - 1
    t4 = (80*TDS)/t3
    return (Iarray, t4)

def PLOTER(corrente1,tempo1,legenda,titulo):
    #PLOTAGEM
    plt.title(titulo)
    plt.ylabel("Tempo (segundos)")
    plt.xlabel("Corrente (A)")
    plt.loglog(corrente1,tempo1, label=legenda)
    plt.legend()
    plt.grid(True, which="both", ls="-")
    
    plt.xlim(100, 4000)
    plt.ylim(0.1, 300)

    plt.show()

    return 0

def main(args):
    print("PYCOORD - v 0.1")
    #_____DADOS DO SISTEMA_____________
    Sbase = 100 #MVA
    Vbase = 13.8 #kV
    #_____INSERIR DADOS DO TRAFO_________
    Xt = 6 # %
    St = 5 # MVA
    




    #gerando curva IEC NI NO 1
    I_1, T_1 = IEC_NI(260,1200,0.2)
    I_2, T_2 = IEC_MI(260,1200,0.2)

    #PLOTAGEM
    PLOTER(I_1,T_1,"Curva A","RELES DE FASE")
    PLOTER(I_2,T_2,"Curva B", "RELES DE NEUTRO")
    
    return 0

if __name__ == '__main__':
    import sys
    import time
    import numpy as np
    import matplotlib.pyplot as plt
    sys.exit(main(sys.argv))