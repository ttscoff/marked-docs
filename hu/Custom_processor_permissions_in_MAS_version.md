<!-- MT-DRAFT: machine translation; human review required -->

# Egyéni processzorengedélyek a MAS verzióban

A sandbox korlátozások miatt a Marked Mac App Store verziója nem tud bizonyos típusú bináris eszközöket egyéni processzorként végrehajtani. Ha ebbe a korlátozásba ütközik, néhány lépést kipróbálhat.

1. Győződjön meg arról, hogy belépett a **Megjelölt** Beállítások ({% kbd cmd , %}) elembe a **Speciális** panelen, és rákattintott az "Engedélyek frissítése" lehetőségre. Ez megpróbálja a Megjelölt hozzáférést biztosítani a teljes alapértelmezett meghajtóhoz, kiküszöbölve a szkriptekkel és segédprogramokkal kapcsolatos problémákat, amelyeknek hozzá kell férniük az ideiglenes mappákhoz és a nem alapértelmezett helyekhez.
2. Próbáljon meg egy szkriptet. Hivatkozzon a futtatni kívánt segédprogramra (multimarkdown, kramdown stb.) egy shell szkriptben. Lehet bash, Ruby, Perl vagy Python szkript. Ezután a Speciális beállításokban állítsa be a processzort a kapcsolódó shellre vagy végrehajtható fájlra, a paramétereket pedig a szkript helyére. Például létrehozhatok egy bash szkriptet a ~/scripts/mmd_wrapper.sh címre mentve:

        #!/bin/bash
        macska | /usr/local/bin/multimarkdown

    Ezután tegye végrehajthatóvá (`chmod a+x ~/scripts/mmd_wrapper.sh`), és adja meg az egyéni processzor beállításaimat:

        Processzor: /bin/bash
        Érvek: /Users/me/scripts/mmd_wrapper.sh
3. Egyes végrehajtható fájlok (különösen a Pandoc) egyszerűen nem működnek a sandboxon belül. Ebben az esetben vegye fel velem a kapcsolatot a végrehajtáskor megjelenő hibaablakon keresztül, hogy megkapja a crossgrade licencet a közvetlen verzióra.