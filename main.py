#THIS PROJECT WAS MADE BY JACOB COPELAND.

import time
import random
import sys

print("Welcome to the Oregon Trail!")

time.sleep(1)

global food
global oxen
global ammo
global money
global clothes
global parts
global sickperson
global leadername
global secondname
global thirdname
global fourthname
crosseddalles=None
getsick=None
disease=None
sickperson=None
sickname=None
hasjob=False

print("""Many kinds of people made the trip to Oregon. You may:
[1] Be a banker from Boston
[2] Be a carpenter from Ohio
[3] Be a farmer from Iowa""")
job=input("What is your choice? ")

bankermoney=1600
carpentermoney=800
farmermoney=400
leadername=input("What is the first name of the wagon leader? ")
secondname=input("What is the first name of the second person? ")
thirdname=input("What is the first name of the third person? ")
fourthname=input("What is the first name of the fourth person? ")
print("[1] ", leadername)
print("[2] ", secondname)
print("[3] ", thirdname)
print("[4] ", fourthname)
print("It is May 1st. The trip is around 2700 miles. You are just getting ready to leave but need to buy some supplies.")
if job=="1":
  print("You have $",bankermoney," but you do not have to spend it all.")
  money=1600
if job=="2":
  print("You have $",carpentermoney," but you do not have to spend it all.")
  money=800
if job=="3":
  print("You have $",farmermoney," but you do not have to spend it all.")
  money=400
print("You can buy all your supplies at Gerald's General Store")

print("There are 2 oxen in a yoke. I recommend at least 3 yokes. It is $40 for a yoke.")
yoke=int(input("How many yokes do you want to buy? "))
money-=int(yoke)*40
print("You have $",money,"left.")

print("You will need some food, I would get at least 200 pounds. It costs $1 for 5 pounds.")
food=int(input("How many pounds of food do you want? "))
money-=food/5
print("You have $",money,"left.")

print("You will need warm clothing on the road. I recommend 2 sets of clothing per person (you have 4). Each set costs $10.")
clothes=int(input("How many sets of clothes do you want? "))
money-=int(clothes)*10
print("You have $",money,"left.")

print("I sell ammunition in boxes of 10 bullets. It costs $1 for a box.")
ammo=int(input("How many boxes of ammo do you want? "))
money-=int(ammo)
print("You have $",money,"left.")

print("Last but not least, I sell spare parts. It is $10 per part.")
parts=int(input("How many spare parts do you want? "))
money-=int(parts)*10
print("You have $",money,"left.")

print("Now that you are done shopping, its time to take off on the journey.")
time.sleep(1)

milesremaining=2100
loseclothes=None
loseyoke=None
robber=None
death=None
breakdown=None

def getsick():

    

    disease=random.randint(1,3)
    sickperson=random.randint(1,4)

    #sick with dysentery
    if disease==1 and sickperson==1:
      print(leadername,"is sick with dysentery.")
    if disease==1 and sickperson==2:
      print(secondname,"is sick with dysentery.") 
    if disease==1 and sickperson==3:
      print(thirdname,"is sick with dysentery.")
    if disease==1 and sickperson==4:
      print(fourthname,"is sick with dysentery.") 

    if disease==2 and sickperson==1:
      print(leadername,"is sick with cholera.")
    if disease==2 and sickperson==2:
      print(secondname,"is sick with cholera.") 
    if disease==2 and sickperson==3:
      print(thirdname,"is sick with cholera.")
    if disease==2 and sickperson==4:
      print(fourthname,"is sick with cholera.") 

    if disease==3 and sickperson==1:
      print(leadername,"is sick with measles.")
    if disease==3 and sickperson==2:
      print(secondname,"is sick with measles.") 
    if disease==3 and sickperson==3:
      print(thirdname,"is sick with measles.")
    if disease==3 and sickperson==4:
      print(fourthname,"is sick with measles.") 

    if sickperson == 1 and leadername != "dead":
      print(leadername,"has recovered from illness.")
    if sickperson ==2 and secondname != "dead":
      print(secondname,"has recovered from illness.")
    if sickperson==3 and thirdname != "dead":
        print(thirdname,"has recovered from illness.")
    if sickperson==4 and fourthname != "dead":
        print(fourthname,"has recovered from illness.")

