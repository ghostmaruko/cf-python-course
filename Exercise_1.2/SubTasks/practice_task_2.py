# Step 1: Creare la tupla con la popolazione mondiale
total_population = (
    6789088686,
    6872767093,
    6956823603,
    7041194301,
    7125828059,
    7210581976,
    7295290765,
    7379797139,
    7464022049,
    7547858925,
    7631091040,
    7713468100,
    7794798739
)

# Step 2: Slice (primo terzo dei dati)
sliced_total_population = total_population[:4]

# Step 3: Trova il valore massimo
max_population = max(sliced_total_population)

# Step 4: Stampare i risultati
print("Total population:", total_population)
print("Sliced population:", sliced_total_population)
print("Maximum population in slice:", max_population)
