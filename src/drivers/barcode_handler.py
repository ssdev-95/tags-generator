from .tag_creator_handler import TagCreatorHandler
from barcode import Code128
from barcode.writer import ImageWriter, SVGWriter


class BarcodeHandler(TagCreatorHandler):
    def create_tag(self, product_code: str, extension: str) -> str:
        if extension == 'SVG':
            writer = SVGWriter()
        else:
            writer = ImageWriter()
            writer.set_options({ 'format': extension.upper() })
        tag = Code128(product_code, writer=writer)
        tag_path = f'/tmp/brc-{tag}.{extension.lower()}'
        tag.save(tag_path)
        return tag_path
