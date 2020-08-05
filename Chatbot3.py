"""Cornell Bots"""

#Cornel baselines

@registerbot
class HRED_cornell(chatbot):
    def _init_(self):
        super()._init_("HRED_cornell", "HRED movies", base_path + "cornell/hred_canonical")
        
@registerbot
class VHRED_cornell(chatbot):
    def _init_(self):
        super()._init_("VHRED_cornell", "VHRED movies", base_path + "cornell/vhread_canonical")
    
@registerbot
class VHCR_cornell(chatbot):
    def _init_(self):
        super()._init_("VHCR_cornell", "VHCR movies", base_path + "cornell/vhcr_cannonical")
 
# # Models trained on cornell with deepmoji discriminator
# @registerbot
# class emotion_HRED_cornell(Chatbot):
#     def __init__(self):
#         super().__init__("emotion_HRED_cornell", "ELSA-emo HRED movies", base_path + "cornell/emotion_hred_default")
#         #super().__init__("emotion_HRED_cornell", "ELSA-emo HRED movies", base_path + "cornell/emotion_hred_hparam")

# @registerbot
# class emotion_VHRED_cornell(Chatbot):
#     def __init__(self):
#         super().__init__("emotion_VHRED_cornell", "pet ELSA", base_path + "cornell/emotion_vhred_default")

# @registerbot
# class emotion_VHRED_cornell_hparam(Chatbot):
#     def __init__(self):
#         super().__init__("emotion_VHRED_cornell_hparam", "ELSA-emo VHRED movies", base_path + "cornell/emotion_vhred_hparam")

# @registerbot
# class emotion_VHCR_cornell(Chatbot):
#     def __init__(self):
#         super().__init__("emotion_VHCR_cornell", "ELSA-emo VCHR movies", base_path + "cornell/emotion_vhcr_default")


# # Models trained on cornell with infersent discriminator
# @registerbot
# class infersent_HRED_cornell(Chatbot):
#     def __init__(self):
#         super().__init__("infersent_HRED_cornell", "ELSA-infer HRED movies", base_path + "cornell/infersent_hred_default")

# @registerbot
# class infersent_VHRED_cornell(Chatbot):
#     def __init__(self):
#         #super().__init__("infersent_VHRED_cornell", "ELSA-infer VHRED movies", base_path + "cornell/infersent_vhred_noworddrop")
#         super().__init__("infersent_VHRED_cornell", "ELSA-infer VHRED movies", base_path + "cornell/infersent_vhred_hparam")

# @registerbot
# class infersent_VHCR_cornell(Chatbot):
#     def __init__(self):
#         super().__init__("infersent_VHCR_cornell", "ELSA-infer VCHR movies", base_path + "cornell/infersent_vhcr_default    

# modelos treinados no cornell com bot descritivo
        
@registerbot
class emoinfer_HRED_cornell(chatbot):
    def _init_(self):
    #super().__init__("emoinfer_HRED_cornell", "ELSA HRED movies", base_path + "cornell/emoinfer_hred_default")
    #super().__init__("emoinfer_HRED_cornell", "ELSA HRED movies", base_path + "cornell/emoinfer_hred_hparam")
    super()._init_("emoinfer_HRED_cornell", "EI HRED movies", base_path + "cornell/emoinfer_hred_AG")

@registerbot
class emoinfer_VHRED_cornell(chatbot):
    def _init_(self):
        #super().__init__("emoinfer_VHRED_cornell", "ELSA VHRED movies", base_path + "cornell/emoinfer_vhred_noworddrop")
        super()._init_("emoinfer_VHRED", "EI VHRED movies", base_path + "cornell/emoinfer_vhred_hparam")

@registerbot
class emoinfer_VHCR_cornell(Chatbot):
    def __init__(self):
        #super().__init__("emoinfer_VHCR_cornell", "ELSA VCHR movies", base_path + "cornell/emoinfer_vhcr_default_sentencedrop")
        super().__init__("emoinfer_VHCR_cornell", "EI VCHR movies", base_path + "cornell/emoinfer_vhcr_AG")   

