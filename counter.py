from pynput import keyboard
from texttable import Texttable
from datetime import datetime
t = Texttable()

c=str(0)
c1=str(0)
c2=str(0)
c3=str(0)

with keyboard.Events() as events:
    for event in events:
        if event.key == keyboard.Key.esc:
            break
        elif (str(event)) == "Press(key='1')":
                c = int(c.split()[0])
                c+=1
                c = ' --> '.join((str(c),datetime.now().strftime('%d/%m/%y %H:%M')))
                t.add_rows([['Panchamruta[1]', 'Gaadipuje[2]','Karpur Arti[3]','Rudra[4]'], [c,c1,c2,c3]])
                print(t.draw())
        elif (str(event)) == "Press(key='2')":
                c1 = int(c1.split(' ',1)[0])
                c1+=1
                c1 = ' --> '.join((str(c1),datetime.now().strftime('%d/%m/%y %H:%M')))
                t.add_rows([['Panchamruta[1]', 'Gaadipuje[2]','Karpur Arti[3]','Rudra[4]'], [c,c1,c2,c3]])
                print(t.draw())       
        elif (str(event)) == "Press(key='3')":
                c2 = int(c2.split(' ',1)[0])
                c2+=1
                c2 = ' --> '.join((str(c2),datetime.now().strftime('%d/%m/%y %H:%M')))
                t.add_rows([['Panchamruta[1]', 'Gaadipuje[2]','Karpur Arti[3]','Rudra[4]'], [c,c1,c2,c3]])
                print(t.draw())       
        elif (str(event)) == "Press(key='4')":
                c3 = int(c3.split(' ',1)[0])
                c3+=1
                c3 = ' --> '.join((str(c3),datetime.now().strftime('%d/%m/%y %H:%M')))
                t.add_rows([['Panchamruta[1]', 'Gaadipuje[2]','Karpur Arti[3]','Rudra[4]'], [c,c1,c2,c3]])
                print(t.draw())  