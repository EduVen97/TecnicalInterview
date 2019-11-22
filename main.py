#Clase main del code test de la entrevista.
#Me di cuenta que me complique en la 3era pregunta al no revisar la clase CAT y ver que parametros recibia el objeto
#Ademas me deje intimidar por la list de objetos.
#Una fiesta de gatos 

from cat import CAT,Ball

ListOfCats = []
ListOfBalls = []
def main():
     
    #Llenando las dos listas
    ListOfCats.append(CAT("Garfield",20))
    ListOfCats.append(CAT("Pelusa",9))
    ListOfCats.append(CAT("Misifu",5))
    ListOfCats.append(CAT("Lucifer",10))
    ListOfCats.append(CAT("Felicia",12))
    ListOfCats.append(CAT("Catria",17))
    ListOfBalls.append(Ball(True,10))
    ListOfBalls.append(Ball(False,2))
    ListOfBalls.append(Ball(False,3))
    ListOfBalls.append(Ball(False,5))
    ListOfBalls.append(Ball(True,8))
    ListOfBalls.append(Ball(True,25))
    ListOfBalls.append(Ball(False,16))
    ListOfBalls.append(Ball(True,1))
    ListOfBalls.append(Ball(False,9))
    ListOfBalls.append(Ball(True,2))
    
    InviteYourself()
    GatosInvitados()
    NumerodeBolasGatos()
    exitResult = CatExit()#No me acuerdo bien de cual era la 4ta Pregunta
    print(exitResult,"gatos han salido de la fiesta")


#Invitate a la fiesta 
def InviteYourself():
    print("Eduardo ha sido Invitado")
    return 

#Cuenta el numero de gatos invitados a la fiesta
def GatosInvitados():
    Resultado=0
    for x in ListOfCats:
        Resultado+=1
    print("Hay",Resultado,"gatos en la fiesta")
    return

#Cuenta el numero de bolas con las cuales puede jugar cada gato
#Los gatos no pueden jugar con bolas mayores a su peso,
#Los gatos de 20kg o mas no juegas con bolas usadas. 
def NumerodeBolasGatos():
    for SelectedCat in ListOfCats:
        BallsToPlay=0 #Numero de bolas con las cuales puede jugar el gato 
        for SelectedBall in ListOfBalls:

            if ((SelectedBall.NewOrUsed == True) and (SelectedCat.Weight>=20)): #Si la bola es nueva y el gato pesa mas de 20kg
                if (SelectedCat.Weight>SelectedBall.Weight): #Si el peso del gato supera al de la bola
                    BallsToPlay+=1

            if (SelectedCat.Weight<20): #Los gatos que tengan peso menor a 20 juegan con cualquier bola
                if (SelectedCat.Weight>SelectedBall.Weight): #Si el peso del gato supera al de la bola
                    BallsToPlay+=1

        print(SelectedCat.Name,"puede jugar con:",BallsToPlay,"bolas")
    return

#No me acuerdo bien de la 4ta pregunta, me acuerdo que habia que pasar una variable
#por return a una variable que se imprimia en main.
#CatExit
#Si hay gatos que tienen 4 o menos bolas con las cual jugar estos salen de la fiesta
def CatExit():
    GatosSaliendo = 0
    for SelectedCat in ListOfCats:
        BallsToPlay=0 #Numero de bolas con las cuales puede jugar el gato 
        for SelectedBall in ListOfBalls:

            if ((SelectedBall.NewOrUsed == True) and (SelectedCat.Weight>=20)): #Si la bola es nueva y el gato pesa mas de 20kg
                if (SelectedCat.Weight>SelectedBall.Weight): #Si el peso del gato supera al de la bola
                    BallsToPlay+=1

            if (SelectedCat.Weight<20): #Los gatos que tengan peso menor a 20 juegan con cualquier bola
                if (SelectedCat.Weight>SelectedBall.Weight): #Si el peso del gato supera al de la bola
                    BallsToPlay+=1

        if (BallsToPlay<=4):
            GatosSaliendo+=1
            
    return GatosSaliendo
if __name__ == "__main__":
    main()
    