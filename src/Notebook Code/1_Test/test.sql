CREATE OR REPLACE TEMP VIEW numbers AS
SELECT explode(array(1,2,3,4,5)) AS n;
