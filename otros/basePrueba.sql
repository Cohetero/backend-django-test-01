CREATE TABLE extra_fields
(
    id          serial PRIMARY KEY,
    brand       VARCHAR(255),
    package     VARCHAR(255),
    price VARCHAR(255)
);

CREATE TABLE catalog_products
(
    id             serial PRIMARY KEY,
    name           VARCHAR(255),
    description    VARCHAR(255),
    extra_field_id INT,
    FOREIGN KEY (extra_field_id)
        REFERENCES extra_fields (id)
);
  
CREATE TABLE products_blacklist
(
    id         serial PRIMARY KEY,
    product_id INT,
    FOREIGN KEY (product_id)
        REFERENCES catalog_products (id)
);

-- Insert Extra Fields
INSERT INTO extra_fields (brand, package, price) VALUES ('vegetalistos', 'bolsa', '45.0');
INSERT INTO extra_fields (brand, package, price) VALUES ('pepsico', 'botella', '120.0');
INSERT INTO extra_fields (brand, package, price) VALUES ('vegetalistos', 'bolsa', '15.0');
INSERT INTO extra_fields (brand, package, price) VALUES ('vegetalistos', 'botella', '5.0');

-- Insert Products
INSERT INTO catalog_products (name, description, extra_field_id) VALUES ('jicama 45gr', '', 1);
INSERT INTO catalog_products (name, description, extra_field_id) VALUES ('Sabritas Medianas', '145 gr', 2);

INSERT INTO catalog_products (name, description) VALUES ('Mirinda', 'sabor naranja');

INSERT INTO catalog_products (name, description, extra_field_id) VALUES ('Lechuga', 'Romana', 3);
INSERT INTO catalog_products (name, description, extra_field_id) VALUES ('jugo de mora', '1 litro', 4);

-- Blacklist
INSERT INTO products_blacklist (product_id) VALUES (1);
INSERT INTO products_blacklist (product_id) VALUES (5);

SELECT *
FROM extra_fields
ORDER BY CAST(price AS DECIMAL ) DESC;

-- Solo traer el segundo
SELECT *
FROM extra_fields
ORDER BY CAST(price AS DECIMAL ) DESC
LIMIT 1 OFFSET 1;
