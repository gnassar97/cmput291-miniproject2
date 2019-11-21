awk -F':' '{print $1"\n"$2}' < emails.txt | 
sed 's/\\/ /g' | db_load -T -c duplicates=1 -t btree ./index/em.idx 
