# Milk man problems

<img align="right" src="http://folk.uio.no/torenord/milk.png" width="500px">

Alle melkemenn er kjent med dette klassiske problemet fra middelalderen:

Du er ute og leverer melk på din daglige leveringsrunde. De to siste
på runden skal ha *N* liter melk hver, men du oppdager et
kjempeproblem! Du har tre melkespann med forskjellig volum, men ingen
av dem er på *N* liter. Det er ingen markeringer på innsiden av
melkespannene, slik at du blir nødt til å fordele melken ved å helle
den frem og tilbake mellom spannene på en eller annen måte. Når du
heller, heller du alltid til spannet du heller fra er tomt eller
spannet du heller til er fullt.

Du har et spann på *A* liter, et på *B* liter og et på *C* liter slik
at *A > B > C*. Spannet på *A* liter er fullt med melk. Spannene med
*B* og *C* liter er tomme.

For eksempel: Du har tre spann på *A = 12*, *B = 8* og *C = 5* liter.

1. Hell 8 liter fra A to B.
2. Hell 5 liter fra B to C.
3. Hell 5 liter fra C to A.
4. Hell 3 liter fra B to C.
5. Hell 8 liter fra A to B.
6. Hell 2 liter fra B to C.
7. Hell 5 liter fra C to A.

Nå er det 6 liter i A og 6 liter i B. Det er altså mulig å fordele
melken likt i 7 steg. For disse spannene er dette faktisk den korteste
fremgangsmåten.

Din oppgave er, gitt volumene på *A = 500*, *B = 333*, *C = 100* og at
*A* er full med melk, og du skal ende opp med *A/2* i ett av spannene
og *A/2* i et av de andre spannene, hvor mange steg er det i den
korteste fremgangsmåten for å oppnå dette?