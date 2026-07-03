# 2. Objetivos do Projeto

## Objetivo Geral

A APTP tem como objetivo fornecer uma plataforma capaz de monitorar continuamente a qualidade de operação de redes Wi-Fi sob a perspectiva de um dispositivo cliente, coletando métricas de conectividade, desempenho e estabilidade para auxiliar na identificação de falhas, degradações e comportamentos anormais da infraestrutura sem fio.

A plataforma foi concebida para operar de forma permanente, permitindo acompanhar a evolução das condições da rede ao longo do tempo e disponibilizando essas informações por meio de uma interface web intuitiva.

---

## Objetivos Específicos

Entre os principais objetivos da plataforma destacam-se:

- Monitorar continuamente a conectividade Wi-Fi.
- Verificar a disponibilidade da rede local e da Internet.
- Coletar métricas de desempenho da comunicação sem fio.
- Detectar eventos de desconexão e reconexão da interface Wi-Fi.
- Registrar alterações relevantes no estado da conexão.
- Armazenar informações históricas para análise posterior.
- Disponibilizar indicadores em tempo real por meio de um dashboard web.
- Facilitar processos de diagnóstico e troubleshooting.
- Servir como ferramenta de validação da qualidade operacional de Access Points.
- Permitir futura integração com plataformas de monitoramento e observabilidade.

---

## Princípios do Projeto

Durante o desenvolvimento da APTP foram adotados alguns princípios que orientam toda a arquitetura da plataforma.

### Simplicidade

Sempre que possível, a solução deve privilegiar implementações simples, legíveis e de fácil manutenção.

### Modularidade

Cada componente possui responsabilidades bem definidas, reduzindo o acoplamento entre as partes do sistema.

### Escalabilidade

Novas funcionalidades devem poder ser adicionadas sem necessidade de reestruturação significativa da arquitetura existente.

### Manutenibilidade

A organização do código deve facilitar correções, evoluções e substituição de componentes.

### Independência Tecnológica

Os módulos devem possuir baixo acoplamento, permitindo substituições futuras de bibliotecas, frameworks ou tecnologias sem impacto significativo sobre o restante da aplicação.

### Monitoramento Contínuo

A plataforma foi concebida para operar continuamente, realizando coletas periódicas e disponibilizando informações atualizadas durante todo o período de funcionamento.

### Evolução Incremental

O desenvolvimento da APTP segue uma estratégia baseada em sprints, permitindo a implementação gradual de novas funcionalidades sem comprometer a estabilidade da plataforma.
