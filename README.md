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
$ cat /etc/yum.repos.d/fedora.repo | head -n 19
[fedora]
name=Fedora $releasever - $basearch
#baseurl=http://download.example/pub/fedora/linux/releases/$releasever/Everything/$basearch/os/
metalink=https://mirrors.fedoraproject.org/metalink?repo=fedora-$releasever&arch=$basearch
enabled=1
countme=1
metadata_expire=7d
repo_gpgcheck=0
type=rpm
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-fedora-$releasever-$basearch
skip_if_unavailable=False

[fedora-debuginfo]
name=Fedora $releasever - $basearch - Debug
#baseurl=http://download.example/pub/fedora/linux/releases/$releasever/Everything/$basearch/debug/tree/
metalink=https://mirrors.fedoraproject.org/metalink?repo=fedora-debug-$releasever&arch=$basearch
enabled=0
metadata_expire=7d
~~~

~~~
$ cat /etc/yum.repos.d/fedora.repo | python inilex.py | head -n 49
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
(EQUALS,'=',8,284)
(STRING,'0',8,285)
(STRING,'type',9,287)
(EQUALS,'=',9,291)
(STRING,'rpm',9,292)
(STRING,'gpgcheck',10,296)
(EQUALS,'=',10,304)
(STRING,'1',10,305)
(STRING,'gpgkey',11,307)
(EQUALS,'=',11,313)
(STRING,'file:///etc/pki/rpm-gpg/RPM-GPG-KEY-fedora-$releasever-$basearch',11,314)
(STRING,'skip_if_unavailable',12,379)
(EQUALS,'=',12,398)
(STRING,'False',12,399)
(LBRACKET,'[',14,406)
(STRING,'fedora-debuginfo',14,407)
(RBRACKET,']',14,423)
(STRING,'name',15,425)
(EQUALS,'=',15,429)
(STRING,'Fedora $releasever - $basearch - Debug',15,430)
(STRING,'metalink',17,573)
(EQUALS,'=',17,581)
(STRING,'https://mirrors.fedoraproject.org/metalink?repo=fedora-debug-$releasever&arch=$basearch',17,582)
(STRING,'enabled',18,670)
(EQUALS,'=',18,677)
(STRING,'0',18,678)
(STRING,'metadata_expire',19,680)
(EQUALS,'=',19,695)
(STRING,'7d',19,696)
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
