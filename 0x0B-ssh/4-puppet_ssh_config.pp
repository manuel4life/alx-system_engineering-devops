#How to Config the server to add lines in there!!
exec { 'Append Line IdentityFile':
  command => '/bin/echo -e "IdentityFile ~/.ssh/holberton\nPasswordAuthentication no" >> /etc/ssh/ssh_config',
  path    => '/etc/ssh/ssh_config',
}