"""Reddit casual bots"""

#baseline models trained on reddit_casual
@registerbot
class HRED_reddit_casual(Chatbot):
    def _init_(self):
        super()._init_("HRED_reddit_casual", "HRED reddit", 
             #base_path + "reddit_casual/reddit_casual_hred_canonical",
             base_path + "reddit_casual/hred_new_hparams", 
             max_conversation_length = 10)
        
@registerbot 
class VHRED_reddit_casual(chatbot):
    def _init_(self):
        super()._init_("VHRED_reddit_casual", "VHRED reddit",
             #base_path + "reddit_casual/reddit_casual_vhred_canonical",
             base_path + "reddit_casual/vhred_new_hparams"
             max_conversation_length = 10)


# # Models trained on r/casual with deepmoji discriminator
# @registerbot
# class emotion_HRED_casual(Chatbot):
#     def __init__(self):
#         super().__init__("emotion_HRED_casual", "ELSA-emo HRED reddit",
#                          base_path + "reddit_casual/emotion_hred_canonical",
#                          max_conversation_length=10)

# @registerbot
# class emotion_VHRED_casual(Chatbot):
#     def __init__(self):
#         super().__init__("emotion_VHRED_casual", "ELSA-emo VHRED reddit",
#                          base_path + "reddit_casual/emotion_vhred_big_noworddrop",
#                          max_conversation_length=10)

# @registerbot
# class emotion_VHCR_casual(Chatbot):
#     def __init__(self):
#         #super().__init__("emotion_VHCR_casual", "ELSA-emo VCHR reddit", base_path + "reddit_casual/emotion_vhcr_big_worddrop")
#         super().__init__("emotion_VHCR_casual", "ELSA-emo VHCR reddit",
#                          base_path + "reddit_casual/emotion_vhcr_hparam",
#                          max_conversation_length=10)


# # Models trained on r/casual with infersent discriminator
# @registerbot
# class infersent_HRED_casual(Chatbot):
#     def __init__(self):
#         super().__init__("infersent_HRED_casual", "ELSA-infer HRED reddit",
#                          base_path + "reddit_casual/infersent_hred_default",
#                          max_conversation_length=10)

# @registerbot
# class infersent_VHRED_casual(Chatbot):
#     def __init__(self):
#         super().__init__("infersent_VHRED_casual", "ELSA-infer VHRED reddit",
#                          base_path + "reddit_casual/infersent_vhred_big_noworddrop",
#                          max_conversation_length=10)

# @registerbot
# class infersent_VHCR_casual(Chatbot):
#     def __init__(self):
#         #super().__init__("infersent_VHCR_casual", "ELSA-infer VCHR reddit", base_path + "reddit_casual/infersent_vhcr_default_sentencedrop")
#         super().__init__("infersent_VHCR_casual", "ELSA-infer VHCR reddit",
#                          base_path + "reddit_casual/infersent_vhcr_hparam",
#                          max_conversation_length=10)

#models trained on r/casual with boot discriminators
@registerbot
class emoinfer_HRED_casual(Chatbot):
    def __init__(self):
        #super().__init__("emoinfer_HRED_casual", "ELSA HRED reddit", base_path + "reddit_casual/emoinfer_hred_default")
        super().__init__("emoinfer_HRED_casual", "EI HRED reddit",
                         base_path + "reddit_casual/emoinfer_hred_AG",
                         max_conversation_length=10)

@registerbot
class emoinfer_VHRED_casual(Chatbot):
    def _init_(self):
        super()._init_("emoinfer_VHRED_casual", "EI VHRED reddit", 
             base_path + "reddit_casual/emoinfer_vhred_AG",
             max_conversation = 10)
        
