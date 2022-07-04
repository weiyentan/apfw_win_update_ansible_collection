#!/usr/bin/python
# Make coding more python3-ish, this is required for contributions to Ansible
from __future__ import (absolute_import, division, print_function)
from turtle import delay
__metaclass__ = type
from ansible.errors import AnsibleError, AnsibleConnectionFailure
from ansible.plugins.action import ActionBase
from ansible.utils.display import Display
from datetime import datetime, timedelta
from time import sleep
display = Display()


class ActionModule(ActionBase):
    TRANSFERS_FILES = False
    _VALID_ARGS = frozenset((
            'duration_hrs'
            'wait'
            'delay'
        ))
    DEFAULT_DURATION_HRS = 3
    DEFAULT_WAIT = 10
    DEFAULT_DELAY = 5

    def __init__(self, *args, **kwargs):
        super(ActionModule, self).__init__(*args, **kwargs)

    def _check_delay(self, key, default):
        """Ensure that the value is positive or zero"""
        value = int(self._task.args.get(key, self._task.args.get(key, default)))
        if value < 0:
            value = 0
        return value

    @property
    def duration_hrs(self):
        
        return self._check_delay('duration_hrs', self.DEFAULT_DURATION_HRS)

    @property
    def wait(self):
        return self._check_delay('wait', self.DEFAULT_WAIT)
    
    @property
    def delay(self):
        return self._check_delay('delay', self.DEFAULT_DELAY)
    
    def convertfrom_seconds_to_minutes(self,seconds):
        secondsvalue = seconds
        converttominutes = seconds // 60
        return converttominutes

    def do_until_success_timeout(self, duration_hrs , wait):
        starttime = datetime.utcnow
        result = {}
        patchingstatus = 'inprogress'
        max_end_time = datetime.utcnow() + timedelta(hours=duration_hrs)
        while datetime.utcnow < max_end_time :
            try:
              module_return = self._execute_module(module_name='win_apfwcompliance', module_args=module_args, task_vars=task_vars, tmp=tmp)
            except:
               if isinstance(e, _ReturnResultException):
                   msg = " The host {{ inventory_host}} results had an error . . . Continuing"
                   display.display(msg)
              
               if isinstance(e, AnsibleConnectionFailure ):
                   msg = " The host {{ inventory_host was not able to be contactable"
                   display.display(msg)

            if not module_return.get('failed'):
              for key, value in module_return['apfw_patchingstatus'].items():
                if key == 'Patchstatus':
                    patchstatus = value['Patchstatus']
              if patchstatus != 'inprogress':
                if patchstatus == 'success':
                    patchingstatus = 'success'
                    display.v('Patches were successfully installed within the timeframe of the Patching Window')
                    break
                
              if patchstatus == 'failed':
                    patchingstatus = 'failed'
                    display.v('Patches failed to install within the timeframe of the Patching')
                    break
            else:
              display.v("Host not contactable Retrying in 10 seconds")
              sleep(10)
        
        if patchingstatus == 'success':
            result['patchingstatus'] = 'success'
            elapsed = datetime.utcnow() - starttime
            result['elapsed'] = elapsed.seconds
        if patchingstatus == 'failed':
            msg = "The patching didn't complete in time."
            raise AnsibleError( msg  )
                

             

    def run(self, tmp=None, task_vars=None):
        result = {}
        var_duration_hrs = self.duration_hrs()
        var_wait = self.wait()
        var_delay = self.delay()
        convert_minutes_to_seconds = var_delay * 60

        sleep(convert_minutes_to_seconds)

        patchingresults = self.do_until_success_timeout(var_duration_hrs , var_wait)

