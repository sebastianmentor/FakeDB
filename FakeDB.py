import random
import mysql.connector
from mysql.connector import Error
from faker import Faker
from productsProvider import RandomProduct, Product, PRODUKT_TYPE, PRODUCT_NAME_AND_TYPE

Faker.seed(33422)

MAX_NUMBER_OF_CUSTOMERS = 100000
MAX_NUMBER_OF_ORDERS = 5*MAX_NUMBER_OF_CUSTOMERS
HOST = 'localhost'
DATABASE_NAME = 'TestFake'
USER = 'root'
PWD = 'password'



fake = Faker('sv_SE')

create_table_customer = """
CREATE TABLE `Customer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `last_name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `zipcode` int(5) NOT NULL,
  `city` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `street` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `ssn` varchar(12) COLLATE utf8_unicode_ci NOT NULL,
  `added` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
"""

create_table_product_type = """
CREATE TABLE `ProductType` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
"""
create_table_product = """
CREATE TABLE `Product` (
  `productName` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `productType` int NOT NULL, 
   PRIMARY KEY (`productName`),
   FOREIGN KEY (`productType`) REFERENCES ProductType(`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
"""
create_table_order = """
CREATE TABLE `Order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customer` INT NOT NULL,
  `orderDate` Date NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`customer`) REFERENCES Customer(`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
"""

create_table_order_details = """
CREATE TABLE `OrderDetails` (
  `id` int(12) NOT NULL AUTO_INCREMENT,
  `order` int NOT NULL,
  `product` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `antal` int NOT NULL,
  `price` int NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`order`) REFERENCES `Order`(`id`),
  FOREIGN KEY (`product`) REFERENCES Product(`productName`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
"""


try:
  conn = mysql.connector.connect(host=HOST, database = DATABASE_NAME,
                                   user=USER, password=PWD)

  if conn.is_connected():
    cursor = conn.cursor()

    try:
        cursor.execute(create_table_customer)
        cursor.execute(create_table_product_type)
        cursor.execute(create_table_product)
        cursor.execute(create_table_order)
        cursor.execute(create_table_order_details)
        print("Table created")
    except Exception as e:
        print("Error creating table", e)

    # Create all customers
    for i in range(MAX_NUMBER_OF_CUSTOMERS):
        address = fake.address().strip().split('\n')
        zipcode, county= address[1].split() 

        ssn = fake.ssn()
        email = fake.email()
        first_name = fake.first_name()
        last_name = fake.last_name()
        added = fake.date()
        row = (first_name, last_name, email, zipcode, county, address[0], ssn, added)
        
        cursor.execute(' \
            INSERT INTO `Customer` (first_name, last_name, email, zipcode, city, street, ssn, added) \
            VALUES ("%s", "%s", "%s", %s, "%s", "%s", "%s", "%s"); \
            ' % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            )

        if i % 100 == 0:
            print("Person iteration %s" % i)
            conn.commit()
    
    # Create productType
    for prod_name, prod_id in PRODUKT_TYPE.items():
        cursor.execute(
            f'INSERT INTO `ProductType` (id, type) VALUES ("{prod_id}","{prod_name}")' 
            )
    conn.commit()
    print('ProductType Created')

    # Create products
    for prod_name,prod_type in PRODUCT_NAME_AND_TYPE.items():
       cursor.execute(
          f'INSERT INTO `Product` (productName, productType)\
            VALUES ("{prod_name}", "{PRODUKT_TYPE[prod_type]}");'
       )
    conn.commit()
    print('Products Created')
    
    # Create orders
    for order_number in range(1, MAX_NUMBER_OF_ORDERS + 1):
        
        customer_id = random.randint(1, MAX_NUMBER_OF_CUSTOMERS)
        cursor.execute(
            f'INSERT INTO `Order` (customer, orderDate) VALUES ("{customer_id}", "{fake.date()}");'
            )
        
        if order_number % 100 == 0:
          print(f'Order iteration {order_number}')
          conn.commit()


    # Create orderDetails
    for order_number in range(1, MAX_NUMBER_OF_ORDERS + 1):

      number_of_ordered_items = int(random.gauss(mu=3, sigma=1))
      if number_of_ordered_items < 1:
          number_of_ordered_items = 1

      for _ in range(number_of_ordered_items):
        p:Product = RandomProduct()

        cursor.execute(
           f'INSERT INTO `OrderDetails` (`order`, product, antal, price)\
            VALUES ("{order_number}","{p.namn()}","{p.antal()}","{p.pris()}");'
           )
      
      conn.commit()

      if order_number %100==0:
         print(f'OrderDetails iteration {order_number}')
        




except Error as e :
    print ("error", e)
    pass
except Exception as e:
    print ("Unknown error %s", e)
finally:
    #closing database connection.
    if(conn and conn.is_connected()):
        conn.commit()
        cursor.close()
        conn.close()