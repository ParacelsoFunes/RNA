from math import gamma
import numpy as np
import random


recompensas_tamano_efecto = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas2 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas3 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1,],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas4 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,-1,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas5 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas6 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas7 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas8 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,-1,-1],[0,-1,0,-1,-1],[0,-1,-1,-1,-1],[0,-1,-1,-1,-1],[100,-1,-1,-1,-1],[-1,-1,0,-1,100],[-1,-1,0,-1,-1]])
recompensas9 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,-1,-1],[0,-1,0,-1,1],[0,-1,-1,0,-1],[0,-1,-1,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas10 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas11 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas12 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,-1,0,-1,-1],[-1,-1,0,-1,-1]])
recompensas13 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,-1,-1],[0,-1,0,-1,-1],[0,-1,0,-1,-1],[0,-1,-1,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas14 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,-1,0,-1],[0,-1,-1,-1,-1],[0,-1,-1,-1,-1],[0,-1,-1,-1,-1],[0,-1,-1,-1,-1],[100,-1,-1,-1,-1],[-1,-1,-1,-1,100],[-1,-1,0,-1,-1]])
recompensas15 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1,],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas16 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas17 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas18 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas19 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,-1,-1],[0,-1,0,-1,-1],[0,-1,-1,0,-1],[0,-1,-1,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,-1,-1,-1]])
recompensas20 = np.array([[-1,0,-1,-1,-1],[-1,0,-1,-1,-1],[-1,0,-1,0,-1],[-1,-1,-1,0,-1],[-1,-1,0,0,-1],[-1,-1,0,100,-1],[-1,-1,-1,0,-1],[-1,-1,0,0,-1],[-1,-1,0,-1,-1],[0,-1,0,-1,-1],[0,-1,-1,-1,-1],[0,-1,-1,-1,-1],[100,-1,-1,-1,-1],[-1,-1,0,-1,100],[-1,-1,0,-1,-1]])
recompensas21 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,-1,-1],[0,-1,0,-1,-1],[0,-1,-1,0,-1],[0,-1,-1,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas22 = np.array([[-1,0,-1,0,-1,],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas23 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas24 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas25 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas26 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas27 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,3,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,1,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas28 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,-1,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,-1,-1],[0,-1,0,-1,-1],[0,-1,-1,0,-1],[0,-1,-1,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas29 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,-1,-1],[0,-1,0,-1,-1],[0,-1,-1,0,-1],[0,-1,-1,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas30 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,-1,-1,-1]])
recompensas31 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas32 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas33 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas34 = np.array([[-1,-1,-1,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,-1,100,-1],[0,-1,-1,-1,-1],[0,-1,-1,-1,-1],[0,-1,-1,-1,-1],[0,-1,-1,-1,-1],[0,-1,-1,-1,-1],[0,-1,-1,-1,-1],[100,-1,-1,-1,-1],[-1,-1,0,-1,100],[-1,-1,0,-1,-1]])
recompensas35 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas36 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,-1,-1],[-1,0,0,-1,-1],[-1,0,-1,-1,-1],[-1,0,-1,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,-1,-1,100],[-1,-1,0,-1,-1]])
recompensas37 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas38 = np.array([[-1,0,-1,-1,-1],[-1,0,-1,-1,-1],[-1,0,-1,0,-1],[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[-1,-1,-1,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])# revisar el tercer valor desde la matriz uno hasta aqui.
recompensas39 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,-1,-1],[0,-1,0,-1,-1],[0,-1,-1,0,-1],[0,-1,-1,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas40 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas41 = np.array([[-1,-1,-1,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,-1,-1],[0,-1,-1,-1,-1],[0,-1,-1,-1,-1],[0,-1,-1,-1,-1],[0,-1,-1,0,-1],[0,-1,-1,0,-1],[100,-1,0,-1,-1],[-1,-1,0,-1,-1]])
recompensas42 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas43 = np.array([[-1,0,-1,0,-1,],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas44 = np.array([[-1,0,-1,-1,-1],[-1,0,-1,-1,-1],[-1,0,-1,0,-1],[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,-1,0,100,-1],[-1,-1,-1,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,-1,-1],[0,-1,0,-1,-1],[100,-1,-1,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas45 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,-1,-1],[0,-1,0,-1,-1],[0,-1,-1,0,-1,],[0,-1,-1,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas46 = np.array([[-1,0,-1,-1,-1],[-1,0,-1,-1,-1],[-1,0,-1,0,-1],[-1,-1,-1,0,-1],[-1,-1,0,0,-1],[-1,-1,0,100,-1],[-1,-1,-1,0,-1],[-1,-1,0,0,-1],[-1,-1,0,-1,-1],[0,-1,0,-1,-1],[0,-1,-1,0,-1],[0,-1,-1,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,-1,-1,-1]])
recompensas47 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,-1,-1],[0,-1,0,-1,-1],[0,-1,-1,0,-1],[0,-1,-1,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,-1,-1,-1]])
recompensas48 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,-1,1],[0,-1,0,-1,-1],[0,-1,-1,0,-1],[0,-1,-1,0,-1],[100,-1,0,-1,-1,],[-1,0,0,-1,100]]),[-1,-1,0,-1,-1]
recompensas49 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,-1,-1],[-1,-1,0,-1,-1],[-1,-1,-1,-1,-1],[-1,0,-1,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,-1,-1],[-1,-1,0,-1,-1],[-1,-1,-1,0,-1],[-1,-1,-1,0,-1],[100,-1,0,-1,-1],[-1,0,-1,-1,100],[-1,-1,0,-1,-1]])
recompensas50 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas51 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,-1,-1],[0,-1,0,-1,-1],[0,-1,-1,0,-1],[0,-1,-1,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas52 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
recompensas53 = np.array([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100],[-1,-1,0,-1,-1]])
matriz_recompensas_agrupadas_TA = [recompensas_tamano_efecto,recompensas2,recompensas3,recompensas4,recompensas5,recompensas6,recompensas7,recompensas8,recompensas9,recompensas10,recompensas11,recompensas12,recompensas13,recompensas14,recompensas15,recompensas16,recompensas17,recompensas18,recompensas19,recompensas20,recompensas21,recompensas22,recompensas23,recompensas24,recompensas25,recompensas26,recompensas27,recompensas28,recompensas29,recompensas30,recompensas31,recompensas32,recompensas33,recompensas34,recompensas35,recompensas36,recompensas37,recompensas38,recompensas39,recompensas40,recompensas41,recompensas42,recompensas43,recompensas44,recompensas45,recompensas46,recompensas47,recompensas48,recompensas49,recompensas50,recompensas51,recompensas52,recompensas53]

