# Recherche de personas comportementaux multicanaux

[简体中文](README.zh-CN.md) | [English](README.en.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Português](README.pt.md)

Utiliser la langue explicitement demandée, sinon celle de la demande. Conserver les commandes, identifiants de Skill, clés JSON, valeurs d’énumération, unités et citations originales. Distinguer traduction et original. Ne déduire ni pays, ni devise, ni juridiction de la langue. Lire les références détaillées utiles et maintenir tous les contrôles et autorisations existants.

## Installation et utilisation

Télécharger ou cloner le dépôt, puis copier le répertoire du Skill indiqué, avec ses references, scripts, assets et autres dépendances existantes, dans le répertoire de Skills de l’hôte. Conserver son nom et SKILL.md. Changer la langue de documentation ne demande pas de nouvelle installation. Les commandes proposées ne prouvent ni installation ni activation.

```sh
git clone https://github.com/PDBen-Auto/multi-channel-persona-research-skill.git
```

## Recherche de personas comportementaux multicanaux

`multi-channel-persona-research`

Relier preuves autorisées, segments, comparaison en aveugle et protocole A/B réel sans confondre préférence simulée et résultat.

Répertoire du Skill: `.`

**Fondements et dépendances**

Décision/périmètre clairs et preuves lisibles autorisées. Une conclusion multicanale exige au moins deux types de sources indépendants. Navigateur, analytique et plateforme d’essai selon besoin.

**Entrées**

decision_question, target_scope et evidence_sources datées/autorisées obligatoires. Variantes, référence, cadre d’échantillonnage, contraintes coût/sécurité et fenêtre facultatifs. Minimiser les données propriétaires.

**Sorties**

persona-research.md : registre des sources, ID/codage/conflits, groupes comportementaux, comparaison par groupe et protocole. Parts inconnues : aucun taux de victoire global.

[Déroulement · Limites et conditions d’arrêt · Exemple de demande](references/i18n/fr.md)

> Utilise `$multi-channel-persona-research` — Comparer en aveugle deux pages de réservation avec forums et support autorisé, puis prévoir un essai randomisé sans promettre de gain de conversion ; réponds en français en conservant les preuves, les inconnues et les limites d’autorisation.

## Couverture linguistique et validation

Ce guide localisé couvre objectif, prérequis, entrées, sorties, étapes, exemples et limites. Il ne traduit pas chaque référence ligne par ligne. Les références techniques détaillées, cas historiques, erreurs de scripts, interfaces d’exemple et images restent dans leur langue originale et peuvent être expliqués à la demande. Structure, liens et contraintes essentielles sont vérifiés ; aucune relecture par un locuteur natif de chaque langue n’est revendiquée.

Avant livraison, rapprocher entrées, preuves, valeurs manquantes, fichiers et critères d’achèvement d’origine. Marquer les étapes non exécutées comme non vérifiées ; la réussite d’un script ne valide pas une conclusion métier.
