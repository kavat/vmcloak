# Copyright (C) 2016-2018 Jurriaan Bremer.
# This file is part of VMCloak - http://www.vmcloak.org/.
# See the file 'docs/LICENSE.txt' for copying permission.

from vmcloak.abstract import Dependency

class TightVNC(Dependency):
    name = "tightvnc"
    default = "2.8.84"
    exes = [{
        "version": "2.8.84",
        "arch": "amd64",
        "filename": "tightvnc-2.8.84-gpl-setup-64bit.msi",
        "md5": "d9e810a84ebe69e403a5f7e4c5ab9a37"
    }]

    def run(self):
        self.upload_file("/opt/vmcloak/{}".format(self.filename), "C:\\{}".format(self.filename))
        self.a.execute("msiexec /i C:\\{} /quiet /norestart ADDLOCAL=Server SET_USEVNCAUTHENTICATION=1 VALUE_OF_USEVNCAUTHENTICATION=1 SET_PASSWORD=1 VALUE_OF_PASSWORD=password".format(self.filename))
        self.a.remove("C:\\%s" % self.filename)
