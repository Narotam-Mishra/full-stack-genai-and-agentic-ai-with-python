
import arrow
from collections import namedtuple

brewing_time = arrow.utcnow()
brewing_time.to("Europe/Rome")
print(f"brewing_time: {brewing_time}")

chaiProfile = namedtuple("chaiProfile", ["flavor", "aroma"])