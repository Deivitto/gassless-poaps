// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Test, console2} from "forge-std/Test.sol";
import {SmartWallet} from "../src/SmartWallet.sol";
import {IEntryPoint} from "../src/interfaces/IEntryPoint.sol";
import {UserOperation} from "../src/interfaces/UserOperation.sol";

contract SmartWalletTest is Test {

    IEntryPoint goerli_entryPointContract;
    SmartWallet sw;
    
    address user;

    function setUp() public {
        goerli_entryPointContract = IEntryPoint(0x0576a174D229E3cFA37253523E645A78A0C91B57);
        user = makeAddr("user");
        sw = new SmartWallet(goerli_entryPointContract, user);
    }


    function testExecuteUserOp() public {
        // sender of the user op
        address _sender = user;
        // nonce for replay protection
        uint256 _nonce = 1;
        // if set, for contract creation
        bytes memory _initCode;
        // methods to execute on THIS contract
        bytes memory _callData = abi.encodeWithSignature("hello()");
        // gas limit passed to callData method call
        uint256 _callGasLimit = 21000;
        // gas for validateUserOps and validatePaymasterUserOp
        uint256 _verificationGasLimit = 21000;
        // gas to cover batch overhead
        uint256 _preVerificationGas = 21000;  
        // same as EIP-1559 gas parameter
        uint256 _maxFeePerGas = 21000;      
        // same as EIP-1559 gas parameter
        uint256 _maxPriorityFeePerGas = 21000;
        // If set, this field holds the paymaster address and paymaster-specific data.
        bytes memory _paymasterAndData;
        // Sender-verified signature over the entire request, the EntryPoint address and the chain ID
        bytes memory _signature;

        UserOperation memory userop = sw.createUserOp(
            _sender, 
            _nonce, 
            _initCode, 
            _callData, 
            _callGasLimit, 
            _verificationGasLimit, 
            _preVerificationGas, 
            _maxFeePerGas, 
            _maxPriorityFeePerGas, 
            _paymasterAndData, 
            _signature
        );

        console2.logBytes(abi.encode(userop));
        
    }

    

}
