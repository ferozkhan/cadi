import os
from fabric.api import *

env.project_name = 'cadi'
env.hosts = os.environ.get('server_ip').split(',')
env.user = os.environ.get('user')
env.key_filename = os.environ.get('keys').split(',')
env.path = '/var/www/cadi'


def check(service='nginx'):
	run('/etc/init.d/%s status' % service)


def setup():
	sudo('aptitude install -y python-setuptools')
	sudo('aptitude install -y nginx')
	sudo('easy_install pip')
	sudo('mkdir -p /var/log/uwsgi/')	
	

def prepare_and_upload_tar_from_git():
	local('git archive --format=tar master | gzip > release.tar.gz')
	sudo('mkdir -p %(path)s' % env, pty=True)
	sudo('chown -R %(user)s %(path)s' % env)
	put('release.tar.gz', '%(path)s/' % env)
	run('cd %(path)s && tar -zxvf release.tar.gz' % env, pty=True)
	local('rm -f release.tar.gz')


def deploy():
	setup()
	prepare_and_upload_tar_from_git()
	sudo('pip install -r %(path)s/requirements.txt' % env)
	sudo('cp %(path)s/conf/cadi-nginx /etc/nginx/sites-enabled/' % env)
	sudo('/etc/init.d/nginx restart')
