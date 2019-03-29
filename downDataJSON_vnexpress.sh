curl -o ./data/vnexpress.json \
'http://localhost:8983/solr/vnexpress/select?q=url%3Ahtml&rows=50000&wt=json&indent=true'
