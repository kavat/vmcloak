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
        "urls": [
            "https://www.tightvnc.com/download/2.8.84/tightvnc-2.8.84-gpl-setup-64bit.msi"
        ],
        "sha1": "4f9f3e12ffc96dd0c6b479d20ada3f59dc383177"
    }]

    def run(self):
        self.upload_file("/opt/vmcloak/{}".format(self.filename), "C:\\{}".format(self.filename))
        self.a.execute("msiexec /i C:\\{} /quiet /norestart ADDLOCAL=Server SET_USEVNCAUTHENTICATION=1 VALUE_OF_USEVNCAUTHENTICATION=1 SET_PASSWORD=1 VALUE_OF_PASSWORD=password".format(self.filename))
        self.a.remove("C:\\%s" % self.filename)
