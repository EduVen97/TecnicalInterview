#Codigo basado en la entrevista tecnica hecha en Code Crafter (Fino Company C.A.)
#Escrito por Ing. Eduardo Toro. CI 25481480. 22/11/2019

#clase gato usada para la entrevista
#recibe dos parametros:
#nombre del gato (string) y peso (int)
#usada para generar los objeto CAT que seran ingresados a la lista 

class CAT:
    def __init__(self,Name,Weight):
        self.Name = Name
        self.Weight = Weight

#clase Ball usada en la entrevista.
#Recibe dos parametros
#NewOrUsed (boolean) para determinar si la bola esta usada o no (Los gatos de mas de 20 kilos no usan bolas usadas)
#Weight (int) Los gatos que pesen menos que la bola no la pueden usar. 

class Ball:
    def __init__(self,NewOrUsed,Weight):
        self.NewOrUsed = NewOrUsed
        self.Weight = Weight
