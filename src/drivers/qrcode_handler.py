from .tag_creator_handler import TagCreatorHandler
import segno


class QrcodeHandler(TagCreatorHandler):
    def create_tag(self, product_code: str, extension: str) -> str:
        tag = segno.make_qr(product_code)
        tag_path = f'/tmp/qr-{product_code}.{extension.lower()}'
        tag.save(tag_path)
        return tag_path
