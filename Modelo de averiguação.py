"" "Este arquivo carrega todos os chatbots disponíveis e calcula o agregado 
probabilidade que eles colocam em cada frase no conjunto de dados, ponderada por cada modelo
pontuação ou proporção predefinida nos dados. "" "

importar  argparse
importar  os
import  sys
importar  numpy  como  np
importar  pandas  como  pd
importar  tocha

do  modelo . modelos  import  VariationalModels
do  modelo . utils  import  to_var , EOS_ID

import  replay_buffer
import  run_rl

TEST_WEIGHTS  = {
    'emotion_VHRED_cornell' : .5 ,
    'infersent_HRED_cornell' : .1 ,
    'emoinfer_VHCR_casual' : .2 ,
    'emoinfer_VHRED_casual' : .3 ,
}

# Do estudo real, os pesos são classificações de qualidade
PREDEFINED_MODEL_WEIGHTS  = {
    # Reddit
    'emotion_HRED_casual' : 3.125 ,
    'infersent_VHRED_casual' : 3.047619048 ,
    'emotion_VHRED_casual' : 2.913043478 ,
    # 'emoinfer_VHRED_casual': 2.863636364,
    # 'emoinfer_HRED_casual': 2.714285714,
    # 'VHRED_reddit_casual': 2.694444444,
    # 'emoinfer_VHCR_casual': 2.692307692,
    # 'VHCR_reddit_casual': 2.615384615,
    # 'infersent_VHCR_casual': 2.533333333,
    # 'HRED_reddit_casual': 2.527272727,
    # 'emotion_VHCR_casual': 2.5,
    # 'infersent_HRED_casual': 2.5,

    # Cornell
    'emoinfer_VHCR_cornell' : 2.547619048 ,
    'infersent_VHCR_cornell' : 2.541666667 ,
    'emotion_VHRED_cornell' : 2.529411765 ,
    # 'emotion_VHCR_cornell': 2.5,
    # 'infersent_HRED_cornell': 2.388888889,
    # 'infersent_VHRED_cornell': 2.380952381,
# 'emoinfer_HRED_cornell': 2.346938776,
# 'emoinfer_VHRED_cornell': 2.333333333,
# 'emotion_HRED_cornell': 2.238095238,
# 'HRED_cornell': 2.181818182,
# 'VHCR_cornell': 2.132075472,
# 'VHRED_cornell': 2.02173913,
}

# Os pesos abaixo são baseados em dados piloto, antes de executar o estudo
# PREDEFINED_MODEL_WEIGHTS = {
# # Cornell
# 'HRED_cornell': 211,
# 'VHRED_cornell': 202,
# 'VHCR_cornell': 159,
# 'emotion_HRED_cornell': 157,
# 'emotion_VHRED_cornell': 998, # 1061 (ELSA_) + 137 (emoção_)
# 'emotion_VHRED_cornell_hparam': 200, # alocado de cima
# 'emotion_VHCR_cornell': 173,
# 'infersent_HRED_cornell': 48, # Não há como distinguir de casual, então forneceu 2/3 de um total de 73 aqui
# 'infersent_VHCR_cornell': 145, # Não há como distinguir de casual, então forneceu 2/3 do total de 220 aqui
# 'infersent_VHRED_cornell': 195, # Não há como distinguir de casual, então forneceu 2/3 do total de 296 aqui
# 'emoinfer_HRED_cornell': 36,
# 'emoinfer_VHRED_cornell': 261, # Não há como distinguir do casual, então forneceu 2/3 do total aqui
# 'emoinfer_VHCR_cornell': 283,
# 'input_only_HRED_cornell': 54, # Não há como distinguir, forneceu 1/2 do total de 108 aqui
# 'input_only_VHRED_cornell': 28, # Não há como distinguir, forneceu 1/2 do total de 55 aqui
# 'input_only_VHCR_cornell': 35, # Não há como distinguir, forneceu 1/2 do total de 69 aqui

