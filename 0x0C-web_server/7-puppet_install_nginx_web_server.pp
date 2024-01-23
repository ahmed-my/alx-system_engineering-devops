# install and configure nginx using Puppet
package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure  => running,
  enable  => true,
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {
      listen 80;

      location / {
        return 200 'Hello World!';
      }

      location /redirect_me {
        return 301 http://www.example.com;
      }
  }",
  notify  => Service['nginx'],
}

