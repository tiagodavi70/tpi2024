# Exercícios

## BD1 - Agência
1. Quantos clientes existem na tabela cliente?
2. Liste os modelos de carros cadastrados na tabela carro.
3. Exiba o nome e telemóvel de todos os clientes.
4. Encontre o carro mais caro vendido (preço máximo) na tabela venda.
5. Liste os nomes dos clientes que compraram carros.
6. Quantos carros foram vendidos em total?
7. Liste os detalhes das vendas realizadas em 2024.
8. Liste os clientes que compraram carros por mais de 20,000 euros.
9. Exiba o modelo e a matrícula dos carros vendidos junto com o nome do cliente.

## BD2 - Biblioteca
1. Quantos livros existem na tabela livro?
2. Liste os títulos dos livros disponíveis.
3. Exiba os nomes e emails de todos os utilizadores.
4. Liste todos os empréstimos realizados em 2024.
5. Quais livros ainda não foram devolvidos?


## BD3 - Loja Online
1. Quantos clientes estão cadastrados?
2. Liste os nomes e categorias dos produtos disponíveis.
3. Exiba os pedidos realizados em Janeiro de 2024.
4. Qual é o produto mais caro cadastrado?
5. Quais produtos foram comprados no pedido com o maior valor total?

## Respostas
``` sql
SELECT COUNT(*) AS total_clientes FROM cliente;

SELECT modelo FROM carro;

SELECT nome, telemovel FROM cliente;

SELECT MAX(preco) AS preco_maximo FROM venda;

SELECT DISTINCT c.nome 
    FROM cliente c, venda v
    WHERE c.id = v.id_cliente;

SELECT COUNT(*) AS total_vendas FROM venda;

SELECT * 
    FROM venda 
    WHERE YEAR(data) = 2024;

SELECT c.nome, v.preco  
    FROM cliente c, venda v  
    WHERE c.id = v.id_cliente AND v.preco > 20000;  

SELECT c.nome, cr.modelo, cr.matricula
    FROM cliente c, carro cr, venda v 
    WHERE c.id = v.id_cliente AND v.id_carro = cr.id;
```

```sql
SELECT COUNT(*) AS total_livros FROM livro;

SELECT titulo FROM livro;

SELECT nome, email FROM utilizador;

SELECT * 
    FROM emprestimo 
    WHERE YEAR(data_emprestimo) = 2024;

SELECT l.titulo, e.data_emprestimo
    FROM livro l, emprestimo e
    WHERE l.isbn = e.isbn AND e.data_devoluicao IS NULL;

SELECT DISTINCT u.nome
    FROM utilizador u, emprestimo e
    WHERE u.id = e.id_utilizador AND MONTH(e.data_emprestimo) = 1 AND YEAR(e.data_emprestimo) = 2024;
```

```sql
SELECT COUNT(*) AS total_clientes FROM cliente;

SELECT nome, categoria FROM produto;

SELECT * 
    FROM pedido 
    WHERE MONTH(data) = 1 AND YEAR(data) = 2024;

SELECT nome, preco 
    FROM produto
    ORDER BY preco DESC
    LIMIT 1;

SELECT pr.nome, pr.preco
FROM produto pr, nota_compra nc
WHERE pr.id = nc.id_produto
AND nc.id_pedido = (
  SELECT id
  FROM pedido
  ORDER BY total DESC
  LIMIT 1
);
```