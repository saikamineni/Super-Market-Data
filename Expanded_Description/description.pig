register descmodify.py using jython as cate;

data = LOAD './$SRC' USING PigStorage(',') AS (IndexNo:int, BillNo:int, Date:chararray, Time:chararray,Descriptioninitial:chararray,Quantity:float,Rate:float,Amount:float);

final = FOREACH data GENERATE *, cate.create($4,'./list_descriptions.csv');

dump final;

solution = FOREACH final GENERATE
IndexNo AS IndexNo:int,
BillNo AS BillNo:int,
Date AS Date:chararray,
Time AS Time:chararray,
Description AS Description:chararray,
Quantity AS Quantity:float,
Rate AS Rate:float,
Amount AS Amount:float;


STORE solution INTO './$DEST' USING PigStorage(',');





