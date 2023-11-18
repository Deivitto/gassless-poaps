// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;
import {ERC1155} from "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
import {AccessControl} from "@openzeppelin/contracts/access/AccessControl.sol";

contract Poaps is ERC1155(""), AccessControl {
    // Contract variables
    string public name;
    string public symbol;

    uint256 public totalCollections;

    // CONSTANTS
    bytes32 public constant CREATOR_MINTER_ROLE = keccak256("CREATOR_ROLE");
    bytes32 public constant BACKEND_MINTER_ROLE = keccak256("BACKEND_ROLE");

    // Mappings
    mapping(uint256 _id => Collection) public collection;
    mapping(uint256 _id => string url) private _url;

    struct Collection{
        address creator;
        uint40 endDeadline;
        uint56 maxSupply;
    }

    constructor(string memory _name, string memory _symbol, address _backendMinter) {
        name = _name;
        symbol = _symbol;

        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _grantRole(BACKEND_MINTER_ROLE, _backendMinter);
    }

    // anyone should be able to create a collection
    function createCollection(uint56 maxMint, uint40 deadline, string memory url_) external {
        require(deadline > block.timestamp, "Poaps: deadline must be in the future");
        _grantRole(CREATOR_MINTER_ROLE, msg.sender);

        uint256 _counter = ++totalCollections;

        collection[_counter] = Collection(msg.sender, deadline, maxMint);
        _url[_counter] = url_;

        // emit new collection??
    }

    function mint(uint256 id, address account, uint56 amount, bytes memory data) external {
        require(
            (hasRole(CREATOR_MINTER_ROLE, msg.sender) && collection[id].creator == msg.sender)
            || hasRole(BACKEND_MINTER_ROLE, msg.sender)
        , "Poaps: must have minter role to mint");
        
        require(collection[id].endDeadline > block.timestamp, "Poaps: collection has ended");
        require(amount < collection[id].maxSupply, "Poaps: max supply reached");
        
        collection[id].maxSupply -= amount;

        _mint(account, id, amount, data);
    }
    

    function uri(uint256 id) public view override returns (string memory) {
        // return String.concat(_URL, Strings.toString(id));
        return _url[id];
    }

    function supportsInterface(bytes4 interfaceId) public view virtual override(ERC1155, AccessControl) returns (bool) {
        return interfaceId == type(ERC1155).interfaceId || super.supportsInterface(interfaceId);
    }
}