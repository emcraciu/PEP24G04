objects = ["Masa", 5, "Scaun", 4.5, [5, 6, 7], 8]
for item in objects:
    print(f"Tipul obiectului {item} este {type(item).__name__}")
    if type(item) == list:
        for i in item:
            print(f"Tipul obiectului {i} este {type(i).__name__}")
