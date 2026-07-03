# 6. Frontend

## Visão Geral

O frontend da APTP é responsável pela apresentação das informações disponibilizadas pelo backend, oferecendo uma interface moderna, responsiva e de fácil utilização.

A interface foi desenvolvida utilizando **Tailwind CSS**, complementado pela biblioteca **Flowbite**, permitindo a construção de componentes reutilizáveis e a padronização visual de toda a aplicação.

A renderização das páginas é realizada através do mecanismo de templates **Jinja2**, integrado ao Flask.

---

## Objetivos

A arquitetura do frontend foi desenvolvida para atender aos seguintes objetivos:

- interface limpa e moderna;
- alta legibilidade das informações;
- componentes reutilizáveis;
- responsividade;
- facilidade de manutenção;
- padronização visual;
- evolução incremental.

---

## Arquitetura

O frontend é composto por quatro elementos principais:

```text
Frontend
│
├── Templates (Jinja2)
├── CSS
├── JavaScript
└── Recursos estáticos
```

Cada componente possui responsabilidade específica, reduzindo o acoplamento entre estrutura, apresentação e comportamento.

---

## Templates

Os templates são escritos utilizando **HTML** com **Jinja2**.

Sua responsabilidade é estruturar as páginas da aplicação e receber os dados enviados pelo backend.

Cada página possui seu próprio template, enquanto elementos compartilhados são centralizados em componentes reutilizáveis.

Entre os principais templates encontram-se:

- Base da aplicação;
- Dashboard;
- Sistema;
- Eventos;
- Métricas;
- Configurações.

Todos utilizam uma estrutura comum definida pelo template base.

---

## Template Base

O arquivo `base.html` constitui o núcleo da interface.

Ele define os elementos compartilhados por todas as páginas, como:

- estrutura principal;
- sidebar;
- área de conteúdo;
- importação dos arquivos CSS;
- importação dos scripts JavaScript;
- blocos Jinja utilizados pelas páginas filhas.

Toda nova página da aplicação deve herdar essa estrutura.

---

## Sistema de Estilos

A APTP utiliza uma combinação de três camadas de estilização.

### Tailwind CSS

Responsável pelos estilos utilitários utilizados em toda a aplicação.

Fornece:

- espaçamentos;
- alinhamentos;
- tipografia;
- cores;
- responsividade;
- grids;
- flexbox.

---

### Flowbite

Biblioteca de componentes construída sobre o Tailwind CSS.

É utilizada para acelerar o desenvolvimento da interface, oferecendo componentes consistentes e facilmente customizáveis.

Entre eles:

- botões;
- cards;
- formulários;
- tabelas;
- badges;
- menus;
- elementos de navegação.

---

### CSS Próprio

Além das bibliotecas externas, a APTP possui arquivos CSS específicos destinados às customizações da identidade visual do projeto.

Esses arquivos concentram ajustes que não pertencem ao Tailwind ou ao Flowbite, como:

- identidade visual;
- posicionamento de componentes;
- sidebar;
- layout geral;
- elementos exclusivos da plataforma.

---

## Sidebar

A barra lateral constitui o principal mecanismo de navegação da aplicação.

Ela permanece fixa durante toda a utilização do sistema e oferece acesso aos principais módulos da plataforma.

Entre suas características destacam-se:

- logotipo da APTP no topo;
- identidade visual própria;
- navegação permanente;
- destaque visual para a página ativa;
- organização vertical dos módulos.

A sidebar foi projetada para manter consistência visual entre todas as páginas da aplicação.

---

## Layout

O layout segue uma estrutura composta por duas áreas principais.

```text
+--------------------+--------------------------------+
|                    |                                |
|                    |                                |
|      Sidebar       |        Área de Conteúdo        |
|                    |                                |
|                    |                                |
+--------------------+--------------------------------+
```

A área de conteúdo é dinâmica e varia conforme a página acessada, enquanto a sidebar permanece fixa durante toda a navegação.

---

## Componentes

A interface é composta por componentes reutilizáveis.

Entre eles:

- cards;
- tabelas;
- badges;
- formulários;
- indicadores;
- menus;
- botões;
- painéis.

A reutilização desses componentes garante consistência visual e reduz a duplicação de código.

---

## Responsividade

Embora a plataforma seja utilizada predominantemente em desktops, sua interface foi estruturada para permitir adaptação a diferentes resoluções de tela.

O uso do Tailwind CSS facilita a implementação de comportamentos responsivos sempre que necessário.

---

## Organização

O frontend segue os seguintes princípios:

- separação entre estrutura e estilo;
- reutilização de componentes;
- padronização visual;
- baixo acoplamento;
- facilidade de manutenção;
- escalabilidade.

Esses princípios permitem que novas páginas sejam incorporadas ao sistema preservando a identidade visual da plataforma.

---

## Considerações

O frontend da APTP foi concebido para fornecer uma experiência consistente, moderna e organizada, permitindo que os dados coletados pela plataforma sejam apresentados de forma clara, intuitiva e eficiente.

Sua arquitetura favorece a evolução contínua da interface, mantendo a simplicidade de manutenção e a padronização visual de todos os módulos da aplicação.
