def createLevel(db, Level, Qubits, Monsters, Gates, Description, Success, Failure):
    entry = Level(Qubits=Qubits, Monsters=Monsters, Gates=Gates, Description=Description, Success=Success, Failure=Failure)
    db.session.add(entry)
    db.session.commit()
    print(entry)
    return 1

def createAllLevels(db, Level):
    createLevel(db, Level, 1, 5, "", "Welcome to the first level!", "Success! Good job!", "Try again! You were really close!")
    createLevel(db, Level, 2, 10, "", "Welcome to the second level!", "Success! Good job!", "Try again! You were really close!")
    return "Done"

