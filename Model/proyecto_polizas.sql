CREATE DATABASE IF NOT EXISTS PROYECTO;

USE PROYECTO;

# Tabla Cliente
CREATE TABLE IF NOT EXISTS Cliente (
	id_cliente INT NOT NULL AUTO_INCREMENT,
	nombre VARCHAR(60),
	direccion VARCHAR(255),
	PRIMARY KEY (id_cliente));

# Tabla Vehículo
CREATE TABLE IF NOT EXISTS Vehiculo (
	placas VARCHAR(10) NOT NULL,
	id_factura INT NULL,
	modelo VARCHAR(20),
	marca VARCHAR(20),
	PRIMARY KEY (placas),
	INDEX (placas),
	INDEX (id_factura));

# Tabla Factura
CREATE TABLE IF NOT EXISTS Factura (
	id_factura INT NOT NULL AUTO_INCREMENT,
	placas VARCHAR(10) NOT NULL,
	costo_total FLOAT NOT NULL,
	PRIMARY KEY (id_factura),
	INDEX (id_factura),
	FOREIGN KEY (placas) REFERENCES Vehiculo(placas));


# Tabla Poliza
CREATE TABLE IF NOT EXISTS Poliza (
	id_cliente INT NOT NULL,
	id_factura INT NOT NULL,
	prima_asegurada FLOAT,
	costo_total FLOAT,
	fecha_apertura DATE,
	fecha_vencimiento DATE,
	PRIMARY KEY (id_cliente, id_factura),
	INDEX (id_factura),
	FOREIGN KEY (id_cliente) REFERENCES Cliente (id_cliente),
	FOREIGN KEY (id_factura) REFERENCES Factura(id_factura));
