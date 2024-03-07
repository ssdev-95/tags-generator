import os
from .tag_creator_handler import TagCreatorHandler
from barcode import Code128
from barcode.writer import ImageWriter, SVGWriter
from ..main.server.static import tmp_folder


class BarcodeHandler(TagCreatorHandler):
    def create_tag(self, product_code: str, extension: str) -> str:
        tag_path = f'{tmp_folder}/brc-{product_code}.{extension.lower()}'

        if os.path.exists(tag_path):
            print(f'[DEBUG] Tag already saved! {os.times()}')
            return tag_path

        if extension == 'SVG':
            writer = SVGWriter()
        else:
            writer = ImageWriter()
            #writer.set_options({ 'format': extension.upper() })

        tag = Code128(product_code, writer=writer)
        tag.save(tag_path)
        return tag_path
