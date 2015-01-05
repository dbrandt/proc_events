from .pec import pec_control as control
from .pec import pec_unpack as unpack
from .pec import process_events
from .pec import process_events_rev

class BaseStruct(object):
    fields = ()

    def _fill_struct(self, data):
        for k,v in zip(self.fields, data):
            setattr(self, k, v)


class DictWrapper(dict):
    def __getattr__(self, attr):
        return self[attr]
