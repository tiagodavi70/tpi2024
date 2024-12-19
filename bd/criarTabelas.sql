CREATE TABLE Cliente (
	id_cliente INT AUTO_INCREMENT PRIMARY KEY,
	nome VARCHAR(100),
	telefone VARCHAR(15)
);
CREATE TABLE Carro (
	id_carro INT AUTO_INCREMENT PRIMARY KEY,
	modelo VARCHAR(100),
	marca VARCHAR(50),
	preco DECIMAL(10, 2)
);

CREATE TABLE Venda (
	id_venda INT AUTO_INCREMENT PRIMARY KEY,
	id_cliente INT,
	id_carro INT,
	data_venda DATE,
	FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
	FOREIGN KEY (id_carro) REFERENCES Carros(id_carro)
);


