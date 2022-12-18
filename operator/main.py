from dataclasses import dataclass
import operator


@dataclass(frozen=True)
class LatLon:
    lat: float
    lon: float


@dataclass(frozen=True)
class Metropolis:
    name: str
    country_code: str
    population: float
    coord: LatLon


metro_data: list[Metropolis] = [
    Metropolis("Tokyo", "JP", 36.933, LatLon(35.689722, 139.691667)),
    Metropolis("Delhi NCR", "IN", 21.935, LatLon(28.613889, 77.208889)),
    Metropolis("Mexico City", "MX", 20.142, LatLon(19.433333, -99.133333)),
    Metropolis("New York-Newark", "US", 20.104, LatLon(40.808611, -74.020386)),
    Metropolis("São Paulo", "BR", 19.649, LatLon(-23.547778, -46.635833)),
]

for metro in sorted(metro_data, key=operator.attrgetter("population")):
    print(metro)

print(f"{'*' * 50}")

print(operator.itemgetter(1, 2)(metro_data))
