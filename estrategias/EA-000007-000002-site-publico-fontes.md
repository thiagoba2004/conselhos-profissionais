# EA-000007-000002 — Site público próprio e acervo inicial de fontes

**Projeto:** PRJ-000007 — Conselhos Profissionais  
**Autoridade:** REQ-000007-20261010-002, autorização expressa de 10/10/2026  
**Origem:** EA-000007-000001, constituição documental pública encerrada  
**Infraestrutura existente:** GitHub público; metadata `has_pages=false` no início desta EA, sem site implantado.  
**Modelo inicial de entrega:** GitHub Pages usando arquivos Markdown em `main/docs`, sem framework e sem nova despesa autorizada.

## Objetivo

Implantar **site próprio, independente e não oficial**, com Home, campo de estudo, fontes e sobre, ancorado em registros verificáveis; iniciar um acervo mínimo com links e notas de proveniência, sem alegar pesquisa exaustiva ou atualização contínua já implantada.

## Plano de Fases

1. **FASE 01/05 [F-000007-000002-001] — Escopo, fontes e segurança**: confirmar autorização, visibilidade, host, público-alvo e fontes oficiais datadas. **Gate:** `SOURCE_BASELINE_AND_HOST_CONSTRAINTS_VERIFIED`.
2. **FASE 02/05 [F-000007-000002-002] — Arquitetura e conteúdo**: organizar Home, Eixos, Fontes e Sobre; separar informação estável e referências de pesquisa; evitar afirmação não suportada. **Gate:** `PUBLIC_CONTENT_STRUCTURE_REVIEWED`.
3. **FASE 03/05 [F-000007-000002-003] — Site Markdown preparado**: criar `docs/index.md`, `docs/eixos.md`, `docs/fontes.md`, `docs/sobre.md`; validar links, YAML front matter e referências. Ações documentais de GitHub podem ser feitas por Chat; trabalho de software/build multiarquivo customizado pertence ao Codex. **Gate:** `SITE_SOURCE_STAGED_IN_GITHUB`.
4. **FASE 04/05 [F-000007-000002-004] — Ativação do GitHub Pages**: responsável com acesso a Settings → Pages deve configurar **Deploy from a branch**, branch `main`, folder `/docs`, e salvar. Este ato de configuração não é coberto pela escrita documental do conector GitHub desta sessão. **Gate:** `PAGES_PUBLISHING_SOURCE_CONFIRMED`.
5. **FASE 05/05 [F-000007-000002-005] — Verificação pública**: conferir URL HTTP efetiva, navegação, legibilidade, independência institucional, ausência de dados sigilosos, proveniência de links e estado do deployment. Só então `PUBLIC_SITE_VERIFIED` e encerrar estratégia.

## Fontes iniciais selecionadas em 10/10/2026

1. **Lei nº 3.268/1957** — Lei federal, Planalto: https://www.planalto.gov.br/ccivil_03/leis/l3268.htm. Exemplo de legislação constitutiva e de competências no sistema de conselhos de medicina; não generalizar a todos os conselhos.
2. **Decisão Normativa TCU nº 216/2025** — TCU, norma de prestação de contas: https://pesquisa.apps.tcu.gov.br/redireciona/norma/NORMA-36629. Regras complementares de prestação de contas do segmento dos conselhos de fiscalização profissional; conferir alcance, alterações e vigência.
3. **Ordem de Serviço TCU nº 4/2026** — TCU, ato de organização: https://pesquisa.apps.tcu.gov.br/documento/btcu/Conselhos/%2520%2520%2520/DTRELEVANCIA%2520desc/10. Institui grupo de trabalho sobre governança e formulação de premissas; não equivale à edição de Lei Geral.
4. **Resolução CAU/BR nº 274/2026** — Portal de Transparência CAU/BR: https://transparencia.caubr.gov.br/resolucao274/. Exemplo de alteração normativa setorial; aplicação depende do âmbito do CAU.

A seleção não afirma completude, uniformidade institucional nem vigência de qualquer dispositivo isolado. Cada pesquisa adicional exige atualização datada, recorte e verificação. Fontes de outros sistemas não são transplantadas como se fossem normativas deste Projeto.

## Proteção e limites

- Repositório e futuro site são superfícies públicas: apenas `S0_PUBLICO` ou conteúdo não sensível revisado. Sem formulários, credenciais, logotipos oficiais, dados sigilosos ou serviços pagos.
- O código/fonte do site permanece no repositório atual; conteúdo público é restrito a `/docs`.
- Não duplicar `AGENTS.md`, logs internos, `PROJECT_STATE.json` ou outras fontes de governança no conteúdo de Pages.
- **Não alegar site no ar antes de provar configuração do Pages, pipeline e URL pública**, e não confundir marcador `has_pages=false` com permissão de ativação.
- Uma expansão para portal com interface customizada, backend, busca inteligente, alertas ou automação deve ser tratada com Codex/Work conforme catálogo de executor, autorização e gate local.
