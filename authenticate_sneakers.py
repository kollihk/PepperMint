# Imports

from dataclasses import dataclass
from typing import Any, List
import hashlib
import qrcode as qr


@dataclass
class Product:
    name: str
    serial_no: int
    invoice: int
    #timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S")
    timestamp: str
    hash: str = "0"

    def hash_product(self):
        sha = hashlib.sha256()

        name = str(self.name).encode()
        sha.update(name)

        serial_no = str(self.serial_no).encode()
        sha.update(serial_no)

        invoice = str(self.invoice).encode()
        sha.update(invoice)

        timestamp = str(self.timestamp).encode()
        sha.update(timestamp)

        hash = sha.hexdigest()

        return hash
    '''
    def generate_qrcode(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
            )
        qr.add_data('Some data')
        qr.make(fit=True)

        return qr.make_image(fill_color="black", back_color="white")
    '''
# Create the data class product database
@dataclass
class Database:
    database: List[Product.hash]

    def add_product_hash(self, pr_hash):
        self.database += [pr_hash]


