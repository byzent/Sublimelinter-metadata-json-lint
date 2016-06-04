#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Vicente Aguillaume
# Copyright (c) 2016 Vicente Aguillaume
#
# License: MIT
#

"""This module exports the MetadataJsonLint plugin class."""

from SublimeLinter.lint import RubyLinter


class MetadataJsonLint(RubyLinter):
    """Provides an interface to metadata-json-lint."""

    syntax = 'json'
    cmd = 'metadata-json-lint'
    version_args = '--version'
    version_re = r'\bv(?P<version>\d+\.\d+\.\d+)'
    regex = (
        r'((?P<error>Error)|(?P<warning>Warning)):?P<message>.+$\r?\n'
        r'(?P<message>.+)'
        r'(?P<message>.+)'
    )
    multiline = True
    line_col_base = (0, 0)
