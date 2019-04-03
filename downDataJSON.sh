if [[ "$1" == 'dantri' ]]; then
	ext=htm
fi
if [[ "$1" == 'vnexpress' ]]; then
	ext=html
fi
if [[ "$1" == 'vietnamnet' ]]; then
	ext=html
fi
echo 'ext: '$ext
curl -o data/$1.json \
'http://localhost:8983/solr/'$1'/select?q=url%3A'$ext'&rows=50000&wt=json&indent=true'