@registerbot
class emoinfer_VHCR_casual(Chatbot):
    def __init__(self):
        #super().__init__("emoinfer_VHCR_casual", "ELSA VCHR reddit", base_path + "reddit_casual/emoinfer_vhcr_big_AG")
        #super().__init__("emoinfer_VHCR_casual", "ELSA VHCR reddit", base_path + "reddit_casual/emoinfer_vhcr_hparam")
        super().__init__("emoinfer_VHCR_casual", "EI VHCR reddit",
                         base_path + "reddit_casual/emoinfer_vhcr_AG",
                         max_conversation_length=10)


# Models trained on r/casual with input but no discriminators
# @registerbot
# class input_only_HRED_casual(Chatbot):
#     def __init__(self):
#         super().__init__("input_only_HRED_casual", "HRED reddit extra input", base_path + "reddit_casual/input_only_hred_default")

# @registerbot
# class input_only_VHRED_casual(Chatbot):
#     def __init__(self):
#         super().__init__("input_only_VHRED_casual", "VHRED reddit extra input", base_path + "reddit_casual/input_only_vhred_default_worddrop")

# @registerbot
# class input_only_VHCR_casual(Chatbot):
#     def __init__(self):
#         super().__init__("input_only_VHCR_casual", "VCHR reddit extra input", base_path + "reddit_casual/input_only_vhcr_default_sentencedrop")
    
# Models trained on r/casual with input but no discriminators
# @registerbot
# class input_only_HRED_casual(Chatbot):
#     def __init__(self):
#         super().__init__("input_only_HRED_casual", "HRED reddit extra input", base_path + "reddit_casual/input_only_hred_default")

# @registerbot
# class input_only_VHRED_casual(Chatbot):
#     def __init__(self):
#         super().__init__("input_only_VHRED_casual", "VHRED reddit extra input", base_path + "reddit_casual/input_only_vhred_default_worddrop")

# @registerbot
# class input_only_VHCR_casual(Chatbot):
#     def __init__(self):
#         super().__init__("input_only_VHCR_casual", "VCHR reddit extra input", base_path + "reddit_casual/input_only_vhcr_default_sentencedrop")


""" RL BOTS - Rewards"""
@registerbot
class rl_baseline(Chatbot):
    def __init__(self):
        super().__init__("rl_baseline", "RL - baseline",
                         base_path + "reddit_casual/infersent_vhred_big_noworddrop",
                         max_conversation_length=5)

@registerbot
class rl_rewards_convlen(Chatbot):
    def __init__(self):
        super().__init__("rl_rewards_convlen", "RL - conversation length",
                         base_path + "rl/rewards/conv_len",
                         rl=True)

@registerbot
class rl_rewards_deepmoji(Chatbot):
    def __init__(self):
        super().__init__("rl_rewards_deepmoji", "RL - sentiment",
                         base_path + "rl/rewards/deepmoji",
                         rl=True)

@registerbot
class rl_rewards_emotion_transition(Chatbot):
    def __init__(self):
        super().__init__("rl_rewards_emotion_transition", "RL - sentiment transition",
                         base_path + "rl/rewards/emotion_transition",
                         rl=True)

@registerbot
class rl_rewards_infersent_coherence(Chatbot):
    def __init__(self):
        super().__init__("rl_rewards_infersent_coherence", "RL - lexical similarity",
                         base_path + "rl/rewards/infersent_coherence",
                         rl=True)

@registerbot
class rl_rewards_question(Chatbot):
    def __init__(self):
        super().__init__("rl_rewards_question", "RL - questions",
                         base_path + "rl/rewards/question",
                         rl=True)

@registerbot
class rl_rewards_user_ha(Chatbot):
    def __init__(self):
        super().__init__("rl_rewards_user_ha", "RL - laughter",
                         base_path + "rl/rewards/user_ha",
                         rl=True)

@registerbot
class rl_rewards_words_elicited(Chatbot):
    def __init__(self):
        super().__init__("rl_rewards_words_elicited", "RL - words elicited",
                         base_path + "rl/rewards/words_elicited",
                         rl=True)