'''Recompensa_resto_de_investigacion = np.array([[-1,0,-1,0,-1],[-1,0,0,0-1],[-1,0,0,0,-1],[-1,0,0,0-1],[ -1,0,0,0-1],[ -1,0,0,0-1],[ -1,0,0,0-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[ 0,-1,0,0,-1],[ 0,-1,0,0,-1],[ 0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100]])
Recompensa2 = np.array ([[-1,0,-1,0,-1],[-1,0,0,0-1],[-1,0,0,-1,-1],[-1,0,0,-1,-1],[-1,0,-1,-1-1],[-1,0,-1,-1,-1],[ -1,0,-1,-1,-1],[-1,0,-1,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,-1,-1,100]])
Recompensa3 = np.array ([[-1,-1,-1,0-1],[-1,-1,0,0-1],[ -1,-1,0,0-1],[-1,0,0,-1,-1],[ -1,0,0,-1,-1],[-1,-1,-1,-1,-1],[-1,0,-1,-1,-1],[-1,-1,-1,100,-1],[ 0,-1,-1,-1,-1],[0,-1,-1,0,-1],[0,-1,-1,0,-1],[ 0,-1,-1,0,-1],[-1,-1,0,-1,-1],[-1,-1,-1,0,-1],[-1,-1,-1,-1,-1],[-1,-1,0,-1,-1],[100,-1,-1,-1,-1],[-1,-1,-1,-1,100]])
Recompensa4 = np.array ([[-1,-1,-1,0,-1],[-1,-1,0,0,-1],[-1,0,0,-1,-1],[-1,-1,0,0,-1],[-1,-1,-1,0-1],[-1,0,0,0,-1],[-1,0,0,0-1],[-1,0,0,100,-1],[0,-1,-1,-1,-1],[0,-1,-1,0,-1],[0,-1,-1,-1,-1],[-1,-1,0,-1,-1],[0,-1,-1,0,-1],[ 0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100]])
Recompensa5 = np.array ([[-1,0,-1,-1,-1],[-1,0,0,0,-1],[-1,-1,-1,0,-1],[-1,-1,0,0,-1],[-1,0,0,0,-1],[ -1,0,0,0,-1],[ -1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[-1,-1,0,-1,-1],[0,-1,0,-1,-1],[0,-1,-1,0,-1],[ 0,-1,-1,0,-1],[0,-1,0,0,-1],[ 0,-1,0,0,-1],[ 0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100]])
Recompensa6 = np.array ([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,-1,0,0,-1],[-1,0,0,0,-1],[ -1,0,0,0,-1],[ -1,0,0,0,-1],[ -1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,-1,-1],[0,-1,0,0,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[ 0,-1,0,0,-1],[ 0,-1,0,0,-1],[ 0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100]])
Recompensa7 = np.array ([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,-1,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,-1,-1],[0,-1,0,0,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100]])
Recompensa8 = np. array ([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,-1,0,0,-1],[-1,0,0,0,-1],[ -1,0,0,0,-1],[ -1,0,0,0,-1],[ -1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[ 0,-1,0,0,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[ 0,-1,0,0,-1],[ 0,-1,0,0,-1],[ 0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100]])
Recompensa9 = np.array ([[-1,0,-1,0,-1],[ -1,0,-1,0,-1],[-1,0,0,0,-1],[ -1,0,0,0,-1],[ -1,0,0,0,-1],[ -1,0,0,0,-1],[ -1,0,0,0,-1],[-1,0,0,100,-1],[-1,-1,-1,0,-1],[0,-1,0,0,-1],[ 0,-1,0,0,-1],[ 0,-1,0,0,-1],[ 0,-1,0,0,-1],[ 0,-1,0,0,-1],[ 0,-1,0,0,-1],[ 0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100]])
Recompensa10 = np.array ([[-1,-1,-1,-1,-1],[-1,-1,-1,0,-1],[ -1,-1,-1,0,-1],[-1,0,0,-1,-1],[-1,0,0,-1,-1],[-1,0,-1,-1,-1],[-1,0,-1,-1,-1],[-1,0,-1,100,-1],[-1,-1,-1,-1,-1],[ -1,-1,-1,-1,-1],[0,-1,-1,0,-1],[0,-1,-1,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,-1,-1,100]])
Recompensa11 = np.array ([[-1,0,-1,-1,-1],[-1,0,-1,0-1],[-1,-1,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[ -1,0,0,0,-1],[-1,0,0,100,-1],[-1,-1,-1,0,-1],[-1,-1,0,-1,-1],[0,-1,0,0,-1],[0,-1-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[ 0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100]])
Recompensa12 = np.array ([[-1,0,-1,-1,-1],[-1,0,-1,0-1],[-1,-1,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[ -1,0,0,0,-1],[-1,0,0,100,-1],[-1,-1,-1,0,-1],[-1,-1,0,-1,-1],[0,-1,0,0,-1],[0,-1-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[ 0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100]])
Recompensa13 = np.array ([[-1,0,-1,-1,-1],[-1,0,-1,0-1],[-1,-1,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[ -1,0,0,0,-1],[-1,0,0,100,-1],[-1,-1,-1,0,-1],[-1,-1,0,-1,-1],[0,-1,0,0,-1],[0,-1-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[ 0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100]])
Recompensa14 = np.array ([[-1,0,-1,-1,-1],[-1,0,-1,0-1],[-1,-1,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[ -1,0,0,0,-1],[-1,0,0,100,-1],[-1,-1,-1,0,-1],[-1,-1,0,-1,-1],[0,-1,0,0,-1],[0,-1-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[ 0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100]])
Recompensa15 = np.array ([[-1,0,-1,-1,-1],[-1,0,-1,0-1],[-1,-1,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[ -1,0,0,0,-1],[-1,0,0,100,-1],[-1,-1,-1,0,-1],[-1,-1,0,-1,-1],[0,-1,0,0,-1],[0,-1-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[ 0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100]])
Recompensa16 = np.array ([[-1,0,-1,0,-1],[-1,0,0,0,-1],[ -1,0,0,0,-1],[ -1,0,0,0,-1],[ -1,0,0,0,-1],[ -1,0,0,0,-1],[ -1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,-1,-1],[0,-1,0,0,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[ 0,-1,0,0,-1],[ 0,-1,0,0,-1],[ 0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100]])
Recompensa17 = np.array ([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,-1,-1],[ -1,-1,0,-1,-1],[-1,0,-1,-1,-1],[-1,0,0,0,-1],[-1,0,-1,100,-1],[0,-1,-1,0,-1],[0,-1,0,-1,-1],[ 0,-1,0,-1,-1],[0,-1,-1,-1,-1],[-1,-1,-1,0,-1],[-1,-1,0,0,-1],[ -1,-1,0,0,-1],[-1,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,-1,-1,100]])
Recompensa18 = np.array ([[-1,-1,-1,0,-1],[-1,-1,0,0,-1],[-1,0,0,0,-1],[ -1,0,0,0,-1],[ -1,0,0,0,-1],[ -1,0,0,0,-1],[ -1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,-1,-1],[0,-1,-1,0,-1],[ 0,-1,-1,0,-1],[0,-1,0,0,-1],[ 0,-1,0,0,-1],[ 0,-1,0,0,-1],[ 0,-1,0,0,-1],[ 0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100]])
Recompensa19 = np.array ([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,-1,0,0,-1],[ -1,0,0,0,-1],[ -1,0,0,0,-1],[-1,-1,0,0,-1],[ -1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[ 0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,-1,0,-1],[0,-1,0,-1,-1],[0,-1,0,0,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100]])
Recompensa20 = np.array ([[-1,0,-1,-1,-1],[-1,0,0,0,-1],[-1,0,-1,-1,-1],[-1,0,0,0,-1],[-1,0,-1,0,-1],[-1,0,0,0,-1],[ -1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[-1,-1,0,0,-1],[0,-1,0,0,-1],[-1,-1,0,0,-1],[0,-1,0,0,-1],[ 0,-1,0,0,-1],[ 0,-1,0,0,-1],[ 0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100]])
Recompensa21 = np.array ([[-1,-1,-1,-1,-1],[-1,-1,-1,0,-1],[ -1,-1,-1,0,-1],[-1,0,0,-1,-1],[ -1,0,0,-1,-1],[-1,0,-1,-1,-1],[ -1,0,-1,-1,-1],[-1,-1,-1,100,-1],[-1,-1,-1,-1,-1],[ -1,-1,-1,-1,-1],[0,-1,-1,0,-1],[ 0,-1,-1,0,-1],[-1,-1,0,0,-1],[ -1,-1,0,0,-1],[-1,-1,0,-1,-1],[ -1,-1,0,-1,-1],[100,-1,-1,-1,-1],[-1,-1,-1,-1,100]])
Recompensa22 = np.array ([[-1,0,-1,0,-1],[-1,0,0,0,-1],[ -1,0,0,0,-1],[-1,0,0,-1,-1],[ -1,0,0,-1,-1],[-1,0,-1,-1,-1],[ -1,0,-1,-1,-1],[-1,0,-1,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[ 0,-1,0,0,-1],[0,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,-1,-1,100]])
Recompensa23 = np.array ([[-1,0,-1,-1,-1],[-1,0,0,0,-1],[-1,-1,-1,0,-1],[-1,0,0,-1,-1],[ -1,0,0,-1,-1],[-1,0,-1,-1,-1],[-1,0,-1,-1,-1],[-1,0,-1,100,-1],[0,-1,-1,0,-1],[-1,-1,0,-1,-1],[0,-1,0,0,-1],[0,-1,-1,0,-1],[-1,-1,-1,0,-1],[-1,-1,0,0,-1],[ -1,-1,0,0,-1],[ -1,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,-1,-1,100]])
Recompensa24 = np.array ([[-1,0,-1,0,-1],[-1,0,-1,-1,-1],[-1,0,0,0,-1],[-1,0,-1,-1,1],[-1,0,0,-1,-1],[-1,-1,-1,-1,-1],[-1,0,-1,-1,-1],[-1,0,-1,100,-1],[-1,-1,-1,-0,-1],[0,-1,0,0,-1],[-1,-1,0,0,-1],[0,-1,0,0,-1],[-1,-1,0,-1,-1],[-1,-1,0,0,-1],[-1,-1,-1,0,-1],[-1,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,-1,-1,100]])
Recompensa25 = np.array ([[-1,0,-1,-1,-1],[-1,0,-1,0,-1],[ -1,0,-1,0,-1],[-1,-1,0,-1,-1],[-1,0,0,-1,-1],[-1,0,-1,-1,-1],[ -1,0,-1,-1,-1],[-1,0,0,100,-1],[-1,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,-1,-1,-1],[0,-1,-1,0,-1],[-1,-1,-1,0,-1],[-1,-1,0,0,-1],[ -1,-1,0,0,-1],[-1,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,-1,-1,100]])
Recompensa26 = np.array ([[-1,0,-1,-1,-1],[-1,0,-1,0,-1],[-1,-1,-1,0,-1],[-1,-1,0,-1,-1],[-1,0,0,-1,-1],[-1,0,-1,-1,-1],[ -1,0,-1,-1,-1],[-1,0,-1,100,-1],[-1,-1,-1,0,-1],[-1,-1,0,-1,-1],[0,-1,0,-1,-1],[0,-1,-1,0,-1],[-1,-1,-1,0,-1],[-1,-1,0,0,-1],[ -1,-1,0,0,-1],[ -1,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,-1,-1,100]])
Recompensa27 = np.array ([[-1,0,-1,-1,-1],[-1,0,0,0,-1],[-1,0,-1,0,-1],[-1,-1,0,-1,-1],[-1,0,0,-1,-1],[-1,0,-1,-1,-1],[ -1,0,-1,-1,-1],[-1,0,-1,100,-1],[0,-1,-1,0,-1],[-1,-1,0,0,-1],[0,-1,0,-1,-1	],[0,-1,0,0,-1],[-1,-1,-1,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[ -1,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,-1,-1,100]])
Recompensa28 = np.array ([[-1,0,-1,-1,-1],[-1,-1,-1,0,-1],[-1,0,-1,0,-1],[-1,-1,0,0,-1],[-1,0,0,0,-1],[ -1,0,0,0,-1],[ -1,0,0,0,-1],[-1,0,0,100,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,0,-1],[0,-1,-1,-1,-1],[0,-1,0,0,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[ 0,-1,0,0,-1],[ 0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100]])
Recompensa29 = np.array ([[-1,-1,-1,-1,-1],[-1,-1,-1,0,-1],[-1,0,-1,-1,-1],[-1,-1,0,0,-1],[-1,0,-1,0,-1],[-1,0,0,0,-1],[ -1,0,0,0,-1],[ -1,0,0,100,-1],[ -1,-1,-1,-1,-1],[ -1,-1,-1,0,-1],[ 0,-1,-1,-1,-1],[ -1,-1,0,0,-1],[ 0,-1,-1,0,-1],[0,-1,0,0,-1],[ 0,-1,0,0,-1],[ 0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100]])
Recompensa30 = np.array ([[-1,-1,-1,0,-1],[-1,-1,0,0,-1],[ -1,-1,0,0,-1],[-1,-1,0,-1,-1],[-1,0,0,-1,-1],[-1,0,-1,-1,-1],[ -1,0,-1,-1,-1],[-1,0,-1,100,-1],[0,-1,-1,-1,-1],[ 0,-1,-1,-1,-1],[ 0,-1,-1,-1,-1],[0,-1,-1,0,-1],[-1,-1,-1,0,-1],[-1,-1,0,0,-1],[ -1,-1,0,0,-1],[ -1,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,-1,-1,100]])
Recompensa31 = np.array ([[-1,0,-1,-1,-1],[-1,0,-1,0,-1],[-1,-1,-1,0,-1],[-1,-1,0,0,-1],[-1,0,0,0,-1],[ -1,0,0,0,-1],[ -1,0,0,0,-1],[-1,0,0,100,-1],[-1,-1,-1,0,-1],[-1,-1,0,0,-1],[0,-1,0,-1,-1],[0,-1,0,0,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[ 0,-1,0,0,-1],[ 0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100]])
Recompensa32 = np.array ([[-1,-1,-1,-1,-1],[-1,-1,0,0,-1],[-1,-1,-1,0,-1],[-1,-1,0,-1,-1],[-1,0,0,-1,-1],[-1,0,-1,-1,-1],[ -1,0,-1,-1,-1],[-1,0,-1,100,-1],[0,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[ 0,-1,-1,-1,-1],[0,-1,-1,0,-1],[-1,-1,-1,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[ -1,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,-1,-1,100]])
Recompensa33 = np.array ([[-1,-1,-1,-1,-1],[-1,-1,0,0,-1],[-1,-1,-1,0,-1],[-1,-1,0,0,-1],[-1,0,0,0,-1],[ -1,0,0,0,-1],[ -1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[ 0,-1,-1,-1,-1],[0,-1,-1,0,-1],[ 0,-1,-1,0,-1],[0,-1,0,0,-1],[ 0,-1,0,0,-1],[ 0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100]])
Recompensa34 = np.array ([[-1,0,-1,-1,-1],[-1,0,0,0,-1],[-1,-1,-1,0,-1],[-1,0,0,-1,-1],[ -1,0,0,-1,-1],[-1,0,-1,-1,-1],[-1,0,-1,-1,-1],[-1,0,-1,100,-1],[0,-1,-1,0,-1],[-1,-1,0,-1,-1],[0,-1,0,0,-1],[0,-1,-1,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[ -1,-1,0,0,-1],[ -1,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,-1,-1,100]])
Recompensa35 = np.array ([[-1,-1,-1,0,-1],[ -1,-1,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,-1,-1],[ -1,0,0,-1,-1],[-1,0,-1,-1,-1],[ -1,0,-1,-1,-1],[-1,-1,-1,100,-1],[-1,-1,-1,-1,-1],[0,-1,-1,0,-1],[ 0,-1,-1,0,-1],[0,-1,0,0,-1],[-1,-1,0,0,-1],[ -1,-1,0,0,-1],[-1,-1,0,-1,-1],[ -1,-1,0,-1,-1],[100,-1,-1,-1,-1],[-1,-1,-1,-1,100]])
Recompensa36 = np.array ([[-1,0,-1,-1,-1],[ -1,0,-1,-1,-1],[-1,0,-1,0,-1],[-1,-1,-1,-1,-1],[ -1,-1,-1,-1,-1],[ -1,-1,-1,-1,-1],[ -1,-1,-1,-1,-1],[-1,0,-1,100,-1],[-1,-1,-1,0,-1],[-1,-1,0,0,-1],[-1,-1,0,-1,-1],[-1,-1,-1,0,-1],[ -1,-1,-1,-1,-1],[ -1,-1,-1,-1,-1],[ -1,-1,-1,0,-1],[-1,-1,-1,0,-1],[100,-1,0,-1,-1],[-1,0,-1,-1,100]])
Recompensa37 = np.array ([[-1,0,-1,0,-1],[ -1,0,-1,0,-1],[-1,0,0,-1,-1],[ -1,0,0,-1,-1],[-1,0,-1,-1,-1],[ -1,0,-1,-1,-1],[ -1,0,-1,-1,-1],[-1,0,-1,100,-1],[ -1,-1,-1,0,-1],[0,-1,0,0,-1],[ 0,-1,0,0,-1],[-1,-1,0,0,-1],[ -1,-1,0,0,-1],[ -1,-1,0,0,-1],[ -1,-1,0,0,-1],[ -1,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100]])
Recompensa38 = np.array ([[-1,-1,-1,0,-1],[-1,-1,0,0,-1],[ -1,0,0,-1,-1],[-1,-1,0,-1,-1],[-1,0,0,-1,-1],[-1,0,-1,-1,-1],[ -1,0,-1,-1,-1],[-1,0,-1,100,-1],[0,-1,-1,-1,-1],[0,-1,-1,0,-1],[0,-1,-1,-1,-1],[0,-1,0,0,-1],[-1,-1,-1,0,-1],[-1,-1,0,0,-1],[ -1,-1,0,0,-1],[ -1,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,-1,-1,100]])
Recompensa39 = np.array ([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,-1,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[ -1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,-1,-1],[0,-1,0,0,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[ 0,-1,0,0,-1],[ 0,-1,0,0,-1],[ 0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100]])
Recompensa40 = np.array ([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,-1,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[1,0,0,100,-1],[ 0,-1,-1,0,-1],[0,-1,0,-1,-1],[0,-1,0,0,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100]])
Recompensa41 = np.array ([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,-1,-1],[-1,-1,0,-1,-1],[-1,0,-1,-1,-1],[-1,0,-1,-1,-1],[-1,0,-1,-1,-1],[-1,0,-1,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,-1,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,-1,-1,100]])
Recompensa42 = np.array ([[-1,0,-1,0,-1],[-1,0,-1,0,-1],[-1,-1,0,0,-1],[-1,-1,0,-1,-1],[-1,0,0,-1,-1],[-1,0,-1,-1,-1],[-1,0,-1,-1,-1],[-1,0,-1,100,-1],[-1,-1,-1,0,-1],[0,-1,0,-1,-1],[0,-1,0,-1,-1],[0,-1,-1,0,-1],[-1,-1,-1,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,-1,-1,100]])
Recompensa43 = np.array ([[-1,0,-1,-1,-1],[-1,0,0,0,-1],[-1,-1,-1,0,-1],[-1,0,0,-1,-1],[-1,0,0,-1,-1],[-1,0,-1,-1,-1],[-1,0,-1,-1,-1],[-1,-1,-1,100,-1],[0,-1,-1,0,-1],[-1,-1,0,-1,-1],[0,-1,0,0,-1],[0,-1,-1,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,-1,-1],[-1,-1,0,0,-1],[100,-1,-1,-1,-1],[-1,0,-1,-1,100]])
Recompensa44 = np.array ([[-1,0,-1,0,-1],[-1,0,0,-1,-1],[-1,0,0,0,-1],[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[-1,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100]])
Recompensa45 = np.array ([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,-1,-1],[-1,0,0,-1,-1],[-1,0,-1,-1,-1],[-1,0,-1,-1,-1],[-1,0,-1,-1,-1],[-1,0,-1,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,-1,-1,100]])
Recompensa46 = np.array ([[-1,0,-1,-1,-1],[-1,0,0,0,-1],[-1,-1,-1,0,-1],[-1,-1,0,-1,-1],[-1,0,0,-1,-1],[-1,0,-1,-1,-1],[-1,0,-1,-1,-1],[-1,-1,-1,100,-1],[0,-1,-1,0,-1],[-1,-1,0,-1,-1],[0,-1,0,-1,-1],[0,-1,-1,0,-1],[-1,-1,-1,0,-1],[-1,-1,0,0,-1],[-1,-1,0,-1,-1],[-1,-1,0,0,-1],[100,-1,-1,-1,-1],[-1,0,-1,-1,100]])
Recompensa47 = np.array ([[-1,0,-1,0,-1],[-1,0,0,-1,-1],[-1,-1,0,0,-1],[-1,-1,-1,0-1],[-1,-1,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,-1,-1],[-1,-1,0,-1,-1],[0,-1,-1,-1,-1],[0,-1,-1,0,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100]])
Recompensa48 = np.array ([[-1,0,-1,0,-1],[-1,0,-1,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[-1,-1,-1,0,-1],[0,-1,0,-1,-1],[0,-1,0,-1,-1],[0,-1,0,0,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100]])
Recompensa49 = np.array ([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100]])
Recompensa50 = np.array ([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,-1,-1],[-1,0,0,-1,-1],[-1,0,-1,-1,-1],[-1,0,-1,-1,-1],[-1,0,-1,100,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,-1,-1,100]])
Recompensa51 = np.array ([[-1,-1,-1,0,-1],[-1,-1,0,-1,-1],[-1,0,0,0,-1],[-1,0,-1,-1,-1],[-1,0,0,-1,-1],[-1,0,-1,-1,-1],[-1,0,-1,-1,-1],[-1,-1,-1,100,-1],[0,-1,-1,-1,-1],[0,-1,-1,0,-1],[-1,-1,-1,0,-1],[0,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,-1,-1],[-1,-1,0,0,-1],[100,-1,-1,-1,-1],[-1,0,-1,-1,100]])
Recompensa52 = np.array ([[-1,0,-1,-1,-1],[-1,0,-1,0,-1],[-1,-1,-1,0,-1],[-1,-1,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,-100,-1],[-1,-1,-1,0,-1],[-1,-1,0,-1,-1],[0,-1,0,-1,-1],[0,-1,-1,0,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100]])
Recompensa53 = np.array ([[-1,0,-1,0,-1],[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,-1,-1],[-1,0,-1,-1,-1],[-1,0,-1,-1,-1],[-1,-1,-1,100,-1],[-1,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,-1,-1],[-1,-1,0,-1,-1],[100,-1,-1,-1,-1],[-1,-1,-1,-1,100]])
Recompensa54 = np.array ([[-1,0,-1,0,-1],[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,0,0,-1,-1],[-1,0,0,-1,-1],[-1,0,-1,-1,-1],[-1,0,-1,-1,-1],[-1,0,-1,100,-1],[-1,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[-1,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,-1,-1,100]])
Recompensa55 = np.array ([[-1,0,-1,0,-1],[-1,0,0,0,-1],[-1,-1,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,0,-1],[-1,0,0,100,-1],[0,-1,-1,0,-1],[0,-1,0,-1,-1],[0,-1,0,0,-1],[0,-1,-1,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[0,-1,0,0,-1],[100,-1,0,-1,-1],[-1,0,0,-1,100]])
matriz_Recompensa_agrupadas_dos = [Recompensa_resto_de_investigacion,Recompensa2,Recompensa3,Recompensa4,Recompensa5,Recompensa6,Recompensa7,Recompensa8,Recompensa9,Recompensa10,Recompensa11,Recompensa12,Recompensa13,Recompensa14,Recompensa15,Recompensa16,Recompensa17,Recompensa18,Recompensa19,Recompensa20,Recompensa21,Recompensa22,Recompensa23,Recompensa24,Recompensa25,Recompensa26,Recompensa27,Recompensa28,Recompensa29,Recompensa30,Recompensa31,Recompensa32,Recompensa33,Recompensa34,Recompensa35,Recompensa36,Recompensa37,Recompensa38,Recompensa39,Recompensa40,Recompensa41,Recompensa42,Recompensa43,Recompensa44,Recompensa45,Recompensa46,Recompensa47,Recompensa48,Recompensa49,Recompensa50,Recompensa51,Recompensa52,Recompensa53,Recompensa54,Recompensa55]

def estado_de_inicio():
    return np.random.randint(0,14) '''



