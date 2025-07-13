---
status: Fertig
tags: [meta, konvention, frontmatter]
kapitel: Meta
autor: Zoltán Hrabovszki
---
# YAML-Frontmatter – Schreibkonvention

Um Status, Schlagworte und weitere Metadaten einheitlich zu verwalten, verwenden wir in allen Markdown-Dateien **YAML-Frontmatter**. Dieser Block steht **immer ganz oben** in der Datei.

## Format

```yaml
---
status: In Bearbeitung
tags: [gui, dry, lokatoren]
kapitel: DRY-Prinzip
autor: Zoltán Hrabovszki
---
```

## Felder im Detail

| Feld      | Beschreibung                                                                |
| --------- | --------------------------------------------------------------------------- |
| `status`  | `Entwurf`, `In Bearbeitung`, `Fertig` – aktueller Bearbeitungsstatus        |
| `tags`    | Schlagworte für Suche & Graph (klein geschrieben, ohne `#`, komma-getrennt) |
| `kapitel` | Zugehöriges Buch-Kapitel (z. B. "Beobachtbarkeit", "Testfallstruktur")      |
| `autor`   | Name des Autors                                                             |

## Hinweise

* Frontmatter steht **direkt am Anfang** der Datei, ohne Leerzeile davor.
* Zwischen den Einträgen **keine Leerzeilen**.
* `tags` ist eine **Liste**, daher in eckigen Klammern (`[ ]`) schreiben.
* `status` ist bewusst eingeschränkt auf drei Optionen:

  * `Entwurf`
  * `In Bearbeitung`
  * `Fertig`

## Beispiel

```yaml
---
status: Fertig
tags: [testdaten, abstrahierung]
kapitel: DRY-Prinzip
autor: Zoltán Hrabovszki
---
```

## Optional

Wenn du Plugins wie **Dataview** oder **Tasks** nutzt, kannst du dir automatisch z. B. alle "in Bearbeitung"-Dateien anzeigen lassen.

## Ablageort

Diese Konvention ist in `inhalt/meta/YAML-Frontmatter-Konvention.md` gespeichert und wird versioniert mitgeführt.
