# etlBCB
# etlBCB

<!-- Para melhor vizualição da tabela, utilizar a formatação de Estrutura Markdown: Ctrl+Shift+V -->

# Dados sobre Meios de Pagamento

| *Título* | *Descrição* |
|------------|--------------|
| *Estoque e transações de cartões* | Quantidade de cartões emitidos e ativos e transações realizadas com este instrumento de pagamento. |
| *Meios de Pagamentos Mensais* | Conjunto de informações sobre operações com boletos bancários e de transferências de crédito. Dados ficam disponíveis a partir do 17º dia do mês subsequente. |
| *Meios de Pagamentos Trimestrais* | Conjunto de informações sobre operações com cartões de pagamento e de transferências de crédito (boletos bancários, cartões de crédito e débito, transferências bancárias). Dados ficam disponíveis 90 dias após o final do trimestre. |
| *Quantidade de estabelecimentos credenciados* | Informações referentes à quantidade de estabelecimentos credenciados, total e ativos, discriminados de acordo com as bandeiras e funções dos cartões por eles aceitos. Dados ficam disponíveis 90 dias após o final do trimestre. |
| *Tarifas de intercâmbio (TIC) e volumetria* | Informações referentes às tarifas de intercâmbio e volumetria desagregadas pela função/bandeira/produto do cartão, forma de captura da transação e número de parcelas. Dados ficam disponíveis 90 dias após o final do trimestre. |
| *Taxas de desconto (MDR) e volumetria* | Informações referentes às taxas de desconto (MDR) e volumetria desagregadas pela função/bandeira do cartão, forma de captura da transação e número de parcelas. Dados ficam disponíveis 90 dias após o final do trimestre. |
| *Quantidade de terminais de autoatendimento (ATM)* | Posição de final de trimestre da quantidade de terminais de autoatendimento (ATM) instalados, desagregada pela função, localização, UF e tipo de compartilhamento do terminal. Dados ficam disponíveis 90 dias após o final do trimestre. |
| *Volumetria das operações intrabancárias* | Informações agregadas referentes à quantidade e ao valor das operações realizadas entre clientes da instituição e que não cursaram em sistemas de compensação ou liquidação de transferências de fundos. São incluídos os cheques e boletos de pagamento intrabancários, as arrecadações, as operações de débito automático e de crédito direto e os empréstimos e financiamentos para os clientes. Transferências ou pagamentos realizados via Pix de forma intrabancária não são informados nessa base de dados. Dados ficam disponíveis 90 dias após o final do trimestre. |
| *Volumetria por canal de acesso e produto* | Informações referentes à quantidade e ao valor das operações, de acordo com os produtos (tipo de transação realizada) e os canais de atendimento (canal de acesso em que a transação é realizada). Dados ficam disponíveis 90 dias após o final do trimestre. |
| *Quantidade de terminais POS e PDV* | Informações referentes à quantidade de terminais POS e PDV conectados à rede do credenciador, segregada de acordo com a forma de captura. Dados ficam disponíveis 90 dias após o final do trimestre. |
| *Tarifas cobradas/programa de recompensa/fidelidade* | Informações referentes às tarifas cobradas dos portadores dos cartões de pagamento emitidos pela instituição ou pelas instituições pertencentes ao conglomerado e sobre os programas de recompensa/fidelidade. Dados ficam disponíveis 90 dias após o final do trimestre.



# Estoque e transações de cartões

Quantidade de cartões emitidos e ativos e transações realizadas com este instrumento de pagamento.

---

## Parâmetros