@registerbot
class rl_rewards_manual_upvotes(Chatbot):
    def __init__(self):
        super().__init__("rl_rewards_manual_upvotes", "RL - manual upvotes",
                         base_path + "rl/rewards/manual_upvotes",
                         rl=True)


# """ RL BOTS - testing reward combo"""
# @registerbot
# class rl_rc_my_quality(Chatbot):
#     def __init__(self):
#         super().__init__("rl_rc_my_quality", "RL reward combo 1",
#                          base_path + "rl/combo_testing/my_quality_3000",
#                          rl=True)

# @registerbot
# class rl_rc_my_quality_softmax(Chatbot):
#     def __init__(self):
#         super().__init__("rl_rc_my_quality_softmax", "RL reward combo 2",
#                          base_path + "rl/combo_testing/my_quality_softmax_3000",
#                          rl=True)

# @registerbot
# class rl_rc_my_web_quality_softmax(Chatbot):
#     def __init__(self):
#         super().__init__("rl_rc_my_web_quality_softmax", "RL reward combo 3",
#                          base_path + "rl/combo_testing/my_web_quality_softmax_1000",
#                          rl=True)

# @registerbot
# class rl_web_quality(Chatbot):
#     def __init__(self):
#         super().__init__("rl_web_quality", "RL reward combo 4",
#                          base_path + "rl/combo_testing/web_quality_2000",
#                          rl=True)

""" RL BOTS - Techniques"""
@registerbot
class rl_batch_q(Chatbot):
    def __init__(self):
        super().__init__("rl_batch_q", "RL - Batch Q",
                         base_path + "rl/techniques/batch_q",
                         rl=True)

@registerbot
class rl_batch_q_mc(Chatbot):
    def __init__(self):
        super().__init__("rl_batch_q_mc", "RL - Batch Q MC",
                         base_path + "rl/techniques/batch_q_mc5",
                         rl=True)

@registerbot
class rl_dbcq(Chatbot):
    def __init__(self):
        self.id = 'rl_dbcq'
        self.name = 'RL - DBCQ'
        self.is_test_bot = False
        self.max_conversation_length = 5
        self.safe_mode = True

        kwargs_dict = {'bcq_n': 5, 'mode': 'test'}
        prior_config = get_config_from_dir(
            base_path + "reddit_casual/infersent_vhred_big_noworddrop",
            **kwargs_dict)

        kwargs_dict['load_rl_ckpt'] = True
        rl_config = get_config_from_dir(
            base_path + "rl/techniques/batch_q_mc5",
            **kwargs_dict)

        self.solver = dbcq.DBCQ(prior_config, rl_config)

@registerbot
class rl_kl_control_q(Chatbot):
    def __init__(self):
        super().__init__("rl_kl_control_q", "RL - KL control Q",
                         base_path + "rl/techniques/kl_control_q",
                         rl=True)

@registerbot
class rl_kl_control_psi(Chatbot):
    def __init__(self):
        super().__init__("rl_kl_control_psi", "RL - KL control Psi",
                         base_path + "rl/techniques/kl_control_psi",
                         rl=True)

@registerbot
class rl_model_avg_q(Chatbot):
    def __init__(self):
        super().__init__("rl_model_avg_q", "RL - Model avg Q",
                         base_path + "rl/techniques/model_avg_q",
                         rl=True)

@registerbot
class rl_model_avg_psi(Chatbot):
    def __init__(self):
        super().__init__("rl_model_avg_psi", "RL - Model avg Psi",
                         base_path + "rl/techniques/model_avg_psi",
                         rl=True)


""" ABDUL BOTS"""

@registerbot
class Transformer_reddit_casual(Chatbot):
    def __init__(self):
        super().__init__("Transformer_reddit_casual", "Transformer reddit",
                         base_path + "reddit_casual/abdul_ckpts/vanilla_transformer/",
                         max_conversation_length=10, safe_mode=False)

