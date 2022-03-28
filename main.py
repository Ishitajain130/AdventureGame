
name = input("Hello, what is your name?")
yn = input("Hello "+ name + ". Are you interested in going on a quest? y/n")

if(yn == "n"):
  print("I'm sorry to hear that. It was nice meeting you. Goodbye!")

if(yn == "y"):
  d = input(" Ok, you are at a beach with water at your front;\n a street with cars dashing on it behind you;\n on your left, a path to a forest;\n and to your right an exit to the game.\n Which do you pick?: ")
  if(d == "front"):
    print("You run forward and start swimming, within an hour, you grow tired. You stop struggling, and you drown. GAME OVER")
  if(d == "behind"):
    print("You step out within the cars. A driver, speeding to an appointment, does not see you. You crash, and are killed on the spot. GAME OVER")
  if(d == "left"):
    a = input("You enter the forest, anxious and nervous. The trees loom over you, their sharp hands outstretched. You walk a little faster. Then you reach a cave. The cave is dark, but it was the only way through the forest. Do you want to coninue. If you type 'y', you move on. If you type 'n' you leave the game.")
  if(d == "right"):
    print("It was nice meeting you "+ name + ". I hope we meet again.")

  if(a == "n"):
    print("I'm sorry to hear that. Goodbye.")
  if(a == "y"):
    b = input("You enter the cave, when suddenly there is a flash of movement. You turn around and come face to face with a red monster with yellow eyes, a mouth full of teeth, and claws as sharp as knives. You 1(Punch it)n\ 2(Run as fast as you can)n\ 3(Stay rooted in place).n\ Which do you do? ")
    if (b == "1"):
      print("The monster growls in anger and attacks you. You are dead within moments. GAME OVER")
    elif(b == "2"):
      print("The monster runs after you and lands on top of you. You are dead within moments. GAME OVER")
    elif(b == "3"):
      print("The monster has terrible vision. It turns toward you, but cannot see you. It stalks away, and you breathe a breath of relief.")
      c = input("You continue onward and see two caves. One is short, and one is long. Pick the tunnel on the right(1) or the tunnel on the left(2): ")
      if(c == "1"):
        print("You enter the tunnel on the right. Sadly, this is the longer tunnel.")
        dd = input("You reach a part of the cave where there is no light, and you can hear water. You take out a flashlight and turn it on. Suddenl, there is a screeching noise and it grows louder. There are BATS! The swarm around you. You have two options. (1)Dive into the water.n\ (2)Hope you won't be killed by bats. Which do you pick?")
        if(dd == "2"):
          print("Why would you choose that? I am sorry, but you did not survive. I will not tell you how you died as it is too gruesome to share. GAME OVER")
        if(dd == "1"):
          print("Good choice!")
          e = input("Now that you are in the water, the bats fly away. You continue onwards and see a light ahead. But right as you see the end of the tunnel, a shape of a dog is visible. (1)Do you pet it. (2)Or do you cautiously walk past it.")
          if(e == "1"):
            print("You shouldn't pet stray animals. You are attacked, and you are dead within moments. GAME OVER")
          if(e == "2"):
            print("Good job. The dog appears to be growling, and you walk faster, through the end of the cave. GOOD JOB! You have passed the game. There is a chest of gold for you! Good job and I hope we meet again.")

      if(c == "2"):
        c2 = input("You enter the tunnel on the left. You walk for a while, until it is completely dark. You step on something, and it seems to hold onto you. You try to pull away, but it will not let go. Do you (1) get a rock from the ground and cut it. Or (2) Attempt to push it with your hand.")
        if(c2 == "1"):
          print("Good job picking the logical option. You get a sharp rock, and cut the thing that has a hold of you. Then, you continue onwards. You see an opening to the cave, and reach the end, where there is a chest of gold. GOOD JOB! You have finished the quest.")
        if(c2 == "2"):
          print("You try to push it away, but it grabs your hand, and you become more tangled. I am sorry to infom you that you will never see the light of day again. GAME OVER>")
