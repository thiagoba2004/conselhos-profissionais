# AGENTS.md — Conselhos Profissionais

**project_code:** `PRJ-000007`  
**project_sequence:** `7`  
**project_name:** `Conselhos Profissionais`  
**repository:** `thiagoba2004/conselhos-profissionais`  
**generated_from_kernel:** `1.11`  
**migration_origin:** `EA-000000-000019 / Rota B`

## Missão de governança

Preservar e desenvolver o conteúdo comprovado deste repositório sem inferir
regras de domínio, estado histórico, integrações ou capacidades não
documentadas. Arquivos existentes prevalecem sobre memória conversacional.

## Ordem para novos pedidos

Registrar o pedido em `REQUEST_LOG.jsonl`, confirmar a persistência, identificar
a Estratégia Autônoma e seu Plano de Fases e somente então executar trabalho
substantivo. Nunca afirmar salvamento, commit, publicação ou implantação sem
verificação técnica.

## Fontes da verdade

1. arquivos persistidos neste repositório;
2. `PROJECT_STATE.json`;
3. `STRATEGY_LOG.jsonl` e `REQUEST_LOG.jsonl`;
4. histórico Git comprovado;
5. somente depois, contexto conversacional.

## Preservação

Não reescrever histórico append-only, não fabricar estado desconhecido e não
substituir regras locais mais rigorosas. Mudança destrutiva exige alvo exato,
justificativa, verificação e meio de recuperação.

<!-- MOGP:BEGIN AUTONOMOUS_STRATEGY_NUMBERING_V1 -->

## Numeração canônica de Estratégias Autônomas

Este Projeto usa identidade canônica imutável:

```text
Projeto: PRJ-000007
Estratégia: EA-000007-EEEEEE
Fase: F-000007-EEEEEE-FFF
```

Novas Estratégias exigem sequência local única e registro persistente antes
da execução. Identificadores legados permanecem como evidência e não são
reescritos. O catálogo global é índice; plano, estado e logs locais continuam
como fontes primárias do progresso.

<!-- MOGP:END AUTONOMOUS_STRATEGY_NUMBERING_V1 -->

## Continuidade

Ao responder “Onde paramos?”, informar Projeto, Estratégia, Fase, estado
comprovado, ponto exato e próximo passo lógico. Quando não houver Estratégia
local comprovada, declarar explicitamente `UNKNOWN_NOT_INFERRED`.

## Gate de atribuição de ações por executor — 10/10/2026

**Decisão humana transversal:** manter banco local `governanca/EXECUTOR_ACTION_CATALOG.json`, herdando as ações globais do catálogo `GOV-EXEC-ACTIONS-000001` e a política `GOV-POL-ECO-000001`. Para trabalho persistente, decompor a tarefa em ações identificáveis; antes de cada ação material, conferir `action_id`, `required_executor`, autorização, capacidades, limites, segurança e gates locais. É proibido encaminhar uma ação não classificada ou a executor divergente. A exceção exige decisão humana **expressa e específica**, registrada no catálogo global de overrides, com evidência verificável; aprovação desta política não é autorização genérica de exceção.

Preferir mecanismo determinístico seguro quando suficiente; usar o Chat em análise/documentação acessível e reservar Work/Codex para capacidades técnicas necessárias. A catalogação não substitui metodologia, checkpoints, políticas de sigilo ou autorizações existentes. O verificador `runtime/executor_action_gate.py` no repositório da Governança só bloqueia **despachos que efetivamente o invocarem**: não alegar interceptação automática das interfaces nativas Chat, Work ou Codex, nem mudança de executor sem comprovação.

## Missão e módulos de domínio — 10/10/2026

**Mandato:** `REQ-000007-20261010-001`; Gerador de Agents `EA-000002-000024`; estratégia local `EA-000007-000001`. Preservado o baseline EA-000000-000019 e o kernel atual `1.11`. Não retroagir missão ou estado a datas anteriores à aprovação.

**Missão vigente:** consultar [MISSAO_E_ESCOPO.md](MISSAO_E_ESCOPO.md). O Projeto é independente, **não oficial**, publicamente acessível pelo GitHub. Não representar nem simular representação institucional das entidades pesquisadas.

**Perfil e seleção de módulos:** `thiagoba2004/gerador-de-agents/profiles/conselhos-profissionais.json`. Ativados por evidência: `research`, `legal`, `publication` documental, `information-classification` e `execution-environments`. Demais módulos permanecem pendentes ou não aplicáveis conforme decisão no perfil; **nenhum site ou contato foi aprovado por inferência**.

**Pesquisa:** aplicar [POLITICA_FONTES_E_PUBLICACAO.md](POLITICA_FONTES_E_PUBLICACAO.md), com primazia de fontes institucionais datadas, confronto de versões/vigência, distinção entre fato e tese, e reprovação de conclusões não verificadas. A divulgação pública de parecer de conteúdo jurídico requer validação proporcional e não substitui aconselhamento individual.

**Publicação e segurança:** GitHub é `P2_GIT_PUBLICO_REPOSITORIO`, conforme `INFORMATION_HANDLING_PROFILE.json`. É proibido registrar nele S2+, segredos, dados pessoais não públicos, documentos sigilosos de processos e identidade visual oficial como se o Projeto fosse órgão representado. GitHub público é distinto de GitHub Pages/site em funcionamento.

**Continuidade:** recuperar `PROJECT_STATE.json`, `ROADMAP.md`, o plano `estrategias/EA-000007-000001-constituicao-publica.md` e logs. A presente constituição não certifica corpus de pesquisa nem ativa operações produtivas.

## Site público próprio e acervo inicial — 10/10/2026

**Autorização humana:** `REQ-000007-20261010-002`, estratégia local `EA-000007-000002`. O módulo `web-site` é **ATIVADO** por determinação expressa de criação de site público próprio; `contact-protocol`, automações, backend e software customizado não estão autorizados por inferência.

**Fonte canônica do site:** `main/docs` com quatro páginas Markdown; arquitetura em `SITE_ARCHITECTURE.md`, guia de apresentação em `SITE_STYLE_GUIDE.md` e fontes indexadas em `docs/fontes.md`. O GitHub deve publicar por Pages somente `/docs`, sem copiar os arquivos de governança para a árvore pública do site.

**Distinção de estados:** `SITE_SOURCE_STAGED_IN_GITHUB` significa código-fonte/conteúdo versionados, **não** `PUBLIC_SITE_VERIFIED`. Este último depende de configuração efetiva do Pages, observação HTTP, navegação e registro de evidência. O conector documental desta sessão não altera Settings → Pages.

**Execução por capacidade:** Chat pode registrar e publicar conteúdo Markdown no Git; construção técnica de site customizado/CSS/JavaScript ou build multiarquivo pertence ao Codex, nos limites do catálogo global de ações. Proibidos segredos, S2+, dados pessoais privados e aparência de entidade oficial. A política `POLITICA_FONTES_E_PUBLICACAO.md` continua vinculante.
