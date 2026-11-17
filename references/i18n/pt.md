# Pesquisa multicanal de personas comportamentais

`multi-channel-persona-research` · Português

## Objetivo e âmbito

Ligar provas autorizadas, segmentos, comparação cega e plano A/B real sem confundir preferências simuladas com resultados.

## Fundamento e dependências

Decisão/âmbito e provas legíveis permitidas. Conclusões multicanal exigem pelo menos dois tipos de fonte independentes. Navegador, análise e plataforma experimental conforme necessário.

## Entradas

Obrigatórios decision_question, target_scope, evidence_sources com datas/direitos. Opcionais variantes, base, plano amostral, restrições custo/segurança e janela. Minimizar dados próprios.

## Saídas

persona-research.md: fontes, ID/codificação/conflitos, grupos comportamentais, comparação por grupo e plano experimental. Sem proporções conhecidas, não calcular taxa global de vitória.

## Procedimento

1. Fixar decisão/amostragem
2. escolher canais complementares e vieses
3. deduplicar sem adivinhar identidades entre plataformas
4. codificar tarefas/contexto/alternativas/compromissos
5. formar grupos sustentados
6. ocultar A/B e avaliar dimensões comprovadas
7. predefinir unidade aleatória, métrica, salvaguardas, base, limiar e paragem
8. auditar provas/anonimização.

## Limites e condições de interrupção

Não inventar entrevistas, procurar contactos, inferir atributos sensíveis ou proporções populacionais. Personas IA: synthetic_hypothesis. Sem plataforma/permissão, apenas plano. Casos públicos integralmente fictícios.

## Exemplo de pedido

Use `$multi-channel-persona-research` — Comparar cegamente duas páginas de reserva usando fóruns e suporte autorizado e desenhar ensaio aleatório sem afirmar aumento de conversão; responda em português e preserve as provas, os dados desconhecidos e os limites de autorização.

## Especificação completa

[Entrada do Skill e referências detalhadas](../../SKILL.md).

Use o idioma explicitamente solicitado; caso contrário, siga o idioma do pedido. Preserve comandos, identificadores, chaves JSON, valores enumerados, unidades e citações originais. Distinga traduções e originais. Não deduza país, moeda ou jurisdição pelo idioma. Leia as referências detalhadas relevantes e mantenha todas as verificações e autorizações existentes.

Antes da entrega, confira entradas, provas, valores em falta, ficheiros e critérios de conclusão originais. Assinale como não verificados os passos não executados; o sucesso de um script não valida conclusões comerciais.

## Cobertura linguística e validação

Este guia localizado cobre objetivo, requisitos, entradas, saídas, passos, exemplos e limites; não traduz todas as referências linha por linha. Referências técnicas detalhadas, casos históricos, erros de scripts, interfaces de exemplo e imagens mantêm o idioma original e podem ser explicados a pedido. Verificam-se estrutura, ligações e restrições essenciais; não se afirma revisão por falantes nativos de cada idioma.

