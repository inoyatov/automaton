from __future__ import absolute_import, unicode_literals

import os
from celery import Celery

from git import cmd, Repo, InvalidGitRepositoryError

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'automaton.settings')

app = Celery('automaton')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def pull(self, path):
    try:
        Repo(path)
        cmd.Git(path).pull()
    except InvalidGitRepositoryError as e:
        return 'not git repository'
    except Exception as e:
        return str(e)
    return 'updated successuflly'
