#!/usr/bin/env python

from pathlib import Path
import argparse
import os
import re

# set's REPO to whatever the repository is named
REPO = Path(__file__).parents[1].absolute().name
REPO_PATH = Path(__file__).parents[1].absolute().as_posix()
# ------------------------------------------------------------------------------

'''
A CLI for developing and deploying a service deeply integrated with this
repository's structure. Written to be python version agnostic.
'''


def get_info():
    '''
    Returns:
        str: System args and environment as a dict.
    '''
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description='A CLI for developing and deploying {repo} containers.'.format(repo=REPO),
        usage='\n\tpython cli.py COMMAND [-a --args]=ARGS [-h --help]'
    )

    parser.add_argument('command',
                        metavar='command',
                        type=str,
                        nargs=1,
                        action='store',
                        help='''Command to run in {repo} service.

    bash         - Run BASH session inside {repo} container
    container    - Display the Docker container id for {repo} service
    destroy      - Shutdown {repo} service and destroy its Docker image
    image        - Display the Docker image id for {repo} service
    publish      - Publish repository to python package index.
    python       - Run python interpreter session inside {repo} container
    remove       - Remove {repo} service Docker image
    restart      - Restart {repo} service
    start        - Start {repo} service
    stop         - Stop {repo} service
    tox          - Run tox tests on {repo}
'''.format(repo=REPO))

    parser.add_argument(
        '-a',
        '--args',
        metavar='args',
        type=str,
        nargs='+',
        action='store',
        help='Additional arguments to be passed. Be sure to include hyphen prefixes.'
    )

    temp = parser.parse_args()
    mode = temp.command[0]
    args = []
    if temp.args is not None:
        args = re.split(' +', temp.args[0])

    compose_path = Path(REPO_PATH, 'docker/docker-compose.yml')
    compose_path = compose_path.as_posix()

    user = '{}:{}'.format(os.geteuid(), os.getegid())

    info = dict(
        args=args,
        mode=mode,
        compose_path=compose_path,
        user=user
    )
    return info


# COMMANDS----------------------------------------------------------------------
def get_bash_command(info):
    '''
    Opens a bash session inside a running container.

    Args:
        info (dict): Info dictionary.

    Returns:
        str: Command.
    '''
    cmd = "{exec} bash".format(exec=get_docker_exec_command(info))
    return cmd


def get_container_id_command():
    '''
    Gets current container id.

    Returns:
        str: Command.
    '''
    cmd = 'docker ps | grep {repo} '.format(repo=REPO)
    cmd += "| head -n 1 | awk '{print $1}'"
    return cmd


def get_coverage_command(info):
    '''
    Runs pytest coverage.

    Args:
        info (dict): Info dictionary.

    Returns:
        str: Command.
    '''
    cmd = '{exec} mkdir -p /root/{repo}/docs; {test}'
    args = [
        '--cov=/root/{repo}/python',
        '--cov-config=/root/{repo}/docker/pytest.ini',
        '--cov-report=html:/root/{repo}/docs/htmlcov',
    ]
    args = ' '.join(args)
    cmd += ' ' + args

    cmd = cmd.format(
        repo=REPO,
        exec=get_docker_exec_command(info),
        test=get_test_command(info),
    )
    return cmd


def get_image_id_command():
    '''
    Gets currently built image id.

    Returns:
        str: Command.
    '''
    cmd = 'docker image ls | grep {repo} '.format(repo=REPO)
    cmd += "| head -n 1 | awk '{print $3}'"
    return cmd


