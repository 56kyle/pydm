
import re
import pydm.preprocessor as preprocessor


class Define(preprocessor.Preprocessor):
    keyword = '#define'
    re_syntax = re.compile(r'^#define\s+(\w+)\s+(.*)$')

class If(preprocessor.Preprocessor):
    keyword = '#if'
    re_syntax = re.compile(r'^#if\s+(?P<condition>.*)')
    re_start = re.compile(r'^#if\s+(?P<condition>.*)$')
    re_end = re.compile(r'^#endif$')

class Elif(preprocessor.Preprocessor):
    keyword = '#elif'
    re_syntax = re.compile(r'^#elif\s+(?P<condition>.*)$')
    re_start = re.compile(r'^#elif\s+(?P<condition>.*)$')
    re_end = re.compile(r'^#e.*$')

class Ifdef(preprocessor.Preprocessor):
    keyword = '#ifdef'
    re_syntax = re.compile(r'^#ifdef\s+(?P<condition>.*)$')
    re_start = re.compile(r'^#ifdef\s+(?P<condition>.*)$')
    re_end = re.compile(r'^#endif$')

class Ifndef(preprocessor.Preprocessor):
    keyword = '#ifndef'
    re_syntax = re.compile(r'^#ifndef\s+(?P<condition>.*)$')
    re_start = re.compile(r'^#ifndef\s+(?P<condition>.*)$')
    re_end = re.compile(r'^#endif$')

class Else(preprocessor.Preprocessor):
    keyword = '#else'
    re_syntax = re.compile(r'^#else$')
    re_start = re.compile(r'^#else$')
    re_end = re.compile(r'^#endif$')

class Include(preprocessor.Preprocessor):
    keyword = '#include'
    re_syntax = re.compile(r'^#include\s+(?P<filename>.*)$')

class Error(preprocessor.Preprocessor):
    keyword = '#error'
    re_syntax = re.compile(r'^#error\s+(?P<message>.*)$')

class Warn(preprocessor.Preprocessor):
    keyword = '#warn'
    re_syntax = re.compile(r'^#warn\s+(?P<message>.*)$')

