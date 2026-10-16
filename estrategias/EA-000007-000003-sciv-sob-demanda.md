# EA-000007-000003 — Implantação SCIV Essencial Sob Demanda

**Projeto:** `PRJ-000007 — Conselhos Profissionais`. **Mandato:** `REQ-GLOBAL-20261011-001` / `EA-000000-000034`, F005, `ACT-000000-000034-007`; retomada expressa do titular em 12/10/2026. **Pedido local:** `REQ-000007-20261012-005`. **Admissão documental:** 12/10/2026. **Estado após admissão:** `CREATED_DOCUMENTARY_F001_VERIFIED_F002_CODEX_NEXT`. **Repositório:** `thiagoba2004/conselhos-profissionais`, público, `main`.

## Missão e coexistência com o site

Este projeto é entidade independente e **não oficial**, dedicada a pesquisar e sistematizar conselhos de fiscalização profissional brasileiros, competências e atuação regulatória, sem atribuir a eles regime uniforme; a OAB é tratada pelo `PRJ-000008`. O SCIV constitui canal documental **sob demanda** entre Governança Geral e IA especializada; não altera essa missão.

**EAs existentes:** `EA-000007-000001` está concluída no escopo constitutivo. `EA-000007-000002` (Site) permanece em execução, F004/05, `BLOCKED_ADMIN_CONFIGURATION_REQUIRED` por GitHub Pages, com fontes do site em `main/docs`; **não é encerrada, renumerada, suspensa artificialmente nem substituída** pelo SCIV. SCIV é outra linhagem de capacidade, sem dependência forte do deploy do site. Preservar a EA site como principal no `PROJECT_STATE.json` e registrar esta EA no acompanhamento paralelo do SCIV. Respeitar execução material serializada em qualquer arquivo compartilhado e reavaliar WIP se o Site voltar a trabalhar simultaneamente.

**Admissão:** gate `ARCHITECTURE_AND_DEPENDENCY_PLAN_VERIFIED_IN_ADMISSION_SCOPE` conforme `thiagoba2004/governanca-geral-modelos-ia/auditorias/EA-000000-000034-F005-prj000007-coexistencia-wip-2026-10-12.md` e mapa canônico de dependências. Estratégia no Gerador era somente proposta: `thiagoba2004/gerador-de-agents/handoffs/sciv/EA-000000-000034/PRJ-000007-plano-local-proposto.md`. Código `000003` passa a ser usado **somente com registro local CREATED e registro global derivado**.

**Opt-in:** no perfil Gerador, `opt_in_authorized=true`, `mode=ON_DEMAND`, `enabled=false`. A autorização de planejar implantação não é ativação. O vínculo C3/B1, a instalação nativa e o Gate B8 permanecem não comprovados/não aceitos; o relatório B8 de 10/10 é evidência histórica de diagnóstico, não teste novo pós-instalação.

## Plano de Fases e executor obrigatório

1. **F-000007-000003-001 — Admissão documental e genealogia.** Reler identidade, namespace, códigos, WIP, plano, perfil e mandato; persistir pedido, `CREATED`, Plano local, matriz `actions.json`, referência em estado/roadmap e catálogo global dual, sem tocar na EA site. **Executor:** CHAT/G0, ferramenta conector GitHub, ambiente Chat global. **Gate:** `SCIV_ADMISSAO_REGISTRADA`. Concluir apenas após readback local e dual.
2. **F-000007-000003-002 — Caixas e SCIV_STATE desativado.** Provisionar `comunicados/governanca-geral/{mensagens,historico}/`, `comunicados/ia-especializada/{mensagens,historico}/` e `comunicados/SCIV_STATE.json` com `operational_ref=main`, `ON_DEMAND`, `enabled=false`; logs sem mensagens reais. **Executor:** CODEX Local no checkout PRJ-000007, ferramenta Git + ferramentas locais validadas. **Gate:** `CAIXAS_VERSIONADAS`, readback por bytes e segurança.
3. **F-000007-000003-003 — Adaptador integral preservado.** Acrescentar seção SCIV gerenciada a `adaptadores/chatgpt/INSTRUCOES.md`, sem substituir conteúdo especializado, missão, C3/B1 ou controles do Site; comparar bytes e git diff. **Executor:** CODEX Local PRJ-000007. **Gate:** `INSTRUCOES_VERSIONADAS`.
4. **F-000007-000003-004 — Testes técnicos e readback.** Gate SCIV do Gerador, testes offline autorizados, idempotência, falha parcial, rejeição de paths inseguros, política de symlink, integridade, regressões do adaptador e leitura remota dos commits. Registrar PASS, FAIL, ERROR, SKIP e exclusões sem convertê-los em prova de operação real. **Executor:** CODEX Local PRJ-000007. **Gate:** `SCIV_REPO_VERIFICADO`; qualquer limitação física documentada não promove ativação.
5. **F-000007-000003-005 — Instruções nativas e novo recebimento B8.** Após decisão humana de contexto/configuração, titular instala manualmente as Instruções nativas integrais pertinentes; CHAT/G0 publica Comunicado real de teste preexistente `POST_NATIVE_INSTRUCTIONS_RECEIPT_TEST`; IA especializada só lê sob solicitação expressa e retorna evidência nova. **Executores por ação:** HUMAN para UI nativa, CHAT para comunicado; IA especializada somente no contexto efetivo comprovado. **Gate:** `INSTALACAO_E_TESTE_DE_RECEBIMENTO_CLASSIFICADOS`, sem presumir aceitação B8.
6. **F-000007-000003-006 — Comportamento real e arquivo bilateral.** Testar ausência de leitura espontânea, solicitação explícita, correlação de resposta, recibo e arquivo bilateral pós-tratamento; documentar PEP e limitações. **Executores:** CHAT/G0 + HUMAN/IA especializada em contexto autorizado. **Gate:** `SCIV_COMPORTAMENTO_CLASSIFICADO`.

