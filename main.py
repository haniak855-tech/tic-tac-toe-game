
def sum(a,b,c):
    return a+b+c
def printboard(xState, zState):
        zero='x' if xState[0] else ('o' if zState[0] else 0)
        one='x' if xState[1] else ('o' if zState[1] else 0)
        two='x' if xState[2] else ('o' if zState[2] else 0)
        three='x' if xState[3] else ('o' if zState[3] else 0)
        four='x' if xState[4] else ('o' if zState[4] else 0)
        five='x' if xState[5] else ('o' if zState[5] else 0)
        six='x' if xState[6] else ('o' if zState[6] else 0)
        seven='x' if xState[7] else ('o' if zState[7] else 0)
        eight='x' if xState[8] else ('o' if zState[8] else 0)
        print(f"{zero} | {one} |{two}")
        print(f"--|---|--")
        print(f"{three} | {four} |{five}")
        print(f"--|---|--")
        print(f"{six} | {seven} |{eight}")

def checkwin(Xstate, zState):
   wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
   for win in wins:
     if(sum(Xstate[win[0]],Xstate[wins[1]],Xstate[wins[wins]])==3):
       print("X won the match")
       return 1
     if(sum(zState[wins[0]],zState[wins[1]],zState[wins[2]])==3):
      print("Z won the match")
      return 0

   return -1
if __name__ == "__main__":
   xState= [0,0,0,0,0,0,0,0,0]
   zState= [0,0,0,0,0,0,0,0,0]
   turn=1
   print("welcome to tic tac toe")
   while(True):
      printboard(xState, zState)
      if(turn==1):
         print ("X's chance")
         value= input("please enter a value:")
         try:
            value = int(value)
         except ValueError:
            print("❌ Invalid input! Please enter a number 0–8.")
            continue
         
         if(value>8):
            print('invalid value')
            break
      xState[value]=1

   # else:
   #    print ("O's chance")
   #    value= int(input("please enter a value:"))
   #    zState[value]=1
   #    cwin=checkwin(Xstate, zState)
   #    if(cwin != -1):
   #     print("match over")
   #     break

turn=1-turn