// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Poaps} from "../../src/Poaps.sol";

contract PoapsHarness is Poaps {
    constructor(string memory _name, string memory _symbol, address _backendMinter) Poaps(_name, _symbol, _backendMinter) {}
}