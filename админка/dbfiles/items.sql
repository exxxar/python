CREATE TABLE items (
                 id INT NOT NULL AUTO_INCREMENT,
                 code VARCHAR(13) NOT NULL,
                 name VARCHAR(255) NOT NULL,
                 em VARCHAR(25) NOT NULL,
                 count INT NOT NULL,
                 price DOUBLE NOT NULL,
                 typeId INT NOT NULL,
                 PRIMARY KEY (id)
                ) ENGINE=MyISAM DEFAULT CHARSET=cp1251
