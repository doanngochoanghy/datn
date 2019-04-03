curl -o data/$1.json \
'http://localhost:8983/solr/'$1'/select?q=url%3A'$2'&rows=50000&wt=json&indent=true'
