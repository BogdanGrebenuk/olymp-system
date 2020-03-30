import docker


LANGUAGE_INFO = {
    'python': {
        'compiler': {
            'tag': 'python-compiler',
            'dockerfile': '/home/bohdan/projects/olymp-dev/images/python/DockerfileCompiler'
        },
        'runner': {
            'tag': 'python-runner',
            'dockerfile': '/home/bohdan/projects/olymp-dev/images/python/DockerfileRunner'
        }
    }
}

client = docker.from_env()
