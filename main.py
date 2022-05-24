class Ksiazka:

    def __init__(self, tytul, autor, rok_wydania):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania

    def __str__(self):
        return "'" + self.tytul + "', '" + self.autor + "'"

    def __eq__(self, other):
        return self.tytul == other.tytul

    def __hash__(self):
        return hash(len(self.tytul) * len(self.autor))


class Biblioteka:
    def __init__(self, egzemplarze: dict, limit_wypozyczen: int):
        self.limit_wypozyczen = limit_wypozyczen
        self.egzemplarze = egzemplarze

    def dodaj_egzemplarz_ksiazki(self, tytul: str, autor: str, rok_wydania: int) -> bool:

        if not Ksiazka(tytul, autor, rok_wydania) in self.egzemplarze.keys():
            self.egzemplarze[Ksiazka(tytul, autor, rok_wydania)] = 1
        else:
            self.egzemplarze[Ksiazka(tytul, autor, rok_wydania)] += 1


class Egzemplarz:
    def __init__(self, rok_wydania: int, wypozyczony: bool):
        self.rok_wydania = rok_wydania
        self.wypozyczony = wypozyczony


egzemplarze = {}
biblioteka = Biblioteka(egzemplarze, 100)

print('liczba egzemplarzy: ')
liczba_egz = int(input())

for i in range(0, liczba_egz):
    print("ksiazka: ")
    data = eval(input())
    biblioteka.dodaj_egzemplarz_ksiazki(data[0], data[1], data[2])


def poTytule(ksiazka):
    return ksiazka.tytul


output = []
for ksiazka, wartosc in egzemplarze.items():
    output.append(eval(str(ksiazka)) + (wartosc,))

for posortowane in sorted(output, key=lambda ksiazka: ksiazka[0]):
    print(posortowane)
