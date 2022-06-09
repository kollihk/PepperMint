
# THIS CODE IS RUN ONLY ONCE to generate the QR codes for "Nike Secret NFT Collection"
# Simulating the Manufacturer's Database for product authentication purposes.
# conda activate dev

import qrcode
import pandas as pd

# Creating the manufacturer's df
df= pd.read_csv("./products_DB/product_info.csv", index_col=3)

# Generating the QR code that comes in the box with "Nike Secret NFT Collection" products
i = 0
while i<9:
    file_name = str(df['serial_number'].iloc[i]) + ".png"
    file_path = f"./products_DB/products_QRcodes/{file_name}"
    code = str(df['hashcode'].iloc[i])
    img = qrcode.make(code)
    img.save(file_path)    
    i += 1
# img.show(file_path)
# print(f"{file_name} is saved in {file_path}")