def get_publish_command(info):
    '''
    Publish repository to python package index.

    Args:
        info (dict): Info dictionary.

    Returns:
        str: Command.
    '''
    cmd = '{exec} bash -c "'

    cmd += 'rm -rf /tmp/{repo}; '
    cmd += 'rm -rf /tmp/deps; '
    cmd += 'cp -r /root/{repo}/python /tmp/{repo}; '
    cmd += 'cp /root/{repo}/README.md /tmp/{repo}/README.md; '
    cmd += 'cp /root/{repo}/LICENSE /tmp/{repo}/LICENSE; '
    cmd += 'cp /root/{repo}/pip/MANIFEST.in /tmp/{repo}/MANIFEST.in; '
    cmd += 'cp /root/{repo}/pip/setup.cfg /tmp/{repo}/; '
    cmd += 'cp /root/{repo}/pip/setup.py /tmp/{repo}/; '
    cmd += 'cp /root/{repo}/pip/version.txt /tmp/{repo}/; '

    cmd += 'mkdir /tmp/{repo}/deps; '
    cmd += 'cp /usr/lib/libblosc.so.1.15.1                               /tmp/{repo}/deps/libblosc.so.1; '
    cmd += 'cp /root/boost_1_68_0/stage/lib/libboost_iostreams.so.1.68.0 /tmp/{repo}/deps/libboost_iostreams.so; '
    cmd += 'cp /root/boost_1_68_0/stage/lib/libboost_numpy37.so.1.68.0   /tmp/{repo}/deps/libboost_numpy37.so; '
    cmd += 'cp /root/boost_1_68_0/stage/lib/libboost_python37.so.1.68.0  /tmp/{repo}/deps/libboost_python37.so; '
    cmd += 'cp /usr/lib/x86_64-linux-gnu/libHalf.so.23.0.0               /tmp/{repo}/deps/libHalf.so.23; '
    cmd += 'cp /usr/lib/x86_64-linux-gnu/libm.so.6                       /tmp/{repo}/deps/libm.so.6; '
    cmd += 'cp /root/openvdb/openvdb/libopenvdb.so.7.1.0                 /tmp/{repo}/deps/libopenvdb.so.7.1; '
    cmd += 'cp /usr/lib/x86_64-linux-gnu/libsnappy.so.1.1.7              /tmp/{repo}/deps/libsnappy.so.1; '
    cmd += 'cp /usr/lib/x86_64-linux-gnu/libtbb.so.2                     /tmp/{repo}/deps/libtbb.so.2; '
    cmd += 'cp /usr/lib/x86_64-linux-gnu/libzstd.so.1.3.8                /tmp/{repo}/deps/libzstd.so.1; '
    cmd += 'cp /root/openvdb/openvdb/pyopenvdb.so                        /tmp/{repo}/deps/pyopenvdb.so; '
    cmd += 'chmod +x /tmp/{repo}/deps/*; '

    cmd += '"; '

    cmd += '''{exec2} python3.7 setup.py bdist_wheel
                --bdist-dir ./deps
                --dist-dir ./dist
                --python-tag cp37
                --plat-name linux_x86_64'''
    # cmd += '{exec2} twine upload dist/*; '
    # cmd += '{exec} rm -rf /tmp/{repo}; '
    cmd = cmd.format(
        repo=REPO,
        exec=get_docker_exec_command(info),
        exec2=get_docker_exec_command(info, '/tmp/' + REPO)
    )
    return cmd


def get_python_command(info):
    '''
    Opens a python interpreter inside a running container.

    Args:
        info (dict): Info dictionary.

    Returns:
        str: Command.
    '''
    cmd = "{exec} python3.7".format(exec=get_docker_exec_command(info))
    return cmd


def get_remove_image_command(info):
    '''
    Removes docker image.

    Args:
        info (dict): Info dictionary.

    Returns:
        str: Command.
    '''
    cmd = 'IMAGE_ID=$({image_command}); '
    cmd += 'docker image rm --force $IMAGE_ID'
    cmd = cmd.format(image_command=get_image_id_command())
    return cmd


def get_start_command(info):
    '''
    Starts up container.

    Args:
        info (dict): Info dictionary.

    Returns:
        str: Fully resolved docker-compose up command.
    '''
    cmd = '{compose} up --detach; cd $CWD'
    cmd = cmd.format(compose=get_docker_compose_command(info))
    return cmd


def get_stop_command(info):
    '''
    Shuts down container.

    Args:
        info (dict): Info dictionary.

    Returns:
        str: Fully resolved docker-compose down command.
    '''
    cmd = '{compose} down; cd $CWD'
    cmd = cmd.format(compose=get_docker_compose_command(info))
    return cmd


