# 📁 assets/

Dieses Verzeichnis enthält alle externen Ressourcen wie Bilder und Diagramm-Definitionen für das Buch.
## Struktur

```
assets/  
├── images/ # Gerenderte Bilder (z. B. PNG, SVG)  
│ └── testautomation-resource-shift.png  
│  
├── diagrams/ # Diagramm-Quellen (z. B. PlantUML)  
│ ├── dry-prinzip/  
│ │ ├── testfall-uebersetzungen.puml  
│ │ ├── testfall-uebersetzungen.svg  
│ │ └── testfall-uebersetzungen.png  
│ └── <weiteres-thema>/  
│ └── ...
```

## Konventionen

- Diagramme werden als `.puml` gespeichert und optional als `.svg` oder `.png` gerendert.
- Bildreferenzen im Text (Markdown) zeigen immer auf `../assets/images/`, damit Obsidian und GitBook sie finden.
- Für jedes Thema (z. B. „dry-prinzip“) wird ein Unterordner unter `diagrams/` angelegt.

## Hinweise

- Für automatisch generierte `.svg`/`.png` aus `.puml` ist eine GitHub Action vorgesehen.
- Obsidian zeigt `.puml` nicht nativ an – dafür gibt es das Plugin „PlantUML“.

