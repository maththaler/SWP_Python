from enum import Enum

class Gender(Enum):
    Male = 0
    Female = 1
    
class Person:
    person_count = 0
    gender_count = {Gender.Male: 0, Gender.Female: 0}
    def __init__(self, firstname, lastname, gender) -> None:
        Person.person_count += 1
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        Person.gender_count[gender] += 1

    def check_relative_gender():
        return Person.gender_count[Gender.Male] / Person.person_count, \
            Person.gender_count[Gender.Female] / Person.person_count

class Mitarbeiter(Person):
    mitarbeiter_count = 0
    def __init__(self, firstname, lastname, gender, strength) -> None:
        Mitarbeiter.mitarbeiter_count += 1
        super().__init__(firstname, lastname, gender)
        self.abteilung = None
        self.strength = strength

class Abteilungsleiter(Mitarbeiter):
    abteilungsleiter_count = 0
    def __init__(self, firstname, lastname, gender, strength) -> None:
        Abteilungsleiter.abteilungsleiter_count += 1
        super().__init__(firstname, lastname, gender, strength)

class Abteilung:
    abteilung_count = 0
    abteilung_strength = {}
    def __init__(self, name, abteilungsleiter) -> None:
        Abteilung.abteilung_count += 1
        self.mitarbeiter = []
        self.abteilungsleiter = abteilungsleiter
        self.name = name
        self.abteilungsleiter.abteilung = self

    def add_mitarbeiter(self, mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)
        mitarbeiter.abteilung = self
        Abteilung.abteilung_strength[self.name] = self.get_mitarbeiter_strength()

    def get_mitarbeiter_strength(self):
        count = 0
        for mitarbeiter in self.mitarbeiter:
            count += mitarbeiter.strength
        return count


if __name__ == "__main__":
    p1 = Person("Mathias", "Thaler", Gender.Male)
    p1 = Person("Anna", "Huber", Gender.Female)
    m1 = Mitarbeiter("Michael", "Schwanninger", Gender.Male, 1)
    m2 = Mitarbeiter("Lohannes", "Tamerl", Gender.Male, 90)
    al1 = Abteilungsleiter("Matthias", "Zoller", Gender.Male, 50)
    a1 = Abteilung("Abteilung 1", al1)
    a2 = Abteilung("Abteilung 2", al1)
    a1.add_mitarbeiter(m1)
    a1.add_mitarbeiter(m2)
    #print(al1.abteilung.abteilungsleiter.firstname)
    print(f"Anzahl Mitarbeiter: {Mitarbeiter.mitarbeiter_count}")
    print(f"Anzahl Abteilungsleiter: {Abteilungsleiter.abteilungsleiter_count}")
    print(f"Anzahl Abteilungen: {Abteilung.abteilung_count}")
    print(f"Stärkste Abteilung: {max(Abteilung.abteilung_strength)}")
    print(f"Prozentanteill Männer Frauen: {Person.check_relative_gender()}")