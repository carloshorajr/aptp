# 1. Apresentação

## APTP – Access Point Testing Probe

A **APTP (Access Point Testing Probe)** é uma plataforma desenvolvida para monitoramento, coleta, processamento e visualização de indicadores relacionados ao funcionamento de redes sem fio, tendo como foco principal a análise da qualidade de operação de Access Points em ambientes corporativos.

O projeto surgiu da necessidade de substituir verificações pontuais e subjetivas por um processo contínuo, automatizado e padronizado de coleta de informações, permitindo identificar degradações de desempenho antes que elas sejam percebidas pelos usuários.

Diferentemente de ferramentas tradicionais de monitoramento de infraestrutura, que normalmente concentram sua análise em equipamentos de rede ou servidores, a APTP observa a rede sob a perspectiva de um cliente conectado. Dessa forma, torna-se possível avaliar a experiência real de utilização do ambiente Wi-Fi, medindo parâmetros diretamente relacionados à conectividade e à estabilidade da comunicação.

A plataforma foi concebida para ser executada em hardware de baixo consumo energético, permanecendo instalada de forma permanente nos ambientes monitorados. Cada unidade atua como uma sonda independente, responsável pela coleta local de métricas e pela disponibilização dessas informações através de uma interface web moderna, simples e de fácil interpretação.

Desde sua concepção, o projeto foi estruturado de forma modular, permitindo evolução contínua sem comprometer sua arquitetura. A separação entre coleta de dados, processamento, apresentação e interface gráfica facilita a manutenção, a expansão de funcionalidades e a adaptação a novos cenários de monitoramento.

Mais do que um painel de indicadores, a APTP tem como objetivo fornecer informações confiáveis para apoiar processos de diagnóstico, validação, auditoria e melhoria contínua da infraestrutura de redes sem fio, oferecendo uma visão clara da saúde operacional do ambiente monitorado.

---

Este documento apresenta a arquitetura da plataforma, sua organização interna, as tecnologias utilizadas, o fluxo de funcionamento do sistema e as decisões de projeto adotadas durante seu desenvolvimento. O objetivo é servir como referência técnica para manutenção, evolução e implantação da APTP.
