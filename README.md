<a name="top"></a>
<p align="center">
  <img src=".jpg" alt="PepperMint"/>
</p>


## Table of Contents

- [Table of Contents](#table-of-contents)
  - [Introducting PepperMint](#introducing-PepperMint)
  - [Technology Stack](#technology-stack)
  - [User Experience](#user-experience)
  - [Unanticipated-problems-and-insights](#unanticipated-problems-and-insights)
  - [Future Developments for Consideration](#future-developments-for-consideration)
  - [References](#references)
    


# PepperMint
<p>
PepperMint is an implementation of NFT technology in the real world, as opposed to the metaverse, whereby counterfeit products are known to cause significant harm to businesses and consumers globally. Our blockchain solution is a representation for an entirely tokenised economy, where smart contracts trade assets and commodities, and consumers can see the history of goods they purchase via immutable blockchain records. 
  
The express purpose of our smart contract is to reduce and eliminate counterfeit production, and to act as the conduit for intellectual property rights validation and enforcement for small sized business' and multinational corporations. 

### Features & Benefits 

* Consumers may verify the authenticity of their products and the legitimacy of their ownership. 

* NFTs can be used to verify the authenticity of physical goods by storing all relevant information relating to a product in an NFT on a decentralized network.  The successful use of the technology is based on how the product to be protected can be connected to the DLT. pepperMint() achieves product protection with the use of QR codes in the NFT minting process. 

* Counterfeit and fraud prevention.
  
* QR code 'smart tag' implementation.

* NFT and product owners have the ability to transfer ownership. 

* Eliminate the re-sale of stolen goods with a sustained reduction of the criminalised offence over time.

* Existing solutions offering pre minted NFT's attract transfer fees that in most cases exceeds the minting fee. 

* By contrast, PepperMint provides consumers with the ability to mint NFT's as part of the unboxing process.

* The unboxing experience will result in user generated marketing content by the consumer. User-generated content is an effective marketing strategy. 

* PepperMint isn't reserved for global brands. Minting services available to business' of all sizes.


### Technology Stack

The current version of peppermint() relies on the following technologies to achieve the demonstrated functionality:
* Solidity: an object oriented programing langugage for implementing smart contracts on the Ethereum blockchain. 

* Python: a high level, interpreted, general-purpose programming language. 

* Ganache: a personal ethereum blockchain use to run tests, execute commands and inspect state while controlling how the chain operates. 

* Metmask: cryptocurrency wallet used to interact with the Ethereum blockchain and decentralized applications. 

* Streamlit: an open source app framework in the Python language used to create interactions with smart contracts and data science/ML models.

* qrcode: Python module for QR code generator and encoder.

<br/>
<div align="right">
    <b><a href="#top">↥ back to top</a></b>
</div>
<br/>

### User Experience

<p>
<img align="center" src="images/2Capture.PNG">
<p/>
<br/>

<p>
<img align="center" src="images/3Capture.PNG">
<p/>
<br/>

<br/>
<div align="right">
    <b><a href="#top">↥ back to top</a></b>
</div>
<br/>

### Unancticipated Problems and Insights 

The peppermint() smart contract accepts the name and symbol of a tokenised asset and invokes a peppermint instance. When there are multiple instances of the same contract, the cost of the resulting transactions (gas) will increase by a multiple equivalent to the number of instances generated in the pepperMint() smart contract. 

An upgradable smart contract will contribute to a significant reduction in transaction costs. 

Ethereum contracts are immutable. Once they are deployed to the blockchain they cannot be updated, however the need to alter their logic via upgradable contracts with time is necessary. During a contract upgrade, the following issues are considered:
* Block gas limit.
* Inter-contract dependencies. 
* Implementation of permanent storage. 
* Encapsulating logic in a library of functions. 
* Abstracting via an interface. 

The underlying principles for upgrading an immutable contract can be found in the Ethereum white paper 'DAO' seciton (https://github.com/ethereum/wiki/wiki/White-Paper#decentralized-autonomous-organizations) which states:

> Although code is theoretically immutable, one can easily get around this and have de-facto mutability by having chunks of the code in separate contracts, and having the address of which contracts to call stored in the modifiable storage.

Implementing permanent storage, encapsulating logic in library functions and abstracting via an interface are all in line with the principle where address pointers are used in the calling the original smart contract for interacting with storage and business logic. 

<br/>
<div align="right">
    <b><a href="#top">↥ back to top</a></b>
</div>
<br/>

### Future Developments for Consideration

* RFID and NFC 'smart tag' integration. 

* Off chain validation using Chainlink Oracles. 

* Metaverse implementation.

* Customer service functionality.

* Social media integration. 

* Manufacturer user interface. 

* Gated NFT website with access restricted to VIP token holders. 

* NFT gallery.

<br/>
<div align="right">
    <b><a href="#top">↥ back to top</a></b>
</div>
<br/>

### References 
Counterfeit Goods, a Danger to Public Safety
https://www.ice.gov/features/dangers-counterfeit-items

Lollipuff Undercover: Fake Designer Bags in Asia
https://www.lollipuff.com/lollipuff-undercover-fake-designer-bags-in-asia/

5 Brands Winning in the Metaverse
https://www.thedrum.com/news/2022/06/01/5-brands-winning-the-metaverse

Breitling Becomes the First Luxury Watchmaker to Offer a Digital Passport Based on Blockchain for all of its New Watches
https://www.breitling.com/us-es/news/details/breitling-becomes-the-first-luxury-watchmaker-to-offer-a-digital-passport-based-on-blockchain-for-all-of-its-new-watches-33479  

How to Blockchain, Smart Tags are Tackling Counterfeit Goods
https://www.supplychainbrain.com/blogs/1-think-tank/post/34693-tackling-product-counterfeiting-with-blockchain#:~:text=Blockchain%20helps%20tackle%20counterfeiting%20by,level%2C%20from%20production%20to%20delivery

Non Fungible Tokens (Wikipedia article)
https://en.wikipedia.org/wiki/Non-fungible_token

Defiance ETFs, NFT Outlook for 2022
https://www.defianceetfs.com/nft-outlook-for-2022/

<br/>
<div align="right">
    <b><a href="#top">↥ back to top</a></b>
</div>
<br/>
