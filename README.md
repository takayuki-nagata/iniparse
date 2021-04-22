# Introduction
`iniparse` is a small INI file parser with [PLY](https://ply.readthedocs.io/en/latest/) for lerning usage of a lexical analyzer and parser generator.

- `inilex.py` is a lexer for `iniparse.py`. This can be executed, and reads a given INI file from stdin and prints tokens.
- `iniparse.py` is the parser using the lexer. This reads a given INI file from stdin and generage an python opject representing the INI file, then prints the object as `JSON` format.

The parser is based on a grammar described in <https://metacpan.org/pod/Config::INI>, but the parser inidicates that begening of `#` is also a comment line.

# Usage

~~~
$ cat anyconfigfile.ini | python inilex.py
~~~

~~~
$ cat anyconfigfile.ini | python iniparse.py
~~~

# Example results

~~~
$ cat /etc/yum.repos.d/fedora.repo | python inilex.py | head -n 20
Reading from standard input (type EOF to end):
(LBRACKET,'[',1,0)
(STRING,'fedora',1,1)
(RBRACKET,']',1,7)
(STRING,'name',2,9)
(EQUALS,'=',2,13)
(STRING,'Fedora $releasever - $basearch',2,14)
(STRING,'metalink',4,141)
(EQUALS,'=',4,149)
(STRING,'https://mirrors.fedoraproject.org/metalink?repo=fedora-$releasever&arch=$basearch',4,150)
(STRING,'enabled',5,232)
(EQUALS,'=',5,239)
(STRING,'1',5,240)
(STRING,'countme',6,242)
(EQUALS,'=',6,249)
(STRING,'1',6,250)
(STRING,'metadata_expire',7,252)
(EQUALS,'=',7,267)
(STRING,'7d',7,268)
(STRING,'repo_gpgcheck',8,271)
~~~

~~~
$ cat /etc/yum.repos.d/fedora.repo | python iniparse.py | head -n 50
[
    {
        "fedora": [
            {
                "name": "Fedora $releasever - $basearch"
            },
            {
                "metalink": "https://mirrors.fedoraproject.org/metalink?repo=fedora-$releasever&arch=$basearch"
            },
            {
                "enabled": "1"
            },
            {
                "countme": "1"
            },
            {
                "metadata_expire": "7d"
            },
            {
                "repo_gpgcheck": "0"
            },
            {
                "type": "rpm"
            },
            {
                "gpgcheck": "1"
            },
            {
                "gpgkey": "file:///etc/pki/rpm-gpg/RPM-GPG-KEY-fedora-$releasever-$basearch"
            },
            {
                "skip_if_unavailable": "False"
            }
        ]
    },
    {
        "fedora-debuginfo": [
            {
                "name": "Fedora $releasever - $basearch - Debug"
            },
            {
                "metalink": "https://mirrors.fedoraproject.org/metalink?repo=fedora-debug-$releasever&arch=$basearch"
            },
            {
                "enabled": "0"
            },
            {
                "metadata_expire": "7d"
            },
            {
~~~
