from collections import namedtuple


Env = namedtuple('Env', ['name', 'short', 'other'])

ENVIRONMENTS = [
    Env('development', 'dev', []),
    Env('staging', 'staging', ['stage']),
    Env('production', 'prod', []),
    Env('testing', 'test', ['qa'])
]


def get_env(name):
    for env in ENVIRONMENTS:
        if env.name == name or env.short == name or name in env.other:
            return env
    return None


def short_env_name(name):
    env = get_env(name)
    return env.short if env else None