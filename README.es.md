# Investigación de personas conductuales multicanal

[简体中文](README.zh-CN.md) | [English](README.en.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Português](README.pt.md)

Usa el idioma solicitado expresamente; si no se indica, sigue el de la petición. Conserva comandos, identificadores, claves JSON, valores enumerados, unidades y citas originales. Separa traducciones y originales. No deduzcas país, moneda ni jurisdicción por el idioma. Lee las referencias detalladas pertinentes y conserva todos los controles y permisos existentes.

## Instalación y uso

Descarga o clona el repositorio y copia el directorio del Skill indicado, con sus references, scripts, assets y demás dependencias existentes, al directorio de Skills del entorno. Conserva el nombre y SKILL.md. Cambiar el idioma de la documentación no requiere otra instalación. Los comandos son opciones, no pruebas de instalación ni activación.

```sh
git clone https://github.com/PDBen-Auto/multi-channel-persona-research-skill.git
```

## Investigación de personas conductuales multicanal

`multi-channel-persona-research`

Unir pruebas autorizadas, segmentos de comportamiento, comparación ciega y plan A/B real sin tratar preferencias simuladas como resultados.

Directorio del Skill: `.`

**Fundamento y dependencias**

Decisión/alcance y pruebas legibles autorizadas. Conclusiones multicanal requieren dos tipos de fuente independientes como mínimo. Navegador, analítica y plataforma experimental según necesidad.

**Entradas**

Obligatorios decision_question, target_scope, evidence_sources con fechas/derechos. Opcionales variantes, base, marco muestral, restricciones coste/seguridad y ventana. Minimizar datos propios.

**Salidas**

persona-research.md: fuentes, ID/codificación/conflictos, grupos conductuales, comparación por grupo y plan. Sin proporciones conocidas, no hay tasa de victoria global.

[Procedimiento · Límites y condiciones de parada · Ejemplo de solicitud](references/i18n/es.md)

> Usa `$multi-channel-persona-research` — Comparar a ciegas páginas de reserva con foros y soporte autorizado y diseñar prueba aleatoria sin afirmar aumento de conversión; responde en español y conserva pruebas, datos desconocidos y límites de autorización.

## Cobertura lingüística y validación

Esta guía localizada cubre objetivo, requisitos, entradas, salidas, pasos, ejemplos y límites; no traduce línea por línea todas las referencias. La documentación técnica detallada, los casos históricos, errores de scripts, interfaces de ejemplo e imágenes mantienen su idioma original y pueden explicarse a petición. Se comprueban estructura, enlaces y restricciones esenciales; no se afirma una revisión por hablantes nativos de cada idioma.

Antes de entregar, concilia entradas, pruebas, valores ausentes, archivos y criterios de finalización originales. Marca como no verificados los pasos no ejecutados; el éxito de un script no valida conclusiones comerciales.
