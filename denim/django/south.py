# -*- encoding:utf8 -*-
from fabric import colors
from fabric.api import task
from denim import django


@task
def show_migrations(revision=None, non_applied_only=False):
    """
    Print report of migrations.

    :param revision: revision of the application to run show migrations from.
    :param non_applied_only: only show un-applied migrations.

    """
    if non_applied_only:
        result = django.manage('migrate', args='--list | grep -v "(\*)"', revision=revision, use_sudo=False)
        if result.find('( )') != -1:
            print(colors.red('*'*34))
            print(colors.red('* Migrations need to be applied! *'))
            print(colors.red('*'*34))
        else:
            print(colors.green('Migrations up to date.'))
    else:
        django.manage('migrate', '--list', revision=revision, use_sudo=False)


@task
def migrate(revision=None):
    """
    Apply migrations.

    :param revision: revision of the application to run show migrations from.

    """
    django.manage('migrate', revision=revision, use_sudo=False)
