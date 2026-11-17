# Verhaltenspersonas aus mehreren Kanälen

`multi-channel-persona-research` · Deutsch

## Zweck und Einsatzbereich

Erlaubte Belege, Verhaltenssegmente, verblindeten Konzeptvergleich und echten A/B-Testplan verbinden; simulierte Präferenzen sind keine Ergebnisse.

## Umsetzungsgrundlage und Abhängigkeiten

Entscheidung, Zielgruppe und lesbare erlaubte Belege. Mehrkanalaussagen erfordern mindestens zwei unabhängige Quellentypen. Browser, Analytik und Testplattform nur nach Bedarf.

## Eingaben

Pflicht decision_question, target_scope und evidence_sources mit Datum/Rechten. Optional Varianten, Basiswerte, Stichprobenrahmen, Kosten-/Sicherheitsgrenzen und Testfenster. Eigene Personendaten minimal verarbeiten.

## Ausgaben

persona-research.md: Quellenregister, Beleg-IDs/Codes/Konflikte, Verhaltensgruppen, gruppenbezogener Vergleich und Testplan. Unbekannte Gruppenanteile erlauben keine Gesamt-Siegquote.

## Ablauf

1. Entscheidung/Stichprobe festlegen
2. ergänzende Kanäle und Verzerrung erfassen
3. ohne Identitätsraten deduplizieren
4. Aufgaben, Kontext, Alternativen und Abwägungen codieren
5. belegte Gruppen bilden
6. A/B verblinden und nur belegte Dimensionen bewerten
7. Zufallseinheit, Kennzahl, Schutzmetriken, Basis, Effektschwelle und Stopp vorab definieren
8. Belege und Anonymisierung prüfen.

## Grenzen und Abbruchbedingungen

Keine erfundenen Interviews, Kontaktsuche, sensiblen Merkmalsannahmen oder Bevölkerungsanteile. KI-Personas als synthetic_hypothesis markieren. Ohne Plattform/Erlaubnis nur Plan. Öffentliche Beispiele vollständig fiktiv.

## Beispielanfrage

Verwende `$multi-channel-persona-research` — Forum und autorisierte Supportdaten für zwei verblindete Buchungsseiten nutzen; einen Zufallstest planen statt Konversionsgewinn zu behaupten; antworte auf Deutsch und erhalte Belege, unbekannte Werte und Berechtigungsgrenzen.

## Vollständige Spezifikation

[Skill-Einstieg und Detailreferenzen](../../SKILL.md).

Die ausdrücklich gewünschte Ausgabesprache verwenden, sonst der Sprache der Anfrage folgen. Befehle, Skill-IDs, JSON-Schlüssel, Enumerationswerte, Einheiten und Originalzitate unverändert lassen. Übersetzungen kennzeichnen. Land, Währung und Rechtsordnung nicht aus der Sprache ableiten. Relevante Detailreferenzen lesen und sämtliche bestehenden Prüfungen und Berechtigungsgrenzen einhalten.

Vor der Übergabe Eingaben, Belege, fehlende Werte, Ausgabedateien und ursprüngliche Abschlusskriterien abgleichen. Nicht ausgeführte Schritte als ungeprüft kennzeichnen; ein erfolgreicher Skriptablauf bestätigt keine geschäftliche Aussage.

## Sprachumfang und Prüfung

Dieser lokalisierte Leitfaden umfasst Zweck, Voraussetzungen, Ein- und Ausgaben, Ablauf, Beispiele und Grenzen. Er übersetzt nicht jede Referenz Zeile für Zeile. Technische Detailreferenzen, historische Fälle, Skriptfehler, Beispieloberflächen und Bilder bleiben in der Originalsprache und können auf Wunsch erläutert werden. Struktur, Links und Kernbedingungen werden geprüft; ein muttersprachliches Lektorat je Sprache wird nicht behauptet.

