# Gassless POAPs

A simple permissionless protocol enabling anyone to create a POAP collection using an ERC1155 for a fixed supply and active during a predefined timeframe. Users are able to mint memories in a gasless way. 

#### What does it do?
- Permissionless Proof Of Attendance Protocol
- Cross chain 
- Gasless minting
- ERC-1155
- Easy integration with ERC-4337 and to RIP-75607560
- Secured used Certora property testing


![diagram](https://github.com/Deivitto/gassless-poaps/assets/47452703/4e4a1aaf-ce92-43cb-b8d4-394d795db231)


#### Deployed on
- [*"ethereum sepolia"*](https://sepolia.etherscan.io/address/0x7a479aae93f97f00117571ee1e61bacab2c780a1#code)
- [*"arbitrum sepolia"*](https://sepolia.arbiscan.io/address/0x420fAd7011A85cc6C308941A7245b7c0E695Fe85#code)
- [*"polygon zkEVM testnet"*](https://testnet-zkevm.polygonscan.com/address/0x420fAd7011A85cc6C308941A7245b7c0E695Fe85)
- [*"mantle testnet"*](https://explorer.testnet.mantle.xyz/address/0x343f50A627fc2d4856e606aA15b3b93A616D82AE)

## Presentation

[Gasless POAP presentation](https://docs.google.com/presentation/d/1YhWw14Ch8chmGwQWdXCl38cri8ygIXXrtXC9SYrKH5k/edit?usp=sharing)

## Test frontend
`cd frontend`

To run the frontend nextJS app:
`yarn start`

Launch an anvil node with foundry:
`yarn chain`

Deploy on the local fork:
`yarn deploy`

