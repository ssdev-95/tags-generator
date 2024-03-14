import os
from .tag_creator_handler import TagCreatorHandler
from barcode import Code128
from barcode.writer import ImageWriter, SVGWriter
from ..main.server.static import config


class BarcodeHandler(TagCreatorHandler):
    def create_tag(self, product_code: str, extension: str) -> str:
        tag_path = f'{config["tmp_folder"]}/brc-{product_code}'

        if os.path.exists(tag_path):
            print(f'[DEBUG] Tag already saved! {os.times()}')
            return tag_path

        if extension == 'SVG':
            writer = SVGWriter()
        else:
            writer = ImageWriter()
            writer.set_options({ 'format': extension.upper() })

        tag = Code128(product_code, writer=writer)
        tag.save(tag_path)
        return f'{tag_path}.{extension.lower()}'
