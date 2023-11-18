// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Test, console2} from "forge-std/Test.sol";
import {Poaps} from "../src/Poaps.sol";

contract PoapsTest is Test {
    address creator = makeAddr("poap creator");
    Poaps public poaps;

    function setUp() public {
        poaps = new Poaps("Decentralized Poaps", "POAP", makeAddr("BackendMinter"));

        vm.warp(1000);
    }

    function test_CreateCollection() public {
        assertEq(poaps.totalCollections(), 0, "total collections should be 0");
        vm.startPrank(creator);
        poaps.createCollection(
            uint56(100), 
            uint40(block.timestamp + 10 days), 
            "https://poap.xyz/istambul"
        );

        assertEq(poaps.totalCollections(), 1, "total collections should be 1");

        vm.warp(1000 + 1);

        poaps.mint(1, makeAddr("receiver"), 99, "");

        assertEq(poaps.balanceOf(makeAddr("receiver"), 1), 99, "receiver should have 99 poaps");
        //assertEq(poaps.collection(1), 1, "max supply now should be 1");
        (address _foo0, uint40 _foo1, uint56 mintLeft) = poaps.collection(1);
        assertEq(mintLeft, 1, "mint left should be 1");

    }
}