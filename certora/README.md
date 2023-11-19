OZ has Certora specs for ERC721 but we are using ERC1155. There is some functional overlap but it is basically necessary to create the specs from scratch.

To run the specs:
certoraRun certora/configuration/Poaps.conf --packages @openzeppelin=lib/openzeppelin-contracts
