CREATE TABLE orders
(
    orderid INT PRIMARY KEY,
    customerid INT,
    ordertotal INT
);

INSERT INTO orders VALUES(1,1,1000);
INSERT INTO orders VALUES(2,1,1000);
INSERT INTO orders VALUES(3,1,1000);
INSERT INTO orders VALUES(4,2,2000);
INSERT INTO orders VALUES(5,2,2000);

SELECT customerid, SUM(ordertotal)
FROM orders
GROUP BY customerid; -- RIGHT

SELECT orderid, customerid, SUM(ordertotal)
FROM orders
GROUP BY customerid; -- WRONG
-- customerid la duy nhat, nen khi GROUP BY bang customerid se bi sai
-- Van chay duoc, khong error nhung ket qua tra ve se bi sai

SET SESSION sql_mode='ONLY_FULL_GROUP_BY';
SELECT orderid, customerid, SUM(ordertotal)
FROM orders
GROUP BY customerid; -- ERROR
-- Neu dat sql_mode='ONLY_FULL_GROUP_BY' thi phai GROUP BY toan bo column
-- Tat ca nhung cot nao khong phai aggregate function nhu SUM() hay AVG() deu phai co trong GROUP BY
-- Phai GROUP BY customerid, orderid moi chay duoc
-- SQLServer thuong yeu cau nhu the nay

SET SESSION sql_mode='';
-- Dung lenh nay de tat che do 'ONLY_FULL_GROUP_BY'
