# PRJ-000007 — EA-000007-000003 — rerun F004

Pedido `REQ-000007-20261015-008`, 15/10/2026. Executor CODEX, ação
`ACT-000007-000003-004`, roteamento `TEST_EXECUTION/CODEX` efetivamente
consultado: ALLOW somente de alocação. Publicação de evidências e recibos
expressamente autorizada no pedido atual; autorização anterior `007` preservada.
Classificação: S1 não sensível, revisada para Git público.

## Resultado e alcance

Gate do Gerador **Rota B/SCIV PASS**, matriz atual PASS (7 ações, 6 fases).
`FIRST_EA_ACTION_PLAN_UNVERIFIED` resolvido pela correção canônica
`2af1258c4867da3bd59b0a3ff332f7e34f94bb6c`, obtida em cópia separada e
conferida por fetch do SHA no GitHub. Nenhuma edição do Gerador ou de G0.
Evidência histórica reconhecida: ancestral
`01d3a7cb134fa247ee3bfb89f2d4470648d03721`, contrato terminal
`PUBLIC_DOCUMENTARY_CONSTITUTION_VERIFIED`, fonte `gate`, quatro fases.
Matriz constitutiva permanece ausente, **NOT_BACKFILLED**; nenhum evento antigo
foi corrigido ou reescrito. Resultado integral em [gates-results.json](gates-results.json).

| Suíte final | Executados | PASS | FAIL | ERROR | SKIP |
|---|---:|---:|---:|---:|---:|
| Provisão e filesystem | 12 | 11 | 0 | 0 | 1 |
| Gerador e regressões Rota B | 97 | 97 | 0 | 0 | 0 |
| Runtime SCIV, UTF-8 explícito | 159 | 158 | 0 | 0 | 1 |
| Total final | 268 | 266 | 0 | 0 | 2 |

Primeira tentativa runtime: 157 PASS, 0 FAIL, **1 ERROR**, 1 SKIP.
`test_cli_recovery_across_actual_python_processes` recebeu bytes na codificação
padrão Windows, incompatíveis com a leitura JSON UTF-8. Evidência preservada em
[runtime-results-attempt1.json](runtime-results-attempt1.json). Reexecução integral
com `PYTHONUTF8=1` resolveu o erro, sem modificar runtime ou testes upstream.
O total final não apaga essa tentativa nem conta execuções repetidas como testes novos.

Os dois SKIP são ensaios físicos de symlink da provisão e do runtime,
novamente indisponíveis por Windows `winerror=1314`. **Não são PASS.** Não houve
elevação específica para habilitar symlinks nem recuperação da prova física.
Uso operacional permanece bloqueado por essa limitação e pelos gates humanos.

As suítes incluem idempotência, interrupção parcial/reconciliação, caminhos
inseguros, ambiente inesperado, corrupção, hardlink físico, junction físico,
reparse controlado, preservação do adaptador e regressões negativas do legado.
Python 3.12.10/venv existente; dependências no resultado runtime, sem instalações.
Fontes G0 fixadas no mesmo commit do ensaio anterior:
`86998b2dcea6fb45ecb07f73e9330af26a6fdace`. Imports e comandos revistos;
fixtures, Git e caixas temporárias. Bloqueio de socket no processo principal
não constitui isolamento universal nem PEP live. Logs brutos fora do Git público.

## Identidade, integridade e preservação

Checkout `thiagoba2004/conselhos-profissionais`, `origin` HTTPS esperado, `main`;
HEAD inicial e remoto consultado por transporte:
`38bfb1bdf247a0f06df383a2233443b8c487fc66`. Histórico completo, não shallow,
55 commits iniciais. `git fsck --full` saiu 0, com blobs dangling preexistentes;
nenhuma limpeza executada. Preservadas alterações locais dos logs e dois recibos
anteriores; estes são agora publicados com sua descrição histórica original.

[verification.json](verification.json) registra hashes de 16 arquivos protegidos
e de 81 fontes Python usadas. `docs/`, Site, AGENTS, missão, caixas e adaptador
permanecem iguais ao checkpoint. Bytes externos ao bloco SCIV preservados em
relação à base anterior à provisão. Logs mantêm o prefixo histórico completo.
Git normaliza LF; hashes físicos e Git são distinguidos. Recuperação por novo
commit corretivo, preservando estes e os commits anteriores; sem reset, rebase,
force push, stash automático ou remoção de objetos.

## Publicação, gates e continuidade

F002/F003 têm readback remoto anterior dos seis arquivos, comprovado no recibo
`../EA-000007-000003-publicacao-2026-10-15-readback.json`. F004 está tecnicamente
verificada no escopo documental/offline; publicação e readback deste rerun serão
registrados em recibo novo, por commit e hashes, antes do fechamento do acompanhamento.
O manifesto de publicação relaciona arquivos e hashes exatos revisados.
Recibo publicado descreve o commit de evidências predecessor: não afirma
autoverificação recursiva do commit que contém o próprio recibo.

`enabled=false`, ON_DEMAND, sem mensagens reais, instalação nativa, C3/B1,
aceite B8, comportamento real, serviços ou despesa. F005/F006 não executadas.
F004 pode encerrar somente no escopo de repositório/offline com ressalvas;
isso não habilita SCIV. Site EA-000007-000002 permanece principal, F004
`BLOCKED_ADMIN_CONFIGURATION_REQUIRED`; Pages não foi alterado ou verificado.

Próximo responsável: titular/G0, para reconciliar o catálogo global por ação
própria e decidir o contexto/configuração humana de F005, preservando a pendência
de segurança física antes de qualquer uso operacional. Nenhuma escrita global
ou novo teste de recebimento B8 foi feito por este rerun.

## Readback do rerun F004 — 15/10/2026

Commit 65a24c46a27665171944406c325f8b0d7ccf209d publicado por push normal; copia remota completa, arvore, ancestralidade e 58 arquivos conferidos por bytes. F004 SCIV_REPO_VERIFICADO concluida somente no escopo repositorio/offline com ressalvas. 266 PASS / 2 SKIP; ERROR inicial de encoding preservado e retry UTF-8 aprovado. Dois testes fisicos de symlink NAO aprovados; uso operacional bloqueado. SCIV enabled=false, Site/Pages inalterados. F005 aguarda titular/G0; F006 nao executada. Recibo: auditorias/EA-000007-000003-rerun-f004-2026-10-15/readback.json.
