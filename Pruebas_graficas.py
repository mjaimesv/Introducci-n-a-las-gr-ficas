import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

print(random.random())

random_list = []
for x in range(0,1000):
    # print(x)
    # print(random.random())
    random_list.append(random.random())

    print(random_list)

sns.histplot(y=random_list,
             alpha=0.5,
             # kde=True,
             element="step",
             color="darkgreen"
             )
plt.savefig('prueba.png',)
plt.show()



