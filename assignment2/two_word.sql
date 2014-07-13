select count(*) from(
SELECT docid,count(*) as total FROM  Frequency where term=='world' or term=='transactions' group by docid
having total >=2);
