#!/usr/bin/env python
# coding: utf-8

# # API Scavenger Game
# 
# ## Challenge 1: Fork Languages
# 
# You will find out how many programming languages are used among all the forks created from the main lab repo of your bootcamp.

# In[ ]:


# import libraries here


# Assuming the main lab repo is ironhack-datalabs/madrid-oct-2018, you will:
# 
# #### 1. Obtain the full list of forks created from the main lab repo via Github API.

# In[ ]:


# your code here


# #### 2. Loop the JSON response to find out the language attribute of each fork. Use an array to store the language attributes of each fork.
# Hint: Each language should appear only once in your array.
# Print the language array. It should be something like: ["Python", "Jupyter Notebook", "HTML"]

# In[ ]:


# your code here


# ## Challenge 2: Count Commits
# Count how many commits were made in the past week.
# #### 1. Obtain all the commits made in the past week via API, which is a JSON array that contains multiple commit objects.

# In[ ]:


# your code here


# #### 2. Count how many commit objects are contained in the array.

# In[ ]:


# your code here


# ## Challenge 3: Hidden Cold Joke
# 
# Using Python, call Github API to find out the cold joke contained in the 24 secret files in the following repo:
# 
# https://github.com/ironhack-datalabs/scavenger
# 
# The filenames of the secret files contain .scavengerhunt and they are scattered in different directories of this repo. The secret files are named from .0001.scavengerhunt to .0024.scavengerhunt. They are scattered randomly throughout this repo. You need to search for these files by calling the Github API, not searching the local files on your computer.
# 
# #### 1. Find the secret files.

# In[ ]:


# your code here


# #### 2.  Sort the filenames ascendingly.

# In[ ]:


# your code here


# #### 3. Read the content of each secret files into an array of strings.

# In[ ]:


# your code here


# #### 4. Concatenate the strings in the array separating each two with a whitespace.

# In[ ]:


# your code here


# #### 5. Print out the joke.

# In[ ]:


# your code here

