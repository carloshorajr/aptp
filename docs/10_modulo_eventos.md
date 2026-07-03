# 10. Módulo Eventos

## Visão Geral

O módulo **Eventos** é responsável pelo registro cronológico de todas as ocorrências relevantes identificadas durante o funcionamento da APTP.

Seu objetivo é manter um histórico estruturado das atividades executadas pela plataforma, permitindo rastrear alterações de estado, falhas, alertas e demais situações relevantes ocorridas durante o monitoramento.

Enquanto o módulo **Métricas** responde à pergunta **"Como está a rede?"**, o módulo **Eventos** responde **"O que aconteceu na rede?"**.

Essa distinção torna o histórico de eventos uma importante ferramenta de diagnóstico e auditoria.

---

## Objetivos

O módulo possui os seguintes objetivos:

- registrar eventos relevantes da plataforma;
- manter histórico cronológico das ocorrências;
- facilitar processos de troubleshooting;
- auxiliar na identificação de falhas intermitentes;
- permitir auditoria das atividades executadas pela sonda;
- apoiar futuras análises estatísticas.

---

## Filosofia

A plataforma registra apenas eventos considerados relevantes para operação ou diagnóstico.

Não há interesse em produzir grandes volumes de informações sem utilidade prática.

Cada evento deve representar uma alteração de estado, uma ação executada ou uma condição que mereça atenção do operador.

---

## Estrutura de um Evento

Cada evento registrado pela plataforma deverá conter, sempre que possível, as seguintes informações:

- Data e hora da ocorrência;
- Nível do evento;
- Origem;
- Descrição;
- Categoria;
- Informações complementares (quando aplicável).

Essa padronização permite futuras integrações com ferramentas externas de observabilidade.

---

## Classificação

Os eventos são classificados por níveis de severidade.

### INFO

Representa informações operacionais normais.

Exemplos:

- inicialização da aplicação;
- início de coleta;
- atualização de configuração;
- reconexão bem-sucedida.

---

### WARNING

Representa situações que merecem atenção, mas que não impedem o funcionamento da plataforma.

Exemplos:

- aumento da latência;
- degradação do sinal;
- perda parcial de conectividade;
- alteração inesperada de parâmetros.

---

### ERROR

Representa falhas que comprometem ou impedem alguma funcionalidade da plataforma.

Exemplos:

- perda da interface Wi-Fi;
- falha na coleta;
- impossibilidade de acesso ao gateway;
- erro de leitura de arquivos.

---

## Origem dos Eventos

Os eventos podem ser produzidos por diferentes módulos da plataforma.

Entre eles:

- Sistema;
- Coleta;
- Comunicação;
- Interface de Rede;
- Configurações;
- Serviços internos;
- Backend.

Essa informação permite identificar rapidamente qual componente originou determinada ocorrência.

---

## Fluxo de Funcionamento

O processamento de eventos segue o fluxo abaixo.

```text
Ocorrência

      │

      ▼

Serviço responsável

      │

      ▼

Registro do Evento

      │

      ▼

Persistência

      │

      ▼

Controller

      │

      ▼

Template HTML

      │

      ▼

Interface Web
```

Essa organização mantém desacopladas as responsabilidades de geração, armazenamento e apresentação dos eventos.

---

## Interface

A interface do módulo foi concebida para facilitar consultas históricas.

Entre os recursos previstos destacam-se:

- listagem cronológica;
- filtros por período;
- filtros por nível;
- filtros por origem;
- pesquisa textual;
- ordenação dos registros.

Esses recursos permitem localizar rapidamente eventos específicos mesmo em históricos extensos.

---

## Persistência

Os eventos são armazenados de forma estruturada, preservando sua ordem cronológica.

Essa estratégia permite:

- reconstruir a sequência de acontecimentos;
- identificar padrões recorrentes;
- correlacionar eventos com métricas coletadas;
- apoiar processos de auditoria.

A arquitetura permanece preparada para futura substituição do mecanismo de persistência por banco de dados dedicado.

---

## Evolução Prevista

O módulo foi projetado para receber novos recursos ao longo da evolução da plataforma.

Entre eles:

- exportação para CSV;
- exportação para JSON;
- pesquisa avançada;
- agrupamento por categoria;
- estatísticas automáticas;
- integração com sistemas externos;
- envio de notificações;
- retenção configurável do histórico.

---

## Considerações

O módulo **Eventos** constitui a memória operacional da APTP.

Seu histórico permite compreender a sequência de acontecimentos ocorridos durante a operação da sonda, oferecendo contexto para interpretação das métricas coletadas e apoiando processos de diagnóstico, manutenção e auditoria da plataforma.

Embora opere de forma integrada aos demais módulos, sua função é complementar: registrar **quando**, **onde** e **como** cada ocorrência aconteceu, preservando um histórico confiável da operação da plataforma.