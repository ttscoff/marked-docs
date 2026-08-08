# <%= @title %>

Die Mac App Store (MAS)-Version von Marked wird in einer Sandbox-Umgebung ausgeführt, die aus Sicherheitsgründen bestimmte Vorgänge einschränkt. Dies kann sich auf einige Funktionen auswirken, insbesondere wenn benutzerdefinierte Prozessoren mit externen Binärdateien oder Skripten verwendet werden.

## Allgemeine Sandbox-Einschränkungen [common-sandbox-restrictions]

### Binärdateien für „Befehl ausführen“ [run-command-binaries]

Das häufigste Problem für Benutzer besteht darin, dass externe Binärdateien nicht direkt in der MAS-Version ausgeführt werden können. Dies betrifft:

- **Externe Prozessoren** wie Pandoc, Kramdown oder andere Befehlszeilentools
- **Benutzerdefinierte Skripte**, die auf externen Binärdateien beruhen
- **Systemdienstprogramme**, auf die nicht über die Sandbox zugegriffen werden kann

### Problemumgehungen [workarounds]

#### Binärdateien in das App Bundle kopieren [copying-binaries-to-the-app-bundle]

Wenn Sie externe Prozessoren wie Pandoc in der MAS-Version verwenden müssen, können Sie die Binärdatei in das App-Bundle kopieren:

1. Klicken Sie mit der rechten Maustaste auf Marked.app → **Paketinhalt zeigen**
2. Navigieren Sie zu **Contents/Resources/**
3. Erstellen Sie einen Ordner `bin`, falls dieser noch nicht vorhanden ist
4. Kopieren Sie Ihre Binärdatei (z. B. `pandoc`) in diesen Ordner `bin`
5. Machen Sie sie ausführbar: `chmod +x` auf die Binärdatei anwenden
6. Verweisen Sie in der Aktion „Befehl ausführen“ wie folgt darauf:
   - `YOUR_BINARY_NAME [arguments]`
   - Oder verwenden Sie den vollständigen Pfad: `/Applications/Marked.app/Contents/Resources/bin/YOUR_BINARY_NAME [arguments]`

**Hinweis**: Skripte mit externen Shebangs (wie Python-Skripte, die auf `/opt/homebrew/bin/python` verweisen) werden beim Kopieren in das Bundle automatisch über Systeminterpreter ausgeführt. Die MAS-Version hat möglicherweise immer noch Probleme beim Ausführen von Binärdateien, bei denen es sich tatsächlich um Python- oder Ruby-Skripte und nicht um Binärdateien handelt.

**Wichtig**: Sie müssen die Binärdateien nach jedem App-Update erneut kopieren, da Updates das gesamte Bundle ersetzen.

#### Eingebettete Skripte verwenden [using-embedded-scripts]

Anstatt externe Befehle auszuführen, können Sie die Aktion **Eingebettetes Skript ausführen** in Eigenen Regeln verwenden. Dadurch können Sie Skripte direkt im Code-Editor von Marked schreiben, der auf Systeminterpreter zugreifen kann, die in der Sandbox verfügbar sind.

## Wechsel zur Nicht-Sandbox-Version [crossgrade]

Wenn Sie häufig externe Binärdateien verwenden müssen oder auf andere Sandboxing-Einschränkungen stoßen, sollten Sie einen Wechsel zur Version ohne Sandbox erwägen. Die Version ohne Sandbox unterliegt keinen derartigen Einschränkungen und kann jedes von Ihnen installierte Befehlszeilentool oder Skript ausführen.

### Für Abonnementbenutzer [for-subscription-users]

Wenn Sie ein aktives Mac App Store-Abonnement haben:

1. **Kündigen Sie Ihr MAS-Abonnement** unter Systemeinstellungen → Apple-ID → Medien & Käufe → Abonnements
2. **Laden Sie die kostenlose Testversion herunter** von [https://markedapp.com](https://markedapp.com)
3. **Starten Sie ein Paddle-Abonnement** direkt über die App oder Website

Die Paddle-Version bietet die gleichen Funktionen ohne Sandboxing-Einschränkungen.

### Für Inhaber einer dauerhaften Freischaltung [for-permanent-unlock-holders]

Wenn Sie über den Mac App Store eine permanente Freischaltlizenz oder eine lebenslange Lizenz erworben haben, [schreiben Sie dem Entwickler](mailto:marked@brettterpstra.com?subject=Marked%20License%20Crossgrade&body=Please%20include%20your%20UUID%20%28Help-%3ECopy%20UUID%20in%20Marked%29%20in%20this%20email%20for%20receipt%20verification.), um eine kostenlose lebenslange Paddle-Lizenz anzufordern.

**Wichtig**: Um Ihren Kauf zu bestätigen, geben Sie bitte eine der folgenden Angaben in Ihre E-Mail ein:

- Ihre **Benutzerkennung** (UUID) – kopieren Sie sie mit **Hilfe → UUID kopieren** in Ihre Zwischenablage und fügen Sie sie dann in Ihre E-Mail ein
- Ihre **Transaktions-ID** von Ihrem App Store-Beleg (diese finden Sie in Ihrer Kaufhistorie in der App Store-App)

Der Mac App Store gibt Ihre E-Mail-Adresse nicht an Entwickler weiter, daher überprüfen wir Käufe anhand von Transaktions-IDs oder Benutzerkennungen, die auf unserem Server gespeichert sind. Die Angabe dieser Informationen hilft uns, Ihren Kauf schnell zu überprüfen und Ihre kostenlose Paddle-Lizenz zu generieren.

### Setapp-Version [setapp-version]

Wenn Sie ein Setapp-Abonnement haben, können Sie alternativ die Setapp-Version von Marked verwenden, die ebenfalls ohne Sandbox läuft und vollen Zugriff auf Systemressourcen hat.

## Zusätzliche Ressourcen [additional-resources]

Weitere Informationen zu benutzerdefinierten Prozessoren und ihren Möglichkeiten finden Sie unter [Benutzerdefinierter Prozessor](Custom_Processor.html).

