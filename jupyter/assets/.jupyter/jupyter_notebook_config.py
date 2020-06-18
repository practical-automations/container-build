import os
c.NotebookApp.ip = '*'
c.NotebookApp.allow_remote_access = True
c.KernelManager.shutdown_wait_time = 10.0
c.FileContentsManager.delete_to_trash = False
c.NotebookApp.quit_button = False
c.NotebookApp.terminado_settings = {'shell_command': ['/bin/bash']}
c.NotebookApp.notebook_dir = '/jupyter'

if 'JPL_PASSWORD' in os.environ:
    from notebook.auth import passwd
    c.NotebookApp.password = passwd(os.environ['JPL_PASSWORD'])
    del os.environ['JPL_PASSWORD']
