import pandas as pd
import matplotlib.pyplot as plt

# Citirea fișierului CSV
df = pd.read_csv(r"C:\Users\Admin\Downloads\data.csv")

# 1. Plotează toate valorile
plt.figure()
df.plot()
plt.title("Toate valorile din fișier")
plt.legend(title="Parametri")
plt.show()

# 2. Plotează primele X valori (X = 6)
plt.figure()
df.head(6).plot()
plt.title("Primele 6 valori")
plt.legend(title="Parametri")
plt.show()

# 3. Plotează ultimele Y valori (Y = 12) pentru coloanele 'Durata' și 'Puls'
plt.figure()
df[['Durata', 'Puls']].tail(12).plot()
plt.title("Ultimele 12 valori pentru coloanele Durata și Puls")
plt.legend(title="Parametri")
plt.show()
