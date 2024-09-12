
--duckdb
create table ducks as select 3 as age, 'mandarin' as breed;
show tables;
from ducks;
INSTALL httpfs; 
SELECT * FROM read_csv_auto('netflix_daily_top_10.csv) limit 3;

CREATE TABLE netflix_daily_top_10 AS FROM read_csv_auto('C:\Users\jbcoo\Downloads\netflix_daily_top_10.csv');
COPY netflix_daily_top_10 TO 'C:\Users\jbcoo\Downloads\output.csv' (HEADER, DELIMITER ',');