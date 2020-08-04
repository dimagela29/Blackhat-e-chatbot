import argparse
import os


def interact_with_bot(chatbot, username):
    print("\nPlease enjoy your chat whit{0}! Type 'exit' or 'quit' to end the cat at any pont.\n".format(chatbot.name))
    messages = []
    
    while True:
        message = input("["+ username +"]: ")
        
        if message == "exit" or message == "quit":
            print("Goodbye!")
            return
        
        if not messsage:
            continue
        
        messages.append(message)
        messages = messages[-5:]
        
        response = chatbot.handle_messages(messages)
        
        print("[" + chatbot.name + "]: " + response)
        messages.append(response)
        
        
  if _name_ == "_main_":
      parser = argparse.ArgumentParser()
      parser.add_argument('--models_base_path', type = str,
                          default ='/home/dialog/checkpoints/',
                          help = 'Base path to checkpoints for model averaging.')
      parser.add_argument('--teste_chatbots', action = 'Store_true', 
                          help = 'If true loads bots from test_chatbots instead.')
      parser.set_default(test_chatbots = False)
      kwargs = parser.parse_args()
      
      os.environ['BASE PATH'] = kwargs.models_base_path
      if kwargs.test_chatbots:
          from models.test_chatbots import chatbots
      else:
          from model.web_chatbots import chatbots
          
    username = None
    chatbotid = None
    
    while not username:
        username = input("Digite seu nome por favor \n>")
        
    while True:
        while chatbotid not in chatbots.keys():
            chatbotid = input("Por favor entre com um ID Válido pro chatbot. \nValid choices are ["+",".join(chatbots.keys()) + "]:\n>")
            
            chatbot = chatbots[chatbotid]
            
            interact_with_bot(chatbot, username)
            message = input("Interagir com o Bot? y/n: ")
            
            if message.lower() != 'y':
                break
            
            chatbotid = None
            
            return
        break
    
        
      