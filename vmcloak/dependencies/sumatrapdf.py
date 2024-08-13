# Copyright (C) 2016-2018 Jurriaan Bremer.
# This file is part of VMCloak - http://www.vmcloak.org/.
# See the file 'docs/LICENSE.txt' for copying permission.

from vmcloak.abstract import Dependency
from pathlib import Path

class SumatraPDF(Dependency):
    name = "sumatrapdf"
    default = "3.5.2"
    exes = [{
        "version": "3.5.2",
        "arch": "amd64",
        "filename": "SumatraPDF-3.5.2-64-install.exe",
        "urls": [
            "https://www.sumatrapdfreader.org/dl/rel/3.5.2/SumatraPDF-3.5.2-64-install.exe"
        ],
        "sha1": "a700ecab3628239a7c2831b4f74487419d9aa850"
    }]

    pdfreader_scripts = {
        "win10": Path(
            Dependency.data_path, "win10", "scripts", "pdfreader.ps1"
        )
    }

    def run(self):
        self.upload_dependency("C:\\%s" % self.filename)
        self.a.execute("C:\\{} -install -s -d c:\\SumatraPDF".format(self.filename))
        self.a.remove("C:\\%s" % self.filename)

        pdfreader_script = self.pdfreader_scripts.get("pdfreader")
        if not pdfreader_script:
            raise DependencyError(
                f"OS: {self.h.name} has no service pdfreader script available."
            )

        res = self.run_powershell_file(str(pdfreader_script))
        exit_code = res.get("exit_code")
        if exit_code:
            log.debug(
                f"Service pdfreader return non-zero exit code. {exit_code}. "
                f"Stderr={res.get('stderr')}. stdout={res.get('stdout')}. "
            )
