# Aplicativo de Oficina com SQLite e Python

Este projeto é um aplicativo simples em Python que utiliza o banco de dados SQLite para gerenciar informações de uma oficina. O aplicativo possui um menu em terminal que oferece diversas funcionalidades, incluindo recuperações simples com SELECT Statement, filtros com WHERE Statement, criação de atributos derivados, ordenação dos dados com ORDER BY, condições de filtros aos grupos com HAVING Statement e junções entre tabelas para fornecer uma perspectiva mais complexa dos dados.

## Pré-requisitos

- Python 3.x
- Biblioteca SQLite3 (normalmente já inclusa na instalação padrão do Python)

## Instalação

1. Clone ou faça o download deste repositório.

2. Certifique-se de ter o Python instalado em sua máquina. Caso precise instalá-lo, visite o site oficial do Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)

## Como utilizar

1. Navegue para o diretório onde o projeto foi clonado ou baixado.

2. Abra um terminal ou prompt de comando na pasta do projeto.

3. Execute o aplicativo usando o seguinte comando:


4. O menu do aplicativo será exibido no terminal, permitindo que você escolha entre as diferentes funcionalidades disponíveis.

5. Siga as instruções fornecidas pelo aplicativo para inserir dados de clientes e serviços, realizar consultas e explorar as funcionalidades disponíveis.

## Funcionalidades disponíveis

1. **Inserir cliente**: Permite inserir informações de um novo cliente na base de dados.

2. **Inserir serviço**: Permite inserir informações de um novo serviço associado a um cliente existente.

3. **Recuperação simples (SELECT)**: Recupera e exibe informações de todos os clientes armazenados no banco de dados.

4. **Filtro por veículo (WHERE)**: Recupera e exibe informações dos clientes que possuem um determinado veículo.

5. **Atributo derivado**: Exibe uma recuperação de dados que inclui um atributo derivado (valor_total + valor dos serviços) para cada cliente.

6. **Ordenação por valor total (ORDER BY)**: Recupera e exibe informações de todos os clientes, ordenados pelo valor total de serviços realizados, do maior para o menor.

7. **Filtro por valor mínimo de serviços (HAVING)**: Recupera e exibe informações dos clientes que têm um valor total de serviços igual ou maior que um valor específico fornecido pelo usuário.

8. **Junção entre tabelas**: Recupera e exibe informações dos clientes, incluindo a contagem total de serviços associados a cada cliente.

## Notas importantes

- Este aplicativo é uma implementação simples e básica, não incluindo recursos avançados de tratamento de erros, validações ou segurança. É recomendado apenas para fins educacionais ou para iniciar projetos mais complexos.

- O banco de dados SQLite utilizado pelo aplicativo será criado automaticamente na pasta do projeto quando o aplicativo for executado pela primeira vez.

- Sinta-se à vontade para estender este projeto adicionando mais funcionalidades e melhorias conforme necessário.

## Contribuindo

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhoria, fique à vontade para abrir uma "issue" ou enviar um "pull request" neste repositório.

## Licença

Este projeto está licenciado sob a licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.
