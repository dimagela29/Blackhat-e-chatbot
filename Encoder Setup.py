import os
import shutil
from pathlib import path
import tensorflow as tf
import tensorflow_hub as hub

project_dir = path(_file_).resolve().parent.parent
USE_dir = project_dir.joinpath('Sentenca Universal do encoder')
os.environ["TFHUB_CACHE_DIR"] = str(USE_dir)

#download do encoder
encoder = hub.Module("https://tfhub.dev/google/universal-sentence-encoder-large/3")

#checando erros 
embeddings = encoder([
        "the quick brown fox jump pver the lazy dog."
        "I am a sentence for wich I would like to get its embedding"])

with tf.Session() as sess:
    sess.run([tf.global_variable_initializer(), tf.tables_initializer()])
    embs = sess.run(embeddings)
    assert(embs.shape ==  (2, 512))
    
#move o encoder para saida temporaria do diretorio usando Use como função
temp_dir = [USE_dir.joinpath(dir) for dir in os.listdir(USE_dir)if os.path.isdir(USE_dir.joinpath(dir))][0]
for f in os.listdir(temp_dir):
    shutil.move(str(temp_dir.joinpath(f)),USE_dir)
    
print('#' * 10)
print('#' * 10)
print('Done installing Universal Sentence Encoder')
print('#' * 10)
print('#' * 10)
      