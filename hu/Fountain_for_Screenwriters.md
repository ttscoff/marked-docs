<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A [Fountain](http://fountain.io/) egy speciális szövegjelölő nyelv, amelyet forgatókönyvek írására terveztek. A Fountain szintaxisát használó forgatókönyvírók a Marked segítségével megtekinthetik munkájuk előnézetét. 

A ".fountain" kiterjesztésű fájl megnyitása automatikusan engedélyezi a Fountain támogatást az ablakhoz. A program egy alapértelmezett Fountain stíluslapot alkalmaz az előnézethez és az exportáláshoz.

Bármely dokumentumot kényszeríthet Markdown-ként való feldolgozásra, ha megnyitja a Fogaskerék menüt az Előnézet ablak jobb alsó sarkában, és kiválasztja a **Feldolgozás szökőkútként** lehetőséget.

A szakaszok és a jelenetek fejlécei megjelennek a Tartalomjegyzékben, így gyorsan navigálhat a forgatókönyvben.

## Szkriptek

Használhat "szkripteket" egy normál dokumentumban is, hogy az egyes szakaszokat a Fountain segítségével dolgozza fel és alakítsa ki. Egyszerűen vegye körül a Fountain jelölést a fő dokumentumon belül `[scrippet]` címkékkel:

    [forgatókönyv]
    A forgatókönyved szövege...
    [/scriptet]

Használhat szabványos Marked stílusú címkéket is:

    <!--SCRIPPET-->
    A forgatókönyved szövege...
    <!--/SCRIPPET-->