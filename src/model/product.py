class Product:
    counter: int = 0

    def __init__(self, name: str, price: float) -> None:
        self.__id: int = Product.counter + 1
        self.__name: str = name
        self.__price: float = price
        Product.counter = self.__id

    @staticmethod
    def register(name: str, price: float) -> 'Product':
        product: Product = Product(name, price)
        return product

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    @property
    def id(self) -> int:
        return self.__id
