from pynput import keyboard
from texttable import Texttable
t = Texttable()

c=0
c1=0
c2=0
c3=0

with keyboard.Events() as events:
    for event in events:
        if event.key == keyboard.Key.esc:
            break
        elif (str(event)) == "Press(key='1')":
                c+=1
                t.add_rows([['Panchamruta[1]', 'gadipuje[2]','karpur Arti[3]','Rudra[4]'], [c,c1,c2,c3]])
                print(t.draw())     
        elif (str(event)) == "Press(key='2')":
                c1+=1
                t.add_rows([['Panchamruta[1]', 'gadipuje[2]','karpur Arti[3]','Rudra[4]'], [c,c1,c2,c3]])
                print(t.draw())       
        elif (str(event)) == "Press(key='3')":
                c2+=1
                t.add_rows([['Panchamruta[1]', 'gadipuje[2]','karpur Arti[3]','Rudra[4]'], [c,c1,c2,c3]])
                print(t.draw())       
        elif (str(event)) == "Press(key='4')":
                c3+=1
                t.add_rows([['Panchamruta[1]', 'gadipuje[2]','karpur Arti[3]','Rudra[4]'], [c,c1,c2,c3]])
                print(t.draw())  
