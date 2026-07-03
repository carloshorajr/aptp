# 3. Arquitetura da Solução

## Visão Geral

A APTP foi desenvolvida seguindo uma arquitetura modular baseada no framework Flask, com separação clara entre backend, frontend, recursos estáticos, documentação e infraestrutura de execução.

Essa organização tem como objetivo facilitar a manutenção do projeto, reduzir o acoplamento entre os componentes e permitir que novas funcionalidades sejam adicionadas de forma incremental, preservando a estabilidade da aplicação.

A interface do sistema é construída utilizando Tailwind CSS e Flowbite, enquanto o backend é responsável pelo processamento das informações, coleta de métricas, disponibilização das páginas e comunicação com os demais componentes da plataforma.

Todo o ambiente é executado em containers Docker, garantindo reprodutibilidade do ambiente de desenvolvimento e implantação.

---

## Arquitetura em Camadas

A arquitetura da APTP está organizada em cinco camadas principais.

### Interface (Frontend)

Responsável pela interação com o usuário.

É composta por:

- Templates HTML (Jinja2)
- Tailwind CSS
- Flowbite
- CSS próprio da aplicação
- JavaScript

Sua função é apresentar as informações coletadas pelo sistema de forma clara, organizada e responsiva.

---

### Aplicação (Backend)

Implementada utilizando Flask.

É responsável por:

- Gerenciar as rotas da aplicação.
- Renderizar os templates HTML.
- Processar requisições.
- Disponibilizar dados para o frontend.
- Integrar os serviços internos da plataforma.

Cada módulo da aplicação possui sua própria organização, facilitando a manutenção e evolução do sistema.

---

### Serviços

Camada responsável pelas regras de negócio.

Entre suas responsabilidades estão:

- Processamento das métricas.
- Tratamento das informações coletadas.
- Consolidação de dados.
- Leitura de arquivos JSON.
- Geração de informações utilizadas pelo dashboard.

Esta camada evita que regras de negócio fiquem distribuídas pelas rotas da aplicação.

---

### Persistência

Atualmente a plataforma utiliza arquivos JSON para armazenamento das informações coletadas.

Esses arquivos são utilizados para registrar:

- Eventos.
- Métricas.
- Estado da aplicação.
- Informações auxiliares.

A arquitetura foi projetada para permitir futura substituição por banco de dados sem necessidade de alterações significativas nas demais camadas.

---

### Infraestrutura

Responsável pela execução da plataforma.

Inclui:

- Docker
- Docker Compose
- Scripts de inicialização
- Configurações do ambiente

Essa camada garante que toda a aplicação possa ser executada de forma padronizada em diferentes ambientes.

---

## Fluxo Geral da Aplicação

O funcionamento da APTP pode ser resumido da seguinte forma:

1. O usuário acessa a interface web.
2. O Flask recebe a requisição.
3. A rota correspondente é executada.
4. Os serviços processam ou consultam os dados necessários.
5. As informações são enviadas ao template HTML.
6. O frontend renderiza os componentes utilizando Tailwind CSS e Flowbite.
7. O usuário visualiza os indicadores atualizados.

---

## Características da Arquitetura

A arquitetura da APTP foi concebida para atender aos seguintes princípios:

- Organização modular.
- Baixo acoplamento entre componentes.
- Facilidade de manutenção.
- Evolução incremental.
- Interface moderna e responsiva.
- Separação entre apresentação, processamento e persistência.
- Compatibilidade com futuras expansões da plataforma.

Essa abordagem permite que novas funcionalidades sejam incorporadas ao projeto sem necessidade de reestruturação significativa da base existente, preservando a legibilidade e a organização do código.
