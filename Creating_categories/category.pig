data = LOAD '/SuperMarket/Correctedlist.csv' AS (Description:chararray);

ddata = DISTINCT data;

data = ORDER ddata BY Description ASC;

jandata = LOAD '/SuperMarket/$DATA' USING PigStorage(',') AS (
IndexNo:int,
BillNo:int,
Date:chararray,
Time:chararray,
Description:chararray,
Quantity:float,
Rate:float,
Amount:float);
dump jandata;
crossed = CROSS jandata, data;

re_crossed = FOREACH crossed GENERATE 
jandata::IndexNo AS IndexNo:int,
jandata::BillNo AS BillNo:int,
jandata::Date AS Date:chararray,
jandata::Time AS Time:chararray,
jandata::Description AS Description:chararray,
jandata::Quantity AS Quantity:float,
jandata::Rate AS Rate:float,
jandata::Amount AS Amount:float,
data::Description AS Desc:chararray;

cut_data = FOREACH re_crossed GENERATE SUBSTRING((chararray)$4, 0, (int)SIZE($8)) AS Description:chararray, IndexNo, BillNo, Date, Time, Quantity, Rate, Amount, $8;

clean_data = FILTER cut_data BY $0 MATCHES $8;
dump clean_data;
joined = JOIN jandata by IndexNo LEFT OUTER, clean_data by IndexNo;

re_joined = FOREACH joined GENERATE
jandata::IndexNo AS IndexNo:int,
jandata::BillNo AS BillNo:int,
jandata::Date AS Date:chararray,
jandata::Time AS Time:chararray,
jandata::Description AS Description:chararray,
jandata::Quantity AS Quantity:float,
jandata::Rate AS Rate:float,
jandata::Amount AS Amount:float,
clean_data::Description AS Desc: chararray;

filtered = FILTER re_joined BY ($8 IS not NULL);
un_filtered = FILTER re_joined BY ($8 IS NULL);
dump filtered;

act_data = FOREACH filtered GENERATE IndexNo, BillNo, Date, Time, $8 AS Description:chararray, Quantity, Rate, Amount;

act_undata = FOREACH un_filtered GENERATE IndexNo, BillNo, Date, Time, Description, Quantity, Rate, Amount;

data_new = UNION act_undata, act_data;

ord_data = ORDER data_new BY IndexNo;
dump ord_data;
STORE ord_data INTO '/SuperMarket/$DEST' USING PigStorage(',');
