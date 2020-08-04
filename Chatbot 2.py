def handle_messages(self, messages):
    """
            Takes a list of messages, and combines those with magic to return a response string
        :param messages: list of strings
        :return: string
        """
        greetings = ["hey , how are you ?", "hi , how 's it going ?",
                     "hey , what 's up ?", "hi . how are you ?",
                     "hello , how are you doing today ? ",
                     "hello . how are things with you ?",
                     "hey ! so, tell me about yourself .",
                     "hi . nice to meet you ."]
        #check for no response
        if len(messages) == 0:
            respond with canned greeting response
            return np.random.choice(greetings)
        
        #check for overly short intro messages
        if len(messages) < 2 and len(messages[0]) <= 6: #6 for "hello"
            first_m = messages [0].lower()
            if 'hi' in first_m or 'hey' in first_m or 'hello' in first_m:
                #respond with conned greeting response
                return np.random.choice(greetings)
            
            response = self.solver.generate_response_to_input(
                    messages, max_conversation_length = self.max_conversation_length,
                    emojize = True, debug = False)
            
            #Manually remove inapropriate language from response
            #warning: the following code contains inapropriate languages
            
            if self.safe_mode:
#                            response = response.replace("fag", "<unknown>")
                response = response.replace("gays", "<unknown>")
                response = response.replace("cunt", "%@#$")
                response = response.replace("fuck", "%@#$")
                response = response.replace("shit", "%@#$")
                response = response.replace("dyke", "%@#$")
                response = response.replace("hell", "heck")
                response = response.replace("dick", "d***")
                response = response.replace("bitch", "%@#$")
            return response
    