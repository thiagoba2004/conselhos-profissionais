# Política de fontes, verificação e publicação — PRJ-000007

**Escopo:** repositório público de pesquisa independente sobre Conselhos Profissionais  
**Ativação documental:** 10/10/2026 · **Responsabilidade:** governança local deste Projeto

## Segurança e superfícies

O GitHub do Projeto é **público** (`P2_GIT_PUBLICO_REPOSITORIO`). Somente informações `S0_PUBLICO` e artefatos `S1_INTERNO_NAO_SENSIVEL` especificamente revisados para exposição pública podem ser versionados aqui. Proibidos dados confidenciais (S2+), arquivos privados de clientes, documentos sigilosos de processos, credenciais, chaves, informações de contato pessoais não destinadas à divulgação e materiais de reserva estratégica.

Não é lícito usar branch privado de repositório público como cofre: a visibilidade do repositório e seu histórico exigem a mesma triagem. Caso haja fonte restrita legítima, usar superfície privada apropriada fora deste repositório, em conformidade com a Governança Geral, sem copiá-la para cá.

## Pesquisa auditável

1. Registrar a pergunta de pesquisa e definir recorte temporal, competência e entidade.
2. Identificar fonte primária institucional ou norma oficial; conservar URL, título, identificador, órgão e data de consulta. Fontes derivadas são complementares.
3. Conferir versão, vigência, alteração/revogação, hierarquia e recorte de aplicação antes de afirmar obrigação ou conclusão jurídica.
4. Separar fatos documentados, alegações, divergências, interpretação e hipótese. Não inventar precedentes, nomes de órgãos, atribuições ou competência.
5. Se não houver acesso/certeza, indicar `NÃO_VERIFICADO` e conservar a pendência, sem fabricar síntese.
6. Quando pertinente, consultar bibliografia acadêmica e BDTD/IBICT como descoberta, verificando cada obra na origem.

## Publicação

- Texto-fonte público: Markdown; HTML somente quando existir efetiva implantação de site/página aprovada; JSON/JSONL apenas para logs, estado, catálogos ou outros consumidores reais.
- Distinguir `RASCUNHO`, `REVISADO`, `VERSIONADO_NO_GITHUB`, `PUBLICADO_EM_SITE` e `VERIFICADO_PUBLICAMENTE`.
- A publicação de um README no GitHub **não** demonstra um site GitHub Pages, sistema de busca, canal de atendimento ou pesquisa concluída.
- Apresentar sempre a natureza **não oficial/independente** do Projeto; não copiar identidade visual nem usar logos de instituições como identidade própria.
- A pesquisa jurídica pública não constitui consultoria personalizada, representação profissional ou orientação para descumprimento de deveres.

## Controle de alteração

Qualquer peça substantiva deve ter Estratégia/escopo local, fontes verificadas, revisão e comprovação do destino público antes de ser apresentada como concluída. Preservar a versão anterior no Git e manter o `REQUEST_LOG.jsonl`, `STRATEGY_LOG.jsonl` e `PROJECT_STATE.json` coerentes.

**Não ativado por esta política:** GitHub Pages, novo formulário, credenciais, trabalho agendado, mecanismo de IA autônoma, nova despesa.
