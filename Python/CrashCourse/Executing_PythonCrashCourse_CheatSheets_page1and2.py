
# coding: utf-8

# # BEGINNER'S PYTHON CHEAT SHEET

# In[1]:


# pages 1 & 2


# In[3]:


#Variables and Strings
print('Hello World')


# In[4]:


msg = 'Hello world'
msg


# In[5]:


first_name = 'Brian' 
last_name = 'Cox' 
full_name = first_name + ' ' + last_name 
full_name


# In[6]:


bikes = ['trek', 'redline', 'giant']
first_bike = bikes[0]
first_bike
last_bike = bikes[-1]
last_bike


# In[7]:


for bike in bikes:
    print(bike)


# In[8]:


bikes2 = [] 
bikes2.append('cannondale') 
bikes2.append('specialized') 
bikes2.append('k2')
print(bikes2)


# In[9]:


squares = [] 
for x in range(1, 11): 
    squares.append(x**2)
squares


# In[10]:


finishers = ['Don', 'Kris', 'Matt', 'Joe'] 
first_two = finishers[:2]
first_two


# In[11]:


copy_of_bikes = bikes[:]
copy_of_bikes


# In[12]:


# TUPLE
dimensions = (1920, 1080)
dimensions


# In[13]:


x = 3.14
if x <= 42:
    print("The variable x is not less or equal to 42")
    if x != 42:
        print("The variable x is not equal to 42")
print(f"The variable x is equal to {x}")


# In[14]:


'trek' in bikes


# In[15]:


'surly' in bikes


# In[16]:


game_active = True 
can_edit = False

game_active


# In[17]:


# DICTIONARY
alien = {'color': 'green', 'points': 5}
print("The alien's color is " + alien['color'])
alien['x_position'] = 0
alien


# In[20]:


# Looping through all key-value pairs
fav_numbers = {'Sharon': 3.14, 'Vale': 2.81} 
for name, number in fav_numbers.items(): 
    print(name + ' loves ' + str(number))


# In[21]:


# Looping through all keys

for name in fav_numbers.keys(): 
    print(name + ' loves a number')


# In[22]:


# Looping through all values

for number in fav_numbers.values(): 
    print(str(number) + ' is a favorite')


# In[24]:


# USER INPUT
name = input("What's your name? ") 
print("Hello, " + name + "!")


# In[25]:


age = input("How old are you? ") 
age = int(age) 

pi = input("What's the value of pi? ") 
pi = float(pi)
pi


# In[26]:


# WHILE LOOPS
current_value = 1 
while current_value <= 5: 
    print(current_value) 
    current_value += 1


# In[27]:


msg = '' 
while msg != 'quit': 
    msg = input("What's your message? ") 
    print(msg)


# In[28]:


# FUNCTIONS
def greet_user():
    """Display a simple greeting.""" 
    print("Hello!") 
greet_user()


# In[29]:


def greet_user(username): 
    """Display a personalized greeting.""" 
    print("Hello, " + username + "!") 
greet_user('SDK')


# In[30]:


def make_pizza(topping='bacon'): 
    """Make a single-topping pizza.""" 
    print("Have a " + topping + " pizza!") 

make_pizza() 
make_pizza('pepperoni')


# In[31]:


def add_numbers(x, y): 
    """Add two numbers and return the sum.""" 
    return x + y 

sum = add_numbers(3, 5) 
print(sum)


# In[34]:


# CLASSES
class Dog(): 
    """Represent a dog.""" 
    def __init__(self, name): 
        """Initialize dog object.""" 
        self.name = name 
    def sit(self): 
        """Simulate sitting.""" 
        print(self.name + " is sitting.") 

my_dog = Dog('Remi') 
print(my_dog.name + " is a great dog!") 
my_dog.sit()


# In[35]:


### Inheritance
class SARDog(Dog): 
    """Represent a search dog.""" 
    def __init__(self, name): 
        """Initialize the sardog.""" 
        super().__init__(name) 
    def search(self): 
        """Simulate searching.""" 
        print(self.name + " is searching.") 

my_dog = SARDog('Remi')
print(my_dog.name + " is a search dog.") 
my_dog.sit() 
my_dog.search()


# In[36]:


pwd


# In[37]:


get_ipython().magic('pwd')
# WORKING WITH FILES
filename = 'sharon_d_kenny.txt' 
with open(filename, 'a') as file_object: 
    with open(filename, 'w') as file_object:
        file_object.write("Jeg elsker Python\n")
        
file_object.close()
print("file closed\n")

with open(filename, 'r') as file_object2: 
    lines = file_object2.readlines() 
for line in lines:
    print(line)


# In[39]:


# EXCEPTIONS
prompt = "How many tickets do you need? " 
num_tickets = input(prompt) 
try: 
    num_tickets = int(num_tickets) 
except ValueError: 
    print("Please try again.") 
else: 
    print("Your tickets are printing.")

