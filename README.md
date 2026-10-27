# Coffee Corp BrewLedger - Contributor Check

Coffee Corp verwaltet Kaffeebohnen und Lagerbestände mit **BrewLedger**.
Dieses Repository enthält eine kleine Python-Anwendung, die den Service darstellt.

Der Service ist für diese Challenge allerdings **egal** - eure Aufgabe ist
unter [Ziel](#ziel) beschrieben!

> [!IMPORTANT]
> Dieses Repository ist **public**. Postet keine persönlichen oder anderweitig
> schützenswerten Daten in dieses Repository.

## Ziel

**🚩 Dein Ziel ist es, eine Datei im Verzeichnis `/flags/` auf dem `main`-Branch
anzulegen.**

- ✅ Als Consultant von Coffee Corp hast du bereits `push`-Zugriff auf das
  Repository. Du kannst daher Branches und Commits pushen und sogar **Pull
  Requests mergen**.
- ⚠️ Coffee Corp hat mit Insider Threats gerechnet und einige
  Sicherheitsmaßnahmen eingerichtet.

Die Sicherheitsmaßnahmen sind:

- Auf `main` kann nicht direkt gepusht werden. Das Pushen eines neuen Branches und das
  Öffnen eines Pull Requests sind zwingend erforderlich.
- **Force-Pushes**, mit denen bestehende Commits überschrieben werden könnten,
  sind auf dem `main`-Branch blockiert, auf anderen Branches aber weiterhin
  erlaubt. Dort kann frei gearbeitet werden.
- Das Mergen eines Pull Requests erfordert, dass der Workflow
  `check-authors.yaml` erfolgreich abgeschlossen wurde. Details stehen im
  Abschnitt [Check Authors Workflow](#check-authors-workflow).
- Änderungen außerhalb von `/flags/` sind durch [`CODEOWNERS`](.github/CODEOWNERS)
  geschützt und benötigen ein Review. Das informiert Coffee Corp über deine Versuche
  und führt hier nicht zum Ziel 😉

> [!CAUTION]
> Schreibrechte auf dem Repository erlauben auch das Ändern anderer Pull
> Requests und Branches, einschließlich der Branches anderer Teams.
> Wir sind alle Security Specialists - dieses Challenge ist **nicht** dafür gedacht,
> mit euren "Hacker-Fähigkeiten" anzugeben.
> **Ein solcher Versuch führt zum Ausschluss deines gesamten Teams von allen
> CTFs und zur Entfernung bereits erzielter CTF-Punkte. Das verschlechtert
> selbstverständlich auch kollektiv die Prüfungsnote der Gruppe.**

### Check Authors Workflow

Dieser Workflow ist die Sicherheitsmaßnahme von Coffee Corp gegen nicht
autorisierte Commits. Er prüft die `committer`-E-Mail-Adresse jedes Commits, den
ein Pull Request enthält, und validiert deren E-Mail-Domain.

Eine Adresse wie `barista@coffeecorp.com` ist erlaubt, eine Adresse wie
`you-account@gmail.com` ist ungültig.

> [!TIP]
> Diese Challenge lässt sich am besten lokal auf deinem Rechner mit dem
> `git`-Befehl bearbeiten.

## Git Cheat Sheet

`git` bietet sehr viele Funktionen. Die folgenden Befehle können hilfreich sein:

- `git clone <repository>` kopiert dieses Repository auf deinen lokalen Rechner.
- `git checkout -b <name>` erstellt einen neuen Branch.
- `git add <files>` fügt Dateien zum nächsten Commit hinzu.
- `git commit -m '<your message>'` erstellt einen Commit auf dem aktiven Branch
  mit allen Dateien, die seit dem letzten Commit per `git add` vorgemerkt wurden.
- `git config` konfiguriert `git` nur für das aktuelle Repository. Mit
  `git config --global` würdest du die Einstellung für deinen lokalen Benutzer
  setzen; das ist hier nicht erforderlich.
- `git push --set-upstream origin <name>` pusht einen neuen lokalen Branch in
  das Remote-Repository. Danach reicht für denselben Branch einfach `git push`.
- `git reset HEAD~1` entfernt den letzten Commit aus der lokalen `git`-Historie,
  behält aber die Dateiänderungen. Danach musst du sie erneut mit `git add` und
  `git commit` in die Historie aufnehmen. Dadurch weichen Remote- und lokales
  Repository voneinander ab; du musst anschließend entweder `git push --force`
  nutzen oder die divergierenden Commits mergen.
- `git push --force` pusht die lokale Version des Branches und überschreibt
  Commits am Ziel. Das kann nützlich sein, wenn ein Fehler korrigiert oder eine
  geänderte Historie gepusht werden muss, bei der ein normaler `git push` abgelehnt
  wird.

> [!WARNING]
> `git push --force` kann Teile der `git`-Historie ohne weitere Warnung löschen.
> In diesem Test-Repository ist der Befehl auf **deinem eigenen Branch** relativ
> sicher (beachte den Hinweis im Abschnitt [Ziel](#ziel)). In einem echten
> Repository sollte der Einsatz sorgfältig abgewogen werden.

Für diese Challenge nicht erforderlich, aber für die Arbeit mit VS Code einen
Blick wert:

> [!TIP]
> `Git Graph` ist eine schlanke VS-Code-Erweiterung, die die lokale Git-Historie
> visualisiert und mehrere Git-Operationen als anklickbare GUI-Aktionen anbietet.

## Repository Layout

- `.github/workflows/check-authors.yaml` enthält die erforderliche
  Contribution-Prüfung.
- `.github/CODEOWNERS` schützt alle Dateien außer `flags/` vor
  Änderungen ohne Approval.

Alle übrigen Dateien sind kleine Beispieldateien, damit das Repository wie eine
kleine Anwendung aussieht. Sie sind absichtlich einfach gehalten, damit der
Workflow der interessante Teil dieser Übung bleibt.
