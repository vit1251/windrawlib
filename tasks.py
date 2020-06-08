
from invoke import task

@task(default=True)
def build(c):
    """ Cross compile
    """
    c.run('meson builddir --cross-file cross_win32.ini', pty=True, echo=True)
    c.run('ninja -C builddir', pty=True, echo=True)