# -*- coding: utf-8 -*-
#
#  OPENCOORD.py
#  Versao de 25/06/2021 
#
#  Copyright 2020 Mansur <Mansur@DESKTOP-C68E9EI>



from sys import float_repr_style

from numpy import sqrt


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
    plt.ylim(0.4, 1000)

    plt.show()

    return 0

#_______________________________________________________________________#



def main(args):
    print("OPENCOORD - v 1.0")
    with open("DATA.dat", encoding="utf8") as file:
        data = file.readlines()
    
    OUT = open("RELAORIO.OUT", 'w')
    OUT.writelines("#______OPENCOORD V1.0_________\n")

    #_____DADOS DO SISTEMA_____________
    Sbase = float(data[9])       #MVA
    Vbase_BT = float(data[10])   #kV
    Vbase_AT = float(data[11])   #kV
    Zbase_BT = pow(Vbase_BT,2)/Sbase   #Ohm
    Zbase_AT = pow(Vbase_AT,2)/Sbase   #Ohm
   

    #_______________DADOS DO TRAFO_________
    Xt = float(data[14]) #(%)
    St = float(data[13]) #MVA
    Conexao = data[15] #SRT
    Fuse = float(data[16])
    K = float(data[17])
    Inom_trafo_MT = (1000*St)/(Vbase_AT*sqrt(3))
    inrush = K*Inom_trafo_MT
    OUT.writelines("#____DADOS DO TRAFO___\n")
    OUT.writelines("    I nominal AT: "+str(Inom_trafo_MT) + " A\n")
    OUT.writelines("    I in-rush: " + str(inrush) + " A\n")
    OUT.writelines("    X (%): "+str(Xt))
    



    

    #gerando curva IEC NI NO 1
    I_1, T_1 = IEC_NI(260,1200,0.2)
    I_2, T_2 = IEC_MI(260,1200,0.2)

    #PLOTAGEM
    PLOTER(I_1,T_1,"Curva A","RELES DE FASE")
    PLOTER(I_2,T_2,"Curva B", "RELES DE NEUTRO")

    OUT.close()
    file.close()
    return 0

if __name__ == '__main__':
    import sys
    import time
    import numpy as np
    import matplotlib.pyplot as plt
    sys.exit(main(sys.argv))