@registerbot
class hrl_vhred_baseline(Chatbot):
    def __init__(self):
        super().__init__("hrl_vhred_baseline", "HRL VHRED baseline",
                         base_path + "reddit_casual/abdul_ckpts/vanilla_vhred/",
                         max_conversation_length=10, safe_mode=False)

""" Abdul study 1 - different rewards """

# Flat rl
@registerbot
class reinforce_flatrl_bot_deepmoji(Chatbot):
    def __init__(self):
        super().__init__("reinforce_flatrl_bot_deepmoji", "REINFORCE - sentiment",
                         base_path + "reddit_casual/abdul_ckpts/reinforce/flat_rl/reward_bot_deepmoji/",
                         max_conversation_length=10, safe_mode=False, rl=True)

@registerbot
class reinforce_flatrl_question(Chatbot):
    def __init__(self):
        super().__init__("reinforce_flatrl_question", "REINFORCE - question",
                         base_path + "reddit_casual/abdul_ckpts/reinforce/flat_rl/reward_question/",
                         max_conversation_length=10, safe_mode=False, rl=True)

@registerbot
class reinforce_flatrl_USE_similarity(Chatbot):
    def __init__(self):
        super().__init__("reinforce_flatrl_USE_similarity", "REINFORCE - USE similarity",
                         base_path + "reddit_casual/abdul_ckpts/reinforce/flat_rl/reward_USE_similarity/",
                         max_conversation_length=10, safe_mode=False, rl=True)

@registerbot
class reinforce_flatrl_repetition(Chatbot):
    def __init__(self):
        super().__init__("reinforce_flatrl_repetition", "REINFORCE - repetition",
                         base_path + "reddit_casual/abdul_ckpts/reinforce/flat_rl/reward_conversation_repetition/",
                         max_conversation_length=10, safe_mode=False, rl=True)

@registerbot
class reinforce_flatrl_toxicity(Chatbot):
    def __init__(self):
        super().__init__("reinforce_flatrl_toxicity", "REINFORCE - toxicity",
                         base_path + "reddit_casual/abdul_ckpts/reinforce/flat_rl/reward_toxicity/",
                         max_conversation_length=10, safe_mode=False, rl=True)

# HRL
@registerbot
class reinforce_hrl_bot_deepmoji(Chatbot):
    def __init__(self):
        super().__init__("reinforce_hrl_bot_deepmoji", "VHRL - sentiment",
                         base_path + "reddit_casual/abdul_ckpts/reinforce/joint_hrl/reward_bot_deepmoji/",
                         max_conversation_length=10, safe_mode=False, rl=True)

@registerbot
class reinforce_hrl_question(Chatbot):
    def __init__(self):
        super().__init__("reinforce_hrl_question", "VHRL - question",
                         base_path + "reddit_casual/abdul_ckpts/reinforce/joint_hrl/reward_question/",
                         max_conversation_length=10, safe_mode=False, rl=True)

@registerbot
class reinforce_hrl_USE_similarity(Chatbot):
    def __init__(self):
        super().__init__("reinforce_hrl_USE_similarity", "VHRL - USE similarity",
                         base_path + "reddit_casual/abdul_ckpts/reinforce/joint_hrl/reward_USE_similarity/",
                         max_conversation_length=10, safe_mode=False, rl=True)

@registerbot
class reinforce_hrl_repetition(Chatbot):
    def __init__(self):
        super().__init__("reinforce_hrl_repetition", "VHRL - repetition",
                         base_path + "reddit_casual/abdul_ckpts/reinforce/joint_hrl/reward_conversation_repetition/",
                         max_conversation_length=10, safe_mode=False, rl=True)

