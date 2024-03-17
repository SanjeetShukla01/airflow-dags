import abc
import copy
import logging


class JobTemplate(metaclass=abc.ABCMeta):

    def __init__(self, params):
        self.params =params


    @property
    @abc.abstractmethod
    def template(self):
        pass

    def generate_config(self):
        params_copy = copy.copy(self.params)
        del params_copy['task_id']
        return {
            self.params["task_id"]: params_copy
        }

    @abc.abstractmethod
    def generate_command(self, task_params:dict):
        pass

    def validate_template_params(self, task_params:dict):
        logging.info('No validation function was specified for this template --> no validation was done for the params for this task')
        pass
