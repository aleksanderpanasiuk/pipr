# Zadanie 1

Zaprojektuj klasę reprezentującą planetę. Każda planeta powinna posiadać:
* atrybuty prywatne: nazwa, liczba księżyców, położenie w przestrzeni trójwymiarowej (X, Y, Z).
* konstruktor z parametrami (x, y, z, nazwa) gdzie nazwa jest domyślnie ciągiem pustym,
* metody umożliwiające ustawienie i odczytanie wartości atrybutów prywatnych,
* metodę zwracającą napis opisujący planetę.

Napisz funkcje obliczającą odległość pomiędzy dwoma planetami (planety przekazywane jako parametry funkcji).

Napisz testy dla stworzonych klas oraz funkcji obliczającej odległość. 

Podpowiedź: funkcja sqrt obliczająca pierwiastek kwadratowy znajduje się w module math biblioteki standardowej.

# Zadanie 2
Zaprojektuj klasę reprezentującą paczkę przewożoną przez firmę kurierską. Każda paczka powinna posiadać:
* atrybuty prywatne:
  * nazwę nadawcy (jedna linia tekstu),
  * nazwę odbiorcy (jedna linia tekstu),
  * wymiary: wysokość, szerokość, długość,
  * wagę;
* metody:
  * konstruktor,
  * metody umożliwiające ustawienie i odczytanie wartości atrybutów prywatnych,
  * zwracającą najmniejszy z wymiarów paczki,
  * zwracający największy z wymiarów paczki,
  * zwracającą napis opisujący paczkę. Należy uwzględnić między innymi największy i najmniejszy wymiar paczki (korzystając z wcześniej napisanych metod).
  
Napisz testy dla utworzonej klasy.

Podpowiedź: można skorzystać z funkcji min oraz max.

# Zadanie 3
Zaprojektuj klasy reprezentujące:
* Artystę (atrybuty: nazwisko, rok urodzenia; metodę zwracającą napis opisujący wykonawcę),
* Piosenkę (atrybuty: wykonawca, tytuł, czas trwania; metodę zwracającą napis opisujący piosenkę).

Klasy powinny mieć: atrybuty prywatne, konstruktor z parametrami (część z wartościami domyślnymi), metody umożliwiające ustawienie i odczytanie wartości atrybutów prywatnych klasy.

Napisz testy dla podanych klas.
