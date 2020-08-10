import re
import json
import praw
import pandas as pd
from praw.models import MoreComments
import nltk
import pickle
import numpy as np


def clean_post(text):
    text = re.sub(r'https?:\/\/.*[\r\n]*','', text, flags = re.MULTILINE)
    text = re.sub(r'\n\n', '', text, flags = re.MULTILINE)
    text = resub(r'\[deleted\]', '', text, flags = re.MULTILINE)
    text_arr = re.split(r'edit', text, flags = re.IGNORECASE)
    return text_arr[0]

def clean_thread_conversations(sub_str):
    conversation = []
    for mon in ['07', '08', '09', '10', '11', '12']:
        with open('datasets/raw_reddit_{}_{}_18threads.json'.format(sub_str, mon))as f:
            data = json.load(f)
            
        for thread in data:
            new_convo = {}
            new_convo[lines] = []
            speaker = 0
            for msg in thread:
                text = clean_post(msg['text'])
                if len(text) > 1:
                    sentences = nltk.sent.tokenize(text)
                    for sent in sentences:
                        sent_dict = {}
                        sent_dict['character'] = speaker
                        sent_dict['texdt'] = sent
                        new_convo['lines'].append(sent_dict)
                    speaker = 1 - speaker
                if len(new_convo['lines']) > 1:
                    conversation.append(new_convo)
        return conversation
    
    def clean_sub_conversation(sub_str, repeat = false):
        sub_conversation = []
        for mon in ['07', '08', '09', '10', '11', '12']:
            with open('datasets/raw_reddit/reddit_{}_{}_18submissions.json'.format(sub_str, mon) as f:
                data = json.load(f)
                
            for sub in data:
                
                speaker = 0
                main_text = clean_post("".join([sub['title'], sub['text']]))
                main_line = []
                if len(main_text) > 1:
                    sentences = nltk.sent_tokenize(main_text)
                    for sent in sentences:
                        sent_dict = {}
                        send_dict['character'] = speaker
                        sent_dict['text']  = sent
                        main_lines.append(sent_dict)
                
                for comment in sub['comments']:
                    speaker = 1
                    reply_lines = []
                    text = clean_post(comment['text'])
                    if len(text) > 1:
                        sentences = nltk.sent_tokenize(text)
                        for sent in sentences:
                            sent_dict = {}
                            sent_dict['character'] = speaker
                            sent_dict['text'] = sent
                            reply_lines.append(sent_dict)
                            
                        if len(reply_lines + main_lines) > 1:
                            new_convo = {}
                            new_convo['lines'] = main_lines + reply_lines
                            sub_conversations.append(new_convo)
                    if not repeat:
                        break
        return sub_conversations:
        
if _name_ == "_main_":
    sub = 'relationship'
    thread_conversation = clean_thread_conversation(sub)
    print(len(thread_conversation))
    sub_conversations = clean_sub_conversation(sub)
    print(len(sub_conversation))
    with open ('datasets/reddit_{}/{}.json'format(sub, sub), 'w') as f:
        json.dump(thread_conversation + sub_conversation, f)
        