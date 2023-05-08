# def piramida():
#     rows = int(input("Num: "))
#     pira = for i in range(1, rows+1):
#              for j in range(1, i+1):
#                 print(j, end=" ")
#             print('\n', end='')
#     return pira

#print(pira)
# rows = int(input("Num: "))
# for i in range(1, rows+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print('\n', end='')
# for i in range(rows,1,-1):
#     for j in range(1, i):
#         print(j, end=" ")
#     print('\n', end='')
#
# rows = int(input("Num: "))
# for i in range(0,rows+1):
#     for j in range(1,i+1):
#         print(j,end= " ")
#     print('\n',end=((" ")*(rows-i)))

    #def board_build():
booth_list = []
board = int(input("board's size: "))
space_no_end = "+~~~~~"
space_end = "+"
space = (f"{(space_no_end)*board}{space_end}")
print(f" {space}")
for i in range(0,(board*board),board):
    for j in range(1,board+1):
        booth = (j + i)
        kir = "|"
        kirstart = (f" {kir}  {booth}")
        kirot1 = (f"  {booth}  ")
        kirot2 = (f" {booth}  ")
        kirot3 = (f" {booth} ")
        if booth < 100:
            if booth < 10:
                if booth == 1:
                    print(kirstart,end="  |")
                else: print(kirot1,end="|")
            else: print(kirot2,end="|")
        else: print(kirot3, end="|")
    print('\n',space,'\n',end=" |")
for b in range(1,board+1):
    booth_list.append(b)
print("'m happy to present you: ~THE BOARD~  (angle's singing uuuuhhh)")
    #player_names()
