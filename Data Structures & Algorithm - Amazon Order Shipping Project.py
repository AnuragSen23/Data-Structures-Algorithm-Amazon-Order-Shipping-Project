#!/usr/bin/env python
# coding: utf-8

# # Data Structures & Algorithm - Amazon Order Shipping Project

# Data Structure concept of Priority Queue was employed to arrange the Order of Product delivery of customers on the basis of their Prime Subscription.

# ### submitted by: Anurag Sen (as5864@srmist.edu.in) 

# User_Details - 
# 1. User ID
# 2. Name
# 3. E-mail Address
# 4. isPrime categorisation (1 if non-Prime; 0 if Prime)
# 5. details on Order_Cart.

# ### • User_ID Generation 

# In[64]:


import string
import random

def generate_id():
    id1 = ''
    id2 = ''
    p1 = list(string.ascii_letters)
    p2 = list(string.digits)

    for i in range(2):
        id1 += random.choice(p1)
    for j in range(4):
        id2 += random.choice(p2)
    uid = id1+id2
    return uid
    
#generate_id()


# ### User Registration and Order Placing 

# In[65]:


class Amazon:
    def __init__(self):
        self.uid = None
        self.Name = None
        self.email = None
        self.Order_cart = None
        self.isPrime = 1
        
    def get_details(self):
        self.uid = generate_id()
        self.Name = input("Enter your name: ")
        self.email = input("Enter e-mail address: ")
        
    def buy_items(self):
        self.Order_cart = [i for i in input("Enter the items you'd like to order: ").split(', ')]
        
    def get_prime(self):
        self.isPrime = 0


# In[66]:


user_list = []


# ### Sorting on Prime | Non-Prime Delivery - Priority Queue

# In[67]:


def find_user_pos(new_user):     
    user_count = len(user_list)
    pos = 0
    for i in range(user_count):                 #looping operation has Time Complexity: O(n)
        if user_list[i].isPrime <= new_user.isPrime:
            pos += 1
    return pos


# In[68]:


res = 'yes'
while res == 'yes':
    new_user = Amazon()
    new_user.get_details()
    
    resp = input("Would you like to place orders?: ")
    resp = resp.lower()
    
    if resp == 'yes':
        new_user.buy_items()
        
    resp = input("Do you want to buy Prime and enjoy Prime benefits?: ")
    resp = resp.lower()

    if resp == 'yes':
        new_user.get_prime()
    
    pos = find_user_pos(new_user)
    user_list.insert(pos, new_user)
    #user_list.append(new_user)
        
    res = input("Add more users?: ")
    print("\n")
    res = res.lower()
    
        
    


# In[69]:


print(user_list)


# In[70]:


print("Delivery Order: ")
for i in user_list:
    print(i.Name, i.isPrime, i.Order_cart)


# ### Prime | Non-Prime Delivery - Priority Queue using Sorted function

# In[71]:


user_list = sorted(user_list, key= lambda x: x.isPrime) #Sorting algorithms like Quick sort with Time complexity: O(nlogn)
print("Sorted Delivery orders: ")
for i in user_list:
    print(i.Name, i.isPrime)


# ### Conclusion 

# In[73]:


import datetime
A = datetime.datetime.now()
date = A.strftime("%d/%m/%Y")
time = A.strftime("%H:%M")
day = A.strftime("%A")

for i in user_list:
    if i.isPrime == 0:
        print(f"Hello {i.Name} (Customer ID: {i.uid}),")
        print(f"Your order(s) {i.Order_cart} were confirmed on {date} [{day}], at {time} and has been shipped under Prime delivery.")
        print("\n")
    else:
        print(f"Hello {i.Name} (Customer ID: {i.uid}),")
        print(f"Your order(s) {i.Order_cart} were confirmed on {date} [{day}], at {time} and has been shipped.")
        print("Switch to Prime and get your products delivered quicker!")
        print("\n")


# In[ ]:




