CREATE DATABASE if NOT EXISTS  tp_poo_vale;

USE tp_poo_vale;

CREATE TABLE Cliente(
id INT PRIMARY KEY,
Nombre VARCHAR(50),
Apellido VARCHAR(50),
DNI INT(8),
Email VARCHAR(100),
Direccion VARCHAR(100)
);

CREATE TABLE Producto(
id INT PRIMARY KEY,
Nombre VARCHAR(50),
Descripcion VARCHAR(50),
Precio DOUBLE
);

CREATE TABLE Compra(
id INT PRIMARY KEY,
id_cliente INT,
id_producto INT,
FOREIGN KEY (id_cliente)REFERENCES cliente(id),
FOREIGN KEY (id_producto) REFERENCES producto(id)
);



CREATE TABLE if NOT EXISTS Factura(
id INT PRIMARY KEY,
unidad INT(10),
fecha DATE,
id_compra INT,
FOREIGN KEY (id_compra) REFERENCES compra(id)
);




