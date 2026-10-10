# Arquitetura do Site Público — Conselhos Profissionais

**Projeto:** PRJ-000007 · **Autorização:** REQ-000007-20261010-002  
**Repositório:** público, GitHub · **Plataforma de publicação escolhida:** GitHub Pages por `main/docs`  
**Estado desta especificação:** documentação aprovada para implantação; deploy ainda não comprovado.

## Finalidade e arquitetura de informação

Diversidade dos regimes normativos e desenho dos conselhos profissionais. O site é uma ferramenta pública de acesso a referências primárias, sem representar uma entidade oficial.

| Página | Fonte Markdown | Saída esperada do Pages | Finalidade |
|---|---|---|---|
| Início | `docs/index.md` | `/` | Apresentação pública e recorte inicial |
| Eixos de pesquisa | `docs/eixos.md` | `/eixos.html` | Organização temática, sem conclusões antecipadas |
| Fontes oficiais | `docs/fontes.md` | `/fontes.html` | Índice curado de fontes externas verificadas |
| Sobre | `docs/sobre.md` | `/sobre.html` | Missão, método, limites e transparência |

Navegação horizontal presente no início de cada página, acessível também sem JavaScript. Links internos **relativos** e compatíveis com a URL de repositório `/nome-do-projeto/`.

## Fronteira de publicação

A fonte do Pages deverá ser somente `main/docs`. Não expor por cópia ou importação `AGENTS.md`, `PROJECT_STATE.json`, `REQUEST_LOG.jsonl`, `STRATEGY_LOG.jsonl` ou demais arquivos internos. Conteúdo do site não possui dados pessoais privados, credenciais, formulários nem integração de servidor.

A configuração administrativa deve ser feita em `Settings → Pages → Build and deployment → Deploy from a branch → main → /docs → Save`. Nenhuma configuração da API ou workflow extra está presumida.

## Evolução permitida, condicionada a validação técnica

- A versão inicial **documental Markdown** pode ser publicada via GitHub Pages sem etapa customizada de software. Layout e estilos padronizados do provedor não implicam identidade visual final homologada.
- Design visual responsivo próprio, CSS, templates, interações, motor de busca ou recursos de software deverão passar pela atribuição de executor `CODEX` e por testes adequados; não são pré-requisito para publicação da edição documental.
- Não ativar backend, tracking, analytics, formulários ou serviços externos sem escopo e autorização específicos.

## Aceite

A fase de implantação termina somente após observar URL pública e status do GitHub Pages, testar navegação, verificar segurança/exposição, integridade dos links e leitura mobile. Atualizar `PROJECT_STATE.json` a partir de evidências, não de previsão. Não declarar `PUBLIC_SITE_VERIFIED` antes do aceite HTTP real.
