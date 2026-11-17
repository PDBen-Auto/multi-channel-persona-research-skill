# Investigación de personas conductuales multicanal

`multi-channel-persona-research` · Español

## Objetivo y alcance

Unir pruebas autorizadas, segmentos de comportamiento, comparación ciega y plan A/B real sin tratar preferencias simuladas como resultados.

## Fundamento y dependencias

Decisión/alcance y pruebas legibles autorizadas. Conclusiones multicanal requieren dos tipos de fuente independientes como mínimo. Navegador, analítica y plataforma experimental según necesidad.

## Entradas

Obligatorios decision_question, target_scope, evidence_sources con fechas/derechos. Opcionales variantes, base, marco muestral, restricciones coste/seguridad y ventana. Minimizar datos propios.

## Salidas

persona-research.md: fuentes, ID/codificación/conflictos, grupos conductuales, comparación por grupo y plan. Sin proporciones conocidas, no hay tasa de victoria global.

## Procedimiento

1. Fijar decisión/muestreo
2. escoger canales complementarios y sesgos
3. deduplicar sin adivinar identidades entre plataformas
4. codificar tareas/contexto/alternativas/intercambios
5. formar grupos con pruebas
6. ocultar etiquetas A/B y evaluar dimensiones demostradas
7. predefinir unidad aleatoria, métrica, protecciones, base, umbral y parada
8. auditar evidencia/anonimización.

## Límites y condiciones de parada

No inventar entrevistas, extraer contactos, inferir atributos sensibles ni proporciones poblacionales. Personas IA: synthetic_hypothesis. Sin plataforma/permiso solo plan. Casos públicos completamente ficticios.

## Ejemplo de solicitud

Usa `$multi-channel-persona-research` — Comparar a ciegas páginas de reserva con foros y soporte autorizado y diseñar prueba aleatoria sin afirmar aumento de conversión; responde en español y conserva pruebas, datos desconocidos y límites de autorización.

## Especificación completa

[Entrada del Skill y referencias detalladas](../../SKILL.md).

Usa el idioma solicitado expresamente; si no se indica, sigue el de la petición. Conserva comandos, identificadores, claves JSON, valores enumerados, unidades y citas originales. Separa traducciones y originales. No deduzcas país, moneda ni jurisdicción por el idioma. Lee las referencias detalladas pertinentes y conserva todos los controles y permisos existentes.

Antes de entregar, concilia entradas, pruebas, valores ausentes, archivos y criterios de finalización originales. Marca como no verificados los pasos no ejecutados; el éxito de un script no valida conclusiones comerciales.

## Cobertura lingüística y validación

Esta guía localizada cubre objetivo, requisitos, entradas, salidas, pasos, ejemplos y límites; no traduce línea por línea todas las referencias. La documentación técnica detallada, los casos históricos, errores de scripts, interfaces de ejemplo e imágenes mantienen su idioma original y pueden explicarse a petición. Se comprueban estructura, enlaces y restricciones esenciales; no se afirma una revisión por hablantes nativos de cada idioma.