def get_tox_command(info):
    '''
    Run tox tests.

    Args:
        info (dict): Info dictionary.

    Returns:
        str: Command.
    '''
    cmd = '{exec} bash -c "'
    cmd += 'rm -rf /tmp/{repo}; '
    cmd += 'cp -R /root/{repo}/python /tmp/{repo}; '
    cmd += 'cp /root/{repo}/README.md /tmp/{repo}/; '
    cmd += 'cp /root/{repo}/LICENSE /tmp/{repo}/; '
    cmd += 'cp /root/{repo}/docker/* /tmp/{repo}/; '
    cmd += 'cp /root/{repo}/pip/* /tmp/{repo}/; '
    cmd += 'cp -R /root/{repo}/resources /tmp; '
    cmd += r"find /tmp/{repo} | grep -E '__pycache__|\.pyc$' | parallel 'rm -rf'; "
    cmd += 'cd /tmp/{repo}; tox'
    cmd += '"'
    cmd = cmd.format(
        repo=REPO,
        exec=get_docker_exec_command(info),
    )
    return cmd


# DOCKER------------------------------------------------------------------------
def get_docker_command(info):
    '''
    Get misc docker command.

    Args:age
        info (dict): Info dictionary.

    Returns:
        str: Command.
    '''
    cmd = 'CWD=$(pwd); '
    cmd += 'cd {repo_path}/docker; '
    cmd += 'REPO_PATH="{repo_path}" CURRENT_USER="{user}" IMAGE="{repo}" '
    cmd += 'docker {mode} {args}; cd $CWD'
    args = ' '.join(info['args'])
    cmd = cmd.format(
        repo=REPO,
        repo_path=REPO_PATH,
        user=info['user'],
        mode=info['mode'],
        args=args
    )
    return cmd


def get_docker_exec_command(info, working_directory=None):
    '''
    Gets docker exec command.

    Args:
        info (dict): Info dictionary.
        working_directory (str, optional): Working directory.

    Returns:
        str: Command.
    '''
    cmd = '{up_command}; '
    cmd += 'CONTAINER_ID=$({container_command}); '
    cmd += 'docker exec --interactive --tty --user \"root:root\" -e {env} '
    if working_directory is not None:
        cmd += '-w {} '.format(working_directory)
    cmd += '$CONTAINER_ID '
    cmd = cmd.format(
        env='PYTHONPATH="${PYTHONPATH}:' + '/root/{}/python" '.format(REPO),
        up_command=get_start_command(info),
        container_command=get_container_id_command(),
    )
    return cmd


def get_docker_compose_command(info):
    '''
    Gets docker-compose command.

    Args:
        info (dict): Info dictionary.

    Returns:
        str: Command.
    '''
    cmd = 'CWD=`pwd`; cd {repo_path}/docker; '
    cmd += 'REPO_PATH="{repo_path}" CURRENT_USER="{user}" IMAGE="{repo}" '
    cmd += 'docker-compose -p {repo} -f {compose_path} '
    cmd = cmd.format(
        repo=REPO,
        repo_path=REPO_PATH,
        user=info['user'],
        compose_path=info['compose_path'],
    )
    return cmd


# MAIN--------------------------------------------------------------------------
def main():
    '''
    Print different commands to stdout depending on mode provided to command.
    '''
    info = get_info()
    mode = info['mode']
    docs = os.path.join('/root', REPO, 'docs')
    cmd = get_docker_command(info)

    if mode == 'bash':
        cmd = get_bash_command(info)

    elif mode == 'container':
        cmd = get_container_id_command()

    elif mode == 'coverage':
        cmd = get_coverage_command(info)
        cmd += '; ' + get_fix_permissions_command(info, docs)

    elif mode == 'destroy':
        cmd = get_stop_command(info)
        cmd += '; ' + get_remove_image_command(info)

    elif mode == 'image':
        cmd = get_image_id_command()

    elif mode == 'publish':
        # cmd = get_tox_command(info)
        # cmd += ' && ' + get_publish_command(info)
        cmd = get_publish_command(info)

    elif mode == 'python':
        cmd = get_python_command(info)

    elif mode == 'remove':
        cmd = get_remove_image_command(info)

    elif mode == 'restart':
        cmd = get_stop_command(info)
        cmd += '; ' + get_start_command(info)

    elif mode == 'start':
        cmd = get_start_command(info)

    elif mode == 'stop':
        cmd = get_stop_command(info)

    elif mode == 'tox':
        cmd = get_tox_command(info)

    # print is used instead of execute because REPO_PATH and CURRENT_USER do not
    # resolve in a subprocess and subprocesses do not give real time stdout.
    # So, running `command up` will give you nothing until the process ends.
    # `eval "[generated command] $@"` resolves all these issues.
    print(cmd)


if __name__ == '__main__':
    main()