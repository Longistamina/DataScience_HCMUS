-- vi du ve giao tac (transaction)
/*
- ACID
- transaction la mot don vi cong viec (work unit)
- thuc hien mot cong viec bao gom nhieu buoc (nhieu lenh)
- cong viec goi la thanh cong khi tat ca cac buoc thanh cong
- neu nhu co it nhat 1 buoc that bai --> cong viec that bai
- cai dat transaction:
	- neu nhu cac lenh (trong transaction) thanh cong --> commit (save)
    - neu co it nhat 1 lenh that bai (trong transaction) --> rollback (undo)
*/
-- bang thu nghiem transaction
-- chay tung cau lenh mot de hieu

CREATE TABLE test_transaction
SELECT * FROM employees;

ALTER TABLE test_transaction ENGINE=INNODB; -- use InnoDB engine for transaction

-- don't have to run these-------------------v
SELECT TABLE_NAME,                           I
       ENGINE                                I
FROM   information_schema.TABLES             I
WHERE  TABLE_SCHEMA = 'humanresources';      I
-- don't have to run these-------------------^

START TRANSACTION; -- Explicit Transaction <> Implicit Transaction
SELECT COUNT(*) AS 'Before delete' FROM test_transaction; -- Count before delete
DELETE FROM test_transaction;
SELECT COUNT(*) AS 'After delete' FROM test_transaction;  -- Count after delete
ROLLBACK;
SELECT COUNT(*) AS 'After rollback' FROM test_transaction; -- Rollback to restore previous status (before delete), then count

START TRANSACTION;
SELECT COUNT(*) AS 'Before delete' FROM test_transaction;
DELETE FROM test_transaction;
SELECT COUNT(*) AS 'After delete' FROM test_transaction;
COMMIT;
SELECT COUNT(*) AS 'After commit' FROM test_transaction;  
-- After commit, the changes have been saved so now count = 0 = after delete

DROP TABLE test_transaction;