# 4. Estrutura do Projeto

A APTP foi organizada de forma modular, separando claramente os componentes responsáveis pela interface, processamento, infraestrutura, armazenamento de dados e documentação.

Essa organização facilita a manutenção do código, reduz o acoplamento entre módulos e permite a evolução contínua da plataforma.

---

## Estrutura Geral

```text
aptp/
├── backend/
├── data/
├── docker/
├── docs/
├── frontend/
├── scripts/
├── requirements.txt
├── README.md
└── docker-compose.yml
```

Cada diretório possui uma responsabilidade específica dentro da arquitetura da aplicação.

---

## backend/

Contém toda a lógica da aplicação.

É responsável por:

- inicialização do Flask;
- registro dos Blueprints;
- rotas da aplicação;
- serviços internos;
- processamento das informações;
- comunicação entre frontend e backend.

Nenhum elemento visual é desenvolvido neste diretório.

Sua responsabilidade é exclusivamente o funcionamento da aplicação.

---

## frontend/

Contém todos os recursos responsáveis pela interface do usuário.

Neste diretório encontram-se:

- templates HTML (Jinja2);
- arquivos CSS;
- arquivos JavaScript;
- imagens;
- ícones;
- componentes visuais.

Toda alteração relacionada à experiência do usuário deve ocorrer nesta camada.

---

## data/

Responsável pelo armazenamento dos dados produzidos pela aplicação.

Entre eles:

- eventos;
- métricas;
- informações auxiliares;
- estados internos da plataforma.

Nesta versão do projeto, os dados são persistidos em arquivos JSON.

A estrutura foi planejada para permitir futura migração para um banco de dados sem alterações significativas na arquitetura.

---

## scripts/

Reúne scripts auxiliares utilizados pela plataforma.

Esses scripts são responsáveis por atividades como:

- coleta de informações;
- monitoramento;
- automações;
- inicialização de serviços;
- manutenção do ambiente.

Cada script possui responsabilidade única e deve permanecer independente dos demais sempre que possível.

---

## docker/

Contém todos os arquivos necessários para execução da plataforma utilizando Docker.

Entre eles:

- Dockerfile;
- docker-compose;
- configurações de containers;
- definições do ambiente de execução.

Toda configuração relacionada à infraestrutura da aplicação deve permanecer centralizada neste diretório.

---

## docs/

Destinado exclusivamente à documentação do projeto.

Seu objetivo é concentrar toda a documentação técnica necessária para desenvolvimento, manutenção e implantação da plataforma.

Entre os documentos previstos encontram-se:

- arquitetura;
- estrutura do projeto;
- fluxo da aplicação;
- componentes;
- padrões adotados;
- roadmap;
- guias de instalação.

---

## Arquivos da Raiz

Além dos diretórios principais, alguns arquivos possuem papel fundamental no funcionamento da plataforma.

### docker-compose.yml

Define todos os containers utilizados pela aplicação durante o desenvolvimento e implantação.

---

### requirements.txt

Lista todas as dependências Python necessárias para execução do backend.

---

### README.md

Apresenta uma visão geral do projeto, instruções básicas de instalação e informações iniciais para novos desenvolvedores.

---

## Organização do Código

Durante o desenvolvimento da APTP foram adotados alguns padrões de organização.

### Separação de responsabilidades

Cada diretório possui uma função bem definida.

Evita-se misturar regras de negócio, apresentação e infraestrutura.

---

### Modularização

Cada funcionalidade é implementada em módulos independentes, permitindo manutenção e expansão sem impacto significativo nas demais partes da aplicação.

---

### Evolução incremental

A arquitetura foi concebida para crescer de forma gradual.

Novos módulos podem ser adicionados sem necessidade de reorganização estrutural do projeto.

---

## Objetivo da Estrutura

A organização adotada busca oferecer:

- facilidade de manutenção;
- baixo acoplamento;
- alta legibilidade;
- escalabilidade;
- reutilização de componentes;
- padronização do desenvolvimento.

Essa estrutura constitui a base sobre a qual todas as funcionalidades da APTP são implementadas.
