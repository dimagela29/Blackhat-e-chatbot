from collections import OrderedDict
from abc import ABC, abstractmethod
from parlai_solver import ParlAISolver
from model.solver import Solver, VaritionalSolver
from model.data_loader import get_loader
from model.configs import get_config_from_dir
from models.utils import vocab, tokenizer
from model.rl import dbcq
import os
import numpy as np
import pickle
from nodel.models import VaritionalModels
import emoji

chatbots = OrderedDict()

#use enviroment variable for base path
if 'BASE_PATH' not in os.environ:
    base_path = "/home/dialog/checkpoint/"
else:
    base_path = os.environ['BASE_PATH']
    
def registerboot(botclass):
    bot = botclass()
    chatbots[bot.id] = bot
    
def load_pickle(path):
    with open(path, 'rb') as f:
        return pickle.load(f)
    
class Chatbot(ABC):
    def _init_(self, id, name, checkpoint_path, max_conversation_lenght = 5,
               max_sentence_lenght = 30, is_test_bot = False, rl = False,
               safe_mode = True):
        """
        All chatbots should extend this class and be registered with the @registerbot decorator
        :param id: An id string, must be unique!
        :param name: a user-friendly string shown to the end user to identify the chatbot. Should be unique.
        :param checkpoint_path: Directory where the trained model checkpoint is saved.
        :param max_conversation_length: Maximum number of conversation turns to condition on.
        :param max_sentence_length: Maximum number of tokens per sentence.
        :param is_test_bot: If True, this bot it can be chosen from the list of bots
        you see at /dialogadmins screen, but will never be randmly
        assigned to users landing on the home oage.
        """
        self.id = id
        self.name = name
        self.checkpoint_path = checkpoint_path
        self.max_conversation_length = max_conversation_length
        self.max_sentence_length = max.sentence_length
        self.is_teste_bot = is_test_bot
        self.safe_mode = safe_mode
        
        print("\n\nCretaing Chatbot", name)
        
        self.config = get_config_from_dir(checkpoint_path, mode = 'test',
                                          load_rl_ckpt =  rl)
        
        self.config.beam_size = 5
        
        print ("Carregando vocabulario")
        self.vocab = Vocab()
        self.vocab.load(self.config.word2id_path, self.config.id2word_path)
        print(f'Vocabulary size: {self.vocab.vocab_size}')
        
        self.config.vocab_size = sel.vocab.vocab_size
        
        #if checkpoint is for an emotion model, load that pickle file 
        emotion_sentences = None 
        if self.config.emotion:
            emotion_sentences = load_pickle(self.config>emojis_path)
            
        
        #load inferest embeddings if necessary
        infersent_sentences = None
        if self.config.infersent:
            print("Loading infersent sentences embeddings...")
            infersent_sentences = load_pickles(self.config.infersent_path)
            embedding_size = infersent_sentences [0] [0].shape[0]
            self.config.infersent_output_size = embedding_size
            
        
        self.data_loader = get_loader(
                sentences = load_pickle(self.config.sentences_path),
                conversation_length = load_pickle(self.config.conversation_length_path),
                sentence_length = load_pickle(self.config.sentence_legth_path),
                vocab = self.vocab,
                batch_size = self.config.batch_size,
                emojis = emotion_sentences)
        
        if self.config.model in VariationalModels:
            self.solver = VariationalSolver(self.config, None, self.data_loader,
                                            vocab = self.vocab, is_train = False)
            
        elif self.config.model == "Transformar":
            self.solver = ParlAISolver(self.config)
        else:
            self.solver = Solver(self.config, None, self.data_loader,
                                 vocab = self.vocab, is_train = False)
        self.solver.build()
        
            