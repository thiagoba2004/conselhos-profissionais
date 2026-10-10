# Verificação da fonte do Site — EA-000007-000002

**Data:** 10/10/2026  
**Projeto:** PRJ-000007 — Conselhos Profissionais  
**Mandato:** REQ-000007-20261010-002  
**Método:** leitura de arquivos no GitHub `main`, conferência determinística de conteúdo e estado estruturado. Não é teste de deploy, renderização real do Jekyll, acessibilidade mobile ou inspeção do histórico integral.

## Resultado

- `docs/index.md`: presente com YAML front matter e entrada pública.
- `docs/eixos.md`, `docs/fontes.md` e `docs/sobre.md`: presentes.
- Navegação relativa: `./`, `eixos.html`, `fontes.html`, `sobre.html` em todas as quatro páginas — **PASSOU**.
- Índice de fontes: **4** referências institucionais externas identificadas, com notas de escopo e corte de 10/10/2026 — **PASSOU** no inventário documental, sem prova de cobertura exaustiva.
- Natureza independente/não oficial declarada; nenhuma tag `<script>`, `<form>` ou padrão trivial de senha no conteúdo novo — **PASSOU** a inspeção delimitada.
- `PROJECT_STATE.json`: sem URL Pages inventada e `public_http_verified=false` — **PASSOU**.
- `SITE_ARCHITECTURE.md` e `SITE_STYLE_GUIDE.md`: existentes; estilo customizado **não** implementado.
- Módulo `web-site` promovido para **ATIVADO** no perfil do Gerador, após autorização humana para site próprio.

## Gate e dependência externa

**`SITE_SOURCE_STAGED_IN_GITHUB=VERIFIED`** para os arquivos Markdown, não para o deploy Pages.

**`PAGES_PUBLISHING_SOURCE_CONFIRMED=BLOCKED_ADMIN_CONFIGURATION_REQUIRED`**: GitHub metadata `has_pages=false` na verificação inicial. Esta sessão dispõe do conector de leitura/escrita de conteúdo, **não** de ação administrativa para habilitar GitHub Pages.

O responsável precisa configurar `Settings → Pages → Deploy from a branch → main → /docs → Save`. Após a confirmação, verificar o status GitHub Pages e a URL HTTP pública, além de navegação e legibilidade, para fechar F04/F05. Não usar URL prevista como evidência de publicação.

**Estado desta EA:** `IN_PROGRESS_AWAITING_PAGES_SETTINGS`; nenhum workflow, build customizado, novo custo ou operação externa foi criado.
