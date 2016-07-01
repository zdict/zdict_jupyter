#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ipykernel.kernelbase import Kernel
from pexpect.replwrap import REPLWrapper


class ZdictKernel(Kernel):
    implementation = 'zdict'
    implementation_version = '0.0.1'
    language = 'zdict'
    language_version = '0.9.4'
    language_info = {'mimetype': 'text/plain'}
    banner = "zdict kernel"

    def do_execute(self,
                   code,
                   silent,
                   store_history=True,
                   user_expressions=None,
                   allow_stdin=False):

        zdict = REPLWrapper(u"zdict", u"[zDict]: ", None)
        output = zdict.run_command(code.strip())

        if not silent:
            stream_content = {'name': 'stdout', 'text': output}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {
            'status': 'ok',
            # The base class increments the execution count
            'execution_count': self.execution_count,
            'payload': [],
            'user_expressions': {},
        }
