from fabric.api import prefix
import utils
import paths

__all__ = ('create', 'activate')


def create(path=None, use_sudo=True, user=None):
    """
    Create a virtual environment.

    :path: location to create virtual env; default is deploy path.
    :use_sudo: run this command with sudo; default is True.
    :user: when using sudo run as this user; default is None (or root).

    """
    if not path:
        path = paths.get_deploy_path()
    utils.run_as('virtualenv %s' % path, use_sudo=use_sudo, user=user)

def activate(path=None):
    """
    Context manager to enable a virtual env.

    :path: location of the virtual env to activate; default is deploy path.

    """
    if not path:
        path = paths.get_deploy_path()
    return prefix('source %s' % paths.join_paths(path, 'bin/activate'))
