#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2023-07-17 04:48:17
# @Author  : 崔立波 (baiyuexingchen@gmail.com)
# @Link    : http://blog.sina.com.cn/dejavu1
# @Version : 1


from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio
import sys
import os
###############################################
#以下开始
# read XXX.txt
path=sys.argv[1]
file_path= os.path.dirname(path)
file_name = os.path.basename(path).split(".")[0]
data = ''
with open(path,'r',encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        data += line
print(data)
# download and load all models
preload_models()

# generate audio from text
text_prompt = data
audio_array = generate_audio(text_prompt)

# save audio to disk
write_wav(file_path+"\\"+file_name+".wav", SAMPLE_RATE, audio_array)
  
# play text in notebook
Audio(audio_array, rate=SAMPLE_RATE)