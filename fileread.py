f = open("countries.txt")

countries=[]

for line in f:
   line = line.strip()
   countries.append(line)
   
f.close()

print(len(countries))

for country in countries:
    if country[0] == "U":
       print(country)
