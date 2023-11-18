// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "./BaseAccount.sol";

// Very very basic smart contract wallet initial implementation
contract SmartWallet is BaseAccount{

    IEntryPoint public immutable entryPointContract;
    address owner;


    constructor(IEntryPoint _entryPoint, address _owner){
        entryPointContract = _entryPoint;
        owner = _owner;
    }

    function entryPoint() public view override returns (IEntryPoint) {
        return entryPointContract;
    }


    

    function _validateSignature(UserOperation calldata userOp,bytes32 userOpHash) internal override returns (uint256 validationData){}



}
