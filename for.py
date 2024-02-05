students={"male":["Tom","Sam","Franco","Adam"],
    "female":["Sarah","Tara","Lilly","Lavya"]
    }
for key in students.keys():
    for name in students[key]:
        if 'a' in name:
            print(name)