#Funcion nueva
def obtener_acciones_TA(estado_actual, matriz_recompensas_agrupadas_TA):
    acciones_disponibles_TA = []
    print("Matriz_de_recompensas_agrupadas", matriz_recompensas_agrupadas_TA)
    print("Longitud matrices matrices agrupadas",len(matriz_recompensas_agrupadas_TA))
    for i in range(len(matriz_recompensas_agrupadas_TA)):
        print("*********************")
        print("*********************")
        print("MATRIZ No. ", i, ": ")
        
        print(matriz_recompensas_agrupadas_TA[i])
        print("Estado Actual: ", estado_actual)

        for accion in enumerate(matriz_recompensas_agrupadas_TA[estado_actual]):
            if (accion[0] == estado_actual):
                print("Accion: ",accion)
                print("Indice:",accion[0])
                print("Contenido:",accion[1])
                print("Acciones disponibles del Estado Actual:",accion[1])
                print("Primer elemento de la accion: ", accion[1][0])
                if accion[1][0]!=-1: # si el contenido es -1

                    acciones_disponibles_TA.append(accion[0])# guarda el indice
                    print("Se actualizó acciones_disponibles")
                    
                    escoger_accion = random.choice(acciones_disponibles_TA)
                    print("Elecciones aleatoria de la accion de Tamaño del efecto",escoger_accion)
                    return escoger_accion


