pragma solidity ^0.5.5;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract sneakers is ERC721Full {
    constructor() public ERC721Full("Sneakers", "CEGH") {}
    // address <--> Sneaker ID
    mapping(uint256 => address) public sneakerOwners;

    function mintSneakers(address minter, string memory tokenURI)
        public
        returns (uint256)
    {
        uint256 newSneakerId = totalSupply();
        _mint(minter, newSneakerId);
        _setTokenURI(newSneakerId, tokenURI);
        sneakerOwners[newSneakerId] = minter;
        return newSneakerId;
    }

    function CEGHOwner(address _owner) external view returns(uint256[] memory tokens) {
        uint256 tokenCount = balanceOf(_owner);

        if (tokenCount == 0) {
            // Return an empty array
            return new uint256[](0);
        } else {
            uint256[] memory result = new uint256[](tokenCount);
            uint256 totalSneakers = totalSupply();
            uint256 resultIndex = 0;

            uint256 SneakerId;

            for (SneakerId = 1; SneakerId <= totalSneakers; SneakerId++) {
                if (sneakerOwners[SneakerId] == _owner) {
                    result[resultIndex] = SneakerId;
                    resultIndex++;
                }
            }
            return result;
        }
    }
}