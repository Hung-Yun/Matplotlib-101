
"""

Plotting with categorical variables
It is also possible to create a plot using categorical variables.
Matplotlib allows you to pass categorical variables directly to many plotting functions.

"""

import matplotlib.pyplot as plt

names = ['group_a', 'group_b', 'group_c'] # This would be the index
values = [1, 10, 100] # This would be the value of each column

# We are going to create a figure through plt.figure().
# figsize=(9,3) means the 
plt.figure(2, figsize=(9,3))

# 131 means there are 1x3 subplots in the figure, and we are now plotting the 1st position.
plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)

plt.suptitle('Categorical Plotting') # The attribute is suPtitle, not suBtitle.
plt.show() #Categorical_variable
