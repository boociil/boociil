# GAME KERTAS GUNTING BATU

import random
import os


list_user_ans = []

# Kertas > Batu         |   1 > 3       Kertas < Gunting    1 < 2
# Gunting > kertas      |   2 > 1       Gunting < Batu      2 < 3
# Batu > Gunting        |   3 > 2       Batu < Kertas       3 < 1


def pola_sama_tiga():
    x = len(list_user_ans)
    if (x >= 3):
        for i in range(x-2,3):
            for j in range(i,3):
                if (list_user_ans[i] == list_user_ans[j]):
                    return False
    return True

def cek_menang(user_input,komp_input):
    if (user_input == komp_input):
        return "Seri"
    else:
        if (user_input == 1):
            if(komp_input == 3):
                return "Selamat anda menang"
            else:
                return "Anda Kalah"
        elif (user_input == 2): 
            if(komp_input == 1):
                return "Selamat anda menang"
            else:
                return "Anda Kalah"
        else:
            if(komp_input == 2):
                return "Selamat anda menang"
            else:
                return "Anda Kalah"


def konvert_angka(x):
    if (x == 1):
        return "Kertas"
    elif (x == 2):
        return "Gunting"
    else:
        return "Batu"

# MENU
while True:
    os.system('cls')
    print("Pilih jawaban anda")
    print("1. Kertas")
    print("2. Gunting")
    print("3. Batu")
    print("4. Exit")
    user_Answer = int(input("Jawaban anda :"))
    if (user_Answer == 4):
        exit()
    list_user_ans.append(user_Answer)
    komp_answer = random.randint(1,3)

    print("\nJawaban anda :" + konvert_angka(user_Answer))
    print("Jawaban komp :" + konvert_angka(komp_answer))
    print(cek_menang(user_Answer,komp_answer))
    enteran = input("")