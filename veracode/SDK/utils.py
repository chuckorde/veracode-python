
class Properties(object):
    def _update_properties(self, src=None):
        if hasattr(self, '_properties'):
            for idx, prop in enumerate(self._properties):
                target_prop = prop
                if hasattr(self, '_renamed_properties'):
                    if self._renamed_properties:
                        target_prop = self._renamed_properties[idx]
                setattr(self, target_prop, None)
                if hasattr(src, prop):
                    setattr(self, target_prop, getattr(src, prop))

    def __bool__(self):
        return self.id is not None

    def _dump(self):
        for prop in dir(self):
            if prop.startswith('_'):
                continue
            print(prop, getattr(self, prop))


