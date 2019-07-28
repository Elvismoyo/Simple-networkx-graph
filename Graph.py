#!/usr/bin/env python
# coding: utf-8

# In[49]:


import networkx as nx
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

G = nx.Graph()

G.add_node('Berlin')
G.add_node('Madrid')
G.add_node('Quito')
G.add_node('London')
G.add_node('Helsinki')
G.add_node('Sofia')
G.add_node('Tokyo')
G.add_node('Oslo')
G.add_node('Stockholm')
G.add_node('Monaco')

G.add_edge('Monaco','Stockholm')
G.add_edge('Stockholm','Madrid')
G.add_edge('Madrid','Oslo')
G.add_edge('Oslo','Tokyo')
G.add_edge('Tokyo','Helsinki')
G.add_edge('Helsinki','Quito')
G.add_edge('Quito','Monaco')
G.add_edge('Monaco','London')
G.add_edge('London','Sofia')
G.add_edge('Sofia','Berlin')
G.add_edge('Berlin','Stockholm')
G.add_edge('Stockholm','Tokyo')
G.add_edge('Tokyo','Monaco')
G.add_edge('Oslo','Helsinki')
G.add_edge('Quito','Tokyo')
G.add_edge('Tokyo','Madrid')
G.add_edge('Tokyo', 'Sofia')

nx.draw(G, with_labels= True, font_weight="bold")
plt.show()







