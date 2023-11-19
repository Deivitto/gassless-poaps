OZ has Certora specs for ERC721 but we are using ERC1155. There is some functional overlap but it is basically necessary to create the specs from scratch.

To run the specs:
certoraRun certora/configuration/Poaps.conf
result 1 -> https://prover.certora.com/output/49463/cb52a68b34eb4fd0b578a9123bf26f59?anonymousKey=35ebb783bf185c4afaf7abf7431c24229a9f0329
result 2 -> https://prover.certora.com/output/49463/6b1bcf56ca1a43e4901f17486fd5a832?anonymousKey=d964784f5fbe779aff25a52e9828fbffe57f42de

To run the gambit:
certoraMutate --prover_conf certora/gambit/prover.conf --mutation_conf certora/gambit/mutation.conf
result 1 -> https://prover.certora.com/output/49463/dcbc321f8d6842b9ac6d40ff315cb2f1?anonymousKey=d79c89ce3fcbbeabfbda79cedb2090793a5594cc
result 2 -> https://prover.certora.com/output/49463/3d9b3007930441bb8fa56da7eece24de?anonymousKey=902ad73b88cfae8abc39e1894170e6addb40ba86
