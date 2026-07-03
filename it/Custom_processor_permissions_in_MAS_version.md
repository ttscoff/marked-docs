<!-- MT-DRAFT: machine translation; human review required -->

# Autorizzazioni del processore personalizzate nella versione MAS

A causa delle restrizioni del sandboxing, la versione di Marked del Mac App Store non è in grado di eseguire determinati tipi di strumenti binari come processori personalizzati. Se riscontri questa limitazione, puoi provare alcuni passaggi.

1. Assicurati di essere entrato in Impostazioni **Contrassegnate** ({% kbd cmd , %}), nel riquadro **Avanzate** e di aver fatto clic su "Aggiorna autorizzazioni". Questo tenterà di concedere a Mark l'accesso all'intera unità predefinita, risolvendo i problemi con script e utilità che devono accedere a cartelle temporanee e posizioni non predefinite.
2. Prova a utilizzare uno script. Fai riferimento all'utilità che desideri eseguire (multimarkdown, kramdown, ecc.) in uno script di shell. Può essere uno script bash, Ruby, Perl o Python. Quindi imposta il processore in Impostazioni avanzate sulla shell o sull'eseguibile correlato e i parametri sulla posizione dello script. Ad esempio, posso creare uno script bash salvato in ~/scripts/mmd_wrapper.sh:

        #!/bin/bash
        gatto | /usr/local/bin/multimarkdown

    Quindi rendilo eseguibile (`chmod a+x ~/scripts/mmd_wrapper.sh`) e configura le impostazioni del mio processore personalizzato:

        Processore: /bin/bash
        Argomenti: /Users/me/scripts/mmd_wrapper.sh
3. Alcuni eseguibili (specialmente Pandoc) semplicemente non funzioneranno all'interno del sandboxing. In questo caso contattami tramite la finestra di errore che appare al momento dell'esecuzione per ricevere una licenza crossgrade alla versione diretta.