estado_actual_TA = np.random.randint (0,14) 
accion_TA = obtener_acciones_TA(estado_actual_TA,matriz_recompensas_agrupadas_TA)


for i in range(len(matriz_recompensas_agrupadas_TA)):
    print("No. Matriz cero: ", i)
    matriz_calidad_TA = np.zeros([14,5])
    print(matriz_calidad_TA)
    gamma = 0.8 







def tomar_accion_TA(estado_actual_TA, matriz_recompensas_agrupadas_TA, gamma):
    print("Estado actua TA: ", estado_actual_TA)
    print("Matriz recompensas TA: ", matriz_recompensas_agrupadas_TA)
    print("Gama: ", gamma)

    accion = obtener_acciones_TA(estado_actual_TA, matriz_recompensas_agrupadas_TA)
    print("Accion en tomar_accion_TA: ", accion)

    recompensa_actual = matriz_recompensas_agrupadas_TA[estado_actual_TA, accion]
    print("Recompensa_actual: ",  matriz_recompensas_agrupadas_TA[estado_actual_TA, accion])
    #for i in range(len(matriz_recompensas_agrupadas_TA)):
     #   recompensa_actual = matriz_recompensas_agrupadas_TA[estado_actual_TA, accion]
      #  print("Recompensa actual en tomar_accion_TA", recompensa_actual)

    '''
    print(" *******************************************: ")
    print(" INICIA MATRIZ Q: ")
    print(" *******************************************: ")
    print('recompensa actual: ',recompensa_actual)
   
    recompensa_nueva = max(matriz_calidad_TA[accion,])
    print('recompensa nueva: ',recompensa_nueva)


    estado_actualq = recompensa_actual+(gamma * recompensa_nueva)
    print('Estado actual Q: ',estado_actualq)
    
    print(" *******************************************: ")
    print(" ACTUALIZACIÓN DE MATRIZ Q: ")
    print(" *******************************************: ")
    matriz_calidad_TA[estado_actual_TA,accion] = estado_actualq
    print('Matriz de calidad',"\n",matriz_calidad_TA) 

    nuevo_estado_TA = accion
    print("NUEVO_ESTADO" , nuevo_estado_TA)
    if nuevo_estado_TA == 15:
        print('Objetivo alcanzado!!!!')
    else:
         print(f'Estado anterior: {estado_actual_TA} Nuevo estado: {nuevo_estado_TA}')
    return nuevo_estado_TA
    '''

   
    
tomar_accion_TA(estado_actual_TA,matriz_recompensas_agrupadas_TA,gamma)

















