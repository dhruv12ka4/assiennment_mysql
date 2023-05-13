USE testdb;

CREATE TABLE SalesPeople(Snum INT PRIMARY KEY , Sname VARCHAR(35) NOT NULL UNIQUE , City VARCHAR(35) , Comm INT); 
CREATE TABLE Customers(Cnum INT PRIMARY KEY , Cname VARCHAR(35) , City VARCHAR(35) NOT NULL , Snum INT ,FOREIGN KEY (Snum) REFERENCES SalesPeople(Snum) ); 
CREATE TABLE Orders(Onum INT PRIMARY KEY , Amt FLOAT , Odate DATE ,Cnum INT, Snum INT ,FOREIGN KEY (Cnum) REFERENCES Customers(Cnum),FOREIGN KEY (Snum) REFERENCES SalesPeople(Snum) ); 

INSERT INTO SalesPeople
VALUES
(1001, 'Peel', 'London', .12),
(1002, 'Serres', 'Sanjose', .13),
(1004, 'Motika', 'London', .11),
(1007, 'Rifkin', 'Barcelona', .15),
(1003, 'Axelrod', 'Newyork', .10);

INSERT INTO Customers
VALUES
(2001, 'Hoffman', 'London', 1001),
(2002, 'Giovanni', 'Rome', 1003),
(2003, 'Liu', 'Sanjose', 1002),
(2004, 'Grass', 'Berlin', 1002),
(2006, 'Clemens', 'London', 1001),
(2008, 'Cisneros', 'Sanjose', 1007),
(2007, 'Pereira', 'Rome', 1004);

INSERT INTO Orders
VALUES
(3001, 18.69, '1990-10-3', 2008, 1007),
(3003, 767.19, '1990-10-3', 2001, 1001),
(3002, 1900.10, '1990-10-3', 2007, 1004),
(3005, 5160.45, '1990-10-3', 2003, 1002),
(3006, 1098.16, '1990-10-3', 2008, 1007),
(3009, 1713.23, '1990-10-4', 2002, 1003),
(3007, 75.75, '1990-10-4', 2004, 1002),
(3008, 4273.00, '1990-10-5', 2006, 1001),
(3010, 1309.95, '1990-10-6', 2004, 1002),
(3011, 9891.88, '1990-10-6', 2006, 1001);

#Queries : 

# Count the number of Salesperson whose name begin with ‘a’/’A’.
SELECT Count(*) FROM salespeople WHERE sname LIKE 'a%' or sname LIKE 'A%' ;

# Display all the Salesperson whose all orders worth is more than Rs. 2000.
select * from SalesPeople left join Orders on orders.Snum = salespeople.Snum where Amt > 2000;

# Count the number of Salesperson belonging to Newyork.
SELECT Count(*) FROM salespeople WHERE city = 'Newyork' ;

# Display the number of Salespeople belonging to London and belonging to Paris.
SELECT Count(sname) from salespeople WHERE city='London' and city='Paris';

# Display the number of orders taken by each Salesperson and their date of orders.
SELECT count(*) as No_of_orders,odate,snum from orders group by odate,snum;
