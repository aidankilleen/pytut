import warnings
import matplotlib.pyplot as plt
import numpy as np
from pylj import md, util, sample, forcefields

warnings.filterwarnings('ignore')


r = np.linspace( 3e-10, 8e-10, 100 )
E = forcefields.lennard_jones(r, [1.36e-134, 9.27e-78])


plt.plot( r, E )
plt.xlabel( '$r/m$' )
plt.ylabel( '$E/J$' )
plt.show()