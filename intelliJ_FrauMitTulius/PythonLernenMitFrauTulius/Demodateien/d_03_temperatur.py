# beispiel wird wieder aufggriffen bei try (Exception)

print ("Durchschnittstemperatur")
t1 = float(input("Wert 1: "))
t2 = float(input("Wert 2: "))
t3 = float(input("Wert 3: "))
#print("Eingabe :", t1, t2, t3)
#print("Eingabe:{0} °C, {1} °C, {3} °F".format(t1, t2,t3))
meinString = "Eingabe:{0} °C, {1} °C, {2} °F".format(t1,t2,t3)
print(meinString)
d=(t1+t2+t3)/3
#print("Durchschnitt:",(t1+t2+t3)/3)
print("Durchschnitt:",d)