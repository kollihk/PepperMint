# capstone-project: Workflow

1. User buys a limited edition sneakers
2. In order for the user to mint an NFT, two things needs to be done:
	* Prove that the shoes are genuine and NOT counterfiet one
	* Proof that he is the owner ( Invoice or crypto payment receipt)
3. Assuming the packaging / sneakers has a QR code for the user to scan, it needs to be decoded into hash
4. Compare the hash in streamlit against manufacturer' database (either through Chainlink/streamlit)
5. If the hash is found, a call to the contract function is made to mint an NFT
4. Verify that the minted NFT is in users' wallet

## installations
* pip install streamlit_option_menu
* pip install OpenCV 
* pip install OpenCV 
* pip install webbrowser ( built in )


### User Journey 
#### Consumer 

##### Step 1: QR Code 
 
 
##### Step 2: Hash Code 
TBA
 
##### Step 3: 
 
#### Manufacturer
##### Step 1: Allocate serial number / product details for hash compilation 
* The eth-abi library provides utilities to convert python values to and from solidity’s binary ABI format. 
* The Contract Application Binary Interface (ABI) is the standard way to interact with contracts in the Ethereum ecosystem, both from outside the blockchain and for contract-to-contract interaction.
* Online hash generators might not comply with the ABI standard. I recommend we avoid online hash generators for this reason.
 
#### Step 2: Hash code creation 
 
* To ensure compliance with ABI standards, we can create hashing codes using the eth-abi library. Python values can be encoded into binary values for a given ABI type. 
* Eth-abi allows the user to check whether a certain python value is encodable for a given abi type. 
* The user may select an ‘encodable’ python value from a dropdown list in the Streamlit UI. The list will reflect the content of a python dict made up of encodable python values needed to generate the hashing code. 
 
Note for discussion: 
* Web3.py accepts struct arguments as dictionaries.
* Eth-abi functionality.
