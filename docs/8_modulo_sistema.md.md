# 8. Módulo Sistema

## Visão Geral

O módulo **Sistema** concentra as informações relacionadas ao estado operacional da sonda onde a APTP está sendo executada.

Seu objetivo é disponibilizar ao usuário uma visão detalhada do ambiente de execução da plataforma, permitindo verificar rapidamente as condições atuais do equipamento, interfaces de rede e utilização dos principais recursos do sistema operacional.

As informações apresentadas neste módulo são obtidas diretamente da própria sonda, refletindo seu estado em tempo real.

---

## Objetivos

O módulo Sistema possui os seguintes objetivos:

- apresentar informações gerais da sonda;
- exibir indicadores de utilização dos recursos do equipamento;
- listar as interfaces de rede disponíveis;
- auxiliar no diagnóstico de problemas locais;
- servir como base para validação do funcionamento da plataforma.

---

## Informações Apresentadas

O módulo foi concebido para apresentar, entre outras, as seguintes informações:

### Identificação

- Hostname da sonda.
- Identificação do equipamento.

---

### Tempo de Funcionamento

Informações relacionadas ao tempo de operação contínua da sonda.

Exemplos:

- Uptime.
- Tempo desde a última inicialização.

---

### Processamento

Indicadores relacionados à utilização do processador.

Exemplos:

- Uso atual da CPU.
- Percentual de utilização.

---

### Memória

Indicadores referentes ao consumo de memória do sistema operacional.

Exemplos:

- Memória utilizada.
- Percentual de utilização.

---

### Armazenamento

Informações relativas ao armazenamento disponível.

Exemplos:

- Espaço utilizado.
- Espaço total.
- Percentual de ocupação.

---

### Interfaces de Rede

O módulo apresenta todas as interfaces de rede detectadas pelo sistema.

Para cada interface podem ser disponibilizadas informações como:

- nome da interface;
- descrição;
- endereço IP;
- endereço MAC;
- SSID (quando aplicável);
- demais informações relevantes.

Essa visão permite validar rapidamente se a sonda encontra-se conectada conforme esperado.

---

## Origem das Informações

Os dados apresentados neste módulo são obtidos através dos serviços internos da aplicação.

De forma simplificada, o fluxo ocorre da seguinte maneira:

```text
Sistema Operacional
        │
        ▼
 Serviços de Coleta
        │
        ▼
SystemService
NetworkService
        │
        ▼
SystemController
        │
        ▼
system.html
        │
        ▼
Interface Web
```

Essa organização mantém a separação entre coleta, processamento e apresentação das informações.

---

## Estrutura da Página

A interface do módulo Sistema é composta por um conjunto de cards reutilizáveis.

Cada card representa uma categoria específica de informação.

Exemplo:

```text
Sistema

┌──────────────┐
│ Hostname     │
└──────────────┘

┌──────────────┐
│ Uptime       │
└──────────────┘

┌──────────────┐
│ CPU          │
└──────────────┘

┌──────────────┐
│ Memória      │
└──────────────┘

┌──────────────┐
│ Disco        │
└──────────────┘

┌──────────────┐
│ Interfaces   │
└──────────────┘
```

A utilização de componentes reutilizáveis permite manter consistência visual em toda a plataforma.

---

## Responsabilidades do Controller

O controller do módulo possui como responsabilidades:

- solicitar informações aos serviços internos;
- consolidar os dados necessários;
- preparar o contexto enviado ao template;
- renderizar a página do módulo.

Sempre que possível, regras de negócio permanecem nos serviços, mantendo o controller responsável apenas pela coordenação da requisição.

---

## Responsabilidades dos Serviços

A coleta das informações é realizada por serviços especializados.

Entre suas responsabilidades estão:

- consultar o sistema operacional;
- identificar interfaces de rede;
- calcular utilização dos recursos;
- organizar os dados para apresentação.

Essa separação favorece reutilização do código e facilita testes e manutenção.

---

## Evolução Prevista

O módulo Sistema foi projetado para receber novos indicadores conforme a evolução da plataforma.

Entre as funcionalidades previstas destacam-se:

- temperatura do equipamento;
- carga média do sistema;
- informações detalhadas de armazenamento;
- versão do sistema operacional;
- versão do kernel;
- arquitetura do processador;
- monitoramento de processos;
- utilização da rede em tempo real.

Essas funcionalidades poderão ser incorporadas sem alterações estruturais na arquitetura existente.

---

## Considerações

O módulo Sistema representa a principal fonte de informações sobre a própria sonda.

Além de auxiliar no diagnóstico operacional da plataforma, ele fornece os dados necessários para validar se o ambiente de execução encontra-se em condições adequadas para realização das coletas e do monitoramento contínuo da rede.