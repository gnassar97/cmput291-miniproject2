awk -F ':' '{print $1,$2}' < dates.txt | 
sed 's/\\/\\\\/g' | db_load -T -t btree da.idx 