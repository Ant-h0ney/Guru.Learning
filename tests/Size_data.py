import dataclasses


@dataclasses.dataclass
class Dimension:
    width: int
    height: int = 800

    def __repr__(self):
        return f'Size[{self.width}*{self.height}]'


desktop_size = Dimension(width=1200)
mobile_size = Dimension(width=600)
