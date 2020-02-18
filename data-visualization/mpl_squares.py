import matplotlib.pyplot as plt

# squares = [1, 4, 9, 16, 25]
# fig, ax = plt.subplots()
# ax.plot(squares)

# plt.show()

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

"""
    >>> import matplotlib.pyplot as plt
    >>> plt.style.available
    ['Solarize_Light2', 'seaborn-white', 'seaborn-pastel', 'seaborn-muted', 
    'seaborn-whitegrid', 'classic', 'seaborn-colorblind', 'seaborn-paper', 
    'ggplot', 'dark_background', '_classic_test', 'fivethirtyeight', 'seaborn-deep', 
    'bmh', 'tableau-colorblind10', 'seaborn-poster', 'fast', 'seaborn-darkgrid', 
    'grayscale', 'seaborn-notebook', 'seaborn', 'seaborn-bright', 'seaborn-ticks', 
    'seaborn-dark', 'seaborn-dark-palette', 'seaborn-talk']
"""
plt.style.use('seaborn')

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=4)

plt.show()