while milesremaining > 0:  
  time.sleep(3)
  food -= 10
  milesremaining -= 30
  print("You have",milesremaining,"miles remaining.")
  print("You have",food,"pounds of food remaining.")
  print("You have",yoke,"yoke left.")
  print("You have",clothes,"sets of clothes left.")
  print("")
  if milesremaining==1710:
     print("You have reached Courthouse Rock.")
     getsick()
      

     loseclothes=random.randint(1,7)
     loseyoke=random.randint(1,15)

     if loseclothes==1:
        clothes-=1
     if loseyoke==1:
        yoke-=1

     if clothes == 0:
        print("You have died due to a lack of clothing.")
     if yoke==0:
        print("You have been stopped due to lack of oxen.")

     time.sleep(2.5)
  if milesremaining==1380:
     print("You have reached Chimney Rock.")
     time.sleep(2)
     robber=random.randint(1,4)
     if robber==1:
        clothes-=2
        parts-=1
        ammo-=1
        print("You have been robbed. You lost 2 sets of clothes, 1 spare part, and 1 box of ammunition.")
        breakdown=random.randint(1,3)
     if breakdown==3:
        parts-=1
        print("Your wagon has broken down. You used 1 spare part to repare it.")

     getsick()

     if loseclothes==1:
       clothes-=1
     if loseyoke==1:
        yoke-=1

     if clothes == 0:
       print("You have died due to a lack of clothing.")
     if yoke==0:
       print("You have been stopped due to lack of oxen.")


     time.sleep(2.5)

  if milesremaining==1200:
    print("You have reached Fort Laramie.")
    time.sleep(2)
  
    if robber==1:
      clothes-=2
      parts-=1
      ammo-=1
      print("You have been robbed. You lost 2 sets of clothes, 1 spare part, and 1 box of ammunition.")
      breakdown=random.randint(1,3)
    if breakdown==3:
      parts-=1
      print("Your wagon has broken down. You used 1 spare part to repare it.")

    getsick()
    
    if loseclothes==1:
           clothes-=1
    if loseyoke==1:
           yoke-=1

    if clothes == 0:
           print("You have died due to a lack of clothing.")
    if yoke==0:
           print("You have been stopped due to lack of oxen.")


    time.sleep(2.5)

  if milesremaining==900:
      print("You have reached Independence Rock.")
      time.sleep(2)
      if robber==1:
       clothes-=2
       parts-=1
       ammo-=1
       print("You have been robbed. You lost 2 sets of clothes, 1 spare part, and 1 box of ammunition.")
       breakdown=random.randint(1,3)
      if breakdown==3:
        parts-=1
        print("Your wagon has broken down. You used 1 spare part to repare it.")


      getsick()


      if loseclothes==1:
        clothes-=1
      if loseyoke==1:
        yoke-=1

      if clothes == 0:
          print("You have died due to a lack of clothing.")
      if yoke==0:
          print("You have been stopped due to lack of oxen.")


      time.sleep(2.5)
  if milesremaining==720:
      print("You have reached Soda Springs.")
      time.sleep(2)
      if robber==1:
          clothes-=2
          parts-=1
          ammo-=1
          print("You have been robbed. You lost 2 sets of clothes, 1 spare part, and 1 box of ammunition.")
      breakdown=random.randint(1,3)
      if breakdown==3:
        parts-=1
        print("Your wagon has broken down. You used 1 spare part to repare it.")


      getsick()
      loseclothes=random.randint(1,7)
      loseyoke=random.randint(1,15)

      if loseclothes==1:
        clothes-=1
      if loseyoke==1:
        yoke-=1
      if clothes == 0:
        print("You have died due to a lack of clothing.")
      if yoke==0:
        print("You have been stopped due to lack of oxen.")


      time.sleep(2.5)
  if milesremaining==510:
      print("You have reached Fort Boise.")
      time.sleep(2)
      if robber==1:
          clothes-=2
          parts-=1
          ammo-=1
          print("You have been robbed. You lost 2 sets of clothes, 1 spare part, and 1 box of ammunition.")
      breakdown=random.randint(1,3)
      if breakdown==3:
        parts-=1
        print("Your wagon has broken down. You used 1 spare part to repare it.")


      getsick()
      loseclothes=random.randint(1,7)
      loseyoke=random.randint(1,15)

      if loseclothes==1:
          clothes-=1
      if loseyoke==1:
          yoke-=1

      if clothes == 0:
          print("You have died due to a lack of clothing.")
      if yoke==0:
          print("You have been stopped due to lack of oxen.")


      time.sleep(2.5)

  if milesremaining==150:
      print("You have reached the Dalles.")
      print("""Would you like to buy a ferry for $10 or caulk the wagon and try your luck?
      [1] Buy Ferry
      [2] Caulk the Wagon""")
      dalleschoice=input()
      if dalleschoice=="1":
        if money > 9:
          print("You have made it across the Dalles!")
          crosseddalles=True
        if money < 10:
          print("You do not have enough money to purchase a ferry. You are required to attempt to caulk the wagon.")
          dalleschoice="2"
      if dalleschoice=="2":
        dallesrandom=random.randint(1,10)
        if dallesrandom <= 3:
          print("You safely made it accross the Dalles!")
          crosseddalles=True
        if dallesrandom >= 4:
          print("Your wagon has unfortunately sank and everyone inside has died.")
          crosseddalles=False

      if crosseddalles==False:
       sys.exit()

      if milesremaining==0:
       print("You have succesfully made it to Oregon. You will now live a happy life.")
       sys.exit()
  if food <= 15:
      if ammo <= 0:
        print("You are out of ammo and have died due to lack of food.")
        time.sleep(2)
        sys.exit()
      
      
  if food <= 15:
    death=random.randint(1,4)
    if death==1:
      if sickperson==1:
        print(leadername,"has died due to complications with ilness.")
        leadername="dead"
      if sickperson==2:
        print(secondname,"has died due to complications with ilness.")
        secondname="dead"
      if sickperson==3:
        print(thirdname,"has died due to complications with ilness.")
        thirdname="dead"
      if sickperson==4:
        print(fourthname,"has died due to complications with ilness.")
        fourthname="dead"

    
      print("You are running low on food. It is time for you to hunt.")
      time.sleep(1.25)
      food += random.randint(40,220)
      time.sleep(.5)
      print("You used up 1 box of ammo.")
      ammo -= 1
      print("You now have ",food,"pounds of food.")
