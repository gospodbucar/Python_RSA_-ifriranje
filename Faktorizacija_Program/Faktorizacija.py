#  Janez Bučar, 35160122, izjavljam da je program moje delo, 26.12.2021
#  je zapis naravnega števila v obliki produkta faktorjev, ki so vsi praštevila.

n = 31313
for i in range(2, n + 1):
    if n % i == 0:
        count = 1
        for j in range(2, (i//2 + 1)):
            if(i % j == 0):
                count = 0
                break
        if(count == 1):

            print(i)

"""

vnesemo število, ki ga želimo faktorizirati --> n.
uporabimo zanko for od i=2 do i=n+1.
preverimo, ali je ostanek pri deljenju vrednosti i in števila n enak 0.
Ohranimo count = 1 in ponovno uporabimo zanko for znotraj zanke od j=2 do j=i//2+ 1.
preverimo če je ostanek deljenja i % j enak 0. če je pogoj izpolnjen
je vrednost štetja nastavljena na 0 in stavek prekinemo.
na koncu preverimo pogoj, če je count ==1, in prikažemo vrednost i.


"""