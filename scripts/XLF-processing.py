#!/usr/bin/env python
# coding: utf-8

# In[1]:


#from xml.dom import minidom
from bs4 import BeautifulSoup
import re
import os
import sys

# In[42]:


xlf_path = sys.argv[1]
output_path = sys.argv[2]
with open(xlf_path) as f:
    content = f.read()

soup = BeautifulSoup(content)
segments = soup.findAll("trans-unit")


# In[46]:


sentences = []
for segment in segments:
    target = segment.find("target")
    full_sentence = "".join([m.text for m in target.find_all("mrk")])
    if "\n" in full_sentence:
        print(full_sentence)
    full_sentence = full_sentence.replace('\n','')
    sentences.append(full_sentence)


# In[44]:


with open(output_path,'w') as f:
    for s in sentences:
        f.write(s+"\n")


# In[45]:


len(sentences)


# In[ ]:




