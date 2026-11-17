# Pesquisa multicanal de personas comportamentais

[简体中文](README.zh-CN.md) | [English](README.en.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Português](README.pt.md)

Use o idioma explicitamente solicitado; caso contrário, siga o idioma do pedido. Preserve comandos, identificadores, chaves JSON, valores enumerados, unidades e citações originais. Distinga traduções e originais. Não deduza país, moeda ou jurisdição pelo idioma. Leia as referências detalhadas relevantes e mantenha todas as verificações e autorizações existentes.

## Instalação e utilização

Transfira ou clone o repositório e copie o diretório do Skill indicado, com as suas references, scripts, assets e demais dependências existentes, para o diretório de Skills do ambiente. Preserve o nome e SKILL.md. Mudar o idioma da documentação não exige outra instalação. Os comandos são opções, não provas de instalação ou ativação.

```sh
git clone https://github.com/PDBen-Auto/multi-channel-persona-research-skill.git
```

## Pesquisa multicanal de personas comportamentais

`multi-channel-persona-research`

Ligar provas autorizadas, segmentos, comparação cega e plano A/B real sem confundir preferências simuladas com resultados.

Diretório do Skill: `.`

**Fundamento e dependências**

Decisão/âmbito e provas legíveis permitidas. Conclusões multicanal exigem pelo menos dois tipos de fonte independentes. Navegador, análise e plataforma experimental conforme necessário.

**Entradas**

Obrigatórios decision_question, target_scope, evidence_sources com datas/direitos. Opcionais variantes, base, plano amostral, restrições custo/segurança e janela. Minimizar dados próprios.

**Saídas**

persona-research.md: fontes, ID/codificação/conflitos, grupos comportamentais, comparação por grupo e plano experimental. Sem proporções conhecidas, não calcular taxa global de vitória.

[Procedimento · Limites e condições de interrupção · Exemplo de pedido](references/i18n/pt.md)

> Use `$multi-channel-persona-research` — Comparar cegamente duas páginas de reserva usando fóruns e suporte autorizado e desenhar ensaio aleatório sem afirmar aumento de conversão; responda em português e preserve as provas, os dados desconhecidos e os limites de autorização.

## Cobertura linguística e validação

Este guia localizado cobre objetivo, requisitos, entradas, saídas, passos, exemplos e limites; não traduz todas as referências linha por linha. Referências técnicas detalhadas, casos históricos, erros de scripts, interfaces de exemplo e imagens mantêm o idioma original e podem ser explicados a pedido. Verificam-se estrutura, ligações e restrições essenciais; não se afirma revisão por falantes nativos de cada idioma.

Antes da entrega, confira entradas, provas, valores em falta, ficheiros e critérios de conclusão originais. Assinale como não verificados os passos não executados; o sucesso de um script não valida conclusões comerciais.
