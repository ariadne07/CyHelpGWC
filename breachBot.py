#Breach Bot Starter Code
breachYear = 2017

#Greets user
print("Hello! I'm BreachBot.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

#Recounts year of breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since the Hong Kong Electoral Office data breach!")

#Describes breach
print("This breach occured in 2017 when two laptops were stolen from the Hong Kong Electoral Office.")
print("3.7 million voter registration records were lost and the stolen data included physical adresses, ID card numbers, and phone numbers.\n")

#Introduces breach
print("Would you like to learn about the Hong Kong Registration and Electoral Office data breach?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organization's response, or (c) I would like to year your reflection")
  topic = input()
  
  if topic.lower() == "a":
    print("This breach occured in 2017 when two laptops were stolen from the Hong Kong Electoral Office. 3.7 million voter registration records were lost and the stolen data included physical adresses, ID card numbers, and phone numbers.")
  
  elif topic.lower() == "b":
    print("Hong Kong's privacy Commissioner for Personal Data launched an investigation. The region began enforcing the Personal Data (Privacy) Ordinance, though it lagged behind until another scandal. Noncompliance with the principles isn't a criminal offense but ignoring an enforcement order can result in large fines and prison time. The organization apologized but didn’t recommend anything to affected users due to the theft appearing to be an internal issue.")
  
  elif topic.lower() == "c":
    break
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")

#PART 2 ######################################################################################################################################

#Introduces my take
print("\nI'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

#Shares my take
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to CIA Triad, (b) my reaction, (c) my advice, or (d) none")
  topic = input()
  
  if topic.lower() == "a":
    print("Sensitive data such as physical addresses and id numbers were stolen in this breach. It relates to the importance of confidentiality because this data falling into the wrong hands can put people into physical danger. In addition, this specific breach could have led to voter intimidation and therefore skewed future elections.")  
  
  elif topic.lower() == "b":
    print("I think the organization took important steps towards future safety and security, however, they could have done more. I think they should make it a criminal offense to directly go against their data protection principles without having to be directly told. The lack of consequences would likely cause more problems in the future.")

  elif topic.lower() == "c":
    print("I would tell them to take action by holding Hong Kong’s electoral office accountable for the breach and increase security measures in their offices.")

  elif topic.lower() == "d":
    break
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")

#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")
