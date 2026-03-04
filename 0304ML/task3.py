customers = [
    {"name": "Apex Corp",    "region": "East",  "purchases": 34_000},
    {"name": "BlueSky LLC",  "region": "West",  "purchases": 87_500},
    {"name": "CoreTech",     "region": "East",  "purchases": 12_200},
    {"name": "Delta Group",  "region": "West",  "purchases": 56_000},
    {"name": "Edge Systems", "region": "East",  "purchases": 29_800},
]

east=[n for n in customers if n["region"]=="East"]
total=sum(n["purchases"] for n in east)/len(east)

customers[{"name"}]="Fusion Inc"
customers[{"region"}]="North"
customers[{"purchases"}]=44_000

print(east)
print(total)
print(customers)