# 9. Módulo Métricas

## Visão Geral

O módulo **Métricas** é responsável por apresentar os indicadores coletados pela sonda durante o monitoramento contínuo da rede.

Seu objetivo é transformar os dados produzidos pelos processos de coleta em informações claras, organizadas e úteis para avaliação da qualidade operacional da infraestrutura monitorada.

Enquanto o módulo **Sistema** descreve o estado da própria sonda, o módulo **Métricas** descreve o comportamento da rede observada pela sonda.

Essa distinção constitui um dos princípios fundamentais da arquitetura da APTP.

---

## Objetivos

O módulo possui como principais objetivos:

- apresentar os indicadores coletados pela sonda;
- acompanhar a qualidade da conexão Wi-Fi;
- permitir análise da estabilidade da comunicação;
- identificar degradações de desempenho;
- apoiar processos de troubleshooting;
- disponibilizar histórico das medições realizadas.

---

## Filosofia de Coleta

A APTP foi concebida para medir a rede sob a perspectiva de um dispositivo cliente.

Isso significa que todas as medições representam a experiência observada pela própria sonda, simulando o comportamento de um equipamento conectado normalmente ao Access Point.

Essa abordagem diferencia a plataforma de soluções tradicionais de monitoramento baseadas exclusivamente em equipamentos de infraestrutura.

---

## Organização das Métricas

As métricas são agrupadas por categorias.

Essa organização facilita a leitura da interface e permite expansão futura sem necessidade de reorganização estrutural.

---

### Conectividade

Indicadores relacionados ao estado da conexão.

Exemplos:

- estado da interface;
- conexão Wi-Fi;
- disponibilidade da Internet;
- disponibilidade do gateway.

---

### Qualidade do Sinal

Indicadores relacionados à comunicação sem fio.

Exemplos:

- RSSI;
- intensidade do sinal;
- frequência utilizada;
- canal;
- largura de canal.

---

### Desempenho

Indicadores relacionados ao desempenho da comunicação.

Exemplos:

- latência;
- jitter;
- perda de pacotes;
- tempo médio de resposta.

---

### Transferência

Indicadores relacionados à capacidade da conexão.

Exemplos:

- taxa de transmissão;
- taxa de recepção;
- velocidade negociada;
- bitrate.

---

### Estabilidade

Indicadores utilizados para identificar oscilações.

Exemplos:

- reconexões;
- desconexões;
- reassociações;
- mudanças de Access Point;
- alterações de frequência.

---

## Processo de Coleta

De forma simplificada, o fluxo de funcionamento pode ser representado conforme o diagrama abaixo.

```text
Interface de Rede
        │
        ▼
 Scripts de Coleta
        │
        ▼
 Serviços Internos
        │
        ▼
 Processamento
        │
        ▼
 Armazenamento
        │
        ▼
 Controller
        │
        ▼
 Template HTML
        │
        ▼
 Dashboard
```

Essa organização garante independência entre coleta, processamento e apresentação das informações.

---

## Atualização das Informações

As métricas são produzidas continuamente durante o funcionamento da sonda.

Cada ciclo de coleta atualiza os indicadores disponíveis para consulta na interface web.

Essa estratégia permite acompanhar a evolução da qualidade da conexão ao longo do tempo.

---

## Estrutura da Página

O módulo foi concebido para apresentar seus indicadores utilizando componentes reutilizáveis.

Exemplo:

```text
Métricas

┌──────────────────────────────┐
│ Qualidade do Sinal           │
└──────────────────────────────┘

┌──────────────────────────────┐
│ Latência                     │
└──────────────────────────────┘

┌──────────────────────────────┐
│ Perda de Pacotes             │
└──────────────────────────────┘

┌──────────────────────────────┐
│ Taxas de Transmissão         │
└──────────────────────────────┘

┌──────────────────────────────┐
│ Estabilidade                 │
└──────────────────────────────┘
```

Cada grupo poderá evoluir independentemente conforme novas métricas forem incorporadas ao projeto.

---

## Evolução Prevista

O módulo foi planejado para suportar futuras funcionalidades, entre elas:

- gráficos históricos;
- séries temporais;
- indicadores de tendência;
- comparação entre períodos;
- análise estatística;
- exportação de dados;
- filtros avançados;
- consolidação por período;
- comparação entre sondas.

A arquitetura adotada permite incorporar esses recursos preservando a organização existente.

---

## Considerações

O módulo **Métricas** representa o núcleo técnico da APTP.

É através dele que a plataforma transforma informações coletadas pela sonda em indicadores capazes de representar, de forma objetiva, a qualidade da infraestrutura monitorada.

Sua evolução constitui uma das principais direções do projeto, uma vez que os indicadores produzidos serão a principal fonte de informação utilizada para diagnóstico, validação e acompanhamento contínuo da rede.