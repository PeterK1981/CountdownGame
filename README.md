# Countdown (Solo) — Terminal-Wortspiel

Ein leichtgewichtiges Terminal-Remake des **Countdown-Buchstabenspiels**:  
Ziehe Buchstaben, bilde das längste gültige Wort, sammle Punkte und knacke die Highscore-Liste.  
Variante: **Solo**, ohne Zeitdruck, mit „KI-Hinweis“ auf längere Wörter.

---

## 🔗 Referenz

Das Originalspiel ist die britische Fernsehshow **Countdown (game show)**  
(https://en.wikipedia.org/wiki/Countdown_(game_show)),  
siehe Abschnitt *Letters round* für Regeln und Ablauf.  
Diese Implementation weicht bewusst davon ab (siehe unten).

---

## 🎮 Kurzüberblick

- Plattform: Python, Terminal  
- Runden: 3 Runden pro Spiel  
- Mechanik: Ziehung von 11 Buchstaben mit leichter Häufigkeitsverzerrung, mindestens 1 Vokal  
- Punkte: Länge des gültigen Wortes  
- Solo-Variante: Kein Timer, kein Gegenspieler  
- Hinweisgeber: Zufallssucher schlägt längere Wörter vor („Könnte es besser gehen?“)  
- Highscores: Top-10 mit Name und Zeitstempel werden lokal gespeichert

---

## ⚙️ Abweichungen vom Original

Das TV-Original nutzt 9 Buchstaben, Spielerauswahl von Konsonanten/Vokalen und 30 Sekunden Zeitlimit.  
Hier gelten:

- Solo-Spiel, keine Gegner  
- Keine Zeitbeschränkung  
- 11 Buchstaben statt 9, automatisch generiert  

---

## 💻 Voraussetzungen

- Python ≥ 3.9 (nutzt moderne Typannotationen)  
- Keine externen Bibliotheken  
- Folgende Dateien im Arbeitsverzeichnis:
  - `CountDownGame_solo.py`  
  - `anagrams.pkl`  
  - `highscores.pkl` (wird automatisch angelegt)

---

## ▶️ Start

1. Lege `CountDownGame_solo.py` und `anagrams.pkl` ins gleiche Verzeichnis  
2. Öffne das Terminal  
3. Starte mit  
   ```bash
   python CountDownGame_solo.py
   ```  
4. Folge den Anweisungen im Terminal: Buchstaben ansehen → Wort eingeben → Punkte erhalten → nächste Runde  

Nach deinem Tipp zeigt das Spiel deine Punktzahl und ggf. ein längeres gefundenes Wort.  
Am Ende kannst du dich in die Highscore-Liste eintragen.

---

## 📁 Dateien

| Datei | Funktion |
|-------|-----------|
| `CountDownGame_solo.py` | Hauptskript (Ziehung, Validierung, Highscores, Hinweisgeber) |
| `anagrams.pkl` | Wörterbuch: Mapping von sortierten Buchstaben → Wortliste |
| `highscores.pkl` | Lokale Top-10-Liste, kann gelöscht werden zum Zurücksetzen |

---

## 📚 Anagramm-Wörterbuch (`anagrams.pkl`)

Format: Python-`dict`  
- Key: `tuple(sorted(chars))`  
- Value: `list[str]` aller Wörter mit denselben Buchstaben  

Beispiel:  
```python
{('a','c','t'): ['act','cat']}
```

Das Spiel prüft zusätzlich, ob dein Wort mit der gezogenen Buchstaben-Multimenge gebildet werden kann.

---

## 🧩 Spielregeln in dieser Version

- Buchstabenpool mit Häufigkeitsbias; pro Runde werden 11 Buchstaben gezogen  
- Gültigkeit deines Wortes:
  1. Wort steht im Anagramm-Lexikon  
  2. Buchstabenverwendung überschreitet nicht die gezogene Multimenge  
- Punkte = Wortlänge, sonst 0  
- Nach Eingabe sucht der Hinweisgeber stochastisch nach längeren Treffern

---

## ⚠️ Bekannte Grenzen

- Der Hinweisgeber ist zufallsbasiert und nicht vollständig – längere Wörter können übersehen werden  
- Gültigkeit hängt vollständig von der Wortliste ab
- Die Wortliste wurde aus der Datei words_alpha.txt erstellt (Quelle: https://github.com/dwyl/english-words


---

## 🏆 Highscores

- Am Spielende automatische Anzeige  
- Zurücksetzen: `highscores.pkl` löschen  
- Limit: Top 10, sortiert nach Punkten und Zeitstempel

---

## 💡 Plattformhinweis

Konsolenbereinigung nutzt `cls` (Windows) bzw. `clear` (Unix).  
In IDE-Konsolen bleibt der Bildschirminhalt ggf. sichtbar.

---

## 🙏 Idee

Idee nach dem klassischen **Countdown**-Buchstabenspiel.

Regelreferenz siehe Wikipedia – Countdown (game show) → *Letters round*.  
Abweichungen zur Show sind in dieser README dokumentiert.
