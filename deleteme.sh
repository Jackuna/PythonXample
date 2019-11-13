mysql -ucyberkeeda -p{MysqlPass} mysql -e "update mytbl set f_title='{$APVmode}' where id=1;select f_title from mytbl; select f_title from mytbl;"
