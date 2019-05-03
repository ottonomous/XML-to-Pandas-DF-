#!/usr/bin/env python
# coding: utf-8

# In[87]:


import xml.etree.ElementTree as ET
# load and parse the file
xmlTree = ET.parse('/Users/upmetrics/Desktop/990AllXML/201703039349200245_public.xml')

elemList = []

for elem in xmlTree.iter():
    elemList.append(elem.tag) # indent this by tab, not two spaces as I did here

# now I remove duplicities - by convertion to set and back to list
elemList = list(set(elemList))

cols2 = {}
for item in elemList:
    cols2.update({item : [0,1]})
df2 = pd.DataFrame(data = cols2)
cols = df2.columns.astype(list)


# In[88]:


from xml.etree import cElementTree as ElementTree

def parser(data, tags):
    tree = ElementTree.iterparse(data, events=('start', 'end'))
    _, root = next(tree)
    
    for event, node in tree:
        if node.tag in tags:
            yield node.tag, node.text
        root.clear()


# In[96]:


pd.DataFrame(parser('/Users/upmetrics/Desktop/990AllXML/201703039349200245_public.xml', elemList)))


# In[89]:


DF_list = []

import os 
for filename in os.listdir('/Users/upmetrics/Desktop/990AllXML copy/'):
     DF_list.append(pd.DataFrame(parser('/Users/upmetrics/Desktop/990AllXML copy/{}'.format(filename), elemList)))

Total = pd.concat(DF_list)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