@registerbot
class reinforce_hrl_toxicity(Chatbot):
    def __init__(self):
        super().__init__("reinforce_hrl_toxicity", "VHRL - toxicity",
                         base_path + "reddit_casual/abdul_ckpts/reinforce/joint_hrl/reward_toxicity/",
                         max_conversation_length=10, safe_mode=False, rl=True)


""" Abdul study 2 - combined reward"""

@registerbot
class reinforce_flatrl_combined(Chatbot):
    def __init__(self):
        super().__init__("reinforce_flatrl_combined", "REINFORCE - combined",
                         base_path + "reddit_casual/abdul_ckpts/reinforce/flat_rl/flat_combined/",
                         max_conversation_length=10, safe_mode=False, rl=True)

@registerbot
class reinforce_hrl_combined(Chatbot):
    def __init__(self):
        super().__init__("reinforce_hrl_combined", "VHRL - combined",
                         base_path + "reddit_casual/abdul_ckpts/reinforce/joint_hrl/joint_combined/",
                         max_conversation_length=10, safe_mode=False, rl=True)

@registerbot
class reinforce_hrl_alternate_combined(Chatbot):
    def __init__(self):
        super().__init__("reinforce_hrl_alternate_combined", "Decoupled VHRL - combined",
                         base_path + "reddit_casual/abdul_ckpts/reinforce/alternate_hrl/alternate_combined/",
                         max_conversation_length=10, safe_mode=False, rl=True)

@registerbot
class hrl_psi_learning_baseline(Chatbot):
    def __init__(self):
        super().__init__("hrl_psi_learning_baseline", "Psi-learning - combined",
                         base_path + "reddit_casual/abdul_ckpts/psi_learning/",
                         max_conversation_length=10, safe_mode=False, rl=True)

""" PREVIOUS BOTS """

# @registerbot
# class MHH(Chatbot):
#     """
#     This is only a dummy chatbot for MHH grant submission.
#     """
#     def __init__(self):
#         self.id = "ELSA_dummy"
#         self.name = "ELSA"
#         self.max_conversation_length = 100

#     def handle_messages(self, messages):
#         user_lines = ['Hey Elsa, I am really struggling right now.',
#                       "My finals are coming up and I haven't been getting a lot of sleep... plus I am working a full-time job. Generally speaking I don't feel like I have time for myself.",
#                       "Sort of, I am spending all my weekends catching up on assignments and feel tired throughout the week, but I'm also performing well and have made a lot of progress as a UROP. I think I just don't feel like I can or have spent much time relaxing, catching up with friends and my mood hasn't been so great.",
#                       'Well, I used to ride my bike a lot, but it has been too cold.',
#                       "Going out to eat at a nice restaurant and having some friends over to play video games... but I honestly, haven't done those things in a while and everyone seems busy like me.",
#                       'Yes',
#                       "Hmm... I don't know, I think I just want to hang out with my friends more throughout the week. I am sure there is some time to do that I bet even just a small amount of more time with them will make me happier.",
#                       'I could, I guess check how available my friends are for the upcoming week, and see if I can plan a fancy dinner when many people are free.',
#                       'I feel better now. Thanks for the chat Elsa.',
#                       'Great. Talk to you soon!']    # list of sentences

#         bot_lines = ['Would you feel comfortable telling me about what you are struggling with?',
#                      f'I see.  It sounds to me like you are feeling stressed about all your demands {emoji.emojize(":pensive:", use_aliases=True)}, is that right?',
#                      f'I see. It takes a lot of commitment to be a great student and full-time worker so great job, VERY great job {emoji.emojize(":thumbsup: :clap:", use_aliases=True)}. It sounds like you value that, but are having trouble relaxing?  Can you tell me how you relaxed in the past?',
#                      f'What other kinds of things did you do to relax {emoji.emojize(":relieved:", use_aliases=True)} ?',
#                      'I see, so to summarize, you mentioned there are many things are stressing you out, such as spending all of your weekends catching up on assignments, working full time, losing sleep. You’d like to relax more, but are struggling with that, is that correct?',
#                      'What would you like to see different about your current situation?',
#                      'Suppose socializing with your friends more is a 10 and 1 is your current situation. You may not be ready to change, but at least what would it take to go from 1 to 10?',
#                      f'It sounds like you have a plan of action {emoji.emojize(":ok_hand:", use_aliases=True)}, how does that make you feel?',
#                      'You’ve come a long way 😊! Again, you may or may not be ready to change, but feel free to update me on how that goes.',
#                      'Talk to you soon 😊']      # list of sentences
#         # return bot_lines[int(len(messages)/2)]
#         for i in range(len(user_lines)):
#             if messages[-1] == user_lines[i]:
#                 return bot_lines[i]
#         return ''