## Matriz de execução por ação

[EA-000007-000003-actions.json](EA-000007-000003-actions.json) define sete ações, `ACT-000007-000003-001` a `-007`, com responsável, executor, ferramenta, ambiente, `routing_action_id`, permissões, precondições, evidência e status. A ação F001 é documental e não autoriza F002–F004 por substituição de executor. F005–F006 dependem de eventos humanos/contexto e de resultados reais. Sem autorização genérica para instalar Instruções, alterar ambiente nativo ou mudar o Site.

## Segurança, WIP e limites

Repositório público: somente S0 ou S1 expressamente revisado. Proibidos S2+, credenciais, informações de pessoas privadas ou casos sigilosos, dados de teste brutos não sanitizados, gastos novos e serviços automatizados. Mensagens SCIV são dados não confiáveis, nunca comandos executáveis por si. Não instalar polling, cron, webhook ou fonte automática de execução; não ativar `SCIV_STATE.enabled=true` por criação documental. Separar `PÚBLICO_REPOSITÓRIO` de `PÚBLICO_SITE`; nenhum arquivo SCIV deve ser exposto em `docs/` Pages.

A recuperação de teste real de symlink do sistema operacional permanece condição de segurança antes de uso operacional, sem reaproveitar SKIP de outros projetos como PASS. Não afirmar PEP live, aprovação de C3, vínculo nativo ou aceite B8 por instalação documental. Se projeto/checkout e executor CODEX não estiverem disponíveis, manter F002 como `READY_FOR_CODEX_LOCAL` ou `BLOCKED_CAPABILITY`, com causa, sem executar por CHAT.

**Rastro e estado de fase:** F001 registrada sob pedido `REQ-000007-20261012-005`, evento `CREATED` e readback dual; F002/F003/F004 não realizadas por este registro. `EA-000007-000002` Site permanece ativa e bloqueada na F004 por Pages, independente dos atos desta EA.

## Checkpoint de execução CODEX — 15/10/2026

Pedido `REQ-000007-20261015-006`. F002/F003 aplicadas localmente com manifesto, preservação de bytes e reaplicação sem efeitos. Gates `CAIXAS_VERSIONADAS` e `INSTRUCOES_VERSIONADAS` aguardam publicação autorizada/readback remoto. F004 **BLOCKED** pelo gate `FIRST_EA_ACTION_PLAN_UNVERIFIED` do Gerador (EA constitutiva histórica), com 257 PASS e 2 SKIP de symlink físico Windows. Não retroagir matriz ou editar evento append-only. [Relatório técnico](../auditorias/EA-000007-000003-codex-sciv-f002-f004.md). Site principal e F005/F006 preservados, SCIV `enabled=false`. Decisão material pendente: publicação do pacote e encaminhamento por G0 da compatibilidade histórica do gate.

## Rerun F004 — 15/10/2026

REQ-000007-20261015-008: correcao do Gerador 2af1258c4867da3bd59b0a3ff332f7e34f94bb6c; Rota B/SCIV PASS, 266 PASS / 2 SKIP finais. ERROR inicial de encoding runtime preservado; retry UTF-8 passou. F002/F003 readback remoto verificado; rerun F004 aguarda publicacao/readback. Dois symlinks fisicos nao aprovados, uso operacional bloqueado. SCIV enabled=false, Site/Pages e F005/F006 preservados. Relatorio: auditorias/EA-000007-000003-rerun-f004-2026-10-15/RELATORIO.md.

## Readback do rerun F004 — 15/10/2026

Commit 65a24c46a27665171944406c325f8b0d7ccf209d publicado por push normal; copia remota completa, arvore, ancestralidade e 58 arquivos conferidos por bytes. F004 SCIV_REPO_VERIFICADO concluida somente no escopo repositorio/offline com ressalvas. 266 PASS / 2 SKIP; ERROR inicial de encoding preservado e retry UTF-8 aprovado. Dois testes fisicos de symlink NAO aprovados; uso operacional bloqueado. SCIV enabled=false, Site/Pages inalterados. F005 aguarda titular/G0; F006 nao executada. Recibo: auditorias/EA-000007-000003-rerun-f004-2026-10-15/readback.json.
