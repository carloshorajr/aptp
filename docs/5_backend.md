# 5. Backend

## Visão Geral

O backend da APTP é desenvolvido utilizando o framework **Flask**, responsável por toda a lógica da aplicação, processamento das informações, disponibilização das páginas da interface web e integração entre os componentes internos da plataforma.

A escolha do Flask ocorreu devido à sua simplicidade, modularidade e facilidade de manutenção, características compatíveis com a proposta da APTP de evoluir continuamente sem aumentar desnecessariamente a complexidade da aplicação.

O backend foi organizado de forma modular, permitindo que novas funcionalidades sejam incorporadas gradualmente por meio de Blueprints, serviços e módulos independentes.

---

## Responsabilidades

O backend possui as seguintes responsabilidades principais:

- inicializar a aplicação Flask;
- registrar os Blueprints;
- disponibilizar as rotas HTTP;
- processar as requisições do usuário;
- coletar e preparar os dados apresentados na interface;
- ler os arquivos JSON utilizados pela plataforma;
- renderizar os templates HTML;
- centralizar as regras de negócio da aplicação.

---

## Arquitetura

De forma simplificada, o fluxo interno do backend pode ser representado conforme o diagrama abaixo.

```text
                Navegador
                     │
                     ▼
              Requisição HTTP
                     │
                     ▼
                  Flask
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
      Blueprints            Serviços
          │                     │
          └──────────┬──────────┘
                     ▼
              Leitura dos Dados
                     │
                     ▼
            Renderização Jinja2
                     │
                     ▼
                Página HTML
```

---

## Blueprints

A aplicação utiliza a arquitetura baseada em **Blueprints**, recurso nativo do Flask que permite dividir o sistema em módulos independentes.

Cada Blueprint representa uma área funcional da aplicação.

Essa abordagem oferece diversas vantagens:

- organização do código;
- facilidade de manutenção;
- reutilização de componentes;
- baixo acoplamento;
- expansão gradual da plataforma.

---

## Rotas

As rotas representam os pontos de entrada da aplicação.

Cada rota possui responsabilidade única, normalmente relacionada a uma página específica da interface.

Exemplos:

- Dashboard
- Sistema
- Eventos
- Métricas
- Configurações

Cada rota prepara os dados necessários e renderiza o template correspondente.

---

## Renderização de Templates

A interface web é construída utilizando o mecanismo de templates **Jinja2**, integrado ao Flask.

Esse mecanismo permite combinar:

- HTML;
- dados provenientes do backend;
- estruturas condicionais;
- laços de repetição;
- reutilização de componentes.

A separação entre lógica e apresentação torna o código mais organizado e facilita a manutenção da interface.

---

## Serviços

Sempre que possível, as regras de negócio são implementadas em serviços independentes.

Essa abordagem evita que as rotas acumulem responsabilidades além do tratamento da requisição.

Os serviços são responsáveis por atividades como:

- leitura de informações;
- consolidação de dados;
- processamento de métricas;
- preparação dos indicadores apresentados ao usuário.

---

## Persistência

Nesta versão da plataforma, a persistência das informações é realizada utilizando arquivos JSON.

O backend é responsável por:

- abrir os arquivos;
- validar sua existência;
- interpretar seu conteúdo;
- disponibilizar os dados às páginas da aplicação.

Essa solução foi adotada por apresentar simplicidade durante as primeiras fases do projeto.

A arquitetura permanece preparada para futura substituição por um banco de dados relacional ou não relacional, sem necessidade de alterações significativas nas demais camadas.

---

## Integração com o Frontend

O backend não realiza qualquer renderização visual diretamente.

Sua responsabilidade limita-se a:

1. receber a requisição;
2. processar os dados necessários;
3. enviar essas informações ao template HTML.

Toda a apresentação visual é realizada pelo frontend utilizando Tailwind CSS, Flowbite e componentes próprios da APTP.

---

## Princípios Adotados

O desenvolvimento do backend segue os seguintes princípios:

- modularização;
- responsabilidade única;
- baixo acoplamento;
- alta legibilidade;
- facilidade de manutenção;
- expansão incremental.

Esses princípios permitem que novas funcionalidades sejam adicionadas sem comprometer a organização da aplicação.

---

## Considerações

O backend constitui o núcleo operacional da APTP.

Sua função é disponibilizar as informações produzidas pelos módulos internos da plataforma e fornecer ao frontend todos os dados necessários para construção da interface, mantendo clara separação entre processamento, persistência e apresentação.
