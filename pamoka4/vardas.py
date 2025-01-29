my_dictionary = {
    "obuolys": "vaisius, augantis ant medžių",
    "knyga": "rinkinys atspausdintų lapų, susegtų kartu, turintis tekstą ar paveikslėlius",
    "kompiuteris": "elektroninis įrenginys, skirtas duomenims saugoti ir apdoroti",}

while True:
    enter_input = input("Įveskite žodį, arba pabaiga: ")
    if enter_input.lower() == 'pabaiga':
        print("Programa baigta")
        break
    elif enter_input in my_dictionary:
        print(f"Žodžio {my_dictionary.get(enter_input)} reikšmė: {my_dictionary.get(enter_input)}")
        break
    else:
        print(f"Žodžio  reikšmės nėra žodyne.")