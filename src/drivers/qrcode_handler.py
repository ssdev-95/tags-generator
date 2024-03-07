import os
from .tag_creator_handler import TagCreatorHandler
import segno
from ..main.server.static import tmp_folder


class QrcodeHandler(TagCreatorHandler):
    def create_tag(self, product_code: str, extension: str) -> str:
        tag_path = f'{tmp_folder}/qr-{product_code}.{extension.lower()}'
        if os.path.exists(tag_path):
            print(f'[DEBUG] Tag already saved! {os.times()}')
            return tag_path

        tag = segno.make_qr(product_code)
        tag.save(tag_path)
        return tag_path
