select count(c) from
(select term as c from Frequency where docid=='10398_txt_earn' and count==1
union 
select term as c from Frequency where docid=='925_txt_trade' and count==1);

