import tof
import scipp as sc
from trex.utils import centers_to_edges
from typing import TYPE_CHECKING
from trex.utils import calculate_variable_range_at

if TYPE_CHECKING:
    from trex.instrument import Instrument
    from trex.params import DetectorParameters


class Detector(tof.Detector):  # type: ignore
    def __init__(self, parameters: "DetectorParameters", instrument: "Instrument"):
        self.instrument = instrument
        super().__init__(name=parameters.name, distance=parameters.distance)
