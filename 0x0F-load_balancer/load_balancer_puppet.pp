#!/usr/bin/env puppet
# Setup custom HTTP header in Nginx configuration

exec { 'update system':
  command => '/usr/bin/apt-get update',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

exec { 'redirect_me':
  command  => 'sed -i "24i\        rewrite ^/redirect_me https://th3-gr00t.tk/ permanent;" /etc/nginx/sites-available/default',
  creates  => '/etc/nginx/sites-available/default',
  require  => File['/etc/nginx/sites-available/default'],
  notify   => Service['nginx'],
}

exec { 'HTTP header':
  command  => 'sed -i "25i\        add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
  creates  => '/etc/nginx/sites-available/default',
  require  => File['/etc/nginx/sites-available/default'],
  notify   => Service['nginx'],
}

service { 'nginx':
  ensure => 'running',
  enable => true,
}