# # Reddit casual
# 'HRED_reddit_casual': 113,
# 'VHRED_reddit_casual': 80,
# 'VHCR_reddit_casual': 67,
# 'emotion_HRED_casual': 59,
# 'emotion_VHRED_casual': 66, # 43 + 23 (ELSA_VHRED_reddi)
# 'emotion_VHCR_casual': 155, # 143 + 12 (ELSA_VHCR_reddit)
# 'infersent_HRED_casual': 25, # Não há como distinguir de cornell, então forneceu 1/3 do total de 73 aqui
# 'infersent_VHCR_casual': 75, # Não há como distinguir de cornell, então forneceu 1/3 do total de 220 aqui
# 'infersent_VHRED_casual': 101, # Não há como distinguir de cornell, então forneceu 1/3 do total de 296 aqui
# 'emoinfer_HRED_casual': 114,
# 'emoinfer_VHRED_casual': 112,
# 'emoinfer_VHCR_casual': 29,
# 'input_only_HRED_casual': 54, # Não há como distinguir, forneceu 1/2 do total de 108 aqui
# 'input_only_VHRED_casual': 28, # Não há como distinguir, forneceu 1/2 do total de 55 aqui
# 'input_only_VHCR_casual': 35, # Não há como distinguir, forneceu 1/2 do total de 69 aqui
#}


def  parse_args ():
    parser  =  argparse . ArgumentParser ()
    analisador . add_argument ( '--experience_path' , type = str , default = None ,
                        help = 'Caminho para um .csv contendo experiências' )
    analisador . add_argument ( '--save_path' , type = str , default = None ,
                        help = 'Caminho para salvar csv com recompensa computada' )
    analisador . add_argument ( '--models_base_path' , type = str , default = None ,
                        help = 'Caminho básico para pontos de verificação para cálculo da média do modelo.' )
    analisador . add_argument ( '--model_weights' , type = str , default = 'predefinido' ,
                        help = "Como ponderar as probabilidades de cada modelo. Pode"
                             "ser 'predefinido' ou 'proporcional'" )
    analisador . add_argument ( '--batch_size' , type = int , default = 32 )
    analisador . add_argument ( '--separate_datasets' , action = 'store_true' ,
                        help = "Se verdadeiro, não mescle as probabilidades dos modelos"  + \
                             "de conjuntos de dados diferentes" )
    analisador . set_defaults ( separate_datasets = FALSO )
    return  parser . parse_args ()


def  get_default_rl_config ():
    return  run_rl . parse_config_args ()


