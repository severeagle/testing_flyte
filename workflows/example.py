import pandas as pd
import json
from flytekit import task, workflow, new_context, current_context
from flytekit.configuration import Config
import os
from flytekit.remote.remote import FlyteRemote

import flytekit.configuration as conf

CURDIR = os.path.dirname(__file__)


@task()
def my_shitty_task()->pd.DataFrame:
    print("HHHOI", current_context().raw_output_prefix)
    return pd.DataFrame([{'a':1,'b':2}, {'a':1,'b':-1}])

@workflow
def wf():
    df = my_shitty_task()

def main():
    wf()

if __name__ == '__main__':
    wf()