# -*- coding: utf-8 -*-

VERSION = (0, 4, 2)
PRERELEASE = None # alpha, beta or rc
REVISION = None


def generate_version(version, prerelease=None, revision=None):
    version_parts = ['.'.join(map(str, version))]
    if prerelease is not None:
        version_parts.append('-{}'.format(prerelease))
    if revision is not None:
        version_parts.append('.{}'.format(revision))
    return ''.join(version_parts)


__version__ = '.'.join(map(str, VERSION))
