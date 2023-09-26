# Install Nginx
package { 'nginx':
  ensure => installed,
}

# Set Nginx to listen on port 80
file_line { 'nginx_listen':
  path    => '/etc/nginx/sites-available/default',
  line    => '    listen 80 default_server;',
  match   => '^    listen\s*80;',
  replace => true,
}

# Configure error page
file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page\n",
}

# Configure Nginx to serve the redirect_me file
file { '/etc/nginx/sites-available/default':
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    error_page 404 /404.html;
    location = /404.html{
       internal;
    }

    location /redirect_me {
        return 301 http://www.redirectedpage.com/;
    }
}
  ",
  notify  => Service['nginx'],
}

# Test Nginx configuration for syntax errors
exec { 'nginx_test_config':
  command     => '/usr/sbin/nginx',
  logoutput   => true,
  refreshonly => true,
}

# Restart Nginx service if the configuration is valid
service { 'nginx':
  ensure     => running,
  enable     => true,
  subscribe  => File['/etc/nginx/sites-available/default'],
  require    => Exec['nginx_test_config'],
}
# Create index file with "Hello World!" message
file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World!',
}

# Create redirect_me file with redirect information
file { '/var/www/html/redirect_me':
  content => "HTTP/1.1 301 Moved Permanently\r\nLocation: http://www.redirectedpage.com/\r\n\r\n",
}
