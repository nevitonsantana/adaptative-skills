#!/bin/bash

# Script para criar issues do Kanban Adaptative Skills
# Uso: ./scripts/create-kanban-issues.sh

set -e

echo "🎯 Criando issues do Kanban Adaptative Skills..."
echo ""

# Função para criar issue com labels
create_issue() {
    local title="$1"
    local body="$2"
    local labels="$3"
    
    echo "📝 Criando: $title"
    gh issue create --title "$title" --body "$body" --label "$labels" --repo nevitonsantana/adaptative-skills
    echo ""
}

# HIGH PRIORITY (P0)
create_issue \
  "Completar Domain Skeletons Pendentes" \
  "## Descrição
Implementar estruturas básicas para domains faltantes (product-management, governance, compliance)

## Critérios de Aceite
- [ ] Cada domain tem SKILL.md mínimo com core moves
- [ ] Templates de optional modules aplicados
- [ ] Triggers documentados

## Estimativa
3 dias

## Labels
domain-expansion, high-priority" \
  "priority: critical,category: domain-expansion"

create_issue \
  "Criar Guia de Telemetry Prática" \
  "## Descrição
Documentar como coletar, armazenar e analisar métricas de uso das skills

## Critérios de Aceite
- [ ] Schema de eventos definido
- [ ] Exemplos de instrumentação em 3 skills
- [ ] Dashboard template (Grafana/Datadog)

## Estimativa
2 dias

## Labels
telemetry, metrics, high-priority" \
  "priority: critical,category: documentation"

create_issue \
  "Índice de Descoberta de Skills" \
  "## Descrição
Criar sistema de busca/tagging para encontrar skills relevantes por contexto

## Critérios de Aceite
- [ ] Matriz skills × domínios × triggers
- [ ] Script de busca por keywords
- [ ] README com fluxograma de decisão

## Estimativa
2 dias

## Labels
discovery, ux, high-priority" \
  "priority: critical,category: tooling"

create_issue \
  "Política de Versionamento por Skill" \
  "## Descrição
Definir regras claras de semver aplicado a skills individuais

## Critérios de Aceite
- [ ] Documento VERSIONING.md
- [ ] Exemplos de major/minor/patch em skills reais
- [ ] Script de validação de changelog

## Estimativa
1 dia

## Labels
governance, versioning, high-priority" \
  "priority: critical,category: governance"

create_issue \
  "Identificar Cross-Skill Patterns" \
  "## Descrição
Extrair padrões reutilizáveis comuns entre múltiplas skills

## Critérios de Aceite
- [ ] Catálogo de 5-10 patterns identificados
- [ ] Templates de pattern aplicáveis
- [ ] Exemplos de composição

## Estimativa
3 dias

## Labels
patterns, refactoring, high-priority" \
  "priority: critical,category: refactoring"

create_issue \
  "Exemplos de Falhas Reais (Failure Cases)" \
  "## Descrição
Documentar casos onde skills falharam e lições aprendidas

## Critérios de Aceite
- [ ] 5-7 failure cases documentados
- [ ] Análise de causa raiz para cada
- [ ] Mitigações propostas

## Estimativa
2 dias

## Labels
learning, documentation, high-priority" \
  "priority: critical,category: documentation"

# MEDIUM PRIORITY (P1)
create_issue \
  "CLI Unificada para Gestão de Skills" \
  "## Descrição
Ferramenta de linha de comando para criar, validar, projetar skills

## Critérios de Aceite
- [ ] Comandos: \`create\`, \`validate\`, \`project\`, \`evolve\`
- [ ] Integração com evolution layer
- [ ] Documentação de uso

## Estimativa
5 dias

## Labels
tooling, cli, medium-priority" \
  "priority: high,category: tooling"

create_issue \
  "Integration Tests para Skills Críticas" \
  "## Descrição
Suite de testes automatizados para skills de alto impacto

## Critérios de Aceite
- [ ] Tests para top 5 skills mais usadas
- [ ] CI pipeline configurado
- [ ] Coverage report > 80%

## Estimativa
4 dias

## Labels
testing, ci-cd, medium-priority" \
  "priority: high,category: testing"

create_issue \
  "Skill Bundles por Persona" \
  "## Descrição
Pacotes pré-configurados de skills para personas específicas

## Critérios de Aceite
- [ ] Bundles: Engineer, PM, Designer, QA Lead
- [ ] Documentation de quando usar cada bundle
- [ ] Scripts de instalação por bundle

## Estimativa
3 dias

## Labels
bundles, personas, medium-priority" \
  "priority: high,category: feature"

create_issue \
  "Evolution Layer Automation" \
  "## Descrição
Automatizar partes do loop de evolução (observe → propose)

## Critérios de Aceite
- [ ] Bot que coleta observations automaticamente
- [ ] Template de proposal generation
- [ ] Workflow de review simplificado

## Estimativa
5 dias

## Labels
automation, evolution, medium-priority" \
  "priority: high,category: automation"

# LOW PRIORITY (P2)
create_issue \
  "Visual Skill Map Interativo" \
  "## Descrição
Mapa visual navegável de todas as skills e relações

## Estimativa
4 dias

## Labels
visualization, ux, low-priority" \
  "priority: medium,category: feature"

create_issue \
  "Multi-Agent Coordination Patterns" \
  "## Descrição
Patterns para skills coordenarem entre múltiplos agentes

## Estimativa
5 dias

## Labels
coordination, multi-agent, low-priority" \
  "priority: medium,category: research"

create_issue \
  "Skill Performance Benchmarks" \
  "## Descrição
Baseline de performance para comparar skills

## Estimativa
3 dias

## Labels
benchmarks, performance, low-priority" \
  "priority: medium,category: testing"

create_issue \
  "Community Contribution Guidelines" \
  "## Descrição
Guia completo para contribuições externas

## Estimativa
2 dias

## Labels
community, documentation, low-priority" \
  "priority: medium,category: community"

create_issue \
  "Localization Framework" \
  "## Descrição
Suporte a múltiplos idiomas nas dokumentações

## Estimativa
4 dias

## Labels
i18n, accessibility, low-priority" \
  "priority: medium,category: feature"

echo "✅ Todas as issues foram criadas!"
echo ""
echo "📋 Próximos passos:"
echo "1. Acesse https://github.com/users/nevitonsantana/projects/3/views/1"
echo "2. Adicione as issues às colunas apropriadas do Kanban"
echo "3. Configure a view de Roadmap com os milestones"
echo ""
