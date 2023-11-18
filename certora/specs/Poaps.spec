//certoraRun certora/configuration/Poaps.conf --packages @openzeppelin=lib/openzeppelin-contracts

methods {
    function balanceOf(address, uint256) external returns (uint256) envfree;
    function transferFrom(address,address,uint256) external;
}

/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Helpers                                                                                                             │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/

// Could be broken in theory, but not in practice
definition balanceLimited(address account, uint256 id) returns bool = balanceOf(account, id) < max_uint256;

/*
// https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/certora/specs/ERC721.spec#L103-L120
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Ghost & hooks: ownership count                                                                                      │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
ghost mathint _ownedTotal {
    init_state axiom _ownedTotal == 0;
}

ghost mapping(address => mathint) _ownedByUser {
    init_state axiom forall address a. _ownedByUser[a] == 0;
}

/*hook Sstore _owners[KEY uint256 tokenId] address newOwner (address oldOwner) STORAGE {
    _ownedByUser[newOwner] = _ownedByUser[newOwner] + to_mathint(newOwner != 0 ? 1 : 0);
    _ownedByUser[oldOwner] = _ownedByUser[oldOwner] - to_mathint(oldOwner != 0 ? 1 : 0);
    _ownedTotal = _ownedTotal + to_mathint(newOwner != 0 ? 1 : 0) - to_mathint(oldOwner != 0 ? 1 : 0);
}*/
hook Sstore _balances[KEY address account] address newOwner (address oldOwner) STORAGE {
    _ownedByUser[newOwner] = _ownedByUser[newOwner] + to_mathint(newOwner != 0 ? 1 : 0);
    _ownedByUser[oldOwner] = _ownedByUser[oldOwner] - to_mathint(oldOwner != 0 ? 1 : 0);
    _ownedTotal = _ownedTotal + to_mathint(newOwner != 0 ? 1 : 0) - to_mathint(oldOwner != 0 ? 1 : 0);
}

/*
// https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/certora/specs/ERC721.spec#L122-L143
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Ghost & hooks: sum of all balances                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
ghost mathint _supply {
    init_state axiom _supply == 0;
}

ghost mapping(address => mathint) _balances {
    init_state axiom forall address a. _balances[a] == 0;
}

hook Sstore _balances[KEY address addr] uint256 newValue (uint256 oldValue) STORAGE {
    _supply = _supply - oldValue + newValue;
}

// TODO: This used to not be necessary. We should try to remove it. In order to do so, we will probably need to add
// many "preserved" directive that require the "balanceOfConsistency" invariant on the accounts involved.
hook Sload uint256 value _balances[KEY address user] STORAGE {
    require _balances[user] == to_mathint(value);
}

/*
// https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/certora/specs/ERC721.spec#L186-L200
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Invariant: balanceOf is the number of tokens owned                                                                  │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
// certoraRun certora/configuration/Poaps.conf --rule setOwnerRevertCondition

*/
invariant balanceOfConsistency(address user, uint256 id)
    to_mathint(balanceOf(user, id)) == _ownedByUser[user] &&
    to_mathint(balanceOf(user, id)) == _balances[user]
    {
        preserved {
            require balanceLimited(user, id);
        }
    }

/*