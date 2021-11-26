import json

class ProductDAO:
    def all(self):
        with open('products.json', encoding='utf-8') as f:
            productsJson = f.read()
        return json.loads(productsJson)
    
    def byCode(self, code):
        products = self.all()
        product = None
        for p in products:
            if p['code'] == code:
                product = p
        return product
