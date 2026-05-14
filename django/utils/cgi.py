from __future__ import unicode_literals

import re


def parse_header(line):
    """
    Parse a Content-Type-like header.

    This is a local replacement for cgi.parse_header, which was removed from
    the Python standard library in Python 3.13.
    """
    parts = _parse_header_params(';' + line)
    key = next(parts)
    params = {}
    for part in parts:
        index = part.find('=')
        if index >= 0:
            name = part[:index].strip().lower()
            value = part[index + 1:].strip()
            if len(value) >= 2 and value[0] == value[-1] == '"':
                value = value[1:-1]
                value = value.replace('\\\\', '\\').replace('\\"', '"')
            params[name] = value
    return key, params


def _parse_header_params(s):
    while s[:1] == ';':
        s = s[1:]
        end = s.find(';')
        while end > 0 and s.count('"', 0, end) % 2:
            end = s.find(';', end + 1)
        if end < 0:
            end = len(s)
        value = s[:end]
        yield value.strip()
        s = s[end:]


def valid_boundary(boundary):
    if isinstance(boundary, bytes):
        pattern = b'^[ -~]{0,200}[!-~]$'
    else:
        pattern = '^[ -~]{0,200}[!-~]$'
    return re.match(pattern, boundary)
