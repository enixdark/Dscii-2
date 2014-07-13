select count(*) from (
select docid,sum(count) as total from Frequency group by docid having total > 300);


