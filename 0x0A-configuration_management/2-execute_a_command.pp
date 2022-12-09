# Create's a manifest, that kills a process with Puppet

exec { 'pkill':
  command => 'pkill killmenow',
  path    => '/usr/local/bin/:/bin/'
}
