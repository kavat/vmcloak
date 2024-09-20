# Copyright (C) 2016-2018 Jurriaan Bremer.
# This file is part of VMCloak - http://www.vmcloak.org/.
# See the file 'docs/LICENSE.txt' for copying permission.

from vmcloak.abstract import Dependency, DependencyError
from pathlib import Path

class TorBrowser(Dependency):
    name = "torbrowser"
    default = "13.5.4"
    exes = [{
        "version": "13.5.4",
        "arch": "amd64",
        "filename": "tor-browser-windows-x86_64-portable-13.5.4.exe",
        "urls": [
            "https://www.torproject.org/dist/torbrowser/13.5.4/tor-browser-windows-x86_64-portable-13.5.4.exe"
        ],
        "sha1": "767569ba116622ae3abdb8e41bfae6fe09039624"
    }]

    def run(self):
        self.upload_dependency("C:\\%s" % self.filename)
