# -*- coding: utf-8 -*-
"""
Created on Tue May 27 11:07:32 2025

@author: Orion-Trd-1
"""

import numpy as np
import matplotlib.pyplot as plt

#Normal distribution ,172,8 cm standerd deviation ,300heights
heights = np.random.normal(172,8,300)


plt.boxplot(heights)
plt.show()