# Verhaltenspersonas aus mehreren Kanälen

[简体中文](README.zh-CN.md) | [English](README.en.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Português](README.pt.md)

Die ausdrücklich gewünschte Ausgabesprache verwenden, sonst der Sprache der Anfrage folgen. Befehle, Skill-IDs, JSON-Schlüssel, Enumerationswerte, Einheiten und Originalzitate unverändert lassen. Übersetzungen kennzeichnen. Land, Währung und Rechtsordnung nicht aus der Sprache ableiten. Relevante Detailreferenzen lesen und sämtliche bestehenden Prüfungen und Berechtigungsgrenzen einhalten.

## Installation und Nutzung

Das Repository herunterladen oder klonen und das angegebene Skill-Verzeichnis mit seinen vorhandenen references, scripts, assets und weiteren Abhängigkeiten in das Skill-Verzeichnis des Hosts kopieren. Name und SKILL.md beibehalten. Ein Sprachwechsel erfordert keine weitere Installation. Installationsbefehle sind Optionen und kein Nachweis einer Installation oder Aktivierung.

```sh
git clone https://github.com/PDBen-Auto/multi-channel-persona-research-skill.git
```

## Verhaltenspersonas aus mehreren Kanälen

`multi-channel-persona-research`

Erlaubte Belege, Verhaltenssegmente, verblindeten Konzeptvergleich und echten A/B-Testplan verbinden; simulierte Präferenzen sind keine Ergebnisse.

Skill-Verzeichnis: `.`

**Umsetzungsgrundlage und Abhängigkeiten**

Entscheidung, Zielgruppe und lesbare erlaubte Belege. Mehrkanalaussagen erfordern mindestens zwei unabhängige Quellentypen. Browser, Analytik und Testplattform nur nach Bedarf.

**Eingaben**

Pflicht decision_question, target_scope und evidence_sources mit Datum/Rechten. Optional Varianten, Basiswerte, Stichprobenrahmen, Kosten-/Sicherheitsgrenzen und Testfenster. Eigene Personendaten minimal verarbeiten.

**Ausgaben**

persona-research.md: Quellenregister, Beleg-IDs/Codes/Konflikte, Verhaltensgruppen, gruppenbezogener Vergleich und Testplan. Unbekannte Gruppenanteile erlauben keine Gesamt-Siegquote.

[Ablauf · Grenzen und Abbruchbedingungen · Beispielanfrage](references/i18n/de.md)

> Verwende `$multi-channel-persona-research` — Forum und autorisierte Supportdaten für zwei verblindete Buchungsseiten nutzen; einen Zufallstest planen statt Konversionsgewinn zu behaupten; antworte auf Deutsch und erhalte Belege, unbekannte Werte und Berechtigungsgrenzen.

## Sprachumfang und Prüfung

Dieser lokalisierte Leitfaden umfasst Zweck, Voraussetzungen, Ein- und Ausgaben, Ablauf, Beispiele und Grenzen. Er übersetzt nicht jede Referenz Zeile für Zeile. Technische Detailreferenzen, historische Fälle, Skriptfehler, Beispieloberflächen und Bilder bleiben in der Originalsprache und können auf Wunsch erläutert werden. Struktur, Links und Kernbedingungen werden geprüft; ein muttersprachliches Lektorat je Sprache wird nicht behauptet.

Vor der Übergabe Eingaben, Belege, fehlende Werte, Ausgabedateien und ursprüngliche Abschlusskriterien abgleichen. Nicht ausgeführte Schritte als ungeprüft kennzeichnen; ein erfolgreicher Skriptablauf bestätigt keine geschäftliche Aussage.
