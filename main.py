def chatbot():
  name = input("Chatbot: What is your name? ")
  
  if name == "Messi":
    print('Nice to meet you GOAT')
  else:
    print(f"Chatbot: Nice to meet you, {name}! How are you today?")
  while True:
    user_input = input('You:')
    if user_input == "Nice to meet you too! What's your name?":
      print("Thanks! I am chatbot, You can talk to me about anything you want.")
    elif user_input == "Who is the goat":
      print('Messi without any doubt.')
    elif user_input == "How to learn coding?":
      print('Join Code2College.')
    else:
      print("Sorry! I can't help with this topic. Ask Google.")
      break

chatbot()