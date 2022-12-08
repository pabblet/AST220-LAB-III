from astropy.io import ascii
import matplotlib.pyplot as plt

age=input('Ingrese edad: ') #4-> 4[Gyr], 0-> varias edades

plt.style.use('ggplot')
data= ascii.read('Stars.csv')
r= data['r']
g= data['g']
plt.scatter(g-r, r, s=1, color='#444444', label='data')

parsec= ascii.read('Parsec'+age+'.dat')
rMag= parsec['rmag']
gMag= parsec['gmag']

if age== '4':
    plt.plot(gMag-rMag, rMag+9.61, color='#BA66C0', ls='--', lw=2, label='Parsec model '+age+' [Gyr]')
elif age== '0':
    plt.scatter(gMag-rMag, rMag+9.61, color='#BA66C0', s=1, label='Parsec models with different ages')

plt.xlabel('g-r')
plt.ylabel('r')
plt.xlim(0.0, 2.0)
plt.ylim(23, 13)
plt.legend(loc='lower left')
plt.show()