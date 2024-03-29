<table>
<tr>
<td>
<a href= "https://www.ipt.br/"><img src="https://www.ipt.br/imagens/logo_ipt.gif" alt="IPT" border="0" width="70%"></a>
</td>
<td><a href= "https://www.inteli.edu.br/"><img src="https://camo.githubusercontent.com/2dec1e5c541f0802d0d2e49a39062ea6d9a375d8a8086ffed7e69e686b2f227e/68747470733a2f2f7777772e696e74656c692e6564752e62722f77702d636f6e74656e742f75706c6f6164732f323032312f30382f32303137323032382f6d617263615f312d322e706e67" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width="30%"></a>
</td>
</tr>
</table>

<font size="+12"><center>
Concepção de sistema de automação industrial
</center></font>

**Conteúdo**

- [Autores](#autores)
- [Visão Geral do Projeto](#visão-geral-do-projeto)
  - [Empresa](#empresa)
  - [O Problema](#o-problema)
  - [Objetivos](#objetivos)
    - [Objetivos gerais](#objetivos-gerais)
    - [Objetivos específicos](#objetivos-específicos)
    - [Escopo Macro](#escopo-macro)
  - [Partes interessadas](#partes-interessadas)
- [Análise do Problema](#análise-do-problema)
  - [Análise da área de atuação](#análise-da-área-de-atuação)
  - [Análise do cenário: Matriz SWOT](#análise-do-cenário-matriz-swot)
  - [Proposta de Valor: Value Proposition Canvas](#proposta-de-valor-value-proposition-canvas)
  - [Matriz de Risco](#matriz-de-risco)
  - [Matriz Oceano Azul](#matriz-oceano-azul)
  - [Análise Financeira](#análise-financeira)
    - [Análise de custo do processo atual](#análise-de-custo-do-processo-atual)
    - [Análise de custo da solução](#análise-de-custo-da-solução)
    - [ROI - Return Over Investment](#roi---return-over-investment)
- [Requisitos do Sistema](#requisitos-do-sistema)
  - [Personas](#personas)
  - [Jornada do Usuário](#jornada-do-usuário)
  - [Histórias dos usuários (user stories)](#histórias-dos-usuários-user-stories)
- [Arquitetura do Sistema](#arquitetura-do-sistema)
  - [Arquitetura da Solução - Versão 1](#arquitetura-da-solução---versão-1)
  - [Módulos do Sistema e Visão Geral (Big Picture)](#módulos-do-sistema-e-visão-geral-big-picture)
  - [Descrição dos Subsistemas](#descrição-dos-subsistemas)
    - [Bloco de Interface](#bloco-de-interface)
    - [Braço Robótico](#braço-robótico)
    - [Backend - Computador](#backend---computador)
    - [Embarcados](#embarcados)
  - [Relatório de entrada e saídas](#relatório-de-entrada-e-saídas)
  - [Testes de Componentes - Versão 1](#testes-de-componentes---versão-1)
    - [Braço robótico (Dobot Magician)](#braço-robótico-dobot-magician)
    - [Eletroimã (na Ponte H)](#eletroimã-na-ponte-h)
    - [Shaker (na Ponte H)](#shaker-na-ponte-h)
    - [Requisitos de software](#requisitos-de-software)
  - [Tecnologias Utilizadas](#tecnologias-utilizadas)
    - [Bloco de Interface](#bloco-de-interface-1)
    - [Braço Robótico](#braço-robótico-1)
    - [Backend - Computador](#backend---computador-1)
    - [Embarcados](#embarcados-1)
- [UX e UI Design](#ux-e-ui-design)
  - [Wireframe + Storyboard](#wireframe--storyboard)
  - [Design de Interface - Guia de Estilos](#design-de-interface---guia-de-estilos)
- [Projeto de Banco de Dados](#projeto-de-banco-de-dados)
  - [Modelo Conceitual](#modelo-conceitual)
  - [Modelo Lógico](#modelo-lógico)
- [Teste de Software](#teste-de-software)
    - [Implementação de Servidor](#implementação-de-servidor)
    - [Servidor com Acionamento de Hardware](#servidor-com-acionamento-de-hardware)
- [Prototipação de Hardware](#prototipação-de-hardware)
  - [Projeto dos dispositivos mecânicos](#projeto-dos-dispositivos-mecânicos)
  - [Projeto dos dispositivos eletrônicos](#projeto-dos-dispositivos-eletrônicos)
    - [Listagem de Placa:](#listagem-de-placa)
    - [Esquemático da Placa:](#esquemático-da-placa)
    - [Layout da Placa:](#layout-da-placa)
    - [Lista de Materiais:](#lista-de-materiais)
    - [Método de fabricação:](#método-de-fabricação)
  - [Fabricação dos Dispositivos Eletrônicos](#fabricação-dos-dispositivos-eletrônicos)
  - [Validação dos Dipositivos Eletrônicos](#validação-dos-dipositivos-eletrônicos)
    - [Métodos de Validação e Testes](#métodos-de-validação-e-testes)
- [Análise de Dados](#análise-de-dados)
- [Manuais](#manuais)
  - [Manual de Implantação](#manual-de-implantação)
  - [Manual do Usuário](#manual-do-usuário)
  - [Manual do Administrador](#manual-do-administrador)
- [Referências](#referências)


# Autores

* Bruno Leão
* Filipi Kikuchi
* Gabriela Rodrigues
* Henrique Santos
* Jackson Aguiar
* Luana Parra
* Vitor Zeferino


# Visão Geral do Projeto

## Empresa

O Instituto de Pesquisas Tecnológicas (IPT), vinculado à Secretaria de Desenvolvimento Econômico do Estado de São Paulo,  há 123 anos colabora para o processo de desenvolvimento do País, provê soluções tecnológicas para a indústria, governos e sociedade, habilitando-os a superar os desafios da nossa época. 

Desse modo, como um dos maiores institutos de pesquisas do Brasil, o IPT conta com laboratórios capacitados e equipe de pesquisadores e técnicos altamente qualificados, atuando basicamente em quatro grandes áreas - inovação, pesquisa e desenvolvimento; serviços tecnológicos; desenvolvimento & apoio metrológico, e informação & educação em tecnologia.

## O Problema

Considerando que a separação magnética pode ser uma excelente técnica para avaliação da liberação de minerais/materiais com propriedades magnéticas e que, em uma etapa preliminar exploratória, não estão disponíveis grandes quantidades de amostras para serem submetidas a ensaios em equipamentos de separação magnética com operação contínua, a automação deste procedimento é benéfica do ponto de vista de agilidade e precisão.

Posto isso, o processo atual é manual, ou seja, o operador aproxima um ímã de ferrite ou de terras raras, envolto em um saco plástico, do material submerso em água, espalhado em uma bandeja plástica, tentando manter uma distância constante e, consequentemente, o campo eletromagnético aplicado sobre as partículas. O material ferromagnético gruda no ímã e é posteriormente depositado em outro recipiente.

Assim, por ser um processo manual, a constância da distância é imprecisa e, considerando que o campo eletromagnético é inversamente proporcional à distância, o campo aplicado sobre as partículas também é impreciso, dificultando a determinação do campo necessário para a separação dos minerais. Além disso, para testar diferentes campos é necessário a troca dos ímãs utilizados, resultando na necessidade de se ter diversos ímãs disponíveis.

## Objetivos

### Objetivos gerais

Desenvolver um equipamento automatizado que tenha capacidade de aplicar um campo magnético constante, com intensidade e distância ajustáveis, ao longo de todo a amostra promovendo assim uma separação dos minerais magnéticos, que serão depositados em um recipiente diferente dos minerais não magnéticos que permanecerão depositados na bandeja original.

### Objetivos específicos

A seguir estão os objetivos/benefícios esperados com o desenvolvimento do projeto:

* Manutenção de uma campo magnético constante sobre toda a amostra, reduzindo os erros de ensaio decorrentes da ação humana;
* Maior qualidade na execução do ensaio, principalmente no que tange a repetibilidade e reprodutibilidade;  
* Maior flexibilidade de ensaios, pois o uso de eletroímãs ajustáveis dispensa a necessidade de se ter ímãs com o campo desejado; 
* Determinação mais precisa do campo magnético adequado para diferentes ensaios. 

### Escopo Macro

* Um braço robótico capaz de posicionar um manipulador em posição e distância controladas sobre a bandeja de amostras;
* Eletroímã montado no manipulador do braço robótico com campo magnético ajustável na faixa de 800 a 12.000 Gauss; 
* Estrutura para calibração de posicionamento do braço; 
* Estrutura para calibração de eletroímã; 
* Automação da bandeja de amostra para promover a agitação das partículas; 
* Recipiente com automatização de pesagem para receber material coletado (opcional); 
* Relatório apresentando todos os dados pertinentes do ensaio (opcional). 

## Partes interessadas

* IPT - Instituto de Pesquisas Tecnológicas
* INTELI - Instituto de Tecnologia e Liderança

# Análise do Problema

## Análise da área de atuação

O IPT é formado por diversos departamentos, dentre os quais destaca-se o Departamento de Materiais Avançados, que se dedica a desenvolver materiais capazes de atender às demandas do mercado atual em relação a desempenho, ciclo de vida e impacto socioambiental. O projeto em questão está relacionado a este departamento, mais especificamente ao Laboratório de Processos Metalúrgicos, responsável pelo tratamento de minérios. Nesse laboratório, é utilizada a técnica de separação magnética, a qual permite dissociar elementos que apresentam propriedades ferromagnéticas nas amostras.

A seguir, apresentam-se as etapas do processo de separação magnética realizado no laboratório:

1. Dissolve-se a amostra, contendo os minerais, em uma bandeja com água. Em seguida, um ímã, envolvido em plástico, é colocado próximo à amostra, de modo a projetar seu campo magnético e aderir o material magnético.
2. O ímã é então imerso em uma segunda bandeja contendo apenas água, com o intuito de desprender qualquer material não magnético por arraste.
3. As partículas magnéticas são descarregadas em uma terceira bandeja, obtendo-se, dessa forma, o produto final contendo apenas os materiais de interesse.

## Ideação da proposta da solução 

Para as etapas de ideação na proposta de solução, foram realizadas as seguintes atividades:

Entrevista: Utilizamos esta ferramenta para compreender diretamente as necessidades e problemas dos stakeholders. Inicialmente, apresentamos a empresa e, em seguida, conduzimos uma sessão interativa de perguntas e respostas.

Experimentação: Após a sessão de Q&A, realizamos uma visita monitorada, acompanhada por técnicos e pesquisadores, para conhecer o ambiente de trabalho e os processos de separação magnética. Essa experiência nos permitiu entender melhor as dificuldades enfrentadas pelos profissionais e identificar oportunidades de melhoria.

## Proposta de Valor: Value Proposition Canvas

O Value Proposition Canvas (ou Quadro de Proposta de Valor) é uma ferramenta visual que ajuda as empresas a entenderem as necessidades e desejos de seus clientes e a desenvolverem produtos e serviços que os atendam de forma única e valiosa. 

Sendo assim, ele é dividido em duas partes: a Proposta de Valor do Cliente (trabalhos, dores e ganhos dos clientes) e a Proposta de Valor da Empresa (soluções, benefícios e diferenciais da empresa).

![img](https://github.com/2023M5T2-Inteli/alquimistas/blob/main/docs/img/sprint1/proposta-de-valor.png)

#### Proposta de Valor do Cliente

1. Ganhos: Padronização de análises; Agilidade e precisão na produção de relatórios.
2. Tarefas do Cliente: Reazlizar o processo manual de captação de minérios por meio da utilização de um imã.
3. Dores: Excesso de trabalho braçal; Necessidade de variações de imãs; Falta de precisão nas informações.

#### Proposta de Valor da Empresa 

1. Criadores de ganho: Confiabilidade no resultado das amostras; O colaborador poderá exercer outras funções enquanto o robô faz o serviço.
2. Produtos e serviços: Automatização por meio de um braço robótico para automatizar o serviço realizado pelo colaborador ao IPT na separação.
3. Aliviam as dores: Utilização de um único eletroimã que varia seu magnetismo; Processo automatizado e adaptável; Substitui a necessidade de um colaborador realizando o processo.

## Matriz de Risco

A matriz de risco é uma ferramenta de gerenciamento que permite identificar, avaliar e priorizar os riscos associados ao projeto, sendo uma representação visual dos riscos que podem afetar o sucesso do projeto, organizados em uma tabela que combina a probabilidade de ocorrência de um evento com o impacto que teria no resultado final. 

![img](https://github.com/2023M5T2-Inteli/alquimistas/blob/main/docs/img/sprint1/matriz-de-risco.png)

## Matriz Oceano Azul

A matriz Oceano Azul é uma ferramenta estratégica que ajuda a identificar novas oportunidades de mercado e a criar um espaço de mercado inexplorado, conhecido como "Oceano Azul".

![img](https://github.com/2023M5T2-Inteli/alquimistas/blob/main/docs/img/sprint1/matriz-oceano-azul.png)

 A matriz é composta por quatro quadrantes que avaliam as características do mercado atual e das novas ideias de negócios, levando em consideração fatores como preço, qualidade, conveniência e experiência do cliente. Desse modo, a ideia é que, ao encontrar um Oceano Azul, a empresa possa explorar novas demandas e criar novos mercados, em vez de lutar pelo mesmo espaço limitado de mercado com a concorrência existente.

#### Eliminar
Valores de medições imprecisos; Valores com erros causados pelo uso manual do processo; Intervenção humana.
#### Elevar
Maior confiabilidade dos valores gerados; Agilidade e precisão.
#### Reduzir
Mão de obra manual; Diminuição de gastos operacionais.
#### Criar
Automatização robotizada de um processo manual.

Além disso, o gráfico mostra pontos de comparação entre a solução proposta e o método atual manual. 

## Análise Financeira

### Análise de custo do processo atual

Inicialmente, os custos relacionados ao processo atual provêm da compra dos equipamentos (ímãs de neodímio) e da remuneração da mão de obra. Em um primeiro momento, projetamos que o salário médio de um técnico é de R$ 2.833/mês. Considerando uma carga horária de 8 horas por dia, podemos chegar à estimativa de R$11,80/hora. Através de entrevistas com o parceiro, constatou-se que cada sessão de separação magnética dura cerca de 30 minutos. Consequentemente, o custo do processo é de R$5,90 por sessão. Além disso, deve ser adicionado o custo médio dos ímãs projetados em R$663,00 cada, que devido à sua natureza, não precisam ser substituídos a curto prazo.

### Análise de custo da solução

A solução proposta inclui o uso de um braço robótico Dobot Magician Lite, microcontroladores Raspberry Pi Pico W, além de sensores e atuadores como componentes físicos. Esses componentes foram cuidadosamente selecionados para garantir eficiência e qualidade na operação do sistema, e uma análise de custo se faz necessária para avaliar a viabilidade financeira da implementação da solução.

A análise de custo é essencial para determinar se a solução é economicamente viável e para identificar possíveis pontos de otimização de recursos. Além disso, a análise permite avaliar o retorno sobre o investimento (ROI) e o tempo necessário para que a solução se pague.

![img](https://github.com/2023M5T2-Inteli/alquimistas/blob/main/docs/img/sprint1/analise_financeira.png)

Com base nos custos dos componentes físicos, incluindo o braço robótico, os microcontroladores, sensores e atuadores, bem como os custos de mão de obra, transporte e montagem, a análise de custo fornecerá uma estimativa precisa do investimento necessário para implementar a solução proposta. A partir dessa estimativa, é possível avaliar a viabilidade financeira do projeto e tomar decisões informadas sobre sua implementação.

#### ROI - Return Over Investment
Ao analisar os gastos atuais e os custos relacionados aos equipamentos adquiridos, é possível estimar o tempo necessário para recuperar o valor do investimento. Essa análise visa avaliar o Retorno sobre o Investimento (ROI), ou seja, quanto lucro será gerado em relação ao montante investido. É importante destacar que essa análise não se resume apenas aos custos iniciais, mas leva em consideração os custos contínuos, como manutenção e reposição de peças, por exemplo. Com base nessas informações, é possível tomar decisões estratégicas em relação ao investimento em questão.

![img](https://github.com/2023M5T2-Inteli/alquimistas/blob/main/docs/img/sprint1/roi.png)

# Requisitos do Sistema

## Personas

![img](https://github.com/2023M5T2-Inteli/alquimistas/blob/main/docs/img/sprint1/persona.png)
João Silva, 35 anos

Formação: Engenheiro Químico

Empresa: Instituto de Pesquisa e Tecnologia (IPT) - Setor: Materiais Avançados - Salário: R$3000,00 por mês

Projeto de trabalho: Separação Magnética em Projetos de Mineração

Interesses/Hobbies: Tecnologia, robótica, automação industrial, jogar futebol, viajar e ler sobre novas descobertas científicas

Personalidade: Dinâmico, curioso e apaixonado por soluções tecnológicas inovadoras.

## Jornada do Usuário

A jornada do usuário é um processo que mapeia as interações entre os usuários e um produto ou serviço. Esta jornada é um guia que oferece uma visão geral de todas as etapas pelas quais a persona passa, desde a descoberta do produto ou serviço até o uso e a conclusão da sua interação. 

![img](https://github.com/2023M5T2-Inteli/alquimistas/blob/main/docs/img/sprint1/jornada-do-usuario.png)

## Histórias dos usuários (user stories)

1. Como pesquisador, eu quero ter a capacidade de acionar o robô para que ele possa começar a limpar a amostra de forma automática, a fim de aumentar a eficiência e a precisão do processo de limpeza.
2. Como supervisor, eu quero automatizar o processo para melhorar a precisão do relatório, permitindo que o sistema execute as tarefas repetitivas e de rotina de forma autônoma, evitando erros humanos e aumentando a eficiência.
3. Como supervisor, eu quero automatizar o processo para melhorar a gestão do tempo da equipe, permitindo que eles possam se concentrar em tarefas mais importantes, reduzindo o tempo gasto em tarefas rotineiras e repetitivas, além de minimizar a possibilidade de erros humanos e melhorar a qualidade do trabalho.

# Arquitetura do Sistema

## Arquitetura da Solução - Versão 1

![img](https://github.com/2023M5T2-Inteli/alquimistas/blob/main/docs/img/sprint1/arquitetura-da-solucao-v1.png)

## Arquitetura da Solução - Versão 2
![img](https://github.com/2023M5T2-Inteli/alquimistas/blob/dev/docs/img/sprint4/arquitetura-da-solucao-v2.png)

## Arquitetura da Solução - Versão final
![img](https://github.com/2023M5T2-Inteli/alquimistas/blob/dev/docs/img/sprint4/arquitetura-da-solucao-v2.png)

## Descrição dos Subsistemas

### Bloco de Interface 
O Bloco de Interface é um sistema visual que permite ao usuário controlar os componentes do projeto. O principal processo é o ciclo de coleta de materiais por meio de campos magnéticos, mas também é possível interagir individualmente com os demais componentes do sistema.

### Braço Robótico
O componente do braço robótico é o Dobot Magician Lite, que é o principal responsável por executar a trajetória do processo descrito no item “Bloco de Interface”. 

O Magician Lite é um braço robótico inteligente, leve e multifuncional que se tornou um excelente produto para educação e aprendizado em inteligência artificial.

### Backend - Computador
Sistema integrado que abarca o código do servidor de interface, assim como os controles do Microcontrolador Raspberry Pi Pico. 

### Embarcados 
1. Raspberry Pi Pico: A Raspberry Pi Pico é uma placa microcontrolada de baixo custo e alta performance, com interfaces digitais flexíveis. 
2. Ponte H: A ponte H é um circuito que serve para variar o sentido da corrente em uma determinada carga, bem como controlar sua potência.
  <br>2.1. Elétroimã: O eletroímã é um dispositivo formado por um núcleo de ferro envolto por um solenoide (bobina) que, mediante uma indução de corrente, gera campo magnético.
  <br>2.2. Shaker: O Micro Motor Vibracall é um tipo de motor de tamanho bem reduzido, responsável por produzir vibrações.

#### Soft AP
A Raspberry Pi Pico é uma placa microcontroladora de baixo custo que oferece diversas possibilidades de projetos e configurações, dessa maneira optamos por usar a Raspberry Pi Pico como Soft AP (ponto de acesso), permitindo que ela seja usada para gerar uma rede Wi-Fi para outros dispositivos. Nesse caso específico, usamos uma Raspberry Pi Pico como Soft AP para gerar rede para outro Raspberry Pi Pico, ou seja, usamos uma placa para criar uma rede sem fio que permite que o outro dispositivo possa se conectar e trocar informações com ela.

Para configurar a Raspberry Pi Pico como Soft AP, é necessário utilizar o modo de operação de rede chamado de "Access Point" ou "Ponto de Acesso", tal modo permite que a placa seja configurada como um roteador Wi-Fi que cria sua própria rede e permite que outros dispositivos se conectem a ela. Uma vez que a Raspberry Pi Pico esteja configurada como Soft AP, o outro Raspberry Pi Pico poderá se conectar à rede criada pela primeira placa. Dessa forma, é possível criar uma rede local (LAN) entre as duas placas e permitir a troca de informações entre elas.

Em resumo, usar uma Raspberry Pi Pico como Soft AP permite que ela seja usada para gerar uma rede sem fio e permitir que outros dispositivos se conectem a ela. No caso do projeto, utilizamos uma placa para gerar rede para outra placa, criando uma LAN entre as duas.

#### MQTT
Mais conhecido como Message Queuing Telemetry Transport, MQTT é um protocolo de comunicação leve e de baixo consumo de energia projetado para conectar dispositivos com capacidades de processamento limitadas em redes de comunicação de baixa largura de banda. Ele foi desenvolvido pela IBM em 1999 e, desde então, tornou-se um protocolo padrão em muitas soluções de IoT (Internet das Coisas).

Utilizamos tal protocolo com o objetivo de aprimorar e dar estabilidade à comunicação com o eletroimã. Nesse sentido, o microcontrolador ( Raspberry Pi Pico W ) atua como subscriber de um tópico, vide arquitetura padrão do protocolo, no qual o backend da solução é publisher. Dessa forma, criamos a lógica de que, quando o microcontrolador receber "0" no tópico, ele mantém os eletroimãs desligados, mas quando recebe "1" aciona os eletroimãs.

Nesse mesmo fluxo, dadas as limitações de rede, pensando na implemetação do sistema, criamos um broker, vide arquitetura padrão do protocolo, que roda na rede local fornecida pelo SoftAP/Hostpot e que faz o intermédio entre as entidades "publisher" (Backend) e "subscriber" (microcontrolador) do sistema.

## Relatório de entrada e saídas
Com base na estrutura de Arquitetura desenvolvida para a solução proposta, avaliamos os inputs e outputs esperados para cada sistema de blocos e cada componente do sistema. 
|Indice|Bloco              |Componente de Entrada|Leitura da Entrada              |Componente de Saída |Leitura da Saída                    |Descrição                                                                                                                       |
|------|-------------------|---------------------|--------------------------------|--------------------|------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
|1	   |Robô               |Computador 	         |Sinal de Inicio                 |Dobot Magician Lite |Movimentação                        |Ao acionarmos via computador, o robô irá se movimentar de acordo com as coordenadas corretas.                                   |
|2	   |Robô               |Computador 	         |Sinal de Encerramento	          |Dobot Magician Lite |Pausa no Movimento	                |Ao encerrarmos o movimento via computador, o robô irá parar de se movimentar.                                                   |
|3	   |Backend 	       |Computador 	         |Acionamento da Raspberry Pi Pico|Raspberry Pi Pico   |Inicia o Código no Microcontrolador	|Ao iniciar o código o raspberry pi pico se torna responsável pela atuação de alguns componentes no sistema.                     |
|4	   |Sistemas Embarcados|Raspberry Pi Pico	 |Sinal de Inicio - Acionamento   |Ponte H	           |Alimentação do Shaker e do Eletroimã|Ao iniciar o código o raspberry pi pico ele alimenta a ponte H e essa por sua vez alimenta os componentes do Shaker e Eletroimã |
|5	   |Sistemas Embarcados|Ponte H	             |Sinal de Inicio - Acionamento   |Shaker 	           |Vibração do Shaker 	                |Ao iniciar a alimentação do shaker haverá um botão de acionamento na interface que irá permitir o acionamento do Shaker.        |
|6	   |Sistemas Embarcados|Ponte H	             |Sinal de Inicio - Acionamento   |Eletroimã	       |Criação de Campo Magnético	        |Ao iniciar a alimentação do eletroimã haverá um botão de acionamento na interface que irá permitir o acionamento do mesmo.      |
|7	   |Interface	       |Computador 	         |Acionamento do Shaker           |Shaker 	           |Vibração do Shaker 	                |Ao acionar o shaker via interface, ele inicia sua atuação.                                                                      |
|8	   |Interface	       |Computador 	         |Acionamento do Eletroimã	      |Eletroimã	       |Criação de Campo Magnético	        |Ao acionar o eletroimã via interface, ele inicia sua atuação.                                                                   |

## Tecnologias Utilizadas

### Bloco de Interface 
- HTML 
- CSS 
- JavaScript 
- Bootstrap
- Python (DType)

### Braço Robótico
- Dobot Magician Lite 
- Software - Dobot 
- Python (DType)

### Backend - Computador
- IDE: Thonny 
- Python 
- MicroPython 

### Embarcados 
- IDE: Thonny 
- Python 
- MicroPython 

# UX e UI Design

## Wireframe + Storyboard

Para o desenvolvimento da interface do usuário, optamos por criar uma aplicação web, com uma estrutura elaborada de acordo com as necessidades de entradas e saídas relacionadas ao bloco de Interface na Arquitetura da Solução.

Dessa forma, a primeira versão da nossa interface consiste em uma página principal com um modal que permite ao usuário acionar os componentes do sistema, como o Wifi, o Shaker e o Eletroimã.

![img](https://github.com/2023M5T2-Inteli/alquimistas/blob/main/docs/img/sprint2/interface.png)

[Wireframe no Figma](https://www.figma.com/file/SURaYJTPLilelYLFrS4gdi/Front-IPT?node-id=0%3A1&t=6frlueaWTHFUkmnN-0)


## Design de Interface - Guia de Estilos

Para garantir a qualidade da nossa interface gráfica, desenvolvemos um guia de estilo que busca proporcionar uma experiência visual coesa e intuitiva para o usuário. 

O objetivo principal da nossa interface é permitir o acionamento do ciclo/rotina do robô, além de poder inserir os dados do relatório e conseguir posteriormente gerar um pdf. Abaixo, apresentamos algumas diretrizes que seguimos durante o desenvolvimento da interface gráfica no Figma:

1. Cores: utilizamos uma paleta de cores sóbrias e contrastantes para destacar os botões. Optamos por tons de cinza e preto para o fundo da interface e adicionamos um toque de cor nas bordas dos botões, o que torna a experiência visual mais agradável e fácil de entender.
2. Tipografia: escolhemos uma fonte legível e limpa para a interface. Utilizamos fontes serifadas para os títulos e fontes sans-serif para os textos, garantindo uma hierarquia visual clara e facilitando a leitura.
3. Layout: desenvolvemos uma estrutura simples e organizada para a nossa interface. 
4. Ícones/Formas: utilizamos ícones/formas simples e intuitivos para representar cada um dos componentes do sistema, tornando a interface mais fácil de entender e acessível.

Ao seguir essas diretrizes, conseguimos desenvolver uma interface gráfica coesa e intuitiva, que cumpre seu objetivo de permitir o acionamento do sistema de forma clara e eficiente.

## Detalhamento da interface de usuário

Ao projetar a interface de controle do processo de limpeza de amostras com o Dobot, foi adotado um design minimalista, visando proporcionar um controle visual eficiente e simplificado. A seguir, apresentaremos as principais características da interface e suas funcionalidades, com o objetivo de ajudar os usuários a atingirem seus objetivos em poucas ações.

1. Tela Home: A 'home' trata-se de uma página explicando sobre o objetivo do projeto e com um botão para inserir o relatório.
2. Tela de Inserir Relatório: Na parte inferior da tela anterior, há a opção de adicionar um relatório. Ao clicar nesta opção, o usuário é redirecionado para um formulário onde serão solicitadas informações importantes, tais como o projeto, a massa e a amostra, para compor os dados referentes ao relatório do processo.
3. Tela de Acionamento de ciclo: A página possui um botão circular para iniciar o processo de limpeza com apenas um clique. Caso necessário, o processo pode ser interrompido instantaneamente pelo mesmo botão, que terá seu estado alterado para exibir o texto "Parar", ademais existe um botão para regular a corrente dos eletroimãs. Por fim, adicionamos um botão para gerar um pdf com informações inseridas no relatório e sobre a rotina/ciclo.

# Projeto de Banco de Dados

O Modelo de Banco de Dados foi criado para registrar relatórios de informações sobre cada análise de amostra realizada. O objetivo desse modelo de banco de dados é armazenar e organizar informações relevantes sobre cada análise, como o nome do projeto, o cliente, a amostra, o operador, a quantidade de ciclos, a massa inicial líquida e a massa inicial sólida.

Esses parâmetros são utilizados para caracterizar cada relatório e fornecer informações importantes sobre a análise de amostra realizada. O nome do projeto pode ser usado para categorizar as análises de acordo com a finalidade do projeto, enquanto o cliente pode ser usado para identificar quem solicitou a análise. A amostra, por sua vez, é a matéria-prima analisada, enquanto o operador é a pessoa responsável pela realização da análise. A quantidade de ciclos, a massa inicial líquida e a massa inicial sólida são parâmetros que descrevem a natureza da análise.

Para integrar o banco de dados ao sistema, foi utilizada a SQLAlchemy como ORM (Object-Relational Mapping). A SQLAlchemy é uma biblioteca de mapeamento objeto-relacional para Python que permite a comunicação entre o código Python e o banco de dados relacional. Através da SQLAlchemy, foi possível criar uma classe em Python que define a estrutura padrão dos registros do banco de dados.

A classe em Python pode ser usada para criar objetos que representam os registros do banco de dados, seguindo a estrutura definida pelos parâmetros fornecidos. Dessa forma, é possível armazenar e recuperar informações de forma organizada e eficiente. A integração do banco de dados ao sistema através da SQLAlchemy também permite que as informações sejam facilmente acessadas e atualizadas conforme necessário.

## Modelo Lógico
De acordo com a descrição ja inicialmente indicada para a construção do modelo lógico do banco de dados, nossa estrutura atual se baseia em uma unica entidade chamada de "report".

Constituida pela seguinte estrutura: 
- id: Integer 
- project: String
- client: String
- sample: String
- operator: String
- cycles: Integer
- liquid_initial_mass: Float 
- solid_initial_mass: Float 

A seguir temos a representação lógica do projeto de acordo com a estrutura de dados listada acima: 

![img](https://github.com/2023M5T2-Inteli/alquimistas/blob/dev/docs/img/sprint4/logic_model.png)

## Teste de Componentes - Versão 1

### Braço robótico (Dobot Magician)
O braço mecânico foi testado nas seguintes etapas.

1. Inicialmente, foi realizada a conexão do braço via USB. Posto isso, foi possível explorar as movimentações e funcionalidades do robô (além dos 'acessórios' do robô, como a garra, caneta, sucção) a partir do software Dobot Studio.
2. Com o conhecimento dos limites da movimentação do braço e seu alcance em relação as três bandejasjá posicionadas para a realização da separação magnética, foi instalada a biblioteca pronta, PyDobot, que realiza a comunicação com o robô e códigos em Python, onde testamos os movimentos do Dobot. Posteriormente, criamos uma classe para o desenvolvimento do script da movimentação do robô.
3. Após um feedback do cliente, criamos um movimento da garra em uma das bandejas, que poderá funcionar como um "shaker".

[Vídeo do Braço Robótico](https://www.youtube.com/embed/9Ak5891op9U)

[Vídeo do Braço Robótico funcionando com o Eletroimã](https://youtube.com/shorts/RmgzJqTKww4)


### Eletroimã (na Ponte H)

A partir da arquitetura da solução, estudamos o método de PWM para o funcionamento do eletroimã. Contudo, após discussões no grupo foi utilizada a ponte H que aciona o imã com um botão liga e desliga básico. Posteriormente, será possível conectar esse script ao servidor, e consequentemente ao frontend. 

Assim, abaixo é possível observar o teste do eletroimã sendo acionado: 

[Vídeo do Eletroimã](https://youtube.com/shorts/ryoXvXvyKvg?feature=share)

### Shaker (na Ponte H)

Assim como o eletroimã, e a partir da arquitetura da solução, para o funcionamento do shaker (atuador) foi testado na ponte H, por ser um método mais simples. 

Posto isso, é possível observar o teste do shaker sendo acionado: 

[Vídeo de Controle de Movimentação](https://youtube.com/shorts/p4DXiTl25Kk?feature=share)

## Teste de Componentes - Versão 2
Para a segunda versão do teste de componentes do hardware focamos no acionamento simultâneo dos seguintes componentes: 

- Melhoria de Rota - Movimentação 
- Acionamento do Imã 

### Controle de Movimentação 

[Vídeo do Shaker](https://www.youtube.com/shorts/R82z4bbFPFQ)

### Requisitos de software

# Teste de Software

### Implementação de Servidor 
Para estruturar a renderização das páginas construídas para o software, desenvolvemos um servidor utilizando a biblioteca Flask para Python. O Flask é um framework web leve e flexível para a construção de aplicativos web de maneira fácil e eficiente, permitindo a criação de rotas de acesso às páginas do aplicativo e o gerenciamento das solicitações e respostas HTTP.

Desse modo, as páginas do software são acionadas por meio das rotas desenvolvidas no servidor. Inicialmente, o servidor foi composto pelas páginas de acionamento, parada e envio de relatório, cada uma dessas páginas é responsável por uma funcionalidade específica, como ativar dispositivos eletrônicos, parar o sistema e enviar relatórios de funcionamento.

O funcionamento do servidor está ocorrendo de forma local, de modo que é necessário realizar o seguinte processo para acessar a interface do software:

1) Acessar a pasta `src/backend`, onde está localizado o código do servidor Flask.
2) Executar o comando `python app.py`. Esse comando iniciará o servidor Flask e disponibilizará as rotas de acesso às páginas do software.
3) Acessar o IP fornecido pelo servidor para acessar localmente.

### Servidor com Acionamento de Hardware 
Para estabelecer a conexão entre as APIs que acionam o servidor em Flask e o microcontrolador Raspberry Pi Pico W, responsável por controlar a Ponte H e acionar o Eletroímã, é necessário um processo de transmissão de um código específico que conecte o Raspberry a um provedor de rede. Isso é fundamental para garantir que tanto o servidor quanto o microcontrolador estejam vinculados à mesma rede, viabilizando a comunicação entre eles.

O Módulo Sensor Magnético - Efeito Hall desempenha um papel importante nesse processo, pois é responsável por captar as informações de campo magnético geradas pelo Eletroímã e enviá-las para o Raspberry, que as utiliza para controlar a Ponte H.

Dessa forma, com a conexão estabelecida e o Módulo Sensor devidamente configurado, o servidor pode iniciar o funcionamento do Eletroímã por meio de um endpoint específico que aponta diretamente para o endpoint do microcontrolador responsável pela Ponte H. Quando acionado, o microcontrolador ativa o funcionamento da Ponte H, permitindo que o Eletroímã seja controlado e operado de acordo com as instruções recebidas do servidor.

# Prototipação de Hardware

## Projeto dos dispositivos mecânicos

O projeto mecânico envolve a criação de peças customizadas, fabricadas com o auxílio do software Onshape. O Onshape é um sistema de design auxiliado por computador disponibilizado na internet por meio de um modelo de software como serviço, permitindo o acesso remoto às ferramentas de design e colaboração em tempo real. Além disso, a impressora 3D é utilizada para a fabricação das peças projetadas, proporcionando precisão e rapidez na produção.

### Suporte de Placa:
Desenvolvimento de um suporte para PCB (placa com o circuito eletrônico), produzido pela impressora 3D e posicionado atrás do braço robótico. Assim, o suporte otimiza a experiência do usuário e organiza a arquitetura do projeto.

O desenvolvimento de um suporte para PCB é essencial para a organização e otimização da arquitetura do projeto robótico. A PCB, ou placa com o circuito eletrônico, é um componente crucial para o funcionamento do robô e o suporte, produzido pela impressora 3D, proporciona uma solução eficiente e personalizada para a sua fixação. O suporte é posicionado atrás do braço robótico, aprimorando a experiência do usuário e facilitando a manutenção do dispositivo.

Com a utilização da impressora 3D, o suporte pode ser fabricado com precisão e agilidade, permitindo a personalização de acordo com as necessidades do projeto. Além disso, o uso de materiais resistentes garante a durabilidade e segurança da estrutura, evitando danos à PCB e minimizando a necessidade de manutenção.

Adicionalmente, as conexões por fio serão fixadas no corpo do robô com fita adesiva/isolante, proporcionando uma organização mais eficiente do sistema. Essa solução, combinada com o suporte para PCB, permite um controle mais preciso e confiável do robô, aumentando sua eficiência e desempenho.

![img](https://github.com/2023M5T2-Inteli/alquimistas/blob/dev/docs/img/sprint4/caixa.png)

PS: Esse suporte não foi fabricado, por motivos de tempo de impressão.

### Suporte dos eletroimãs:

Os eletroimãs são componentes cruciais para o funcionamento do Dobot, um robô manipulador multifuncional. Até a Sprint 4, os eletroimãs eram fixados com fita adesiva na própria garra do robô. No entanto, foi identificada a necessidade de criar um suporte personalizado para os imãs, que ainda seria segurado pela garra.

Para atender a essa demanda, foi desenvolvido um suporte com design inspirado no rastelo, onde os imãs estarão em uma 'caixa'. Esse suporte proporciona maior estabilidade e segurança para os eletroimãs, além de simplificar a manutenção do sistema.

A imagem abaixo representa o protótipo do suporte, que será fixado na garra do Dobot. Com a utilização desse suporte personalizado, é possível garantir a eficiência e confiabilidade do sistema, permitindo um controle mais preciso e seguro dos eletroimãs.

![img](https://github.com/2023M5T2-Inteli/alquimistas/blob/dev/docs/img/sprint4/rastelo.png)

### Lista de materiais:

1. Impressora 3D
2. Filamentos PLA

### Método de fabricação:

1. Inicialmente foi desenvolvido o desenho 3D das peças por meio do software Onshape.
2. Em seguida foi realizado o 'fatiamento' dos desenhos, para realizar a impressão 3D.

## Validação dos Dipositivos Mecânicos

### Métodos de Validação e Testes 
A validação do dispositivo mecânico (no caso do projeto somente o suporte de eletroimãs) foi realizada por meio da implementação no projeto.

## Projeto dos dispositivos eletrônicos

### Listagem de Placa: 

A Placa Central foi desenvolvida com a proposta de criar uma placa única para o acionamento dos dispositivos eletrônicos do sistema em questão. Essa placa engloba os principais sistemas que serão acionados, como a Ponte H, o Eletroímã, o Módulo Sensor Magnético Efeito Hall e o Raspberry Pi Pico.

A escolha por uma única placa de acionamento se justifica pela necessidade de uma integração eficiente dos sistemas, visando maximizar a eficiência e a segurança do sistema como um todo. A placa central permite que os diversos sistemas sejam conectados e acionados de maneira mais organizada e simplificada, minimizando a ocorrência de erros e falhas de comunicação.

A placa central também conta com a presença do Raspberry Pi Pico, responsável pela conexão com o servidor em Flask descrito no item "Teste de Software". Este dispositivo é capaz de realizar diversas funções, como o processamento de dados, a execução de códigos e a comunicação com outros dispositivos, tornando-se peça fundamental do sistema como um todo.

A listagem de placa apresentada no projeto é essencial para garantir a integridade e organização do sistema. Com a placa central, é possível realizar uma conexão mais eficiente entre os dispositivos eletrônicos, otimizando o desempenho e minimizando a ocorrência de falhas.

Em resumo, o desenvolvimento da placa central representa um importante aprimoramento do projeto, permitindo a integração eficiente dos sistemas eletrônicos e maximizando a eficiência e segurança do sistema como um todo. A presença do Raspberry Pi Pico também permite uma conexão eficiente com o servidor em Flask e a execução de diversas funções essenciais para o funcionamento do sistema.

### Esquemático da Placa:

A seguir, apresentamos o diagrama esquemático da estrutura eletrônica da placa em questão. Este diagrama foi elaborado com base nas informações e descrições previamente mencionadas referentes à placa principal.

O processo de desenvolvimento do esquemático envolveu uma análise minuciosa das especificações técnicas da placa e das funcionalidades desejadas. Foram considerados aspectos como a configuração dos componentes eletrônicos, a disposição física dos mesmos na placa, bem como as conexões elétricas necessárias entre eles.

O resultado desse processo foi o esquemático completo da estrutura eletrônica da placa, que serve como guia para o desenvolvimento do layout da placa propriamente dita. A partir desse esquemático, é possível obter informações precisas sobre os componentes eletrônicos e suas respectivas conexões, permitindo uma construção precisa e eficiente da placa.

Em resumo, o esquemático da estrutura eletrônica da placa foi desenvolvido de forma cuidadosa e detalhada, levando em consideração todas as informações e especificações técnicas pertinentes. Este documento é essencial para o sucesso do projeto e garantirá a qualidade e eficiência da placa final.

<img src="https://github.com/2023M5T2-Inteli/alquimistas/blob/dev/docs/img/sprint3/Esquemático_v1.png" width="30%">

### Layout da Placa:

Com base no diagrama desenvolvido por meio do software EasyEDA, tornou-se possível estruturar o layout fundamental da placa.

<img src="https://github.com/2023M5T2-Inteli/alquimistas/blob/dev/docs/img/sprint3/Layout_v1.png" style="width: 20%"/>
<img src="https://github.com/2023M5T2-Inteli/alquimistas/blob/dev/docs/img/sprint3/PCB_v1.png" style="width: 20%"/>


### Lista de Materiais:

1. Placa de Trilhas com Fenolite 
2. Raspberry Pi Pico W 
3. Soquete para Raspberry Pi Pico W 
4. Conjunto de Jumpers 
5. Ponte H - L298N
6. Amplificador 
7. Módulo Sensor Magnético Efeito Hall 
8. 2 Eletroimãs 
9. Fonte de 5V - Alimentação 

### Método de fabricação:

1. Inicialmente foi desenvolvido o esquemático de base para o circuito por meio do software EasyEDA: O processo de desenvolvimento do esquemático envolve a elaboração de um diagrama que representa as conexões elétricas entre os componentes eletrônicos que compõem o circuito. Nesta etapa, é considerado aspectos como a disposição dos componentes e as conexões elétricas necessárias. Contudo, encontramos limitações na nossa primeira versão desenvolvida com o EasyEDA (ferramenta de design eletrônico que permite a criação de esquemas e layouts de placas de circuito impresso), com isso desenvolvemos uma segunda versão com o software Fritzing (ambos os esquemáticos estão na pasta 'docs/img/sprint3').
2. Em seguida foi realizado o posicionamento de componentes: Com base no esquemático desenvolvido na etapa anterior, os componentes eletrônicos são posicionados fisicamente na placa de circuito impresso. Nesta etapa, é importante considerar aspectos como a disposição física dos componentes, o espaço disponível na placa e as conexões elétricas necessárias.
3. A próxima etapa foi a soldagem de componentes: Após o posicionamento dos componentes na placa, é necessário realizar a soldagem dos mesmos. Este processo consiste na aplicação de calor em pontos específicos da placa, de modo a fixar os componentes eletrônicos na placa. A soldagem deve ser realizada com cuidado e precisão, visando garantir a qualidade e a segurança do circuito.
4. Por fim, foram realizados testes de funcionamento do circuito utilizando instrumentos como multímetros e osciloscópios para medir e analisar os sinais elétricos do circuito. Os resultados dos testes foram utilizados para verificar se o circuito está operando de acordo com as especificações previamente definidas e para realizar ajustes ou correções, se necessário.

## Fabricação dos Dispositivos Eletrônicos

1. Inicialmente foi realizado o teste com o circuito em protoboard para garantir o funcionamento do circuito. 
2. Posicionamento dos componentes na placa 
3. Soldagem do Soquete - Principal 
4. Soldagem de Jumpers 
5. Posicionamento do Amplificador e Soldagem 
6. Posicionamento do Módulo do Transistor de Efeito Hall e Soldagem 
7. Conexão de Jumpers 

Estruturadas todas as etapas, foi desenvolvido o circuito demonstrado nas imagens abaixo:
<br>
<img src="https://github.com/2023M5T2-Inteli/alquimistas/blob/dev/docs/img/sprint3/circuito1.jpeg" style="width: 20%"/>
<img src="https://github.com/2023M5T2-Inteli/alquimistas/blob/dev/docs/img/sprint3/circuito2.jpeg" style="width: 20%"/>
<img src="https://github.com/2023M5T2-Inteli/alquimistas/blob/dev/docs/img/sprint3/circuito3.jpeg" style="width: 20%"/>
<img src="https://github.com/2023M5T2-Inteli/alquimistas/blob/dev/docs/img/sprint3/circuito4.jpeg" style="width: 20%"/>

## Validação dos Dipositivos Eletrônicos

### Métodos de Validação e Testes 
A validação do dispositivo eletrônico foi realizada por meio da execução do código-fonte ("src"), juntamente com a aplicação da interface da aplicação web ("src/frontend"). A tabela abaixo apresenta os testes realizados, incluindo as entradas e saídas esperadas, bem como os resultados obtidos:

|Componente                                 |Entrada                                                                                                |Saída Esperada                                                                                                                 |Resultado do teste                                                                                                                                                                                    |
|-------------------------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Eletroimãs                                 |Acionar o botão de on/off                                                                              |Os imãs emitirem campo magnético e atrair objetos magnéticos                                                                   |Sucesso. O imã atrai objetos magnéticos ao pressionarmos o botão                                                                                                                                      |
|Circuito (imãs+interface)                  |Pressionar o botão 'start' na interface para acionar os imãs                                           |Os imãs emitirem campo magnético e atrair objetos magnéticos                                                                   |Sucesso. Ao pressionar o botão na aplicação web os imãs atraem os objetos magnéticos                                                                                                                  |
|Módulo Sensor Magnético de Efeito Hall     |Acionar o botão de on/off                                                                              |O sensor identifica o campo magnético em mv/Gauss                                                                              |Sucesso. O módulo sensor responde o valor do campo magnético                                                                                                                                          |
|Circuito (imãs + interface + módulo sensor)|Pressionar o botão 'start' na interface para acionar os imãs e o módulo sensor magnético de efeito hall|Os imãs emitirem campo magnético e atrair objetos magnéticos e o módulo sensor magnético identificar o valor do campo magnético|Sucesso. Ao pressionar o botão na aplicação web os imãs atraem os objetos magnéticos e o módulo sensor de efeito hall faz a leitura do campo magnético (contudo não tem uma granularidade dos valores)|

# Validação da eficácia do sistema

Além dos testes de componentes e dispositivos mecânicos e eletrônicos, foi necessário haver uma validação do sistema integrado completo (movimentação do robô, frontend e backend). 

## Teste de Barreira

[Vídeo da Versão Final do Protótipo](https://www.youtube.com/shorts/ck_-ao5tGDo)

# Adicional 

A equipe de desenvolvimento criou uma estrutura seguindo o padrão de arquitetura MVC (Model-View-Controller) para o projeto. O MVC é um padrão amplamente utilizado na engenharia de software que separa as responsabilidades do sistema em três componentes principais: o Modelo (Model), a Visão (View) e o Controlador (Controller).
Essa estrutura MVC inclui a integração de um sistema que é ativado por meio do uso do protocolo MQTT (Message Queuing Telemetry Transport). O MQTT é um protocolo de comunicação leve e eficiente, frequentemente usado para a troca de mensagens em redes de dispositivos IoT (Internet of Things).

Devido a desafios encontrados na implementação da integração do sistema com o protótipo, a equipe decidiu utilizar a versão inicial do sistema em funcionamento como a versão final do projeto. Isso significa que a estrutura MVC desenvolvida foi considerada como um adicional para atender aos requisitos do projeto e não foi adotada como a versão final.

No entanto, a equipe considerou importante disponibilizar a estrutura de conexão MQTT entre os diferentes componentes do sistema, mesmo que a versão de funcionamento por meio do SOFTAP tenha sido adotada como a versão final. Isso foi feito para permitir a possibilidade de evolução e integração do sistema no futuro, caso seja necessário fazer atualizações ou expandir suas funcionalidades.

A pasta compacta contendo a estrutura de MQTT está disponível dentro da pasta `src`. 

