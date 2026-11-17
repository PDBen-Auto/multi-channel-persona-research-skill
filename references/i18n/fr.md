# Recherche de personas comportementaux multicanaux

`multi-channel-persona-research` · Français

## Objectif et périmètre

Relier preuves autorisées, segments, comparaison en aveugle et protocole A/B réel sans confondre préférence simulée et résultat.

## Fondements et dépendances

Décision/périmètre clairs et preuves lisibles autorisées. Une conclusion multicanale exige au moins deux types de sources indépendants. Navigateur, analytique et plateforme d’essai selon besoin.

## Entrées

decision_question, target_scope et evidence_sources datées/autorisées obligatoires. Variantes, référence, cadre d’échantillonnage, contraintes coût/sécurité et fenêtre facultatifs. Minimiser les données propriétaires.

## Sorties

persona-research.md : registre des sources, ID/codage/conflits, groupes comportementaux, comparaison par groupe et protocole. Parts inconnues : aucun taux de victoire global.

## Déroulement

1. Fixer décision/échantillonnage
2. choisir canaux complémentaires et biais
3. dédupliquer sans deviner l’identité interplateforme
4. coder tâches/contexte/alternatives/arbitrages
5. former groupes étayés
6. masquer A/B et évaluer dimensions soutenues
7. prédéfinir unité aléatoire, indicateur, garde-fous, référence, seuil et arrêt
8. auditer preuves/anonymisation.

## Limites et conditions d’arrêt

Pas d’entretiens inventés, recherche de contacts, inférence sensible ni proportions de population. Personas IA : synthetic_hypothesis. Sans plateforme/accord, protocole seulement. Cas publics entièrement fictifs.

## Exemple de demande

Utilise `$multi-channel-persona-research` — Comparer en aveugle deux pages de réservation avec forums et support autorisé, puis prévoir un essai randomisé sans promettre de gain de conversion ; réponds en français en conservant les preuves, les inconnues et les limites d’autorisation.

## Spécification complète

[Point d’entrée du Skill et références détaillées](../../SKILL.md).

Utiliser la langue explicitement demandée, sinon celle de la demande. Conserver les commandes, identifiants de Skill, clés JSON, valeurs d’énumération, unités et citations originales. Distinguer traduction et original. Ne déduire ni pays, ni devise, ni juridiction de la langue. Lire les références détaillées utiles et maintenir tous les contrôles et autorisations existants.

Avant livraison, rapprocher entrées, preuves, valeurs manquantes, fichiers et critères d’achèvement d’origine. Marquer les étapes non exécutées comme non vérifiées ; la réussite d’un script ne valide pas une conclusion métier.

## Couverture linguistique et validation

Ce guide localisé couvre objectif, prérequis, entrées, sorties, étapes, exemples et limites. Il ne traduit pas chaque référence ligne par ligne. Les références techniques détaillées, cas historiques, erreurs de scripts, interfaces d’exemple et images restent dans leur langue originale et peuvent être expliqués à la demande. Structure, liens et contraintes essentielles sont vérifiés ; aucune relecture par un locuteur natif de chaque langue n’est revendiquée.

