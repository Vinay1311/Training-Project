import random
import tkinter

root = tkinter.Tk()
root.geometry('600x500')
root.title('Roll Dice')


label = tkinter.Label(root, text='', font=('Helvetica', 260))


label2 = tkinter.Label(root, text=' To Roll the Dice Click, Roll The Dice Button ', font=('Helvetica', 10, 'bold'))
label2.place(x=150, y=400)

def roll_dice():
    value = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    result = random.choice(value)
    label.configure(text=result)
    label.pack()

    if result == '\u2680' :
        print("'You rolled a ""One"" (1) ! Click Roll The Dice to roll again.'")
        print('-----------')
        print('|         |')
        print('|    0    |')
        print('|         |')
        print('-----------')

    elif result == '\u2681':
        print("'You rolled a ""Two"" (2) ! Click Roll The Dice to roll again.'")
        print('-----------')
        print('| 0       |')
        print('|         |')
        print('|       0 |')
        print('-----------')

    elif result == '\u2682':
        print("'You rolled a ""Three"" (3) ! Click Roll The Dice to roll again.'")
        print('-----------')
        print('| 0       |')
        print('|    0    |')
        print('|       0 |')
        print('-----------')

    elif result == '\u2683':
        print("'You rolled a ""Four"" (4) ! Click Roll The Dice to roll again.'")
        print('-----------')
        print('| 0     0 |')
        print('|         |')
        print('| 0     0 |')
        print('-----------')

    elif result == '\u2684':
        print("'You rolled a ""Five"" (5) ! Click Roll The Dice to roll again.'")
        print('-----------')
        print('| 0     0 |')
        print('|    0    |')
        print('| 0     0 |')
        print('-----------')

    elif result == '\u2685':
        print("'You rolled a ""Six"" (6) ! Click Roll The Dice to roll again.'")
        print('-----------')
        print('| 0     0 |')
        print('| 0     0 |')
        print('| 0     0 |')
        print('-----------')

   #For UI....
    if(result=='\u2680'):
        label3=tkinter.Label(root, text='You rolled a one! Click Roll The Dice button, to roll again.', font=('Helvetica', 10, 'bold'))
        label3.place(x=135,y=400)
    elif(result=='\u2681'):
        label3=tkinter.Label(root,text='You rolled a two! Click Roll The Dice button, to roll again.',font=('Helvetica' , 10, 'bold'))
        label3.place(x=135,y=400)
    elif(result=='\u2682'):
        label3=tkinter.Label(root,text='You rolled a three! Click Roll The Dice button, to roll again.',font=('Helvetica',10))
        label3.place(x=135,y=400)
    elif(result=='\u2683'):
        label3=tkinter.Label(root,text='You rolled a four! Click Roll The Dice button, to roll again.',font=('Helvetica',10))
        label3.place(x=135,y=400)
    elif(result=='\u2684'):
        label3=tkinter.Label(root,text='You rolled a five! Click Roll The Dice button, to roll again.',font=('Helvetica',10))
        label3.place(x=135,y=400)
    elif(result=='\u2685'):
        label3=tkinter.Label(root,text='You rolled a six! Click Roll The Dice button to, roll again.',font=('Helvetica',10))
        label3.place(x=135,y=400)


button = tkinter.Button(root, text='Roll The Dice', font=("Helvetica", 25, 'bold'), fg='white', bg ='#4ccd82', command=roll_dice)
button.pack()
root.mainloop()
