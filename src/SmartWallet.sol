// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

interface IEntryPoint {

}

contract SmartWallet {

    IEntryPoint entrypoint;
    address owner;

    constructor(IEntryPoint _entrypoint, address _owner){
        entrypoint = _entrypoint;
        owner = _owner;
    }




}
