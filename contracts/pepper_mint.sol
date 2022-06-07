pragma solidity ^0.5.5;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract pepperMint is ERC721Full {
    constructor() public ERC721Full("PepperMint", "CEGH") {}
    // address <--> NFT ID
    mapping(uint256 => address) public nftOwners;

    function mintCEGH(address minter, string memory tokenURI)
        public
        returns (uint256)
    {
        uint256 newNftId = totalSupply();
        _mint(minter, newNftId);
        _setTokenURI(newNftId, tokenURI);
        nftOwners[newNftId] = minter;
        return newNftId;
    }

    function CEGHOwner(address _owner) external view returns(uint256[] memory tokens) {
        uint256 tokenCount = balanceOf(_owner);

        if (tokenCount == 0) {
            // Return an empty array
            return new uint256[](0);
        } else {
            uint256[] memory result = new uint256[](tokenCount);
            uint256 totalNft = totalSupply();
            uint256 resultIndex = 0;

            uint256 NftId;

            for (NftId = 1; NftId <= totalNft; NftId++) {
                if (nftOwners[NftId] == _owner) {
                    result[resultIndex] = NftId;
                    resultIndex++;
                }
            }
            return result;
        }
    }
}