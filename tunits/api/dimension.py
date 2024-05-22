# Copyright 2024 The TUnits Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Dimension abstraction.

This module creates the dimension abstraction which allows the creation of values
that belong to a dimension (e.g. t: Time, x: Length, ...etc). This allows us to
use static types to check code correctness (e.g. time_method(t: Time)).

To add a new dimension, create 3 classes: 
- `class _NewDimension(Dimension):` which implements the abstract methods from
    the abstract `Dimension` class.
- `class NewDimension(_NewDimension, ValueWithDimension)` which represents scalar
    values and doesn't need to implement any methods.
- `class AccelerationArray(_Acceleration, ArrayWithDimension)` which represents
    an array of values sharing the same dimension and unit.
"""

import abc

from functools import cache

import tunits_core
from tunits.api import unit


class Dimension(abc.ABC):
    """Dimension abstraction.

    This abstract class allows the creation of values that belong to a dimension
    (e.g. t: Time, x: Length, ...etc). This allows us to use static types to check
    code correctness (e.g. time_method(t: Time)).

    To add a new dimension, create 3 classes:
        - `class _NewDimension(Dimension):` which implements the abstract methods from
            this class.
        - `class NewDimension(_NewDimension, ValueWithDimension)` which represents scalar
            values and doesn't need to implement any methods.
        - `class AccelerationArray(_Acceleration, ArrayWithDimension)` which represents
            an array of values sharing the same dimension and unit.
    """

    @staticmethod
    @abc.abstractmethod
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        """Returns a tuple of valid base units (e.g. (dB, dBm) for LogPower)."""

    @classmethod
    def is_valid(cls, v: tunits_core.WithUnit) -> bool:
        return any(v.base_units == u.base_units for u in cls.valid_base_units())


class _Acceleration(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (
            unit.default_unit_database.known_units['m']
            / unit.default_unit_database.known_units['s'] ** 2,
        )

    def _value_class(self) -> type[tunits_core.Value]:
        return Acceleration

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return AccelerationArray


class ValueWithDimension(Dimension, tunits_core.Value): ...


class ArrayWithDimension(Dimension, tunits_core.ValueArray): ...


class Acceleration(_Acceleration, ValueWithDimension): ...


class AccelerationArray(_Acceleration, ArrayWithDimension): ...


class _Angle(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (
            unit.default_unit_database.known_units['rad'],
            unit.default_unit_database.known_units['sr'],
        )

    def _value_class(self) -> type[tunits_core.Value]:
        return Angle

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return AngleArray


class Angle(_Angle, ValueWithDimension): ...


class AngleArray(_Angle, ArrayWithDimension): ...


class _AngularFrequency(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (
            unit.default_unit_database.known_units['rad']
            * unit.default_unit_database.known_units['Hz']
            * 2,
        )

    def _value_class(self) -> type[tunits_core.Value]:
        return AngularFrequency

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return AngularFrequencyArray


class AngularFrequency(_AngularFrequency, ValueWithDimension): ...


class AngularFrequencyArray(_AngularFrequency, ArrayWithDimension): ...


class _Area(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (unit.default_unit_database.known_units['m'] ** 2,)

    def _value_class(self) -> type[tunits_core.Value]:
        return Area

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return AreaArray


class Area(_Area, ValueWithDimension): ...


class AreaArray(_Area, ArrayWithDimension): ...


class _Capacitance(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (unit.default_unit_database.known_units['farad'],)

    def _value_class(self) -> type[tunits_core.Value]:
        return Capacitance

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return CapacitanceArray


class Capacitance(_Capacitance, ValueWithDimension): ...


class CapacitanceArray(_Capacitance, ArrayWithDimension): ...


class _Charge(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (unit.default_unit_database.known_units['coulomb'],)

    def _value_class(self) -> type[tunits_core.Value]:
        return Charge

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return ChargeArray


class Charge(_Charge, ValueWithDimension): ...


class ChargeArray(_Charge, ArrayWithDimension): ...


class _CurrentDensity(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (
            unit.default_unit_database.known_units['ampere']
            / unit.default_unit_database.known_units['m'] ** 2,
        )

    def _value_class(self) -> type[tunits_core.Value]:
        return CurrentDensity

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return CurrentDensityArray


class CurrentDensity(_CurrentDensity, ValueWithDimension): ...


class CurrentDensityArray(_CurrentDensity, ArrayWithDimension): ...


class _Density(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (
            unit.default_unit_database.known_units['kg']
            / unit.default_unit_database.known_units['m'] ** 3,
        )

    def _value_class(self) -> type[tunits_core.Value]:
        return Density

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return DensityArray


class Density(_Density, ValueWithDimension): ...


class DensityArray(_Density, ArrayWithDimension): ...


class _ElectricCurrent(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (unit.default_unit_database.known_units['ampere'],)

    def _value_class(self) -> type[tunits_core.Value]:
        return ElectricCurrent

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return ElectricCurrentArray


class ElectricCurrent(_ElectricCurrent, ValueWithDimension): ...


class ElectricCurrentArray(_ElectricCurrent, ArrayWithDimension): ...


class _ElectricPotential(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (unit.default_unit_database.known_units['V'],)

    def _value_class(self) -> type[tunits_core.Value]:
        return ElectricPotential

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return ElectricPotentialArray


class ElectricPotential(_ElectricPotential, ValueWithDimension): ...


class ElectricPotentialArray(_ElectricPotential, ArrayWithDimension): ...


class _ElectricalConductance(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (unit.default_unit_database.known_units['siemens'],)

    def _value_class(self) -> type[tunits_core.Value]:
        return ElectricalConductance

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return ElectricalConductanceArray


class ElectricalConductance(_ElectricalConductance, ValueWithDimension): ...


class ElectricalConductanceArray(_ElectricalConductance, ArrayWithDimension): ...


class _Energy(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (unit.default_unit_database.known_units['joule'],)

    def _value_class(self) -> type[tunits_core.Value]:
        return Energy

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return EnergyArray


class Energy(_Energy, ValueWithDimension): ...


class EnergyArray(_Energy, ArrayWithDimension): ...


class _Force(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (unit.default_unit_database.known_units['newton'],)

    def _value_class(self) -> type[tunits_core.Value]:
        return Force

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return ForceArray


class Force(_Force, ValueWithDimension): ...


class ForceArray(_Force, ArrayWithDimension): ...


class _Frequency(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (unit.default_unit_database.known_units['Hz'],)

    def _value_class(self) -> type[tunits_core.Value]:
        return Frequency

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return FrequencyArray


class Frequency(_Frequency, ValueWithDimension): ...


class FrequencyArray(_Frequency, ArrayWithDimension): ...


class _Illuminance(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (unit.default_unit_database.known_units['lux'],)

    def _value_class(self) -> type[tunits_core.Value]:
        return Illuminance

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return IlluminanceArray


class Illuminance(_Illuminance, ValueWithDimension): ...


class IlluminanceArray(_Illuminance, ArrayWithDimension): ...


class _Inductance(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (unit.default_unit_database.known_units['henry'],)

    def _value_class(self) -> type[tunits_core.Value]:
        return Inductance

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return InductanceArray


class Inductance(_Inductance, ValueWithDimension): ...


class InductanceArray(_Inductance, ArrayWithDimension): ...


class _Length(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (unit.default_unit_database.known_units['m'],)

    def _value_class(self) -> type[tunits_core.Value]:
        return Length

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return LengthArray


class Length(_Length, ValueWithDimension): ...


class LengthArray(_Length, ArrayWithDimension): ...


class _LogPower(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (
            unit.default_unit_database.known_units['dBm'],
            unit.default_unit_database.known_units['dB'],
        )

    def _value_class(self) -> type[tunits_core.Value]:
        return LogPower

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return LogPowerArray


class LogPower(_LogPower, ValueWithDimension): ...


class LogPowerArray(_LogPower, ArrayWithDimension): ...


class _LuminousFlux(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (unit.default_unit_database.known_units['lumen'],)

    def _value_class(self) -> type[tunits_core.Value]:
        return LuminousFlux

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return LuminousFluxArray


class LuminousFlux(_LuminousFlux, ValueWithDimension): ...


class LuminousFluxArray(_LuminousFlux, ArrayWithDimension): ...


class _LuminousIntensity(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (unit.default_unit_database.known_units['candela'],)

    def _value_class(self) -> type[tunits_core.Value]:
        return LuminousIntensity

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return LuminousIntensityArray


class LuminousIntensity(_LuminousIntensity, ValueWithDimension): ...


class LuminousIntensityArray(_LuminousIntensity, ArrayWithDimension): ...


class _MagneticFlux(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (unit.default_unit_database.known_units['weber'],)

    def _value_class(self) -> type[tunits_core.Value]:
        return MagneticFlux

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return MagneticFluxArray


class MagneticFlux(_MagneticFlux, ValueWithDimension): ...


class MagneticFluxArray(_MagneticFlux, ArrayWithDimension): ...


class _MagneticFluxDensity(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (unit.default_unit_database.known_units['tesla'],)

    def _value_class(self) -> type[tunits_core.Value]:
        return MagneticFluxDensity

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return MagneticFluxDensityArray


class MagneticFluxDensity(_MagneticFluxDensity, ValueWithDimension): ...


class MagneticFluxDensityArray(_MagneticFluxDensity, ArrayWithDimension): ...


class _Mass(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (unit.default_unit_database.known_units['kg'],)

    def _value_class(self) -> type[tunits_core.Value]:
        return Mass

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return MassArray


class Mass(_Mass, ValueWithDimension): ...


class MassArray(_Mass, ArrayWithDimension): ...


class _Noise(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (
            unit.default_unit_database.known_units['V']
            / unit.default_unit_database.known_units['Hz'] ** 0.5,
            unit.default_unit_database.known_units['watt']
            / unit.default_unit_database.known_units['Hz'],
        )

    def _value_class(self) -> type[tunits_core.Value]:
        return Noise

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return NoiseArray


class Noise(_Noise, ValueWithDimension): ...


class NoiseArray(_Noise, ArrayWithDimension): ...


class _Power(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (unit.default_unit_database.known_units['watt'],)

    def _value_class(self) -> type[tunits_core.Value]:
        return Power

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return PowerArray


class Power(_Power, ValueWithDimension): ...


class PowerArray(_Power, ArrayWithDimension): ...


class _Pressure(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (unit.default_unit_database.known_units['pascal'],)

    def _value_class(self) -> type[tunits_core.Value]:
        return Pressure

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return PressureArray


class Pressure(_Pressure, ValueWithDimension): ...


class PressureArray(_Pressure, ArrayWithDimension): ...


class _Quantity(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (unit.default_unit_database.known_units['mole'],)

    def _value_class(self) -> type[tunits_core.Value]:
        return Quantity

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return QuantityArray


class Quantity(_Quantity, ValueWithDimension): ...


class QuantityArray(_Quantity, ArrayWithDimension): ...


class _Resistance(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (unit.default_unit_database.known_units['ohm'],)

    def _value_class(self) -> type[tunits_core.Value]:
        return Resistance

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return ResistanceArray


class Resistance(_Resistance, ValueWithDimension): ...


class ResistanceArray(_Resistance, ArrayWithDimension): ...


class _Speed(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (
            unit.default_unit_database.known_units['m']
            / unit.default_unit_database.known_units['s'],
        )

    def _value_class(self) -> type[tunits_core.Value]:
        return Speed

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return SpeedArray


class Speed(_Speed, ValueWithDimension): ...


class SpeedArray(_Speed, ArrayWithDimension): ...


class _SurfaceDensity(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (
            unit.default_unit_database.known_units['kg']
            / unit.default_unit_database.known_units['m'] ** 2,
        )

    def _value_class(self) -> type[tunits_core.Value]:
        return SurfaceDensity

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return SurfaceDensityArray


class SurfaceDensity(_SurfaceDensity, ValueWithDimension): ...


class SurfaceDensityArray(_SurfaceDensity, ArrayWithDimension): ...


class _Temperature(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (unit.default_unit_database.known_units['kelvin'],)

    def _value_class(self) -> type[tunits_core.Value]:
        return Temperature

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return TemperatureArray


class Temperature(_Temperature, ValueWithDimension): ...


class TemperatureArray(_Temperature, ArrayWithDimension): ...


class _Time(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (unit.default_unit_database.known_units['s'],)

    def _value_class(self) -> type[tunits_core.Value]:
        return Time

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return TimeArray


class Time(_Time, ValueWithDimension): ...


class TimeArray(_Time, ArrayWithDimension): ...


class _Torque(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (
            unit.default_unit_database.known_units['newton']
            * unit.default_unit_database.known_units['m'],
        )

    def _value_class(self) -> type[tunits_core.Value]:
        return Torque

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return TorqueArray


class Torque(_Torque, ValueWithDimension): ...


class TorqueArray(_Torque, ArrayWithDimension): ...


class _Volume(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (unit.default_unit_database.known_units['m'] ** 3,)

    def _value_class(self) -> type[tunits_core.Value]:
        return Volume

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return VolumeArray


class Volume(_Volume, ValueWithDimension): ...


class VolumeArray(_Volume, ArrayWithDimension): ...


class _WaveNumber(Dimension):

    @staticmethod
    @cache
    def valid_base_units() -> tuple[tunits_core.Value, ...]:
        return (unit.default_unit_database.known_units['m'] ** -1,)

    def _value_class(self) -> type[tunits_core.Value]:
        return WaveNumber

    def _array_class(self) -> type[tunits_core.ValueArray]:
        return WaveNumberArray


class WaveNumber(_WaveNumber, ValueWithDimension): ...


class WaveNumberArray(_WaveNumber, ArrayWithDimension): ...