# Models trained on cornell with input but no discriminators
# @registerbot
# class input_only_HRED_cornell(Chatbot):
#     def __init__(self):
#         super().__init__("input_only_HRED_cornell", "HRED movies extra input", base_path + "cornell/input_only_hred_default")

# @registerbot
# class input_only_VHRED_cornell(Chatbot):
#     def __init__(self):
#         super().__init__("input_only_VHRED_cornell", "VHRED movies extra input", base_path + "cornell/input_only_vhred_default_worddrop")

# @registerbot
# class input_only_VHCR_cornell(Chatbot):
#     def __init__(self):
#         super().__init__("input_only_VHCR_cornell", "VCHR movies extra input", base_path + "cornell/input_only_vhcr_default_sentencedrop")


# Baseline models trained on reddit_all
# @registerbot
# class HRED_reddit_all(Chatbot):
#     def __init__(self):
#         super().__init__("HRED_reddit_all", "HRED relationships", base_path + "reddit_all/hred_canonical")

# @registerbot
# class VHRED_reddit_all(Chatbot):
#     def __init__(self):
#         super().__init__("VHRED_reddit_all", "VHRED relationships", base_path + "reddit_all/vhred_canonical")

# @registerbot
# class VHCR_reddit_all(Chatbot):
#     def __init__(self):
#         super().__init__("VHCR_reddit_all", "VHCR relationships", base_path + "reddit_all/vhcr_canonical")


# ELSA models trained on reddit_all
# @registerbot
# class ELSA_HRED_reddit_all(Chatbot):
#     def __init__(self):
#         super().__init__("ELSA_HRED_reddit_all", "ELSA HRED relationships", base_path + "reddit_all/emotion_hred_canonical")

# @registerbot
# class ELSA_VHRED_reddit_all(Chatbot):
#     def __init__(self):
#         super().__init__("ELSA_VHRED_reddit_all", "ELSA VHRED relationships", base_path + "reddit_all/emotion_vhred_canonical")

# @registerbot
# class ELSA_VHCR_reddit_all(Chatbot):
#     def __init__(self):
#         super().__init__("ELSA_VHCR_reddit_all", "ELSA VHCR relationships", base_path + "reddit_all/emotion_vhcr_canonical")

# Baselines trained on r/depression
# @registerbot
# class HRED_depression(Chatbot):
#     def __init__(self):
#         super().__init__("HRED_depression", "HRED depression", base_path + "reddit/hred_canonical")


# @registerbot
# class VHRED_depression(Chatbot):
#     def __init__(self):
#         super().__init__("VHRED_depression", "VHRED depression", base_path + "reddit/vhred_canonical")

# @registerbot
# class VHCR_depression(Chatbot):
#     def __init__(self):
#         super().__init__("VHCR_depression", "VHCR depression", base_path + "reddit/vhcr_canonical")


# @registerbot
# class reinforce_hrl_bot_deepmoji(Chatbot):
#     def __init__(self):
#         super().__init__("reinforce_flatrl_bot_deepmoji", "Flat RL bot deepmoji",
#                          base_path + "reddit_casual/abdul_ckpts/reinforce/flat_rl/reward_bot_deepmoji/",
#                          max_conversation_length=10)
