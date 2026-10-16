# ROADMAP — Conselhos Profissionais

**project_code:** `PRJ-000007`  
**status:** `GOVERNANCE_BASELINE_ESTABLISHED`

## Estado comprovado

A infraestrutura mínima de governança foi criada pela
`EA-000000-000019`, usando a Rota B do Gerador. Este arquivo não inventa uma
Estratégia local nem substitui planos substantivos existentes em outros
caminhos do repositório.

## Próximo passo

Reconciliar objetivos, estratégias e fases locais somente a partir de evidência
persistida. Até essa reconciliação, o estado substantivo permanece
`UNKNOWN_NOT_INFERRED`.

## Constituição documental pública — 10/10/2026

**Estratégia:** `EA-000007-000001`, aprovada por `REQ-000007-20261010-001` e conduzida pela Rota B do Gerador `EA-000002-000024`. Esta seção complementa sem apagar a história da EA-000000-000019.

1. **F01:** inventário, identidade e repositório público verificados.
2. **F02:** missão e perfis específicos dos módulos registrados no Gerador.
3. **F03:** README público, missão, protocolo de fontes/publicação, classificação da informação e AGENTS integrados.
4. **F04:** readback, auditoria de conformidade e encerramento documental.

**Gate de conclusão:** `PUBLIC_DOCUMENTARY_CONSTITUTION_VERIFIED`, sem criar site ou afirmar pesquisa substantiva verificada.

**Primeiro candidato de entrega posterior:** Inventariar os conselhos profissionais e fontes institucionais oficiais, estabelecendo critérios sem presumir regimes uniformes. Não iniciar automaticamente; recuperar o mandato local, definir escopo, fonte e critério de verificação e selecionar a estratégia pertinente.

**Restrições:** GitHub público, fonte oficial verificada, representação não oficial, vedação de S2+, dados privados, despesas e implantação web presumida. A verificação de site/Pages permanece `NOT_VERIFIED`.

## EA-000007-000002 — Site próprio e acervo inicial de fontes — 10/10/2026

**Autoridade:** `REQ-000007-20261010-002` · [Plano de Fases](estrategias/EA-000007-000002-site-publico-fontes.md).

- **F01/05:** delimitação de fontes, repositório público e arquitetura Pages — realizada.
- **F02/05:** conteúdo inicial e arquitetura `SITE_ARCHITECTURE.md` — preparada.
- **F03/05:** arquivos `docs/index.md`, `docs/eixos.md`, `docs/fontes.md`, `docs/sobre.md` — salvos em `main`, pendente de auditoria final.
- **F04/05:** habilitar GitHub Pages de `main/docs` — **aguarda configuração pelo proprietário na interface administrativa**.
- **F05/05:** verificar URL pública, conteúdo servido, links e exclusão de dados sensíveis — **NÃO INICIADA**.

**Proveniência:** 4 referências iniciais oficiais identificadas, sem reivindicação de exaustividade ou revisão completa de vigência. **Sem construção de interface customizada nem gasto novo.** O site não deve ser apresentado como publicado antes de evidência de Pages + HTTP.

## EA-000007-000003 — SCIV Essencial Sob Demanda (trilha separada) — 12/10/2026

**Programa:** `EA-000000-000034`, F005; mandato `REQ-GLOBAL-20261011-001`. **Admissão:** `REQ-000007-20261012-005`; [Plano local](estrategias/EA-000007-000003-sciv-sob-demanda.md) e [matriz de ações](estrategias/EA-000007-000003-actions.json); evidência de coexistência/WIP em `thiagoba2004/governanca-geral-modelos-ia/auditorias/EA-000000-000034-F005-prj000007-coexistencia-wip-2026-10-12.md`.

- **F001/06 — Admissão documental:** **VERIFIED_DOCUMENTARY_AND_DUAL_REGISTRY_SCOPE**; `CREATED` local, Plano/matriz/logs e catálogo global registrados, com readback. Gate `SCIV_ADMISSAO_REGISTRADA` satisfeito somente no escopo documental.
- **F002/06 — Caixas/SCIV_STATE desativado:** aplicado e verificado localmente em 15/10/2026; versionamento/readback remoto pendentes de autorização específica.
- **F003/06 — Adaptador SCIV preservador:** bloco aplicado localmente com preservação de bytes; versionamento/readback remoto pendentes.
- **F004/06 — Testes offline/readback:** **BLOCKED**: testes 257 PASS / 2 SKIP; gate do Gerador FAIL `FIRST_EA_ACTION_PLAN_UNVERIFIED` por compatibilidade histórica da EA constitutiva; readback remoto pendente.
- **F005/06 — Instruções nativas/teste B8 pós-instalação:** requer configuração/autorizações humanas, não iniciado.
- **F006/06 — Comportamento real e arquivo:** não iniciado.

**WIP:** o Site `EA-000007-000002` continua a estratégia principal em F004 `BLOCKED_ADMIN_CONFIGURATION_REQUIRED`, com `main/docs` intacto e sem alegar Pages publicado. O SCIV é capacidade documental separada; serializar operações em arquivos compartilhados, sem concorrência de escritores nem promoção do Gate Pages. `ON_DEMAND`, `enabled=false`, B8 não aceito, C3/B1 não comprovados; nenhum site, serviço, polling, webhook ou gasto novo foi autorizado pela admissão.

**Handoff de engenharia emitido em 12/10; execução local registrada em 15/10:** [F002–F004 — CODEX Local PRJ-000007](handoffs/codex/EA-000007-000003-SCIV-F002-F004.md), condicionado a checkout/permite efetivo, segurança e autorização material de efeitos. Global `EA-000000-000034/F005/ACT-008` permanece PLANNED; nenhum SCIV foi ativado.

## Checkpoint CODEX — 15/10/2026

[Relatório F002–F004](auditorias/EA-000007-000003-codex-sciv-f002-f004.md). Pacote local aplicado, SCIV desativado; gates de versão remota pendentes. F004 bloqueada pelo gate histórico do Gerador, sem modificar logs anteriores. Titular/G0 decide publicação e encaminhamento do bloqueio. Site/Pages e F005/F006 SCIV permanecem sem promoção.

## Rerun F004 — 15/10/2026

REQ-000007-20261015-008: correcao do Gerador 2af1258c4867da3bd59b0a3ff332f7e34f94bb6c; Rota B/SCIV PASS, 266 PASS / 2 SKIP finais. ERROR inicial de encoding runtime preservado; retry UTF-8 passou. F002/F003 readback remoto verificado; rerun F004 aguarda publicacao/readback. Dois symlinks fisicos nao aprovados, uso operacional bloqueado. SCIV enabled=false, Site/Pages e F005/F006 preservados. Relatorio: auditorias/EA-000007-000003-rerun-f004-2026-10-15/RELATORIO.md.

## Readback do rerun F004 — 15/10/2026

Commit 65a24c46a27665171944406c325f8b0d7ccf209d publicado por push normal; copia remota completa, arvore, ancestralidade e 58 arquivos conferidos por bytes. F004 SCIV_REPO_VERIFICADO concluida somente no escopo repositorio/offline com ressalvas. 266 PASS / 2 SKIP; ERROR inicial de encoding preservado e retry UTF-8 aprovado. Dois testes fisicos de symlink NAO aprovados; uso operacional bloqueado. SCIV enabled=false, Site/Pages inalterados. F005 aguarda titular/G0; F006 nao executada. Recibo: auditorias/EA-000007-000003-rerun-f004-2026-10-15/readback.json.
