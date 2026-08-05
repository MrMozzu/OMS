
class CategoryNotFound(Exception):

    def __init__(self):

        super().__init__(
            "Category not found"
        )

    
class CategoryAlreadyExists(Exception):

    def __init__(self):

        super().__init__(
            "Category already exists"
        )


class ProductNotFound(Exception):

    def __init__(self):

        super().__init__(
            "Product not found"
        )


class ProductAlreadyExists(Exception):

    def __init__(self):

        super().__init__(
            "Product already exists"
        )