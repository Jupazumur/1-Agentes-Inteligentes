#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
tarea_1.py
------------

Revisa el archivo README.md con las instrucciones de la tarea.

"""
__author__ = 'Juan Pablo Zurita Murillo'

#import entornos_f
import entornos_o
from random import choice

class NueveCuartos(entornos_o.Entorno):
    """
    Clase para un entorno de nueve cuartos.

    El estado se define como (robot, s0, s1, s2, s3, s4, s5, s6, s7, s8)
    donde robot es una coordenada piso, cuarto.
    Piso y cuarto van de [0, 2]
    Hay tres pisos, tres cuartos en cada uno:
    s0-s2 - piso 0, 
    s3-s5 - piso 1, 
    s6-s8 - piso 2.
    Todos pueden estar sucios o limpios.

    Las acciones válidas en el entorno son ("ir_Derecha", "ir_Izquierda", "subir", "bajar" "limpiar", "nada").
    Solo se puede subir si el robot está en los primeros dos pisos. 
    Solo se puede bajar del segundo piso para arriba.

    Los sensores es una tupla (robot, limpio?)
    con la ubicación del robot y el estado de limpieza

    """
    def __init__(self, x0 = [[0,0]] + ["sucio"] * 9):
        """
        Por default inicialmente el robot está en piso 0, cuarto 0, y todos los cuartos
        están sucios

        """          
        self.x = x0[:]
        self.costo = 0

    def accion_legal(self, accion):
        """
        Indica si una acción es legal dentro de la grid 3x3

        """
        piso, cuarto = self.x[0] # self.x[0] es la parte que contiene las coordenadas

        if accion == "ir_Derecha":
            return cuarto < 2
        elif accion == "ir_Izquierda":
            return cuarto > 0
        elif accion == "subir":
            return piso < 2 and cuarto == 2
        elif accion == "bajar":
            return piso > 0 and cuarto == 0
        elif accion in ("limpiar", "nada"):
            return True
        return False
    
    def transicion(self, accion):
        """
        Lógica de transición entre estados

        """
        if not self.accion_legal(accion):
           #raise ValueError("La acción no es legal para este estado")
           return
        
        #robot, a, b = self.x
        piso, cuarto = self.x[0]

        #if accion != "nada" or a == "sucio" or b == "sucio":
        #    self.costo += 1
        # ^ Aca todos tienen el mismo costo

        if accion == "limpiar":
            #self.x[" AB".find(self.x[0])] = "limpio"
            self.costo += 1
            self.x[1 + (3 * piso) + cuarto] = "limpio"

        #elif accion == "ir_A":
        elif accion == "ir_Derecha":
            self.costo += 2
            self.x[0][1] += 1

        #elif accion == "ir_B":
        elif accion == "ir_Izquierda":
            self.costo += 2
            self.x[0][1] -= 1

        elif accion == "subir":
            self.costo += 3
            self.x[0][0] += 1

        elif accion == "bajar":
            self.costo += 3
            self.x[0][0] -= 1

    def percepcion(self):
        """
        Indica donde está el robot y el estado (sucio o limpio) del cuarto
        en el que se encuentra

        """
        #return self.x[0], self.x[" AB".find(self.x[0])]
        piso, cuarto = self.x[0]
        return self.x[0], self.x[1 + (3 * piso) + cuarto]
    
class AgenteAleatorio(entornos_o.Agente):
    """
    Un agente que solo regresa una accion al azar entre las acciones legales

    """
    def __init__(self, acciones):
        self.acciones = acciones

    def programa(self, _):
        return choice(self.acciones)
    
## TEST ##

def test():
    """
    Prueba del entorno y los agentes

    """
    x0= [[0,0]] + ["sucio"] * 9
    
    print("Prueba del entorno con un agente aleatorio")
    entornos_o.simulador(NueveCuartos(x0),
                         AgenteAleatorio(['ir_Derecha', 'ir_Izquierda', 'subir', 'bajar', 'limpiar', 'nada']),
                         100)


if __name__ == "__main__":
    test()


# Requiere el modulo entornos_f.py o entornos_o.py
# Usa el modulo doscuartos_f.py para reutilizar código
# Agrega los modulos que requieras de python

