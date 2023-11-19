OZ has Certora specs for ERC721 but we are using ERC1155. There is some functional overlap but it is basically necessary to create the specs from scratch.

To run the specs:
certoraRun certora/configuration/Poaps.conf

To run the gambit:
certoraMutate --prover_conf certora/gambit/prover.conf --mutation_conf certora/gambit/mutation.conf
result -> https://prover.certora.com/output/49463/dcbc321f8d6842b9ac6d40ff315cb2f1?anonymousKey=d79c89ce3fcbbeabfbda79cedb2090793a5594cc
