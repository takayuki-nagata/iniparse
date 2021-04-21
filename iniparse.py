import sys
import ply.yacc as yacc
import json

from inilex import tokens


def p_ini_file(p):
    '''ini_file : empty
                | section
                | sections'''
    if type(p[1]) is list:
        p[0] = p[1]
    else:
        p[0] = list()
        p[0].append(p[1])


def p_sections(p):
    '''sections : section section
                | sections section'''
    if type(p[1]) is list:
        p[0] = p[1]
        p[0].append(p[2])
    else:
        p[0] = list()
        p[0].append(p[1])
        p[0].append(p[2])


def p_section(p):
    '''section : section_header
               | section_header value_assignment
               | section_header value_assignments'''
    if p[0] is None:
        p[0] = dict()
    if len(p) == 2:
        p[0][p[1]] = None
    else:
        if type(p[2]) is list:
            p[0][p[1]] = p[2]
        else:
            p[0][p[1]] = list()
            p[0][p[1]].append(p[2])


def p_section_header(p):
    'section_header : LBRACKET section_name RBRACKET'
    p[0] = p[2]


def p_section_name(p):
    'section_name : STRING'
    p[0] = p[1]


def p_value_assignments(p):
    '''value_assignments : value_assignment value_assignment
                        | value_assignments value_assignment'''
    if type(p[1]) is list:
        p[0] = p[1]
        p[0].append(p[2])
    else:
        p[0] = list()
        p[0].append(p[1])
        p[0].append(p[2])


def p_value_assignment(p):
    'value_assignment : property_name EQUALS value'
    if p[0] is None:
        p[0] = dict()
    p[0][p[1]] = p[3]


def p_property_name(p):
    'property_name : STRING'
    p[0] = p[1]


def p_value(p):
    'value : STRING'
    p[0] = p[1]


def p_empty(p):
    'empty :'
    pass


def p_error(p):
    print("Syntax error: '%s'" % p)


parser = yacc.yacc()
repos = parser.parse(sys.stdin.read())
print(json.dumps(repos, indent=4))
