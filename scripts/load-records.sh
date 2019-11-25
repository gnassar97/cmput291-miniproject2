awk -F: '{ st = index($0,":");print $1 "\n" substr($0,st+1)}' < ./parsed/recs.txt | 
sed 's/\\/\\\\/g' | db_load -T -c duplicates=1 -t hash ./index/re.idx 
