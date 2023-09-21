import csv
import matplotlib.pyplot as plt

# Specifica il percorso del file CSV da aprire
file_csv = 'data.csv'

# Definisci delle liste vuote per i dati che desideri estrarre
states = []
positive = []
negative = []

# Apri il file CSV in modalità di lettura
with open(file_csv, 'r', newline='') as csvfile:
    # Crea un oggetto lettore CSV
    csvreader = csv.DictReader(csvfile)
    
    # Itera sulle righe del file CSV
    for row in csvreader:
        # Estrai i dati dalle colonne specifiche
        state = row['state']
        pos = int(row['positive'])
        neg = int(row['negative'])
        
        # Aggiungi i dati alle rispettive liste
        states.append(state)
        positive.append(pos)
        negative.append(neg)

# Crea un grafico a linee per i dati positivi e negativi
plt.figure(figsize=(10, 6))
plt.plot(states, positive, label='Positive', marker='o', color='b', linestyle='-')
plt.plot(states, negative, label='Negative', marker='x', color='r', linestyle='-')

# Aggiungi etichette e legenda al grafico
plt.xlabel('State')
plt.ylabel('Count')
plt.title('Positive vs. Negative COVID-19 Cases by State')
plt.legend()

# Mostra il grafico
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()
