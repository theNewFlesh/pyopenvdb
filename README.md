<p>
    <a href="https://www.linkedin.com/in/alexandergbraun" rel="nofollow noreferrer">
        <img src="https://www.gomezaparicio.com/wp-content/uploads/2012/03/linkedin-logo-1-150x150.png"
             alt="linkedin" width="30px" height="30px"
        >
    </a>
    <a href="https://github.com/theNewFlesh" rel="nofollow noreferrer">
        <img src="https://tadeuzagallo.com/GithubPulse/assets/img/app-icon-github.png"
             alt="github" width="30px" height="30px"
        >
    </a>
    <a href="https://pypi.org/user/the-new-flesh" rel="nofollow noreferrer">
        <img src="https://cdn.iconscout.com/icon/free/png-256/python-2-226051.png"
             alt="pypi" width="30px" height="30px"
        >
    </a>
    <a href="http://vimeo.com/user3965452" rel="nofollow noreferrer">
        <img src="https://cdn1.iconfinder.com/data/icons/somacro___dpi_social_media_icons_by_vervex-dfjq/500/vimeo.png"
             alt="vimeo" width="30px" height="30px"
        >
    </a>
    <a href="http://www.alexgbraun.com" rel="nofollow noreferrer">
        <img src="https://i.ibb.co/fvyMkpM/logo.png"
             alt="alexgbraun" width="30px" height="30px"
        >
    </a>
</p>


# pyopenvdb
OpenVDB for python 3.7
Creates a docker container, which is used to build and package pyopenvdb.
pyopenvdb.dockerfile is for development.
prod_pyopenvdb.dockerfile is for testing installation of pyopenvdb pip package.

# Installation
### Currently only for linux systems with x86_64 architecture
1. pip install pyopenvdb
2. Find parent directory of pyopenvdb.so with `find / | grep -P 'pyopenvdb\.so'`
3. `export LD_LIBRARY_PATH=`[parent directory]
4. Add `import numpy` and `import openvdb` to ipykernel_launcher.py to get
   jupyter lab to import without a pointer error.

# Dev Installation
Unless you intend on building and packing OpenVDB python bindings, you do not
need to follow these instructions.
1. Install [docker](https://docs.docker.com/v17.09/engine/installation)
2. Install [docker-machine](https://docs.docker.com/machine/install-machine) (if running on macOS or Windows)
3. Ensure docker-machine has at least 4 GB of memory allocated to it.
4. `git clone git@github.com:theNewFlesh/pyopenvdb.git`
5. `cd pyopenvdb`
6. `chmod +x bin/pyopenvdb`
7. `bin/pyopenvdb start`

The service should take several minutes to start up.

Run `bin/pyopenvdb --help` for more help on the command line tool.

# Usage
`>>>python3.7`

`>>>import openvdb`
