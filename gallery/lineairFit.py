# Open this file with jeroenvantilburg.nl/ppg or any python environment
import matplotlib.pyplot as plt # do not modify; required by ppg
import numpy as np

# Parameters
a_true = 2.234
n = 7
x_min, x_max = 1, 10
ruis = 1.5
force_origin = True # Zet op False als je een gewone lineaire fit wilt

# Data genereren
x = np.linspace(x_min, x_max, n)
y_exact = a_true * x
y_meet = y_exact + np.random.uniform(-ruis, ruis, size=n)

# Lineaire fit berekenen (coefficienten)
if force_origin:
  # Alleen helling berekenen: a = (x·y) / (x·x)
  a_fit = np.sum(x * y_meet) / np.sum(x * x)
  coeffs = np.array([a_fit,0])  
else:
  # Gewone lineaire fit met intercept
  coeffs = np.polyfit(x, y_meet, 1)

# Meetpunten plotten
plt.clf()
plt.axis([0, 12, -0, 30]) # x-as van 0 tot 12, y-as van -5 tot 30
plt.scatter(x, y_meet, color="Blue", marker="+", s=60, label='Meetpunten')

# Fit resultaat plotten
fit_fn = np.poly1d(coeffs)
x_fit = np.linspace(plt.axis()[0], plt.axis()[1], 100)
y_fit= fit_fn(x_fit)
plt.plot(x_fit, y_fit, "r--", label='Lineaire fit' + (' door oorsprong' if force_origin else ''))

# Labels, titels, etc.
plt.xlabel('t (s)', loc='right', fontsize=16)
plt.ylabel('x (m)', loc='top', fontsize=16)
plt.title('Lineaire fit ' + ('(geforceerd door oorsprong)' if force_origin else '(met intercept)'))
plt.legend()
plt.grid(True)

plt.show() # last line; do not modify; required by ppg