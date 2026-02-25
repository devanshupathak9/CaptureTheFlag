for ep in \
index.php.bak index.php.backup index.php.old index.php.orig index.php.save \
index_backup.php index-old.php index_copy.php index1.php index_new.php \
index.php~ .index.php.swp index.php.tmp index.php.save.1
do
  url="http://61.147.171.103:50546/$ep"
  code=$(curl -m 3 -s -o /dev/null -w "%{http_code}" "$url")
  if [ "$code" = "200" ] || [ "$code" = "403" ]; then
    echo "[+] $url -> $code"
  fi
done