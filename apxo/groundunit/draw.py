################################################################################

import apxo.draw as apdraw

################################################################################

def _draw(self):
    apdraw.drawgroundunit(
        *self.xy(),
        self._symbols,
        self.color(),
        self.name(),
        self._stack,
        self._killed
    )

################################################################################
