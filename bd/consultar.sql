SELECT 
	cl.nome AS Cliente,
	cr.modelo AS Carro,
	cr.preco AS Preço,
	v.data_venda AS Data_Venda
FROM 
	Venda AS v
INNER JOIN Cliente AS cl ON v.id_cliente = cl.id_cliente
INNER JOIN Carro AS cr ON v.id_carro = cr.id_carro;

SELECT 
	cl.nome AS Cliente,
	cr.modelo AS Carro,
	cr.preco AS Preço,
	v.data_venda AS Data_Venda
FROM 
	Venda AS v, Cliente as cl, Carro AS cr
WHERE v.id_cliente = cl.id_cliente AND v.id_carro = cr.id_carro;
