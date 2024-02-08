from barcode import Code128
from barcode.writer import ImageWriter

class BarcodeHandler:
    def create_barcode(self, product_code: str, extension: str) -> str:
        writer = ImageWriter()
        writer.set_options({ 'format': extension.upper() })
        tag = Code128(product_code, writer=writer)
        tag_path = f'tmp/brc-{tag}'
        tag.save(tag_path)
        return tag_path
