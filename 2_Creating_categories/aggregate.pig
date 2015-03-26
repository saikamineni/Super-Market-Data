register aggregate.py using jython as cate;

data = LOAD './$SRC' USING PigStorage(',') AS (IndexNo:int, BillNo:int, Date:chararray, Time:chararray,Description:chararray,Quantity:float,Rate:float,Amount:float);

final = FOREACH data GENERATE *, cate.create($4,'./categories.txt');

solution = FOREACH final GENERATE
IndexNo AS IndexNo:int,
BillNo AS BillNo:int,
Date AS Date:chararray,
Time AS Time:chararray,
Description AS Description:chararray,
Category AS Category:chararray,
Quantity AS Quantity:float,
Rate AS Rate:float,
Amount AS Amount:float;

dump solution;

STORE final INTO './$DEST' USING PigStorage(',');





