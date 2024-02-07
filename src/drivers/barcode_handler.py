from barcode import Code128
from barcode.writer import ImageWriter

class BarcodeHandler:
    def create_barcode(self, product_code: str, extension: str) -> str:
        writer = ImageWriter()
        writer.set_options({ 'format': extension })
        tag = Code128(product_code, writer=writer)
        tag_path = f'tmp/{tag}'
        tag.save(tag_path)
        [_, file] = tag_path.split('/')
        print(tag_path)
        return file
