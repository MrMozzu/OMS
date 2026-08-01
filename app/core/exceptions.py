
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