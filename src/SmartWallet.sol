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

    // this should be implemented in the front end via an SDK!
    function createUserOp(
        address _sender,               // sender of the user op
        uint256 _nonce,                // nonce for replay protection
        bytes memory _initCode,         // if set, for contract creation
        bytes memory _callData,         // methods to execute on THIS contract
        uint256 _callGasLimit,          // gas limit passed to callData method call
        uint256 _verificationGasLimit,  // gas for validateUserOps and validatePaymasterUserOp
        uint256 _preVerificationGas,    // gas to cover batch overhead
        uint256 _maxFeePerGas,          // same as EIP-1559 gas parameter
        uint256 _maxPriorityFeePerGas,  // same as EIP-1559 gas parameter
        bytes memory _paymasterAndData, // If set, this field holds the paymaster address and paymaster-specific data.
        bytes memory _signature         // Sender-verified signature over the entire request, the EntryPoint address and the chain ID
        ) external pure returns (UserOperation memory) {

            UserOperation memory userOp = UserOperation({
                sender: _sender,
                nonce: _nonce,
                initCode: _initCode,
                callData: _callData,
                callGasLimit: _callGasLimit,
                verificationGasLimit: _verificationGasLimit,
                preVerificationGas: _preVerificationGas,
                maxFeePerGas: _maxFeePerGas,
                maxPriorityFeePerGas: _maxPriorityFeePerGas,
                paymasterAndData: _paymasterAndData,
                signature: _signature
            });

            return userOp;

    }


    function entryPoint() public view override returns (IEntryPoint) {
        return entryPointContract;
    }




    function hello() public view returns(string memory){
        return "you called me";
    }


    // Empty function: not implemented
    function _validateSignature(UserOperation calldata userOp, bytes32 userOpHash) internal override returns (uint256 validationData){}


}
