# this file will increase the ULIMIT so taht workers can handel more open files.
service { 'nginx':
  ensure => 'running',
  enable => true,
}

file { '/etc/default/nginx':
  ensure => present,
} -> exec { 'increase ULIMIT':
  notify  => Service['nginx'], # set up a relationship
  path    => '/bin/',
  command => "sed -i 's/15/1024/g' /etc/default/nginx"
}
