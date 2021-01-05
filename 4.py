print("************ sobhani *Exercie4* Data-Mining ************")

import keyboard
while True:
   
    MySentence = "Data_Mining,Mr,Vafaee,Azar,99,Marzieh,Sobhani"
    print("Our words are: ",MySentence)
    input("enter for Spliting: ")

    MySentence_Splited = MySentence.split(",")
    print("Word after packaging : ", MySentence_Splited)

    keyboard.wait('q')
    keyboard.send('ctrl+6')