| Nome      | Tipo    | Título    | Descrição                                                                                                                                                          |
|-----------|---------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| trimestre | texto   | Trimestre | Os dados serão trazidos a partir do trimestre fornecido como parâmetro no formato *AAAAT*.                                                                        |
| $format   | texto   | $format   | Tipo de conteúdo que será retornado.                                                                                                                               |
| $select   | texto   | $select   | Propriedades que serão retornadas.                                                                                                                                |
| $filter   | texto   | $filter   | Filtro de seleção de entidades. e.g. Nome eq 'João'. Clique [aqui](#) para as opções de operadores e funções.                                                     |
| $orderby  | texto   | $orderby  | Propriedades para ordenação das entidades. e.g. Nome asc, Idade desc.                                                                                              |
| $skip     | inteiro | $skip     | Índice (maior ou igual a zero) da primeira entidade que será retornada.                                                                                           |
| $top      | inteiro | $top      | Número máximo (maior que zero) de entidades que serão retornadas.                                                                                                 |

---

## Resultado

| Nome                        | Tipo    | Título                                       | Descrição                                                                                                                                                                             |
|-----------------------------|---------|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| trimestre                   | texto   | Trimestre                                    | Corresponde ao ano e trimestre das informações.                                                                                                                                     |
| nomeBandeira                | texto   | Bandeira do cartão                           | Corresponde ao nome da bandeira do cartão.                                                                                                                                            |
| nomeFuncao                  | texto   | Função do cartão                             | Corresponde ao nome da função do cartão (crédito, débito e pré-pago).                                                                                                                  |
| produto                     | texto   | Produto do cartão                            | Categoria atribuída a um cartão de pagamento.                                                                                                                                         |
| qtdCartoesEmitidos          | inteiro | Quantidade de cartões emitidos               | Corresponde ao estoque de cartões emitidos, apurado no trimestre, ou seja, os cartões que foram emitidos em todos os períodos anteriores até o final do trimestre de referência. Os cartões cancelados não integram esta estatística. |
| qtdCartoesAtivos            | inteiro | Quantidade de cartões ativos                 | Corresponde ao estoque de cartões ativos, apurado no final do trimestre. São considerados como ativos os cartões que foram utilizados pelo menos uma vez no período que abrange os doze meses anteriores ao último dia do trimestre de referência. |
| qtdTransacoesNacionais       | inteiro | Quantidade de transações nacionais com cartão | Corresponde à quantidade de transações com cartão realizadas no país.                                                                                                                 |
| valorTransacoesNacionais     | decimal | Valor de transações nacionais com cartão     | Corresponde ao valor em reais de transações com cartão realizadas no país.                                                                                                              |
| qtdTransacoesInternacionais   | inteiro | Quantidade de transações internacionais com cartão | Corresponde à quantidade de transações com cartão realizadas fora do país.                                                                                                              |
| valorTransacoesInternacionais | decimal | Valor de transações internacionais com cartão | Corresponde ao valor em reais de transações com cartão realizadas fora do país.                                                                                                          |


# Meios de Pagamentos Mensais

Conjunto de informações sobre operações com boletos bancários e de transferências de crédito. Dados ficam disponíveis a partir do 17º dia do mês subsequente.

---

## Parâmetros

| Nome     | Tipo    | Título   | Descrição                                                                                                                          |
|----------|---------|----------|------------------------------------------------------------------------------------------------------------------------------------|
| AnoMes   | texto   | Ano-Mês  | Os dados serão trazidos a partir do mês fornecido como parâmetro no formato *AAAAMM*.                                             |
| $format  | texto   | $format  | Tipo de conteúdo que será retornado.                                                                                               |
| $select  | texto   | $select  | Propriedades que serão retornadas.                                                                                                 |
| $filter  | texto   | $filter  | Filtro de seleção de entidades. e.g. Nome eq 'João'. Clique [aqui](#) para as opções de operadores e funções.                     |
| $orderby | texto   | $orderby | Propriedades para ordenação das entidades. e.g. Nome asc, Idade desc.                                                              |
| $skip    | inteiro | $skip    | Índice (maior ou igual a zero) da primeira entidade que será retornada.                                                           |
| $top     | inteiro | $top     | Número máximo (maior que zero) de entidades que serão retornadas.                                                                  |

---

## Resultado

| Nome                 | Tipo    | Título                           | Descrição                                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------|---------|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AnoMes               | texto   | Ano-Mês                          |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| quantidadePix        | decimal | Quantidade Pix                   | Quantidade (em milhares) de transações Pix liquidadas mensalmente no SPI e fora do SPI, considerando ordens de pagamento e devoluções no período. Dados referentes às transações liquidadas fora do SPI estão sujeitas a alterações retroativas, pois dependem da prestação de informação pelos participantes.                                                                                                                         |
| valorPix             | decimal | Valor Pix                        | Volume financeiro (R$ milhões) de transações Pix liquidadas mensalmente no SPI e fora do SPI, considerando ordens de pagamento e devoluções no período. Dados referentes às transações liquidadas fora do SPI estão sujeitas a alterações retroativas, pois dependem da prestação de informação pelos participantes.                                                                                                                     |
| quantidadeTED        | decimal | Quantidade TED                   | Quantidade (em milhares) de transferências por meio de TED realizadas mensalmente. Transferência Eletrônica Direta (TED) – transferência financeira, em tempo real, entre diferentes bancos e demais instituições (financeiras ou de pagamentos) detentoras de conta no Banco Central. Pode ser utilizada para transferir valores entre correntistas de diferentes instituições, e entre as próprias instituições, envolvendo pagamento de obrigações ou não. |
| valorTED             | decimal | Valor TED (R$)                   | Montante financeiro (R$ milhões) transferido por meio de TED mensalmente. Transferência Eletrônica Direta (TED) – transferência financeira, em tempo real, entre diferentes bancos e demais instituições (financeiras ou de pagamentos) detentoras de conta no Banco Central. Pode ser utilizada para transferir valores entre correntistas de diferentes instituições, e entre as próprias instituições, envolvendo pagamento de obrigações ou não.   |
| quantidadeTEC        | decimal | Quantidade TEC                   | Quantidade (em milhares) de transferências por meio de TEC realizadas mensalmente. Transferência Especial de Crédito (TEC) – transferência financeira utilizada por empresas para pagamento de benefícios aos empregados.                                                                                                                                                                                                  |
| valorTEC             | decimal | Valor TEC                        | Montante financeiro (R$ milhões) transferido por meio de TEC mensalmente. Transferência Especial de Crédito (TEC) – transferência financeira utilizada por empresas para pagamento de benefícios aos empregados.                                                                                                                                                                                                  |
| quantidadeCheque     | decimal | Quantidade de Cheques            | Quantidade (em milhares) de cheques interbancários compensados mensalmente.                                                                                                                                                                                                                                                                                                                                                       |
| valorCheque          | decimal | Valor Cheques                    | Montante financeiro (R$ milhões) de cheques interbancários compensados mensalmente.                                                                                                                                                                                                                                                                                                                                              |
| quantidadeBoleto     | decimal | Quantidade Boletos               | Quantidade (em milhares) de boletos interbancários liquidados mensalmente.                                                                                                                                                                                                                                                                                                                                                        |
| valorBoleto          | decimal | Valor Boletos                    | Montante financeiro (R$ milhões) dos boletos interbancários liquidados mensalmente.                                                                                                                                                                                                                                                                                                                                              |
| quantidadeDOC        | decimal | Quantidade DOC                   | Quantidade (em milhares) de transferências realizadas por meio de DOC mensalmente.                                                                                                                                                                                                                                                                                                                                               |
| valorDOC             | decimal | Valor DOC                        | Montante financeiro (R$ milhões) mensal transferido por meio de DOC mensalmente.                                                                                                                                                                                                                                                                                                                                                  |

# Meios de Pagamentos Trimestrais

Conjunto de informações sobre operações com cartões de pagamento e de transferências de crédito (boletos bancários, cartões de crédito e débito, transferências bancárias). Dados ficam disponíveis 90 dias após o final do trimestre.

---

## Parâmetros

| Nome       | Tipo    | Título    | Descrição                                                                                                         |
|------------|---------|-----------|-------------------------------------------------------------------------------------------------------------------|
| trimestre  | texto   | Trimestre | Os dados serão trazidos a partir do trimestre fornecido como parâmetro no formato *AAAAT*.                      |
| $format    | texto   | $format   | Tipo de conteúdo que será retornado.                                                                              |
| $select    | texto   | $select   | Propriedades que serão retornadas.                                                                                |
| $filter    | texto   | $filter   | Filtro de seleção de entidades. e.g. Nome eq 'João'. Clique [aqui](#) para as opções de operadores e funções.     |
| $orderby   | texto   | $orderby  | Propriedades para ordenação das entidades. e.g. Nome asc, Idade desc.                                               |
| $skip      | inteiro | $skip     | Índice (maior ou igual a zero) da primeira entidade que será retornada.                                            |
| $top       | inteiro | $top      | Número máximo (maior que zero) de entidades que serão retornadas.                                                  |

---

## Resultado

| Nome                          | Tipo    | Título                           | Descrição                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------------------|---------|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| datatrimestre                 | texto   | Trimestre                        |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| valorPix                      | decimal | Valor Pix                        | Volume financeiro (R$ milhões) de transações Pix liquidadas trimestralmente no SPI e fora do SPI, considerando ordens de pagamento e devoluções no período. Dados referentes às transações liquidadas fora do SPI estão sujeitas a alterações retroativas, pois dependem da prestação de informação pelos participantes.                                                                                                                     |
| valorTED                      | decimal | Valor TED                        | Montante financeiro (R$ milhões) trimestral transferido por meio de TED. Transferência Eletrônica Direta (TED) – transferência financeira, em tempo real, entre diferentes bancos e demais instituições (financeiras ou de pagamentos) detentoras de conta no Banco Central. Pode ser utilizada para transferir valores entre correntistas de diferentes instituições, e entre as próprias instituições, envolvendo pagamento de obrigações ou não. |
| valorTEC                      | decimal | Valor TEC                        | Montante financeiro (R$ milhões) trimestral transferido por meio de TEC. Transferência Especial de Crédito (TEC) – transferência financeira utilizada por empresas para pagamento de benefícios aos empregados.                                                                                                                                                                                                                  |
| valorCheque                   | decimal | Valor Cheque                     | Montante financeiro (R$ milhões) de cheques interbancários e intrabancários compensados trimestralmente.                                                                                                                                                                                                                                                                                                                          |
| valorBoleto                   | decimal | Valor Boleto                     | Montante financeiro (R$ milhões) de boletos interbancários e intrabancários compensados trimestralmente.                                                                                                                                                                                                                                                                                                                          |
| valorDOC                      | decimal | Valor DOC                        | Montante financeiro (R$ milhões) trimestral transferido por meio de DOC.                                                                                                                                                                                                                                                                                                                                                            |
| valorCartaoCredito            | decimal | Valor Cartão de Crédito          | Valor (R$ milhões) de transações realizadas com cartão de crédito.                                                                                                                                                                                                                                                                                                                                                                |
| valorCartaoDebito             | decimal | Valor Cartão de Débito           | Valor (R$ milhões) de transações realizadas com cartão de débito trimestralmente.                                                                                                                                                                                                                                                                                                                                                  |
| valorCartaoPrePago            | decimal | Valor Cartão Pré-pago            | Valor (R$ milhões) de transações realizadas com cartão pré-pago trimestralmente.                                                                                                                                                                                                                                                                                                                                                    |
| valorTransIntrabancaria       | decimal | Valor Transferência Intrabancária| Montante financeiro (R$ milhões) de transferências realizadas trimestralmente entre contas de clientes da Instituição, inclusive aquelas envolvendo movimentações referentes a aplicações e resgates em fundos de investimento.                                                                                                                                                                                                 |
| valorConvenios                | decimal | Valor Convênio                   | Montante financeiro (R$ milhões) referente a arrecadações trimestrais governamentais (arrecadação de tributos e encargos sociais em virtude de convênios firmados entre a instituição e as entidades governamentais) e não-governamentais (arrecadações referentes aos convênios firmados entre a instituição e entidades privadas).                                                                                        |
| valorDebitoDireto             | decimal | Valor Débito Direto              | Montante financeiro (R$ milhões) trimestral referente a débitos previamente autorizados pelo cliente em sua conta corrente/pagamento, referente ao pagamento de contas recorrentes e a débitos que a instituição efetua na conta dos clientes em virtude de cobrança de tarifas pelos serviços prestados.                                                                                                                       |
| valorSaques                   | decimal | Valor Saque                      | Montante sacado (R$ milhões) nos caixas eletrônicos trimestralmente.                                                                                                                                                                                                                                                                                                                                                              |
| quantidadePix                 | decimal | Quantidade Pix                   | Quantidade (em milhares) de transações Pix liquidadas trimestralmente no SPI e fora do SPI, considerando ordens de pagamento e devoluções no período.                                                                                                                                                                                                                                                                          |
| quantidadeTED                 | decimal | Quantidade TED                   | Quantidade (em milhares) de TED realizadas trimestralmente. Transferência Eletrônica Direta (TED) – transferência financeira, em tempo real, entre diferentes bancos e demais instituições (financeiras ou de pagamentos) detentoras de conta no Banco Central. Pode ser utilizada para transferir valores entre correntistas de diferentes instituições, e entre as próprias instituições, envolvendo pagamento de obrigações ou não. |
| quantidadeTEC                 | decimal | Quantidade TEC                   | Quantidade (em milhares) de TEC realizadas trimestralmente. Transferência Especial de Crédito (TEC) – transferência financeira utilizada por empresas para pagamento de benefícios aos empregados.                                                                                                                                                                                                                             |
| quantidadeCheque              | decimal | Quantidade Cheque                | Quantidade (em milhares) de cheques interbancários e de cheques intrabancários compensados trimestralmente.                                                                                                                                                                                                                                                                                                                       |
| quantidadeBoleto              | decimal | Quantidade Boleto                | Quantidade (em milhares) de cheques interbancários e intrabancários compensados trimestralmente.                                                                                                                                                                                                                                                                                                                                  |
| quantidadeDOC                 | decimal | Quantidade DOC                   | Quantidade (em milhares) de DOC realizados trimestralmente.                                                                                                                                                                                                                                                                                                                                                                      |
| quantidadeCartaoCredito       | decimal | Quantidade Cartão de Crédito     | Quantidade (em milhares) de transações realizadas com cartão de crédito trimestralmente.                                                                                                                                                                                                                                                                                                                                          |
| quantidadeCartaoDebito        | decimal | Quantidade Cartão de Débito      | Quantidade (em milhares) de transações realizadas com cartão de débito trimestralmente.                                                                                                                                                                                                                                                                                                                                            |
| quantidadeCartaoPrePago       | decimal | Quantidade Cartão Pré-pago       | Quantidade (em milhares) de transações realizadas com cartão pré-pago trimestralmente.                                                                                                                                                                                                                                                                                                                                            |
| quantidadeTransIntrabancaria  | decimal | Quantidade de Transferência Intrabancária | Quantidade (em milhares) de transferências realizadas trimestralmente entre contas de clientes da Instituição, inclusive aquelas envolvendo movimentações referentes a aplicações e resgates em fundos de investimento.                                                                                                                                                                                                      |
| quantidadeConvenios         | decimal | Quantidade Convênio              | Quantidade (em milhares) de transações realizadas referentes a arrecadações trimestrais governamentais (arrecadação de tributos e encargos sociais em virtude de convênios firmados entre a instituição e as entidades governamentais) e não-governamentais (arrecadações referentes aos convênios firmados entre a instituição e entidades privadas).                                                         |
| quantidadeDebitoDireto      | decimal | Quantidade Débito Direto         | Quantidade (em milhares) de transações trimestrais referente a débitos previamente autorizados pelo cliente em sua conta corrente/pagamento, referente ao pagamento de contas recorrentes e a débitos que a instituição efetua na conta dos clientes em virtude de cobrança de tarifas pelos serviços prestados.                                                                                                                |
| quantidadeSaques            | decimal | Quantidade de Saque              | Quantidade (em milhares) de saques realizados nos caixas eletrônicos trimestralmente.

# Quantidade de estabelecimentos credenciados

Informações referentes à quantidade de estabelecimentos credenciados, total e ativos, discriminados de acordo com as bandeiras e funções dos cartões por eles aceitos. Dados ficam disponíveis 90 dias após o final do trimestre.

## Parâmetros

| Nome      | Tipo    | Título    | Descrição                                                                                                           |
|-----------|---------|-----------|---------------------------------------------------------------------------------------------------------------------|
| trimestre | texto   | Trimestre | Os dados serão disponibilizados a partir do trimestre fornecido como parâmetro no formato *AAAAT*                 |
| $format   | texto   | $format   | Tipo de conteúdo que será retornado                                                                                 |
| $select   | texto   | $select   | Propriedades que serão retornadas                                                                                   |
| $filter   | texto   | $filter   | Filtro de seleção de entidades. e.g. Nome eq 'João'. Clique [aqui](#) para as opções de operadores e funções.      |
| $orderby  | texto   | $orderby  | Propriedades para ordenação das entidades. e.g. Nome asc, Idade desc.                                                |
| $skip     | inteiro | $skip     | Índice (maior ou igual a zero) da primeira entidade que será retornada                                                |
| $top      | inteiro | $top      | Número máximo (maior que zero) de entidades que serão retornadas                                                      |

## Resultado

| Nome                 | Tipo    | Título                                          | Descrição                                                                                                                                                           |
|----------------------|---------|-------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| trimestre            | inteiro | Trimestre                                       | Data-base de referência (AAAAT)                                                                                                                                     |
| bandeira             | texto   | Bandeira                                        | Indica a marca do cartão que o estabelecimento está credenciado para aceitar.                                                                                      |
| funcaoCartao         | texto   | Função do cartão                                | Em relação ao cartão de pagamento, é a especificação da função nele disponibilizada.                                                                                |
| qtdEstabCredenciados | inteiro | Quantidade de estabelecimentos credenciados     | Quantidade de estabelecimentos credenciados para aceitação de cartões de pagamento.                                                                               |
| qtdEstabAtivos       | inteiro | Quantidade de estabelecimentos credenciados ativos | Quantidade de estabelecimentos credenciados para aceitação de cartões de pagamento que tenham realizado pelo menos 1 transação com cartões de pagamentos no período de 180 (cento e oitenta) dias anteriores ao último dia do trimestre de referência. |

---

# Tarifas de intercâmbio (TIC) e volumetria

Informações referentes às tarifas de intercâmbio e volumetria desagregadas pela função/bandeira/produto do cartão, forma de captura da transação e número de parcelas. Dados ficam disponíveis 90 dias após o final do trimestre.

## Parâmetros

| Nome      | Tipo    | Título    | Descrição                                                                                                           |
|-----------|---------|-----------|---------------------------------------------------------------------------------------------------------------------|
| trimestre | texto   | Trimestre | Os dados serão disponibilizados a partir do trimestre fornecido como parâmetro no formato *AAAAT*                 |
| $format   | texto   | $format   | Tipo de conteúdo que será retornado                                                                                 |
| $select   | texto   | $select   | Propriedades que serão retornadas                                                                                   |
| $filter   | texto   | $filter   | Filtro de seleção de entidades. e.g. Nome eq 'João'. Clique [aqui](#) para as opções de operadores e funções.      |
| $orderby  | texto   | $orderby  | Propriedades para ordenação das entidades. e.g. Nome asc, Idade desc.                                                |
| $skip     | inteiro | $skip     | Índice (maior ou igual a zero) da primeira entidade que será retornada                                                |
| $top      | inteiro | $top      | Número máximo (maior que zero) de entidades que serão retornadas                                                      |

## Resultado

| Nome            | Tipo    | Título                           | Descrição                                                                                                                                                                                                                      |
|-----------------|---------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| trimestre       | inteiro | Trimestre                        | Data-base de referência (AAAAT)                                                                                                                                                                                                |
| produto         | texto   | Produto                          | Categoria atribuída a um cartão de pagamento, sob uma certa denominação, que lhe agrega um conjunto de vantagens, diferenciando-o de acordo com o perfil do portador.                                                       |
| bandeira        | texto   | Bandeira                         | Marca estampada no cartão e que indica a detentora dos direitos e deveres da sua utilização.                                                                                                                                    |
| funcaoCartao    | texto   | Função do cartão                 | Em relação ao cartão de pagamento, é a especificação da função nele disponibilizada.                                                                                                                                             |
| formacaptura    | texto   | Forma de captura                 | Diz respeito à forma de captura da transação, bem como se o cartão é fisicamente apresentado ou não quando do pagamento por bens/serviços.                                                                                    |
| numeroparcelas  | texto   | Número de parcelas               | Número de parcelas, concessão do lojista e definido no momento da compra, sem acréscimo de juros, por meio das quais a dívida será liquidada. Nas operações "à vista" deverá ser informado como 1 (uma) parcela.         |
| valorTransacoes | decimal | Valor das transações             | Soma do valor das transações em reais, líquidas de IOF, realizadas para cada nível de desagregação no trimestre de referência.                                                                                                  |
| qtdTransacoes   | decimal | Quantidade de transações         | É a contagem de todas as transações realizadas para cada nível de desagregação no trimestre de referência da informação.                                                                                                      |
| tarifaIntercambioPonderada | decimal | Tarifa de intercâmbio     | É a tarifa (%) que o credenciador, responsável pela captura da transação, paga ao banco emissor do cartão utilizado. Calculada pela ponderação entre a tarifa de intercâmbio e o valor das transações.                      |

---

# Taxas de desconto (MDR) e volumetria

Informações referentes às taxas de desconto (MDR) e volumetria desagregadas pela função/bandeira do cartão, forma de captura da transação e número de parcelas. Dados ficam disponíveis 90 dias após o final do trimestre.

## Parâmetros

| Nome      | Tipo    | Título    | Descrição                                                                                                           |
|-----------|---------|-----------|---------------------------------------------------------------------------------------------------------------------|
| trimestre | texto   | Trimestre | Os dados serão disponibilizados a partir do trimestre fornecido como parâmetro no formato *AAAAT*                 |
| $format   | texto   | $format   | Tipo de conteúdo que será retornado                                                                                 |
| $select   | texto   | $select   | Propriedades que serão retornadas                                                                                   |
| $filter   | texto   | $filter   | Filtro de seleção de entidades. e.g. Nome eq 'João'. Clique [aqui](#) para as opções de operadores e funções.      |
| $orderby  | texto   | $orderby  | Propriedades para ordenação das entidades. e.g. Nome asc, Idade desc.                                                |
| $skip     | inteiro | $skip     | Índice (maior ou igual a zero) da primeira entidade que será retornada                                                |
| $top      | inteiro | $top      | Número máximo (maior que zero) de entidades que serão retornadas                                                      |

## Resultado

| Nome            | Tipo    | Título                       | Descrição                                                                                                                                                                                                  |
|-----------------|---------|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| trimestre       | inteiro | Trimestre                    | Data-base de referência (AAAAT)                                                                                                                                                                            |
| bandeira        | texto   | Bandeira                     | Marca estampada no cartão e que indica a detentora dos direitos e deveres da sua utilização.                                                                                                               |
| funcaoCartao    | texto   | Função do cartão             | Em relação ao cartão de pagamento, é a especificação da função nele disponibilizada.                                                                                                                        |
| formacaptura    | texto   | Forma de captura             | Diz respeito à forma de captura da transação, bem como se o cartão é fisicamente apresentado ou não quando do pagamento por bens/serviços.                                                                   |
| numeroparcelas  | texto   | Número de parcelas           | Número de parcelas, concessão do lojista e definido no momento da compra, sem acréscimo de juros, por meio das quais a dívida será liquidada. Nas operações "à vista" deverá ser informado como 1 (uma) parcela. |
| qtdDesconto     | decimal | Quantidade de transações     | É a contagem de todas as transações realizadas para cada nível de desagregação no trimestre de referência da informação.                                                                                   |
| valorDesconto   | decimal | Valor das transações         | Soma do valor das transações em reais, líquidas de IOF, realizadas para cada nível de desagregação no trimestre de referência.                                                                               |
| txMediaDesconto | decimal | Taxa de desconto             | É a taxa (%) média ponderada pelo valor das transações, que o credenciador cobrou do estabelecimento credenciado sobre o valor de cada transação efetuada com cartão de pagamento.                      |


# Quantidade de terminais de autoatendimento (ATM)

Posição de final de trimestre da quantidade de terminais de autoatendimento (ATM) instalados, desagregada pela função, localização, UF e tipo de compartilhamento do terminal. Dados ficam disponíveis 90 dias após o final do trimestre.

## Parâmetros

| Nome      | Tipo    | Título    | Descrição                                                                                                           |
|-----------|---------|-----------|---------------------------------------------------------------------------------------------------------------------|
| trimestre | texto   | Trimestre | Os dados serão disponibilizados a partir do trimestre fornecido como parâmetro no formato *AAAAT*                 |
| $format   | texto   | $format   | Tipo de conteúdo que será retornado                                                                                 |
| $select   | texto   | $select   | Propriedades que serão retornadas                                                                                   |
| $filter   | texto   | $filter   | Filtro de seleção de entidades. e.g. Nome eq 'João'. Clique [aqui](#) para as opções de operadores e funções.      |
| $orderby  | texto   | $orderby  | Propriedades para ordenação das entidades. e.g. Nome asc, Idade desc.                                               |
| $skip     | inteiro | $skip     | Índice (maior ou igual a zero) da primeira entidade que será retornada                                                |
| $top      | inteiro | $top      | Número máximo (maior que zero) de entidades que serão retornadas                                                      |

## Resultado

| Nome                   | Tipo    | Título                        | Descrição                                                                                                               |
|------------------------|---------|-------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| trimestre              | inteiro | Trimestre                     | Data-base de referência (AAAAT)                                                                                         |
| codFuncaoTerminal      | texto   | Função do terminal            | Tipo de funcionalidade disponível no ATM                                                                               |
| codLocalizacao         | texto   | Localização                   | Local onde o ATM está fisicamente instalado                                                                            |
| codTipoCompartilhamento| texto   | Tipo de compartilhamento      | Indica se o ATM pode apenas ser utilizado por clientes da instituição ou se o uso é compartilhado                      |
| UF_Terminal            | texto   | Unidade da Federação (UF)     | Unidade da Federação onde está instalado o terminal                                                                    |
| qtdTerminal            | decimal | Quantidade de ATM             | Quantidade instalada de ATM                                                                                             |

---

# Volumetria das operações intrabancárias

Informações agregadas referentes à quantidade e ao valor das operações realizadas entre clientes da instituição e que não cursaram em sistemas de compensação ou de liquidação de transferências de fundos. São incluídos os cheques e boletos de pagamento intrabancários, as arrecadações, as operações de débito automático e de crédito direto e os empréstimos e financiamentos para os clientes. Transferências ou pagamentos realizados via Pix de forma intrabancária não são informados nessa base de dados. Dados ficam disponíveis 90 dias após o final do trimestre.

## Parâmetros

| Nome      | Tipo    | Título    | Descrição                                                                                                           |
|-----------|---------|-----------|---------------------------------------------------------------------------------------------------------------------|
| trimestre | texto   | Trimestre | Os dados serão disponibilizados a partir do trimestre fornecido como parâmetro no formato *AAAAT*                 |
| $format   | texto   | $format   | Tipo de conteúdo que será retornado                                                                                 |
| $select   | texto   | $select   | Propriedades que serão retornadas                                                                                   |
| $filter   | texto   | $filter   | Filtro de seleção de entidades. e.g. Nome eq 'João'. Clique [aqui](#) para as opções de operadores e funções.      |
| $orderby  | texto   | $orderby  | Propriedades para ordenação das entidades. e.g. Nome asc, Idade desc.                                               |
| $skip     | inteiro | $skip     | Índice (maior ou igual a zero) da primeira entidade que será retornada                                                |
| $top      | inteiro | $top      | Número máximo (maior que zero) de entidades que serão retornadas                                                      |

## Resultado

| Nome             | Tipo    | Título                           | Descrição                                     |
|------------------|---------|----------------------------------|-----------------------------------------------|
| trimestre        | inteiro | Trimestre                        | Data-base de referência (AAAAT)               |
| operacao         | texto   | Tipo de operação intrabancária   | Tipo de operação intrabancária realizada.     |
| qtdTransacoes    | decimal | Quantidade de transações         | Quantidade de transações                      |
| valorTransacoes  | decimal | Valor das transações             | Valor das transações                          |

---

# Volumetria por canal de acesso e produto

Informações referentes à quantidade e ao valor das operações, de acordo com os produtos (tipo de transação realizada) e os canais de atendimento (canal de acesso em que a transação é realizada). Dados ficam disponíveis 90 dias após o final do trimestre.

## Parâmetros

| Nome      | Tipo    | Título    | Descrição                                                                                                           |
|-----------|---------|-----------|---------------------------------------------------------------------------------------------------------------------|
| trimestre | texto   | Trimestre | Os dados serão disponibilizados a partir do trimestre fornecido como parâmetro no formato *AAAAT*                 |
| $format   | texto   | $format   | Tipo de conteúdo que será retornado                                                                                 |
| $select   | texto   | $select   | Propriedades que serão retornadas                                                                                   |
| $filter   | texto   | $filter   | Filtro de seleção de entidades. e.g. Nome eq 'João'. Clique [aqui](#) para as opções de operadores e funções.      |
| $orderby  | texto   | $orderby  | Propriedades para ordenação das entidades. e.g. Nome asc, Idade desc.                                               |
| $skip     | inteiro | $skip     | Índice (maior ou igual a zero) da primeira entidade que será retornada                                                |
| $top      | inteiro | $top      | Número máximo (maior que zero) de entidades que serão retornadas                                                      |

## Resultado

| Nome             | Tipo    | Título                      | Descrição                                                                                                                           |
|------------------|---------|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| trimestre        | inteiro | Trimestre                   | Data-base de referência (AAAAT)                                                                                                     |
| canalAcesso      | texto   | Canal de acesso             | Canal de atendimento em que a transação é realizada                                                                                 |
| produto          | texto   | Produto                     | Tipo de transação realizada                                                                                                         |
| acessoATM        | texto   | Acesso ao ATM               | Indica o tipo de acesso disponibilizado no terminal ATM em que foi realizada a transação, bem como se foi efetuada por clientes ou não da instituição |
| qtdTransacoes    | decimal | Quantidade                  | Quantidade de transações                                                                                                              |
| valorTransacoes  | decimal | Valor                       | Valor das transações                                                                                                                  |


# Quantidade de terminais POS e PDV

Informações referentes à quantidade de terminais POS e PDV conectados à rede do credenciador, segregada de acordo com a forma de captura. Dados ficam disponíveis 90 dias após o final do trimestre.

## Parâmetros

| Nome      | Tipo    | Título    | Descrição                                                                                                           |
|-----------|---------|-----------|---------------------------------------------------------------------------------------------------------------------|
| trimestre | texto   | Trimestre | Os dados serão disponibilizados a partir do trimestre fornecido como parâmetro no formato *AAAAT*                 |
| $format   | texto   | $format   | Tipo de conteúdo que será retornado                                                                                 |
| $select   | texto   | $select   | Propriedades que serão retornadas                                                                                   |
| $filter   | texto   | $filter   | Filtro de seleção de entidades. e.g. Nome eq 'João'. Clique aqui para as opções de operadores e funções.             |
| $orderby  | texto   | $orderby  | Propriedades para ordenação das entidades. e.g. Nome asc, Idade desc.                                               |
| $skip     | inteiro | $skip     | Índice (maior ou igual a zero) da primeira entidade que será retornada                                                |
| $top      | inteiro | $top      | Número máximo (maior que zero) de entidades que serão retornadas                                                      |

## Resultado

| Nome                        | Tipo    | Título                              | Descrição                                                                                                                       |
|-----------------------------|---------|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| trimestre                   | inteiro | Trimestre                           | Data-base de referência (AAAAT)                                                                                                 |
| UFTerminal                  | texto   | Unidade da Federação (UF)           | Unidade da Federação                                                                                                            |
| qtdTermPOS                  | decimal | Quantidade de terminais POS         | Quantidade total de terminais POS instalados nos estabelecimentos em cada Unidade da Federação                                   |
| qtdTermPOScompartilhados    | decimal | Quantidade de terminais POS compartilhados | Quantidade de terminais POS instalados nos estabelecimentos em cada Unidade da Federação e que permitem o uso de cartões de bandeiras pertencentes a outras redes |
| qtdTermPOSchip              | decimal | Quantidade de terminais POS com leitora de chip | Quantidade de terminais POS instalados nos estabelecimentos em cada Unidade da Federação e que possuem dispositivos que permitem a leitura do chip dos cartões |
| qtdTermPDV                  | decimal | Quantidade de terminais PDV         | Quantidade de equipamentos PDV (TEF) instalados nos estabelecimentos em cada Unidade da Federação                               |

---

# Tarifas cobradas/programa de recompensa/fidelidade

Informações referentes às tarifas cobradas dos portadores dos cartões de pagamento emitidos pela instituição ou pelas instituições pertencentes ao conglomerado e sobre os programas de recompensa/fidelidade. Dados ficam disponíveis 90 dias após o final do trimestre.

## Parâmetros

| Nome      | Tipo    | Título    | Descrição                                                                                                           |
|-----------|---------|-----------|---------------------------------------------------------------------------------------------------------------------|
| trimestre | texto   | Trimestre | Os dados serão disponibilizados a partir do trimestre fornecido como parâmetro no formato *AAAAT*                 |
| $format   | texto   | $format   | Tipo de conteúdo que será retornado                                                                                 |
| $select   | texto   | $select   | Propriedades que serão retornadas                                                                                   |
| $filter   | texto   | $filter   | Filtro de seleção de entidades. e.g. Nome eq 'João'. Clique aqui para as opções de operadores e funções.             |
| $orderby  | texto   | $orderby  | Propriedades para ordenação das entidades. e.g. Nome asc, Idade desc.                                               |
| $skip     | inteiro | $skip     | Índice (maior ou igual a zero) da primeira entidade que será retornada                                                |
| $top      | inteiro | $top      | Número máximo (maior que zero) de entidades que serão retornadas                                                      |

## Resultado

| Nome                     | Tipo    | Título                                       | Descrição                                                                                                                                                                                                            |
|--------------------------|---------|----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| trimestre                | inteiro | Trimestre                                    | Data-base de referência (AAAAT)                                                                                                                                                                                      |
| funcaoCartao             | texto   | Função                                       | Em relação ao cartão de pagamento, trata-se da especificação da função nele disponibilizada. Na transação é a forma de pagamento escolhida pelo portador e aceita pelo estabelecimento credenciado.           |
| bandeira                 | texto   | Bandeira                                     | É a detentora de todos os direitos e deveres da utilização da marca estampada no cartão, inclusive às bandeiras pertencentes aos emissores.                                                                         |
| produto                  | texto   | Produto                                      | Categoria atribuída a um cartão de pagamento, sob uma certa denominação, que lhe agrega um conjunto de vantagens, diferenciando-o de acordo com o perfil do portador.                                           |
| modalidade               | texto   | Modalidade                                   | Define se o cartão de crédito é emitido em parceria com comerciante/entidade ou não.                                                                                                                                |
| tarifaAnuidadeMedia      | decimal | Tarifa de anuidade média                     | Média simples das tarifas de anuidade praticadas pelo emissor em cada trimestre, para cada combinação de bandeira/produto (receita trimestral das tarifas de anuidade dividida exclusivamente pelo número de cartões que tiveram incidência de cobrança – mesmo que nula – da tarifa no trimestre). No caso de parcelamento, é considerada a receita integral das tarifas de anuidade, cujo vencimento da primeira parcela recaia no trimestre de referência da informação. |
| qtdPontosAcumulados      | decimal | Estoque de pontos creditados nas contas dos portadores | É o estoque de pontos acumulados pelos portadores de cartões, no âmbito dos programas de recompensa, no final do trimestre de referência. Corresponde à soma dos pontos adquiridos no decorrer do trimestre ao estoque de pontos no seu início, deduzindo-se os pontos transferidos para os programas de fidelidade/recompensa de terceiros e aqueles expirados no trimestre. |
| qtdPontosAdquiridos      | decimal | Quantidade de pontos adquiridos no âmbito dos programas de recompensa do emissor | Somatório da quantidade de pontos creditados nas contas dos portadores no decorrer do trimestre de referência.                                                                                                       |
| qtdPontosConvertidos     | decimal | Quantidade de pontos convertidos (transferidos) | Somatório da quantidade de pontos transferidos para os programas de fidelidade/recompensa no decorrer do trimestre de referência.                                                                                    |
| qtdPontosExpirados       | decimal | Quantidade de pontos expirados               | Somatório da quantidade de pontos expirados no decorrer do trimestre de referência, no âmbito dos programas de recompensa do emissor.                                                                              |
| valorGastoProgramaRecompra | decimal | Gasto efetivo do emissor com programas de recompensa | Valor total gasto no trimestre, referente aos repasses para pagamento pela aquisição de bens ou utilização de serviços pelos portadores de cartões, no âmbito dos programas de fidelidade/recompensa de terceiros. |