classe  ModelAverager :
    def  __init__ ( self , kwargs ):
        eu . kwargs  =  kwargs
        eu . separate_datasets  =  kwargs . separar_datasets
        
        # Carregar chatbots
        os . Environ [ 'BASE_PATH' ] =  kwargs . models_base_path
        do  modelo . model_avg_chatbots  importar  chatbots
        eu . chatbots  =  chatbots

        # Carregar buffers de conjunto de dados
        eu . dataset_buffs  = {}
        para  nome , modelo  em  chatbots . itens ():
            se  modelo . config . dados  não  em  si mesmo . dataset_buffs :
                print ( ' \ n Criando buffer para conjunto de dados' , model . config . data )
                buffer  =  replay_buffer . CsvReplayBuffer (
                    kwargs . experience_path , raw = False , config = model . config )
                print ( "Buffer contém" , len ( buffer . buffer ), "responses." )
                eu . dataset_buffs [ modelo . config . dados ] =  buffer
                eu . dataset_len  =  len ( buffer . buffer )

        # Obtenha pesos
        se  kwargs . model_weights  ==  'proporcional' :
            # Calcular a proporção de cada bot no conjunto de dados
            eu . pesos  =  compute_bot_proportion ( chatbots , csv_buff . buffer )
        elif  kwargs . model_weights  ==  'predefinido' :
            eu . pesos  =  PREDEFINED_MODEL_WEIGHTS 

            # Descartar bots que não serão agregados com base em pesos
            to_delete  = [ c  para  c  em  si . chatbots . keys () se  c  não  estiver em  si mesmo . pesos ]
            para  c  em  to_delete :
                del  self . chatbots [ c ]
        mais :
            print ( 'Erro!' , kwargs . model_weights , 'não é uma forma válida de ponderar ' ,
                "modelos. Use 'proporcional' ou 'predefinido'." )

        # Garanta a soma dos pesos em 1 para manter uma distribuição de probabilidade válida
        weight_values  = [ self . pesos [ k ] para  k  em  si mesmo . pesos . chaves ()]
        norm_weights  =  weight_values  /  np . soma ( weight_values )
        para  i , k  em  enumerar ( auto . pesos . teclas ()):
            eu . pesos [ k ] =  norm_weights [ i ]

    def  compute_bot_proportion ( self ):
        passar

    def  average_models ( self ):
        se  eu . separar_datasets :
            averaged_probs  =  dict . fromkeys ( self . dataset_buffs )
            # Não é possível atribuir o valor padrão de [] porque as listas serão compartilhadas
            para  k  em  si . dataset_buffs . chaves ():
                averaged_probs [ k ] = []
        mais :
            averaged_probs  = []
        
        i  =  0
        enquanto  eu  <  self . dataset_len :
            # Obtenha diferentes versões do lote para as diferentes tokenizações
            # esquemas para cada conjunto de dados
            dataset_batches  = {}
            para  conjunto de dados , buff  em  si mesmo . dataset_buffs . itens ():
                lote  =  lustre . get_batch_in_order (
                    eu . kwargs . batch_size )
                dataset_batches [ dataset ] =  self . extract_sentence_data ( lote )
                action_lens  =  dataset_batches [ dataset ] [ 1 ]

            se  eu . separar_datasets :
                batch_probs  =  dict . fromkeys ( self . dataset_buffs )
            mais :
                batch_probs  =  Nenhum

            para  nome , bot  em  si mesmo . chatbots . itens ():
                model_probs  =  self . run_model_on_sentences (
                    bot , dataset_batches [ bot . config . dados ])   # [total de palavras]

                weighted_probs  =  self . pesos [ nome ] *  model_probs . cpu (). entorpecido ()

                se  eu . separar_datasets :
                    if  batch_probs [ bot . config . data ] é  Nenhum :
                        batch_probs [ bot . config . data ] =  weighted_probs
                    mais :
                        batch_probs [ bot . config . dados ] + =  weighted_probs
                mais :
                    se  batch_probs  for  None :
                        batch_probs  =  weighted_probs
                    mais :
                        batch_probs  + =  weighted_probs

            # Coloque tudo de volta na frase apropriada
            # [batch_size, comprimento da frase]
            start  =  np . cumsum ([ 0 , * action_lens [: - 1 ]])
            se  eu . separar_datasets :
                para  k  em  averaged_probs . chaves ():
                    sentenças_prob  = [ batch_probs [ k ] [ s : s + l ]
                              para  s , l  no  zip ( iniciar , action_lens )]

                    # Acumule este lote
                    averaged_probs [ k ]. extend ( frase_probs )
            mais :
                sentenças_prob  = [ batch_probs [ s : s + l ]
                              para  s , l  no  zip ( iniciar , action_lens )]
                # Acumule este lote
                averaged_probs . extend ( frase_probs )

            i  + =  self . kwargs . tamanho do batch

        # Verifique se temos as probabilidades apropriadas que correspondem ao 
        # comprimentos de frase para tudo no buffer
        para  d , b  em  si mesmo . dataset_buffs . itens ():
            imprimir ( "Verificação dupla" , d , "buffer do conjunto de dados" )
            para  i  no  intervalo ( len ( b . ação )):
                action_len  =  lista ( b . ação [ i ]). índice ( EOS_ID ) +  1
                se  eu . separar_datasets :
                    avg_len  =  len ( averaged_probs [ d ] [ i ])
                mais :
                    avg_len  =  len ( averaged_probs [ i ])
                afirmar ( action_len  ==  avg_len ), error_message
                error_message  =  "Existem"  +  str ( action_len ) + \
                    "palavras no buffer no índice"  +  str ( i ) +  "mas"  + \
                    str ( avg_len ) +  "probs"
        print ( "Probabilidades de ação calculadas pela média do modelo!" )

        para  conjunto de dados , buff  em  si mesmo . dataset_buffs . itens ():
            se  não  for eu . separar_datasets :
                lustre . tampão [ 'model_averaged_probs' ] =  averaged_probs
            mais :
                para  d , avg_p  em  averaged_probs . itens ():
                    lustre . buffer [ 'model_averaged_probs_'  +  d ] =  avg_p
            return  buff   # Pode retornar qualquer buffer, as informações relevantes são as mesmas

    def  extract_sentence_data ( self , batch ):
        com  tocha . no_grad ():
            # Extrair informações do lote 
            actions  =  to_var ( torch . LongTensor ( batch [ 'action' ]))   # [batch_size]
            action_lens  =  batch [ 'action_lens' ]

            conversas  = [ np . concatenar (
                ( conv , np . atleast_2d ( lote [ 'ação' ] [ i ])))
                para  i , conv  em  enumerar ( lote [ 'estado' ])]
            sent_lens  = [ np . concatenar (
                ( lente , np . atleast_1d ( lote [ 'action_lens' ] [ i ])))
                para  i , lente  em  enumerar ( lote [ 'state_lens' ])]
            target_conversations  = [ conv [ 1 :] para  conv  em  conversas ]
            targets  = [ enviado  para  conv  em  target_conversations  para  enviado  na  conv ]
            targets  =  to_var ( tocha . LongTensor ( alvos ))
            conv_lens  = [ len ( c ) -  1  para  c  em  conversas ]
            conv_lens  =  to_var ( torch . LongTensor ( conv_lens ))

            # Calcular entradas não variacionais
            hred_convs  = [ conv [: - 1 ] para  conv  em  conversas ]
            hred_sent_lens  =  np . concatenar ([ l [: - 1 ] para  l  em  sent_lens ])
            hred_sent_lens  =  to_var ( torch . LongTensor ( hred_sent_lens ))
            hred_sentences  = [ enviado  para  conv  em  hred_convs  para  enviado  em  conv ]
            hred_sentences  =  to_var ( tocha . LongTensor ( hred_sentences ))
            
            # Calcular entradas variacionais
            sent_lens  =  np . concatenar ([ l  para  l  em  sent_lens ])
            sent_lens  =  to_var ( torch . LongTensor ( sent_lens ))
            frases  = [ enviado  para  conv  em  conversas  para  enviado  em  conv ]
            sentenças  =  to_var ( tocha . LongTensor ( sentenças ))

            return ( ações , action_lens , sentenças , sent_lens , hred_sentences ,
                    hred_sent_lens , alvos , conv_lens )

    def  run_model_on_sentences ( self , bot , batch_tensors ):
        com  tocha . no_grad ():
            ( ações , action_lens , sentenças , sent_lens , hred_sentences ,
            hred_sent_lens , targets , conv_lens ) =  batch_tensors
            se  bot . config . modelo  não está  em  VariationalModels :
                sentenças  =  hred_sentences
                sent_lens  =  hred_sent_lens

            # Executar modelo
            saídas  =  bot . solucionador . modelo ( sentenças , sent_lens , conv_lens , alvos ,
                                    rl_mode = True )
            logits  =  saídas [ 0 ]

            # Índice para obter apenas os valores de saída para as ações realizadas (última frase
            # em cada conversa)
            iniciar  =  tocha . cumsum ( tocha . gato (
                ( to_var ( conv_lens . data . new ( 1 ). zero_ ()), conv_lens [: - 1 ])), 0 )
            action_logits  =  tocha . empilhar (
                [ logits [ s + l - 1 ,:,:]
                para  s , l  em  zip ( start . data . tolist (), conv_lens . data . tolist ())],
                0 )   # [num_sentences, max_sent_len, vocab_size]

            # Limite pelo comprimento real da frase (remova o preenchimento) e aplique
            # lista longa de palavras
            word_logits  =  tocha . gato (
                [ Action_logits [ i ,: l ,:] para  i , l  em  enumerar ( action_lens )],
                0 )   # [total de palavras, tamanho_do_ vocabulário]
            palavra_ações  =  tocha . gato (
                [ Acções [ i ,: l ] para  i , l  em  enumerar ( action_lens )],
                0 )   # [total de palavras]

            # Pegue softmax para obter a distribuição de probabilidade 
            # [total_words, vocab_size]
            word_probs  =  tocha . nn . funcional . softmax ( word_logits , 1 )

            # Extraia os valores q correspondentes às ações realizadas
            relevant_words  =  word_probs . reunir (
                1 , palavra_ações . desaperte ( 1 )). squeeze ()   # [total de palavras]

            retornar  palavras_relevantes


if  __name__  ==  '__main__' :
    "" "Carregar buffer de repetição de experiência do arquivo e computar recompensas nele" ""
    kwargs  =  parse_args ()

    ma  =  ModelAverager ( kwargs )

    # Calcule as probabilidades médias do modelo
    buffer  =  ma . Average_models ()

    # Salvar em arquivo csv processado
    buffer . buffer . to_csv ( kwargs . save_path )