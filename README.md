# capstone-project: Workflow

1. User buys a limited edition sneakers
2. In order for the user to mint an NFT, two things needs to be done:
	* Prove that the shoes are genuine and NOT counterfiet one
	* Proof that he is the owner ( Invoice or crypto payment receipt)
3. Assuming the packaging / sneakers has a QR code for the user to scan, it needs to be decoded into hash
4. Compare the hash in streamlit against manufacturer' database (either through Chainlink/streamlit)
5. If the hash is found, a call to the contract function is made to mint an NFT
4. Verify that the minted NFT is in users' wallet
